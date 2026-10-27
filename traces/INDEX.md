# Traces — our compiler output, followed all the way down

Every set is produced by `tools/trace.py`: PTX -> `ptxas -O3` -> `nvdisasm -hex -c`
-> SASS listings with per-instruction KB links, an opcode->KB cross-ref per arch,
and an sm_89/sm_120 divergence summary per problem.

| set | what | traced against |
|---|---|---|
| [baseline/](baseline/INDEX.md) | all 15 problems + the hand-written example, default tuning | judge-arch compiler at trace time |
| [gepa-glm/](gepa-glm/INDEX.md) | GEPA glm-best tuning (div approx.ftz, nc_loads, rcp/sqrt approx) | same; see [COMPARISON.md](gepa-glm/COMPARISON.md) |
| [gepa-flint/](gepa-flint/INDEX.md) | GEPA flint-best tuning (nc_loads only) | same; see [COMPARISON.md](gepa-flint/COMPARISON.md) |
| [pot/](pot/README.md) | DSPy PoT candidate — negative result (ptxas rejects both rounds) | — |

Regenerate:
- baseline: `python3 tools/trace.py` (writes traces/baseline via --out default)
- a single PTX: `python3 tools/trace.py --ptx file.ptx --out traces/baseline`
- compare two sets: `python3 tools/trace.py --compare traces traces-gepa`

Caveats: comparisons are mnemonic-level (modifier-only changes like LDG.E vs
LDG.E.CONSTANT are invisible); the sm_89 vs sm_120 divergence catalog lives in
[sm120/verify/RESULTS.md](../sm120/verify/RESULTS.md).
