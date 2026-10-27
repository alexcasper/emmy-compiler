"""Deterministic PTX->SASS probe — static candidate screening without a GPU.

The runner JITs/offline-compiles our PTX with ptxas before executing, so SASS
— not PTX — is the ground truth for speed. This probe reproduces that
compilation locally (same ptxas, same arch flag) and extracts structural
metrics that are exactly reproducible:

  - register count / spill bytes           (from ptxas -v)
  - total SASS instructions + opcode mix   (from nvdisasm)
  - memory-op inventory by width           (LDG.E.128 vs .32, LDS.64, ...)
  - hot-loop profile: the innermost backward branch's body, classified
    (FFMA / LDS / LDG / IMAD / ISETP / branch-overhead)

Deterministic by construction: fixed toolchain, no timestamps, no threading.
Usage:
  .venv/bin/python bench/sass_probe.py compile.py IR.json [more...]
  .venv/bin/python bench/sass_probe.py --all            # every task problem
Outputs one JSON object per problem to stdout.
"""
import collections
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
PTXAS = os.path.join(ROOT, ".tools/ptxas13/ptxas")  # 13.0 — matches the judge
# runner (Blackwell sm_120, verified register-for-register via submit.py)
NVDISASM = os.path.join(ROOT, ".tools/bin/nvdisasm")
ARCH = os.environ.get("SASS_ARCH", "sm_120")


def _run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120, **kw)
    if r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} failed:\n{r.stderr[-500:]}")
    return r.stdout + r.stderr


def sass_report(ir_path, candidate=None):
    candidate = candidate or os.path.join(ROOT, "compile.py")
    ptx = _run([sys.executable, candidate, ir_path])
    ptx = ptx.encode()
    assert ptx.decode("ascii", errors="strict"), "PTX must be pure ASCII"
    entry = re.search(r"\.visible \.entry (\w+)", ptx.decode()).group(1)

    # ptxas -v: registers + spills, and the cubin for disassembly
    v = _run([PTXAS, f"-arch={ARCH}", "-v", "-", "-o", "/dev/null"],
             input=ptx.decode())
    regs = re.search(r"Used (\d+) registers", v)
    spills = re.search(r"(\d+) bytes spill stores", v)

    with open("/tmp/sass_probe.ptx", "wb") as f:
        f.write(ptx)
    _run([PTXAS, f"-arch={ARCH}", "/tmp/sass_probe.ptx", "-o", "/tmp/sass_probe.cubin"])
    sass = _run([NVDISASM, "-c", "/tmp/sass_probe.cubin"])

    # instruction lines look like:  /*1e90*/  @!P0 OP.MOD args ; /* ctrl */
    # branch targets are symbolic labels (.L_x_n), defined on their own line
    ilines, label_addr, pending = [], {}, []
    for line in sass.splitlines():
        lm = re.match(r"\s*(\.L_x_\d+):", line)
        if lm:
            pending.append(lm.group(1))
            continue
        m = re.match(r"\s*/\*([0-9a-f]+)\*/\s+(?:@!?P\d\s+)?([A-Z][A-Z0-9._]*)", line)
        if m:
            addr = int(m.group(1), 16)
            ilines.append((addr, m.group(2), line))
            for lbl in pending:
                label_addr[lbl] = addr
            pending = []
    addrs = [a for a, _, _ in ilines]

    # backward branches = loop edges; innermost loop = smallest body span
    loops = []
    for addr, op, line in ilines:
        if op.startswith("BRA"):
            lm = re.search(r"BRA `?\(?(\.L_x_\d+)", line)
            tgt = label_addr.get(lm.group(1)) if lm else None
            if tgt is not None and tgt < addr:
                loops.append((tgt, addr))
    inner = min(loops, key=lambda ta: ta[1] - ta[0]) if loops else None

    hot = collections.Counter()
    if inner:
        t, a_end = inner
        for addr, op, _ in ilines:
            if t <= addr <= a_end:
                hot[op.split(".")[0]] += 1

    mem = collections.Counter()
    for _, op, _ in ilines:
        if op.startswith(("LDG", "STG", "LDS", "STS", "LDGSTS")):
            mem[op] += 1

    return {
        "entry": entry,
        "registers": int(regs.group(1)) if regs else None,
        "spill_bytes": int(spills.group(1)) if spills else 0,
        "total_sass_instrs": len(ilines),
        "opcode_mix": dict(collections.Counter(op.split(".")[0] for _, op, _ in ilines)
                           .most_common()),
        "mem_ops": dict(sorted(mem.items())),
        "hot_loop": ({"span": inner[1] - inner[0], "instrs": sum(hot.values()),
                      "mix": dict(hot.most_common())} if inner else None),
    }


def main():
    argv = sys.argv[1:]
    irs = []
    if argv and argv[0] == "--all":
        base = os.path.join(ROOT, "task/problems")
        for d in sorted(os.listdir(base)):
            if not os.path.isdir(os.path.join(base, d)):
                continue
            irs += [os.path.join(base, d, f) for f in os.listdir(os.path.join(base, d))
                    if f.endswith(".ir.json")]
    else:
        irs = argv
    for ir in irs:
        rep = sass_report(ir)
        rep["problem"] = os.path.basename(ir).replace(".ir.json", "")
        print(json.dumps(rep, sort_keys=True))


if __name__ == "__main__":
    main()
