# QMMA (SM89 SASS)

**NVIDIA:** not listed in the official Ampere/Ada opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)). NVIDIA's Blackwell/Rubin table lists it as "FP8 Matrix Multiply and Accumulate Across a Warp" ([same document](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html)).

Notes: FP8 (e4m3/e5m2) tensor-core MMA - new on sm_89 (category: Tensor core (MMA))

Typically emitted for: `mma.sync.aligned.m16n8k32.row.col.f32.e4m3/e5m2.e4m3/e5m2.f32` (FP8, PTX 8.4+, sm_89)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [qmma_e4m3](../verify/RESULTS.md#qmma_e4m3): `mma.sync.aligned.m16n8k32.row.col.f32.e4m3.e4m3.f32 (FP8, PTX 8.4)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/QMMA.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [QMMA_R_R_R_R](#v1)
- [QMMA_R_R_R_R_R_I](#v2)
- [QMMA_R_R_R_R_UP](#v3)
- [QMMA_R_R_R_R_UP_R_I](#v4)

<a id="v1"></a>
## 1. `QMMA_R_R_R_R`

Syntax: `QMMA R, R, R, R`  
Example: `@P0 QMMA.16816.F16.E4M3.E4M3 R0, R0.ROW, R0.???0, R0;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| modi (op 1) | 73 |
| modi (op 2) | 74 |
| modi 1 | 75-76 |
| modi 2 | 77 |
| modi 3 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010111100100............................00000000000000000000000.
................0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `16816.` |
| `01` | `16832.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `F32.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `E4M3.` |
| `01` | `E5M2.` |
| `10` | `E5M2.` |
| `11` | `E5M2.E5M2.` |

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
## 2. `QMMA_R_R_R_R_R_I`

Syntax: `QMMA.SP R, R, R, R, R, INT_IMM`  
Example: `@P0 QMMA.SP.INVALID0.F16.E4M3.E4M3 R0, R0.ROW, R0.???0, R0, R0, 0x0;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 4 | 40-47 |
| operand 5 | 48-50 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| modi (op 1) | 73 |
| modi (op 2) | 74 |
| modi 1 | 75-76 |
| modi 2 | 77 |
| modi 3 | 78-79 |
| REGOFFSET | 81 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010111100100.......................................000000000000.
................1.00000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `INVALID0.` |
| `01` | `16832.` |
| `10` | `16864.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `F32.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `E4M3.` |
| `01` | `E5M2.` |
| `10` | `E5M2.` |
| `11` | `E5M2.E5M2.` |

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

<a id="v3"></a>
## 3. `QMMA_R_R_R_R_UP`

Syntax: `QMMA R, R, R, R, UP`  
Example: `@P0 QMMA.16816.F16.E4M3.E4M3 R0, R0.ROW, R0.???0, R0, UP6;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (1 slots); READ R (2 slots); READ UP (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| modi (op 1) | 73 |
| modi (op 2) | 74 |
| modi 1 | 75-76 |
| modi 2 | 77 |
| modi 3 | 78-79 |
| operand 4 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010111100100............................00000000000000000000000.
................00000001...00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `16816.` |
| `01` | `16832.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `F32.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `E4M3.` |
| `01` | `E5M2.` |
| `10` | `E5M2.` |
| `11` | `E5M2.E5M2.` |

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

<a id="v4"></a>
## 4. `QMMA_R_R_R_R_UP_R_I`

Syntax: `QMMA.SP R, R, R, R, UP, R, INT_IMM`  
Example: `@P0 QMMA.SP.INVALID0.F16.E4M3.E4M3 R0, R0.ROW, R0.???0, R0, UP6, R0, 0x0;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots); READ R (2 slots); READ UP (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 5 | 40-47 |
| operand 6 | 48-50 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| modi (op 1) | 73 |
| modi (op 2) | 74 |
| modi 1 | 75-76 |
| modi 2 | 77 |
| modi 3 | 78-79 |
| REGOFFSET | 81 |
| operand 4 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010111100100.......................................000000000000.
................1.000001...00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `INVALID0.` |
| `01` | `16832.` |
| `10` | `16864.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `F32.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `E4M3.` |
| `01` | `E5M2.` |
| `10` | `E5M2.` |
| `11` | `E5M2.E5M2.` |

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

