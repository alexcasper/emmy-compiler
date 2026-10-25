# Traces — our compiler output, followed all the way down

Per input: `source.<arch>.ptx` -> ptxas (`-O3`) -> nvdisasm (`-hex -c`) -> SASS listing with per-instruction KB refs, plus an opcode->KB cross-ref and an sm_89/sm_120 divergence summary in `README.md`. Regenerate with `python3 tools/trace.py`.

| input | sm_89 | sm_120 | divergence headline |
|---|---|---|---|
| [k_sum_1_reduce](README.md → `k_sum_1_reduce/`) | 96 instr / 21 ops | 96 instr / 27 ops | 20 shared, 1 replaced per KB, 7 sm_120-only |
| [a01_attention](README.md → `a01_attention/`) | 1760 instr / 29 ops | 1760 instr / 31 ops | 27 shared, 1 replaced per KB, 4 sm_120-only |
| [a02_attention_128](README.md → `a02_attention_128/`) | 416 instr / 28 ops | 416 instr / 30 ops | 26 shared, 1 replaced per KB, 4 sm_120-only |
| [f01_rmsnorm](README.md → `f01_rmsnorm/`) | 280 instr / 31 ops | 288 instr / 36 ops | 29 shared, 1 replaced per KB, 7 sm_120-only |
| [f02_row_softmax](README.md → `f02_row_softmax/`) | 440 instr / 32 ops | 456 instr / 38 ops | 30 shared, 1 replaced per KB, 8 sm_120-only |
| [f03_l2norm](README.md → `f03_l2norm/`) | 264 instr / 31 ops | 272 instr / 36 ops | 29 shared, 1 replaced per KB, 7 sm_120-only |
| [m01_matmul_512](README.md → `m01_matmul_512/`) | 512 instr / 25 ops | 536 instr / 31 ops | 22 shared, 1 replaced per KB, 9 sm_120-only |
| [m02_matmul_rect](README.md → `m02_matmul_rect/`) | 280 instr / 26 ops | 288 instr / 31 ops | 22 shared, 2 replaced per KB, 9 sm_120-only |
| [p00_scalar_add](README.md → `p00_scalar_add/`) | 32 instr / 14 ops | 40 instr / 14 ops | 12 shared, 1 replaced per KB, 2 sm_120-only |
| [p01_vector_add](README.md → `p01_vector_add/`) | 32 instr / 14 ops | 40 instr / 14 ops | 12 shared, 1 replaced per KB, 2 sm_120-only |
| [p02_scale_shift](README.md → `p02_scale_shift/`) | 48 instr / 14 ops | 48 instr / 14 ops | 12 shared, 1 replaced per KB, 2 sm_120-only |
| [p03_relu_mul](README.md → `p03_relu_mul/`) | 48 instr / 15 ops | 56 instr / 15 ops | 13 shared, 1 replaced per KB, 2 sm_120-only |
| [r01_array_sum](README.md → `r01_array_sum/`) | 104 instr / 22 ops | 112 instr / 27 ops | 21 shared, 1 replaced per KB, 6 sm_120-only |
| [r02_big_sum](README.md → `r02_big_sum/`) | 104 instr / 22 ops | 112 instr / 27 ops | 21 shared, 1 replaced per KB, 6 sm_120-only |
| [r03_mean](README.md → `r03_mean/`) | 216 instr / 29 ops | 224 instr / 34 ops | 28 shared, 1 replaced per KB, 6 sm_120-only |
| [r04_row_sum](README.md → `r04_row_sum/`) | 152 instr / 25 ops | 160 instr / 30 ops | 23 shared, 1 replaced per KB, 7 sm_120-only |
