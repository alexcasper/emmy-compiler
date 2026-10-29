# Trace: pot_r1_p00_scalar_add

- Source: gen/trace_src/pot/pot_r1_p00_scalar_add.ptx
- Generated: 2026-10-26 19:04 UTC
- Tools: ptxas `Cuda compilation tools, release 12.9, V12.9.86`, nvdisasm `Cuda compilation tools, release 12.9, V12.9.88`, both `-O3`
- The sm_120 stage consumes a header-retargeted copy of the same PTX (`.target sm_120`, `.version` bumped to >= 8.7); the body is untouched.

- **sm_89: stage 1 FAILED** — `ptxas fatal   : Ptx assembly aborted due to errors`
- **sm_120: stage 1 FAILED** — `ptxas fatal   : Ptx assembly aborted due to errors`
## sm_89 opcode -> KB cross-ref

| opcode | count | KB page | NVIDIA description | NAK cross-check |
|---|---|---|---|---|

## sm_120 opcode -> KB cross-ref

| opcode | count | KB page | NVIDIA description | NAK cross-check |
|---|---|---|---|---|

## sm_89 vs sm_120 divergence summary

Same source PTX, two toolchain targets. Opcode sets are per-mnemonic (nvspas form bits ignored). Renames/replacements cite the sm120 KB divergence notes ([verify/RESULTS.md](../../../sm120/verify/RESULTS.md), [README](../../../sm120/README.md)).

**Shared opcodes (0):** —

Full per-arch tables above; the general (input-independent) divergence catalog lives in [sm120/verify/RESULTS.md](../../../sm120/verify/RESULTS.md).

