#!/usr/bin/env python3
"""Down-the-chain tracer for our own compiler output.

Takes an emmy-compiler artifact (a .ptx file, or a problem directory whose
*.ir.json is fed through compile.py) and follows it all the way down, for BOTH
architectures:

  stage 1   ptxas -arch=sm_89  and  ptxas -arch=sm_120   (staged toolchain)
  stage 2   nvdisasm -hex -c decode to SASS (mnemonics + raw 128-bit encodings)
  stage 3   every emitted SASS opcode mapped to its KB catalog entry
            (sm89/sass/<OP>.md, sm120/sass/<OP>.md) with the KB's NVIDIA
            description and NAK cross-check status attached per instruction

Output per input, under traces/<name>/:
  source.sm89.ptx / source.sm120.ptx   the exact PTX each ptxas saw (the sm_120
                                       copy has its header rewritten: .target
                                       sm_120 and .version bumped to >= 8.7)
  sm89.sass.md / sm120.sass.md         full SASS listing, per-instruction KB refs
  README.md                            provenance, opcode->KB cross-ref tables
                                       for both arches, and the arch-divergence
                                       summary mapped to the KB divergence notes

traces/INDEX.md summarizes all traced inputs.

The sm_120 side activates only when sm120/sass/INDEX.md exists (same gate would
apply to any future arch); without it the sm_120 stage is marked "KB not
available" and the pipeline still runs.

Usage:
  python3 tools/trace.py                     # trace all problems + examples
  python3 tools/trace.py --ptx foo.ptx       # one PTX file
  python3 tools/trace.py --problem task/problems/r01_array_sum
"""
from __future__ import annotations

import argparse
import collections
import datetime
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PTXAS = ROOT / "toolchain" / "cuda12.9" / "bin" / "ptxas"
NVDISASM = ROOT / "toolchain" / "cuda12.9" / "bin" / "nvdisasm"
TRACES = ROOT / "traces"
COMPILE_PY = ROOT / "compile.py"
VENV_PY = ROOT / ".venv" / "bin" / "python"

# Per-arch KB wiring.  `active` gates on the KB's SASS index existing.
ARCHS = {
    "sm_89": {
        "kb": ROOT / "sm89",
        "index": ROOT / "sm89" / "sass" / "INDEX.md",
        "nak": ROOT / "sm89" / "verify" / "nak.json",
        "version": None,           # compile.py targets sm_89 natively
    },
    "sm_120": {
        "kb": ROOT / "sm120",
        "index": ROOT / "sm120" / "sass" / "INDEX.md",
        "nak": ROOT / "sm120" / "verify" / "nak.json",
        "version": "8.7",          # sm_120 needs PTX ISA >= 8.7
    },
}

# sm_89 -> sm_120 opcode replacements established by the sm120 KB probes
# (sm120/verify/RESULTS.md "sm_89 -> sm_120 divergences" / sm120/README.md).
RENAMES = {
    "IMNMX": "VIMNMX", "RED": "REDG", "ULDC": "LDCU", "STM": "STSM",
    "HADD2": "HFMA2 (folding)", "HMUL2": "HFMA2 (folding)",
    "BMMA": "(library-emulated: CALL + IMMA + MOVM)",
    "VABSDIFF4": "(emulated: VIMNMX.U8x4 + VIADD.U8x4 + IDP)",
    "VABSDIFF": "(emulated)",
    "SUQUERY": "(folded into TXQ)",
    "I2F": "UI2F (uniform-datapath FP conversion; found by tracing compile.py output on matmul)",
}

# sm_89 opcode absent on sm_120 for an input, where the KB explains why (opcode
# itself may still exist on sm_120 -- the input just no longer reaches it).
GONE_NOTES = {
    "MOV": "sm_120 loads kernel params via LDC/LDCU directly (KB: prologue divergence); "
           "MOV still exists in the sm_120 ISA but ptxas stops using it here",
    "ULDC": "renamed LDCU",
}


def run(cmd):
    return subprocess.run([str(c) for c in cmd], capture_output=True, text=True)


def tool_versions():
    v = {}
    for name, binary in (("ptxas", PTXAS), ("nvdisasm", NVDISASM)):
        out = run([binary, "--version"]).stdout.strip().splitlines()
        v[name] = next((ln for ln in out if "release" in ln or "Cuda" in ln), out[-1] if out else "?")
    return v


def get_ptx(args, tmpdir: pathlib.Path) -> tuple[str, str]:
    """Return (name, ptx_text)."""
    if args.ptx:
        p = pathlib.Path(args.ptx)
        return p.stem, p.read_text()
    prob = pathlib.Path(args.problem)
    irs = sorted(prob.glob("*.ir.json"))
    if not irs:
        sys.exit(f"no *.ir.json in {prob}")
    r = run([VENV_PY if VENV_PY.exists() else sys.executable, COMPILE_PY, irs[0]])
    if r.returncode:
        sys.exit(f"compile.py failed for {irs[0]}:\n{r.stderr}")
    return prob.name, r.stdout


def retarget(ptx: str, arch: str) -> str:
    """Rewrite the PTX header for the target arch (documented in the trace)."""
    spec = ARCHS[arch]
    out = []
    for line in ptx.splitlines():
        if line.startswith(".target") and arch != "sm_89":
            line = f".target {arch}"
        elif line.startswith(".version") and spec["version"]:
            cur = re.search(r"(\d+)\.(\d+)", line)
            need = tuple(int(x) for x in spec["version"].split("."))
            if cur and tuple(map(int, cur.groups())) < need:
                line = f".version {spec['version']}"
        out.append(line)
    return "\n".join(out) + "\n"


def compile_arch(ptx: str, arch: str, workdir: pathlib.Path):
    """-> (status, cubin path or None, error)."""
    src = workdir / f"source.{arch}.ptx"
    src.write_text(ptx)
    cub = workdir / f"{arch}.cubin"
    r = run([PTXAS, f"-arch={arch}", "-O3", src, "-o", cub])
    if r.returncode:
        return "ptxas error", None, r.stderr.strip().splitlines()[-1] if r.stderr.strip() else ""
    return "ok", cub, ""


DISASM_RE = re.compile(r"\s*/\*[0-9a-f]{4}\*/\s+(.*?)\s*;?\s*/\* (0x[0-9a-f]{16}) \*/")


def disasm(cubin: pathlib.Path):
    """-> list of (op, text, w0, w1)."""
    out = run([NVDISASM, "-hex", "-c", cubin]).stdout.splitlines()
    instrs, i = [], 0
    while i < len(out):
        m = DISASM_RE.match(out[i])
        if m and i + 1 < len(out):
            m2 = re.search(r"/\* (0x[0-9a-f]{16}) \*/", out[i + 1])
            text = m.group(1).rstrip(" ;")
            op = re.sub(r"^@!?U?P[T0-9]+\s+", "", text).split()[0].split(".")[0]
            instrs.append((op, text, m.group(2), m2.group(1) if m2 else "?" * 18))
            i += 2
        else:
            i += 1
    return instrs


# ---------------------------------------------------------------------------
# KB catalog: opcode -> (page exists, NVIDIA description, NAK status)
# ---------------------------------------------------------------------------

def load_kb(arch: str):
    spec = ARCHS[arch]
    kb = {"active": spec["index"].exists(), "desc": {}, "nak": {}}
    if not kb["active"]:
        return kb
    for page in (spec["kb"] / "sass").glob("*.md"):
        if page.stem == "INDEX":
            continue
        m = re.search(r"^\*\*NVIDIA:\*\* (.+)$", page.read_text(errors="replace"), re.M)
        if m:
            kb["desc"][page.stem] = m.group(1)
    if spec["nak"].exists():
        kb["nak"] = json.loads(spec["nak"].read_text()).get("ops", {})
    return kb


def nak_short(kb, op):
    n = kb["nak"].get(op)
    if not n:
        return ""
    return f"NAK: {n['status']}"


def sass_listing(arch, instrs, kb, error=""):
    lines = [f"# SASS listing — {arch}", "",
             f"Decoded with `nvdisasm -hex -c` ({tool_versions()['nvdisasm']}); encodings are the raw two "
             "64-bit words, bit 0 = LSB of word 0. `KB` links the opcode's page in the "
             f"{arch} knowledge base." if kb["active"] else
             f"Decoded with `nvdisasm -hex -c`; {arch} KB not available, no catalog mapping.", ""]
    if error:
        lines += [f"**Stage 1 failed:** `{error}`", ""]
        return "\n".join(lines) + "\n"
    lines += ["| addr | SASS | encoding (w0 w1) | KB |", "|---|---|---|---|"]
    for op, text, w0, w1 in instrs:
        if kb["active"] and op in kb["desc"]:
            ref = f"[{op}](../../{ARCHS[arch]['kb'].name}/sass/{op}.md)"
        elif kb["active"]:
            ref = f"{op} — *not in KB corpus*"
        else:
            ref = op
        lines.append(f"| | `{text}` | `{w0} {w1}` | {ref} |")
    return "\n".join(lines) + "\n"


def crossref_table(arch, instrs, kb):
    counts = collections.Counter(op for op, *_ in instrs)
    if not kb["active"]:
        return [f"## {arch} opcode -> KB cross-ref", "", f"{arch} KB not available — skipped.", ""]
    lines = [f"## {arch} opcode -> KB cross-ref", "",
             "| opcode | count | KB page | NVIDIA description | NAK cross-check |",
             "|---|---|---|---|---|"]
    for op in sorted(counts):
        desc = kb["desc"].get(op)
        page = f"[{op}.md](../../{ARCHS[arch]['kb'].name}/sass/{op}.md)" if desc else "*not in KB corpus*"
        d = (desc.split(". Source:")[0].rstrip(".") if desc else "—")
        lines.append(f"| {op} | {counts[op]} | {page} | {d} | {nak_short(kb, op) or '—'} |")
    lines.append("")
    return lines


def divergence_summary(by_arch):
    """Arch-divergence summary for one input, mapped to the KB divergence notes."""
    if not all(by_arch[a]["kb"]["active"] for a in ("sm_89", "sm_120")):
        return ["## sm_89 vs sm_120 divergence summary", "",
                "Needs both KBs active — skipped.", ""]
    s89 = {op for op, *_ in by_arch["sm_89"]["instrs"]}
    s120 = {op for op, *_ in by_arch["sm_120"]["instrs"]}
    lines = ["## sm_89 vs sm_120 divergence summary", "",
             "Same source PTX, two toolchain targets. Opcode sets are per-mnemonic "
             "(nvspas form bits ignored). Renames/replacements cite the sm120 KB "
             "divergence notes ([verify/RESULTS.md](../../sm120/verify/RESULTS.md), "
             "[README](../../sm120/README.md)).", ""]
    replaced = [(a, RENAMES[a], b) for a in sorted(s89 - s120) for b in [RENAMES.get(a)] if b]
    plain_gone = [a for a in sorted(s89 - s120) if a not in RENAMES]
    new = sorted(s120 - s89)
    shared = sorted(s89 & s120)
    lines += [f"**Shared opcodes ({len(shared)}):** " + (", ".join(f"`{o}`" for o in shared) or "—"), ""]
    if replaced:
        lines += ["### Replaced (sm_89 opcode -> sm_120 successor, per KB)", "",
                  "| sm_89 | sm_120 (KB finding) | observed here on sm_120 |", "|---|---|---|"]
        for a, b, _ in replaced:
            succ = b.split(" ")[0].split("(")[0]
            obs = "yes" if succ in s120 else "not emitted by this input"
            lines.append(f"| `{a}` | {b} | {obs} |")
        lines.append("")
    if plain_gone:
        lines += ["### Emitted on sm_89 but not on sm_120", "",
                  "| opcode | KB explanation |", "|---|---|"]
        for o in plain_gone:
            note = GONE_NOTES.get(o, "not emitted by this input on sm_120; no rename in the KB "
                                     "divergence notes (may still exist in the sm_120 ISA)")
            lines.append(f"| `{o}` | {note} |")
        lines.append("")
    if new:
        lines += ["### Emitted on sm_120 but not on sm_89 (new/renamed-in opcodes)", "",
                  ", ".join(f"`{o}`" for o in new), ""]
    lines += ["Full per-arch tables above; the general (input-independent) divergence "
              "catalog lives in [sm120/verify/RESULTS.md](../../sm120/verify/RESULTS.md).", ""]
    return lines


def trace(name: str, ptx: str, origin: str):
    out = TRACES / name
    out.mkdir(parents=True, exist_ok=True)
    tv = tool_versions()
    readme = [f"# Trace: {name}", "",
              f"- Source: {origin}",
              f"- Generated: {datetime.datetime.now(datetime.UTC):%Y-%m-%d %H:%M UTC}",
              f"- Tools: ptxas `{tv['ptxas']}`, nvdisasm `{tv['nvdisasm']}`, both `-O3`",
              "- The sm_120 stage consumes a header-retargeted copy of the same PTX "
              "(`.target sm_120`, `.version` bumped to >= 8.7); the body is untouched.", ""]
    by_arch = {}
    for arch in ("sm_89", "sm_120"):
        spec = ARCHS[arch]
        kb = load_kb(arch)
        ptx_arch = retarget(ptx, arch) if arch != "sm_89" else ptx
        (out / f"source.{arch}.ptx").write_text(ptx_arch)
        status, cub, err = compile_arch(ptx_arch, arch, out)
        if status != "ok":
            instrs = []
            readme += [f"- **{arch}: stage 1 FAILED** — `{err}`"]
        else:
            instrs = disasm(cub)
            cub.unlink()          # listings are the evidence; keep trace dirs text-only
            readme += [f"- **{arch}: {len(instrs)} SASS instructions, "
                       f"{len({i[0] for i in instrs})} distinct opcodes**"
                       + ("" if kb["active"] else " (KB not available — no catalog mapping)")]
        (out / f"{arch}.sass.md").write_text(sass_listing(arch, instrs, kb, err if status != "ok" else ""))
        by_arch[arch] = {"instrs": instrs, "kb": kb, "status": status, "error": err}
    for arch in ("sm_89", "sm_120"):
        readme += crossref_table(arch, by_arch[arch]["instrs"], by_arch[arch]["kb"])
    readme += divergence_summary(by_arch)
    (out / "README.md").write_text("\n".join(readme) + "\n")
    return {"name": name, "by_arch": {a: {k: v for k, v in d.items() if k != "kb"}
                                      for a, d in by_arch.items()},
            "kb_active": {a: by_arch[a]["kb"]["active"] for a in by_arch}}


def main():
    global TRACES
    ap = argparse.ArgumentParser()
    ap.add_argument("--ptx")
    ap.add_argument("--problem")
    ap.add_argument("--out", default=str(TRACES),
                    help="output traces root (default traces/); use e.g. traces-gepa/ for candidate sets")
    args = ap.parse_args()
    TRACES = pathlib.Path(args.out)

    inputs = []
    if args.ptx or args.problem:
        name, ptx = get_ptx(args, TRACES)
        inputs.append((name, ptx, args.ptx or args.problem))
    else:
        ex = ROOT / "task" / "examples"
        for p in sorted(ex.glob("*.ptx")):
            inputs.append((p.stem, p.read_text(), str(p.relative_to(ROOT))))
        for prob in sorted((ROOT / "task" / "problems").iterdir()):
            if not list(prob.glob("*.ir.json")):
                continue
            name, ptx = get_ptx(argparse.Namespace(ptx=None, problem=str(prob)), TRACES)
            inputs.append((name, ptx, str(prob.relative_to(ROOT))))
    TRACES.mkdir(exist_ok=True)
    summary = [trace(n, p, o) for n, p, o in inputs]
    lines = ["# Traces — our compiler output, followed all the way down", "",
             "Per input: `source.<arch>.ptx` -> ptxas (`-O3`) -> nvdisasm (`-hex -c`) -> "
             "SASS listing with per-instruction KB refs, plus an opcode->KB cross-ref and "
             "an sm_89/sm_120 divergence summary in `README.md`. "
             "Regenerate with `python3 tools/trace.py`.", "",
             "| input | sm_89 | sm_120 | divergence headline |", "|---|---|---|---|"]
    for s in summary:
        a89, a120 = s["by_arch"]["sm_89"], s["by_arch"]["sm_120"]
        cell = lambda d: (f"{len(d['instrs'])} instr / {len({i[0] for i in d['instrs']})} ops"
                          if d["status"] == "ok" else f"FAILED: {d['error'][:40]}")
        s89 = {op for op, *_ in a89["instrs"]}
        s120 = {op for op, *_ in a120["instrs"]}
        n_ren = sum(1 for a in s89 - s120 if a in RENAMES)
        head = (f"{len(s89 & s120)} shared, {n_ren} replaced per KB, "
                f"{len(s120 - s89)} sm_120-only" if a89["status"] == a120["status"] == "ok" else "—")
        lines.append(f"| [{s['name']}](README.md → `{s['name']}/`) | {cell(a89)} | {cell(a120)} | {head} |")
    (TRACES / "INDEX.md").write_text("\n".join(lines) + "\n")
    print(f"{len(summary)} inputs traced -> {TRACES} ; see {TRACES}/INDEX.md")
    for s in summary:
        for arch, d in s["by_arch"].items():
            if d["status"] != "ok":
                print(f"  {s['name']} {arch}: {d['error'][:100]}")


if __name__ == "__main__":
    main()
