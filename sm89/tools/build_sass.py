#!/usr/bin/env python3
"""Fetch the SM89 SASS encoding pages from kuterdinel.com and convert them to markdown.

Usage: python3 sm89/tools/build_sass.py        (re-run is cheap: raw HTML is cached in sm89/.cache/sass)

Writes sm89/sass/<OPCODE>.md (one per instruction, every encoding variant) and
sm89/sass/INDEX.md.  The source pages are machine-derived encodings (no prose), so
each variant is rendered as: syntax, operand access, example, bit-field map,
fixed opcode bits, and modifier tables.

Evidence merged in:
  - NVIDIA's official opcode descriptions (CUDA Binary Utilities, "NVIDIA Ampere GPU and Ada
    Instruction Set" table), fetched into sm89/.cache/refs.
  - sm89/verify/results.json from verify/probes.py (real ptxas/nvdisasm output), if present.
"""
import html
import json
import pathlib
import re
import sys
import time
import urllib.request

BASE = "https://kuterdinel.com/nv_isa_sm89/"
ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "sass"
OUT = ROOT / "sass"
BINUTILS = "https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html"
NV_TABLE = BINUTILS + "#nvidia-ampere-gpu-and-ada-instruction-set"
# The source pages name the two scoreboard fields the other way round from what real ptxas
# output shows (see verify/RESULTS.md, "Control-code scoreboard fields").
FIELD_RENAME = {"r-bar": "write scoreboard (site label: r-bar)",
                "w-bar": "read scoreboard (site label: w-bar)",
                "b-mask": "wait mask (site label: b-mask)"}


def fetch(name):
    path = CACHE / name
    if not path.exists():
        req = urllib.request.Request(BASE + name, headers={"User-Agent": "sm89-kb/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            path.write_bytes(r.read())
        time.sleep(0.2)
    return path.read_text(encoding="utf-8", errors="replace")


def nvidia_table():
    """Opcode -> (section, description) from NVIDIA's Ampere/Ada SASS opcode table."""
    path = ROOT / ".cache" / "refs" / "binutils.html"
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(BINUTILS, headers={"User-Agent": "sm89-kb/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            path.write_bytes(r.read())
    page = path.read_text(encoding="utf-8")

    def rows(start_id, end_id):
        start = page.index(f'id="{start_id}"')
        chunk = page[start:page.index(f'id="{end_id}"', start)] if end_id else page[start:]
        table, section = {}, ""
        for row in re.findall(r"<tr[^>]*>(.*?)</tr>", chunk, re.S):
            cells = [strip_tags(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]
            if len(cells) < 2 or cells[0] == "Opcode":
                continue
            if not cells[1]:
                section = cells[0]
            else:
                table[cells[0]] = (section, cells[1])
        return table

    ada = rows("nvidia-ampere-gpu-and-ada-instruction-set", "hopper-instruction-set")
    # Other architectures' tables, for opcodes NVIDIA only documents elsewhere (e.g. QMMA).
    other = {}
    for name, a, b in (("Turing", "turing-instruction-set", "nvidia-ampere-gpu-and-ada-instruction-set"),
                       ("Hopper", "hopper-instruction-set", "blackwell-and-rubin-instruction-set"),
                       ("Blackwell/Rubin", "blackwell-and-rubin-instruction-set", "cu-filt")):
        for op, (_sec, desc) in rows(a, b).items():
            other.setdefault(op, (name, desc))
    return ada, other


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).replace("\xa0", " ").strip()


CELL_RE = re.compile(r'<td class="[^"]*"(?: colspan="(\d+)")? style="([^"]*)">(.*?)</td>', re.S)
ROW_RE = re.compile(r'<tr class="([^"]*)">(.*?)</tr>', re.S)


def parse_bits(table):
    """Return (fields, fixed) from the 128-bit encoding table.

    fields: list of (name, [(lo, hi), ...]) in first-seen order
    fixed:  128-char string of '0'/'1' for fixed opcode bits, '.' elsewhere
    Bit numbering follows the source page: bit 0 is the first cell of the first row.
    """
    cells = [c for cls, row in ROW_RE.findall(table) if cls != "smoll" for c in CELL_RE.findall(row)]
    # Per-operand flags (cNEG/cABS/...) share the owning operand's background colour.
    owner = {}
    for _span, style, text in cells:
        m = re.search(r"background: (#[0-9A-Fa-f]+)", style)
        if m and strip_tags(text).startswith("operand "):
            owner[m.group(1)] = strip_tags(text).split()[1]
    fields, fixed, pos = {}, ["."] * 128, 0
    for span, style, text in cells:
        n = int(span or 1)
        text = strip_tags(text)
        m = re.search(r"background: (#[0-9A-Fa-f]+)", style)
        if m and not text.startswith("operand") and m.group(1) in owner:
            text = f"{text} (op {owner[m.group(1)]})"
        if text in ("0", "1") and n == 1:
            fixed[pos] = text
        elif text:
            rng = fields.setdefault(text, [])
            if rng and rng[-1][1] == pos - 1:
                rng[-1] = (rng[-1][0], pos + n - 1)
            else:
                rng.append((pos, pos + n - 1))
        pos += n
    return list(fields.items()), "".join(fixed)


def fmt_ranges(rs):
    return ", ".join(f"{a}" if a == b else f"{a}-{b}" for a, b in rs)


def parse_variants(page):
    page = re.sub(r"<style>.*?</style>|<script.*?</script>", "", page, flags=re.S)
    chunks = page.split('<div class="instruction-desc">')[1:]
    variants = []
    for ch in chunks:
        head, _, body = ch.partition("</div>")
        syntax = re.sub(r"\s+", " ", strip_tags(head))
        access = [re.sub(r"\s+", " ", strip_tags(a))
                  for a in re.findall(r'<span class="flat-operand-section"[^>]*>(.*?)</span>', body, re.S)]
        distilled = re.search(r"<p> distilled: (.*?)</p>", body, re.S)
        key = re.search(r"<p> key: (.*?)</p>", body, re.S)
        tables = re.findall(r'(<p>([^<]*))?<table class="instviz">(.*?)</table>', body, re.S)
        enc, mods = None, []
        for _, label, t in tables:
            if enc is None and not label.strip():
                enc = parse_bits(t)
            else:
                rows = []
                for _cls, row in ROW_RE.findall(t):
                    cells = [strip_tags(c[2]) for c in CELL_RE.findall(row)]
                    if len(cells) == 2:
                        rows.append(cells)
                mods.append((label.strip() or "Modifier group", rows))
        variants.append(dict(
            syntax=syntax, access=access,
            distilled=strip_tags(distilled.group(1)) if distilled else "",
            key=strip_tags(key.group(1)) if key else "",
            enc=enc, mods=mods))
    return variants


def evidence(op, results, nak):
    """(short status for the index, markdown lines for the opcode page) from verify/*.json."""
    nak_line, nak_short = [], ""
    if nak and op in nak["ops"]:
        n = nak["ops"][op]
        nak_short = f" · [NAK]({n['ref']})"
        nak_line = [f"Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `{nak['commit'][:12]}`): "
                    f"**{n['status']}**. NAK encodes {', '.join(n['nak'])} ([source]({n['ref']})); "
                    "see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).", ""]
    if not results:
        return nak_short.lstrip(" ·"), (["## Evidence", ""] + nak_line) if nak_line else []
    probes = [p for p in results["probes"] if op in p["expect"] and p["status"] == "ok"]
    seen = results["observed"].get(op, [])
    if probes:
        short = "✓ " + ", ".join(f"[`{p['ptx'].split(' (')[0]}`](../verify/RESULTS.md#{p['name']})"
                                 for p in probes[:2])
    elif seen:
        short = "seen in " + ", ".join(f"[{n}](../verify/RESULTS.md#{n})" for n in seen[:2])
    else:
        short = "not reproduced"
    short += nak_short
    lines = ["## Evidence", ""] + nak_line + [
             f"Checked with {results['tools']['ptxas']} (`-arch=sm_89`) and nvdisasm "
             f"({results['tools']['nvdisasm']}); see [verify/RESULTS.md](../verify/RESULTS.md).", ""]
    if probes:
        lines += ["Claimed lowering confirmed by probe(s):", ""]
        lines += [f"- [{p['name']}](../verify/RESULTS.md#{p['name']}): `{p['ptx']}`" for p in probes]
    elif seen:
        lines.append("Emitted (incidentally) in probe(s): " +
                     ", ".join(f"[{n}](../verify/RESULTS.md#{n})" for n in seen))
    else:
        lines.append("Not produced by any ptxas probe, so the \"typically emitted for\" line above is unverified.")
    extra = {k.split(":")[1]: v for k, v in results.get("unlabelled_bits", {}).items() if k.split(":")[0] == op}
    if extra:
        lines += ["", "Bits marked fixed on the source page that real ptxas output sets "
                      "(typically modifiers or implicit operands the page did not label):", "",
                  "| bit | seen in |", "|---|---|"]
        lines += [f"| {b} | " + "<br>".join(f"`{t}`" for t in ts[:3]) + " |"
                  for b, ts in sorted(extra.items(), key=lambda kv: int(kv[0]))]
    if op in results.get("encoding_mismatch", {}):
        lines += ["", "Real encodings whose 12-bit opcode field matches **no** variant on the source page "
                      "(form missing from the site): " +
                  ", ".join(f"`{t}`" for t in sorted(set(results["encoding_mismatch"][op]))[:3])]
    return short, lines + [""]


def render(op, variants, desc, origin, nv, nv_other, ev_lines):
    out = [f"# {op} (SM89 SASS)", ""]
    if nv:
        out += [f"**NVIDIA:** {nv[1]} ({nv[0]}). Source: [CUDA Binary Utilities, Ampere/Ada instruction set]"
                f"({NV_TABLE})", ""]
    else:
        out += ["**NVIDIA:** not listed in the official Ampere/Ada opcode table "
                f"([CUDA Binary Utilities]({NV_TABLE}))."
                + (f" NVIDIA's {nv_other[0]} table lists it as \"{nv_other[1]}\" ([same document]({BINUTILS}))."
                   if nv_other else ""), ""]
    if desc:
        out += [f"Notes: {desc[1]} (category: {desc[0]})", ""]
    if origin:
        out += [f"Typically emitted for: {origin}", ""]
    out += ev_lines
    out += [f"Encodings: <{BASE}{op}.html> (machine-derived by fuzzing the assembler; no semantics).", "",
            f"{len(variants)} encoding variant(s):", ""]
    for i, v in enumerate(variants, 1):
        out.append(f"- [{v['key'] or v['syntax']}](#v{i})")
    out.append("")
    for i, v in enumerate(variants, 1):
        out += [f'<a id="v{i}"></a>', f"## {i}. `{v['key'] or v['syntax']}`", "",
                f"Syntax: `{v['syntax']}`  ", f"Example: `{v['distilled']}`", ""]
        if v["access"]:
            out += ["Register access: " + "; ".join(v["access"]), ""]
        if v["enc"]:
            fields, fixed = v["enc"]
            out += ["| field | bits |", "|---|---|"]
            out += [f"| {FIELD_RENAME.get(name, name)} | {fmt_ranges(rs)} |" for name, rs in fields]
            out += ["", "Fixed bits (bit 0 first; `.` = field):", "```",
                    fixed[:64], fixed[64:], "```", ""]
        for label, rows in v["mods"]:
            if not rows:
                continue
            out += [f"{label}:", "", "| value | modifier |", "|---|---|"]
            out += [f"| `{a}` | `{b or '(default)'}` |" for a, b in rows]
            out.append("")
    return "\n".join(out)


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(pathlib.Path(__file__).parent))
    from sass_catalog import CATALOG, ORIGIN

    nv, nv_other = nvidia_table()
    res_path = ROOT / "verify" / "results.json"
    results = json.loads(res_path.read_text()) if res_path.exists() else None
    nak_path = ROOT / "verify" / "nak.json"
    nak = json.loads(nak_path.read_text()) if nak_path.exists() else None
    index = fetch("index.html")
    ops = re.findall(r'href="([A-Z0-9_]+)\.html"', index)
    summary = []
    for op in ops:
        variants = parse_variants(fetch(op + ".html"))
        short, ev_lines = evidence(op, results, nak)
        (OUT / f"{op}.md").write_text(
            render(op, variants, CATALOG.get(op), ORIGIN.get(op), nv.get(op), nv_other.get(op), ev_lines) + "\n")
        summary.append((op, len(variants), short))

    by_cat = {}
    for op, n, short in summary:
        cat, desc = CATALOG.get(op, ("Uncategorized", ""))
        by_cat.setdefault(cat, []).append((op, n, desc, short))
    missing_nv = [op for op in ops if op not in nv]
    n_ver = sum(s.startswith("✓") for _, _, s in summary)
    n_nak = sum("[NAK]" in s for _, _, s in summary)
    lines = ["# SM89 SASS instruction index", "",
             f"{len(summary)} opcodes scraped from <{BASE}>. Columns:", "",
             f"- **NVIDIA description**: verbatim from NVIDIA's [Ampere/Ada opcode table]({NV_TABLE}). "
             f"{len(ops) - len(missing_nv)}/{len(ops)} opcodes are listed there; the rest are marked "
             "*not in NVIDIA table*.",
             "- **typically emitted for**: our summary of which PTX/CUDA produces it (`tools/sass_catalog.py`).",
             f"- **evidence**: ✓ = a probe compiled with real `ptxas -arch=sm_89` produced this opcode from the "
             f"linked PTX ({n_ver} opcodes); \"seen in\" = emitted incidentally; \"not reproduced\" = claim "
             "unverified. Details in [../verify/RESULTS.md](../verify/RESULTS.md). "
             f"**NAK** = the opcode number on the source page matches Mesa's open-source NVK compiler "
             f"({n_nak} opcodes, [../verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md)).", ""]
    for cat in sorted(by_cat, key=lambda c: (c == "Uncategorized", c)):
        lines += [f"## {cat}", "",
                  "| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |",
                  "|---|---|---|---|---|"]
        for op, n, desc, short in by_cat[cat]:
            if op in nv:
                nvd = nv[op][1]
            elif op in nv_other:
                nvd = f"*not in Ada table; NVIDIA {nv_other[op][0]} table:* {nv_other[op][1]}"
            else:
                nvd = f"*not in NVIDIA tables*: {desc}"
            lines.append(f"| [{op}]({op}.md) | {nvd} | {ORIGIN.get(op, '')} | {short} | {n} |")
        lines.append("")
    (OUT / "INDEX.md").write_text("\n".join(lines))
    print(f"{len(summary)} opcodes; {len(missing_nv)} not in NVIDIA table: {' '.join(missing_nv)}; "
          f"{n_ver} verified by probes")


if __name__ == "__main__":
    main()
