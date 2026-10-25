# DMMA (SM89 SASS)

**NVIDIA:** Matrix Multiply and Accumulate (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: FP64 tensor-core MMA (m8n8k4) (category: Tensor core (MMA))

Typically emitted for: `mma.sync.aligned.m8n8k4.f64`

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [dmma](../verify/RESULTS.md#dmma): `mma.sync.aligned.m8n8k4.row.col.f64.f64.f64.f64`

Encodings: <https://kuterdinel.com/nv_isa_sm89/DMMA.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [DMMA_R_R_R_R](#v1)
- [DMMA_R_R_R_R_UP](#v2)

<a id="v1"></a>
## 1. `DMMA_R_R_R_R`

Syntax: `DMMA R, R, R, R`  
Example: `@P0 DMMA.884 R0, R0, R0, R0 ;`

Register access: WRITE R (4 slots); READ R (2 slots); READ R (2 slots); READ R (4 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| cABS (op 3) | 74 |
| cNEG (op 3) | 75 |
| modi 1 | 76 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111111000100............................0000000000000000000000..
.............0..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `884.` |
| `1` | `???1.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v2"></a>
## 2. `DMMA_R_R_R_R_UP`

Syntax: `DMMA R, R, R, R, UP`  
Example: `@P0 DMMA.884 R0, R0, R0, R0, UP6 ;`

Register access: WRITE R (4 slots); READ R (2 slots); READ R (2 slots); READ R (4 slots); READ UP (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| cABS (op 3) | 74 |
| cNEG (op 3) | 75 |
| modi 1 | 76 |
| modi 2 | 78-79 |
| operand 4 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111111000100............................0000000000000000000000..
.............0..00000001...00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `884.` |
| `1` | `???1.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

