#!/usr/bin/env python3
"""Compare two trace sets produced by tools/trace.py.

Usage: python3 tools/trace_compare.py BASELINE CANDIDATE [-o OUT.md]

Reads every <name>/<arch>.sass.md in both roots and emits a markdown report:
per problem and per arch, instruction-count deltas and opcode-set deltas, with
each delta opcode annotated from the KB divergence maps (renames / KB-gap).
The report is meant to be committed next to the candidate traces (e.g.
traces-gepa/COMPARISON.md).
"""
from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from trace import GONE_NOTES, RENAMES  # noqa: E402

ROW_RE = re.compile(r"^\|\s*\|\s*`(.+?)`\s*\|")
PRED_RE = re.compile(r"^@!?U?P[T0-9]+\s+")


def opcode(text: str) -> str:
    return PRED_RE.sub("", text).split()[0].split(".")[0]


def load_set(trace_root: pathlib.Path, arch: str):
    """-> {problem: (n_instr, Counter(opcode))} from <root>/<name>/<arch>.sass.md."""
    out = {}
    for d in sorted(p for p in trace_root.iterdir() if p.is_dir()):
        f = d / f"{arch}.sass.md"
        if not f.exists():
            continue
        ops = collections.Counter()
        n = 0
        for line in f.read_text().splitlines():
            m = ROW_RE.match(line)
            if not m:
                continue
            n += 1
            ops[opcode(m.group(1))] += 1
        out[d.name] = (n, ops)
    return out


def annotate(op: str) -> str:
    if op in RENAMES:
        return f"KB rename/replacement: {RENAMES[op]}"
    if op in GONE_NOTES:
        return f"KB note: {GONE_NOTES[op]}"
    return "no KB rename known (may still exist in the ISA)"


def compare(baseline: pathlib.Path, candidate: pathlib.Path, label: str) -> str:
    lines = [f"# Trace comparison: {label}", "",
             f"- baseline: `{baseline}`",
             f"- candidate: `{candidate}`",
             "- Deltas are candidate minus baseline, per problem and arch. Delta opcodes are "
             "annotated from the sm120 KB divergence maps (tools/trace.py).", "",
             "| problem | arch | instr Δ | opcodes added (vs baseline) | opcodes gone |",
             "|---|---|---|---|---|"]
    n_problems = 0
    for arch in ("sm_89", "sm_120"):
        base = load_set(baseline, arch)
        cand = load_set(candidate, arch)
        for name in sorted(set(base) & set(cand)):
            n_problems += 1
            bn, bops = base[name]
            cn, cops = cand[name]
            added = sorted(cops - bops)
            gone = sorted(bops - cops)
            a_txt = ", ".join(f"`{o}` ({annotate(o)})" for o in added) or "—"
            g_txt = ", ".join(f"`{o}` ({annotate(o)})" for o in gone) or "—"
            sign = "+" if cn - bn >= 0 else ""
            lines.append(f"| {name} | {arch} | {sign}{cn - bn} | {a_txt} | {g_txt} |")
    lines.append("")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("baseline", type=pathlib.Path)
    ap.add_argument("candidate", type=pathlib.Path)
    ap.add_argument("-o", "--out", type=pathlib.Path, default=None)
    ap.add_argument("--label", default=None)
    args = ap.parse_args()
    label = args.label or f"{args.baseline} vs {args.candidate}"
    md = compare(args.baseline, args.candidate, label)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(md)
        print(f"wrote {args.out} ({n_problems_str(md)} problem rows)")
    else:
        print(md)


def n_problems_str(md: str) -> str:
    return str(sum(1 for ln in md.splitlines() if ln.startswith("| ") and " | sm_" in ln))


if __name__ == "__main__":
    main()
