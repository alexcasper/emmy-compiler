# Trace comparison: HEAD compiler (b230d47, default tuning) vs GEPA-flint best (EMMY_TUNING: nc_loads only)

- baseline: `traces`
- candidate: `traces-gepa-flint`
- Deltas are candidate minus baseline, per problem and arch. Delta opcodes are annotated from the sm120 KB divergence maps (tools/trace.py).

| problem | arch | instr Δ | opcodes added (vs baseline) | opcodes gone |
|---|---|---|---|---|
| a01_attention | sm_89 | +0 | — | — |
| a02_attention_128 | sm_89 | +0 | — | — |
| f01_rmsnorm | sm_89 | +0 | `IMAD` (no KB rename known (may still exist in the ISA)), `MOV` (KB note: sm_120 loads kernel params via LDC/LDCU directly (KB: prologue divergence); MOV still exists in the sm_120 ISA but ptxas stops using it here) | `NOP` (no KB rename known (may still exist in the ISA)) |
| f02_row_softmax | sm_89 | +0 | — | — |
| f03_l2norm | sm_89 | +0 | — | — |
| m01_matmul_512 | sm_89 | +0 | — | — |
| m02_matmul_rect | sm_89 | +0 | — | — |
| p00_scalar_add | sm_89 | +0 | — | — |
| p01_vector_add | sm_89 | +0 | — | — |
| p02_scale_shift | sm_89 | +0 | — | — |
| p03_relu_mul | sm_89 | +0 | — | — |
| r01_array_sum | sm_89 | +0 | — | — |
| r02_big_sum | sm_89 | +0 | — | — |
| r03_mean | sm_89 | +0 | — | — |
| r04_row_sum | sm_89 | +0 | — | — |
| a01_attention | sm_120 | +0 | — | — |
| a02_attention_128 | sm_120 | +0 | — | — |
| f01_rmsnorm | sm_120 | +0 | — | — |
| f02_row_softmax | sm_120 | +0 | — | — |
| f03_l2norm | sm_120 | +0 | — | — |
| m01_matmul_512 | sm_120 | +0 | — | — |
| m02_matmul_rect | sm_120 | +0 | — | — |
| p00_scalar_add | sm_120 | +0 | — | — |
| p01_vector_add | sm_120 | +0 | — | — |
| p02_scale_shift | sm_120 | +0 | — | — |
| p03_relu_mul | sm_120 | +0 | — | — |
| r01_array_sum | sm_120 | +0 | — | — |
| r02_big_sum | sm_120 | +0 | — | — |
| r03_mean | sm_120 | +0 | — | — |
| r04_row_sum | sm_120 | +0 | — | — |


## Hand-written findings (emmy-a1n)

- `nc_loads` alone produces **zero opcode-level deltas** on either arch (all 30 rows +0): LDG.NC
  shares LDG's mnemonic. The effect is one modifier bit per load — `LDG.E` -> `LDG.E.CONSTANT`
  (word1 ...0x1900 -> ...0x9900); see a01_attention. Any future --compare mode should surface
  modifier-level (encoding) deltas, not just mnemonics.
- Fires on 13/15 problems; the matmuls are the exceptions (readonly_buffers analysis gap).
