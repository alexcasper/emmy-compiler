# BMMA (SM89 SASS)

**NVIDIA:** Bit Matrix Multiply and Accumulate (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Binary (1-bit) tensor-core MMA (category: Tensor core (MMA))

Typically emitted for: `mma.sync.*.b1` (xor/and popc)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [bmma](../verify/RESULTS.md#bmma): `mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc`

Encodings: <https://kuterdinel.com/nv_isa_sm89/BMMA.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [BMMA_R_R_R_R](#v1)
- [BMMA_R_R_R_R_UP](#v2)

<a id="v1"></a>
## 1. `BMMA_R_R_R_R`

Syntax: `BMMA R, R, R, R`  
Example: `@P0 BMMA.88128.XOR.???0 R0, R0.ROW, R0.???0, R0 ;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
| modi (op 1) | 73 |
| modi (op 2) | 74 |
| modi 1 | 75-76 |
| modi 2 | 77-78 |
| modi 3 | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101111000100............................000000000000000000000000
........0......0.000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `88128.` |
| `01` | `168128.` |
| `10` | `168256.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `XOR.` |
| `01` | `INVALID1.` |
| `10` | `AND.` |
| `11` | `INVALID3.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `POPC.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `0` | `ROW.` |
| `1` | `???1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `COL.` |

<a id="v2"></a>
## 2. `BMMA_R_R_R_R_UP`

Syntax: `BMMA R, R, R, R, UP`  
Example: `@P0 BMMA.88128.XOR.???0 R0, R0.ROW, R0.???0, R0, UP6 ;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ R (2 slots); READ UP (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
| modi (op 1) | 73 |
| modi (op 2) | 74 |
| modi 1 | 75-76 |
| modi 2 | 77-78 |
| modi 3 | 80 |
| operand 4 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101111000100............................000000000000000000000000
........0......0.0000001...00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `88128.` |
| `01` | `168128.` |
| `10` | `168256.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `XOR.` |
| `01` | `INVALID1.` |
| `10` | `AND.` |
| `11` | `INVALID3.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `POPC.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `0` | `ROW.` |
| `1` | `???1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `COL.` |

