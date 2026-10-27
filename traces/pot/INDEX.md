# Traces — our compiler output, followed all the way down

Per input: `source.<arch>.ptx` -> ptxas (`-O3`) -> nvdisasm (`-hex -c`) -> SASS listing with per-instruction KB refs, plus an opcode->KB cross-ref and an sm_89/sm_120 divergence summary in `README.md`. Regenerate with `python3 tools/trace.py`.

| input | sm_89 | sm_120 | divergence headline |
|---|---|---|---|
| [pot_r1_p00_scalar_add](README.md → `pot_r1_p00_scalar_add/`) | FAILED: ptxas fatal   : Ptx assembly aborted due | FAILED: ptxas fatal   : Ptx assembly aborted due | — |
