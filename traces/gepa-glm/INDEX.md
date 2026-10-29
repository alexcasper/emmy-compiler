# Traces — our compiler output, followed all the way down

Per input: `source.<arch>.ptx` -> ptxas (`-O3`) -> nvdisasm (`-hex -c`) -> SASS listing with per-instruction KB refs, plus an opcode->KB cross-ref and an sm_89/sm_120 divergence summary in `README.md`. Regenerate with `python3 tools/trace.py`.

| input | sm_89 | sm_120 | divergence headline |
|---|---|---|---|
| [r04_row_sum](README.md → `r04_row_sum/`) | 136 instr / 25 ops | 144 instr / 30 ops | 23 shared, 2 replaced per KB, 7 sm_120-only |
