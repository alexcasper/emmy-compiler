# Traces — our compiler output, followed all the way down

Per input: `source.<arch>.ptx` -> ptxas (`-O3`) -> nvdisasm (`-hex -c`) -> SASS listing with per-instruction KB refs, plus an opcode->KB cross-ref and an sm_89/sm_120 divergence summary in `README.md`. Regenerate with `python3 tools/trace.py`.

| input | sm_89 | sm_120 | divergence headline |
|---|---|---|---|
| [r04_row_sum](README.md → `r04_row_sum/`) | 136 instr / 25 ops | 144 instr / 30 ops | 23 shared, 2 replaced per KB, 7 sm_120-only |

Compare two trace roots: `python3 tools/trace.py --compare BASELINE CANDIDATE` — writes CANDIDATE/COMPARISON.md (per-problem instruction-count and opcode-set deltas per arch, delta opcodes annotated from the KB divergence maps; see tools/trace_compare.py). Note: mnemonic-level only — modifier-only changes (e.g. LDG.E vs LDG.E.CONSTANT) are invisible; see traces-gepa-flint/COMPARISON.md findings.
