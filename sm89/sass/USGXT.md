# USGXT (SM89 SASS)

**NVIDIA:** Uniform Sign Extend (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform sign extend (category: Uniform datapath)

Typically emitted for: warp-uniform sign extension

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/USGXT.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [USGXT_UR_UR_I](#v1)
- [USGXT_UR_UR_UR](#v2)

<a id="v1"></a>
## 1. `USGXT_UR_UR_I`

Syntax: `USGXT UR, UR, INT_IMM`  
Example: `@UP0 USGXT.U32 UR0, UR0, 0x0;`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| modi 1 | 73 |
| W | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010110010001...........0.......0................................
000000000.0.00000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v2"></a>
## 2. `USGXT_UR_UR_UR`

Syntax: `USGXT UR, UR, UR`  
Example: `@UP0 USGXT.U32 UR0, UR0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| modi 1 | 73 |
| W | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010110010100...........0.......0.......0000000000000000000000000
000000000.0.00000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

