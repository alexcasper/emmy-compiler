# USEL (SM89 SASS)

**NVIDIA:** Uniform Select (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform select (category: Uniform datapath)

Typically emitted for: warp-uniform select

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/USEL.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [USEL_UR_UR_I_UP](#v1)
- [USEL_UR_UR_UR_UP](#v2)

<a id="v1"></a>
## 1. `USEL_UR_UR_I_UP`

Syntax: `USEL UR, UR, INT_IMM, UP`  
Example: `@UP0 USEL UR0, UR0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 86-89 |
| cNOT (op 3) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111000010001...........0.......0................................
0000000000000000000000.....10000000000000.....................00
```

<a id="v2"></a>
## 2. `USEL_UR_UR_UR_UP`

Syntax: `USEL UR, UR, UR, UP`  
Example: `@UP0 USEL UR0, UR0, UR0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| operand 3 | 86-89 |
| cNOT (op 3) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111000010100...........0.......0.......0000000000000000000000000
0000000000000000000000.....10000000000000.....................00
```

