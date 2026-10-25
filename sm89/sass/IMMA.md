# IMMA (SM89 SASS)

**NVIDIA:** Integer Matrix Multiply and Accumulate (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Integer (s8/u8/s4/u4) tensor-core MMA (category: Tensor core (MMA))

Typically emitted for: `mma.sync.*.s8/u8/s4/u4`; `wmma` integer

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x237 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4520)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [imma](../verify/RESULTS.md#imma): `mma.sync.aligned.m16n8k32.row.col.s32.s8.s8.s32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/IMMA.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [IMMA_R_R_R_R](#v1)
- [IMMA_R_R_R_R_R_I](#v2)
- [IMMA_R_R_R_R_UP](#v3)
- [IMMA_R_R_R_R_UP_R_I](#v4)

<a id="v1"></a>
## 1. `IMMA_R_R_R_R`

Syntax: `IMMA R, R, R, R`  
Example: `@P0 IMMA.8816.U8.U8 R0, R0.ROW, R0.???0, R0 ;`

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
| modi 1 | 75-79 |
| SAT | 82 |
| modi 2 | 83-84 |
| modi 3 | 85-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111011000100............................000000000000000000000000
........0.......00.....000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00000` | `8816.` |
| `00001` | `INVALID1.` |
| `00010` | `8816.S8.` |
| `00011` | `INVALID1.S8.` |
| `00100` | `8816.INVALID2.` |
| `00101` | `INVALID1.INVALID2.` |
| `00110` | `8816.INVALID3.` |
| `00111` | `INVALID1.INVALID3.` |
| `01000` | `8816.S8.` |
| `01001` | `INVALID1.S8.` |
| `01010` | `8816.S8.S8.` |
| `01011` | `INVALID1.S8.S8.` |
| `01100` | `8816.INVALID2.S8.` |
| `01101` | `INVALID1.INVALID2.S8.` |
| `01110` | `8816.INVALID3.S8.` |
| `01111` | `INVALID1.INVALID3.S8.` |
| `10000` | `8816.INVALID2.` |
| `10001` | `INVALID1.INVALID2.` |
| `10010` | `8816.S8.INVALID2.` |
| `10011` | `INVALID1.S8.INVALID2.` |
| `10100` | `8816.INVALID2.INVALID2.` |
| `10101` | `INVALID1.INVALID2.INVALID2.` |
| `10110` | `8816.INVALID3.INVALID2.` |
| `10111` | `INVALID1.INVALID3.INVALID2.` |
| `11000` | `8816.INVALID3.` |
| `11001` | `INVALID1.INVALID3.` |
| `11010` | `8816.S8.INVALID3.` |
| `11011` | `INVALID1.S8.INVALID3.` |
| `11100` | `8816.INVALID2.INVALID3.` |
| `11101` | `INVALID1.INVALID2.INVALID3.` |
| `11110` | `8816.INVALID3.INVALID3.` |
| `11111` | `INVALID1.INVALID3.INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U4.` |
| `10` | `U4.` |
| `11` | `U4.U4.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `8816.` |
| `01` | `8832.` |
| `10` | `16816.` |
| `11` | `16864.` |

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
## 2. `IMMA_R_R_R_R_R_I`

Syntax: `IMMA.SP R, R, R, R, R, INT_IMM`  
Example: `@P0 IMMA.SP.INVALID0.U8.U8 R0, R0.ROW, R0.???0, R0, R0, 0x0 ;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 4 | 40-47 |
| operand 5 | 48-50 |
| operand 3 | 64-71 |
| modi (op 1) | 73 |
| modi (op 2) | 74 |
| modi 1 | 75-79 |
| SAT | 82 |
| modi 2 | 83-84 |
| modi 3 | 85-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111011000100.......................................0000000000000
........1.......00.....000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00000` | `INVALID0.` |
| `00001` | `INVALID1.` |
| `00010` | `INVALID0.S8.` |
| `00011` | `INVALID1.S8.` |
| `00100` | `INVALID0.INVALID2.` |
| `00101` | `INVALID1.INVALID2.` |
| `00110` | `INVALID0.INVALID3.` |
| `00111` | `INVALID1.INVALID3.` |
| `01000` | `INVALID0.S8.` |
| `01001` | `INVALID1.S8.` |
| `01010` | `INVALID0.S8.S8.` |
| `01011` | `INVALID1.S8.S8.` |
| `01100` | `INVALID0.INVALID2.S8.` |
| `01101` | `INVALID1.INVALID2.S8.` |
| `01110` | `INVALID0.INVALID3.S8.` |
| `01111` | `INVALID1.INVALID3.S8.` |
| `10000` | `INVALID0.INVALID2.` |
| `10001` | `INVALID1.INVALID2.` |
| `10010` | `INVALID0.S8.INVALID2.` |
| `10011` | `INVALID1.S8.INVALID2.` |
| `10100` | `INVALID0.INVALID2.INVALID2.` |
| `10101` | `INVALID1.INVALID2.INVALID2.` |
| `10110` | `INVALID0.INVALID3.INVALID2.` |
| `10111` | `INVALID1.INVALID3.INVALID2.` |
| `11000` | `INVALID0.INVALID3.` |
| `11001` | `INVALID1.INVALID3.` |
| `11010` | `INVALID0.S8.INVALID3.` |
| `11011` | `INVALID1.S8.INVALID3.` |
| `11100` | `INVALID0.INVALID2.INVALID3.` |
| `11101` | `INVALID1.INVALID2.INVALID3.` |
| `11110` | `INVALID0.INVALID3.INVALID3.` |
| `11111` | `INVALID1.INVALID3.INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U4.` |
| `10` | `U4.` |
| `11` | `U4.U4.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `INVALID0.` |
| `01` | `8832.` |
| `10` | `INVALID4.` |
| `11` | `16864.` |

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
## 3. `IMMA_R_R_R_R_UP`

Syntax: `IMMA R, R, R, R, UP`  
Example: `@P0 IMMA.8816.U8.U8 R0, R0.ROW, R0.???0, R0, UP6 ;`

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
| modi 1 | 75-79 |
| SAT | 82 |
| modi 2 | 83-84 |
| modi 3 | 85-86 |
| operand 4 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111011000100............................000000000000000000000000
........0.......00.....1...00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00000` | `8816.` |
| `00001` | `INVALID1.` |
| `00010` | `8816.S8.` |
| `00011` | `INVALID1.S8.` |
| `00100` | `8816.INVALID2.` |
| `00101` | `INVALID1.INVALID2.` |
| `00110` | `8816.INVALID3.` |
| `00111` | `INVALID1.INVALID3.` |
| `01000` | `8816.S8.` |
| `01001` | `INVALID1.S8.` |
| `01010` | `8816.S8.S8.` |
| `01011` | `INVALID1.S8.S8.` |
| `01100` | `8816.INVALID2.S8.` |
| `01101` | `INVALID1.INVALID2.S8.` |
| `01110` | `8816.INVALID3.S8.` |
| `01111` | `INVALID1.INVALID3.S8.` |
| `10000` | `8816.INVALID2.` |
| `10001` | `INVALID1.INVALID2.` |
| `10010` | `8816.S8.INVALID2.` |
| `10011` | `INVALID1.S8.INVALID2.` |
| `10100` | `8816.INVALID2.INVALID2.` |
| `10101` | `INVALID1.INVALID2.INVALID2.` |
| `10110` | `8816.INVALID3.INVALID2.` |
| `10111` | `INVALID1.INVALID3.INVALID2.` |
| `11000` | `8816.INVALID3.` |
| `11001` | `INVALID1.INVALID3.` |
| `11010` | `8816.S8.INVALID3.` |
| `11011` | `INVALID1.S8.INVALID3.` |
| `11100` | `8816.INVALID2.INVALID3.` |
| `11101` | `INVALID1.INVALID2.INVALID3.` |
| `11110` | `8816.INVALID3.INVALID3.` |
| `11111` | `INVALID1.INVALID3.INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U4.` |
| `10` | `U4.` |
| `11` | `U4.U4.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `8816.` |
| `01` | `8832.` |
| `10` | `16816.` |
| `11` | `16864.` |

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
## 4. `IMMA_R_R_R_R_UP_R_I`

Syntax: `IMMA.SP R, R, R, R, UP, R, INT_IMM`  
Example: `@P0 IMMA.SP.INVALID0.U8.U8 R0, R0.ROW, R0.???0, R0, UP6, R0, 0x0 ;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (2 slots); READ R (2 slots); READ UP (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 5 | 40-47 |
| operand 6 | 48-50 |
| operand 3 | 64-71 |
| modi (op 1) | 73 |
| modi (op 2) | 74 |
| modi 1 | 75-79 |
| SAT | 82 |
| modi 2 | 83-84 |
| modi 3 | 85-86 |
| operand 4 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111011000100.......................................0000000000000
........1.......00.....1...00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00000` | `INVALID0.` |
| `00001` | `INVALID1.` |
| `00010` | `INVALID0.S8.` |
| `00011` | `INVALID1.S8.` |
| `00100` | `INVALID0.INVALID2.` |
| `00101` | `INVALID1.INVALID2.` |
| `00110` | `INVALID0.INVALID3.` |
| `00111` | `INVALID1.INVALID3.` |
| `01000` | `INVALID0.S8.` |
| `01001` | `INVALID1.S8.` |
| `01010` | `INVALID0.S8.S8.` |
| `01011` | `INVALID1.S8.S8.` |
| `01100` | `INVALID0.INVALID2.S8.` |
| `01101` | `INVALID1.INVALID2.S8.` |
| `01110` | `INVALID0.INVALID3.S8.` |
| `01111` | `INVALID1.INVALID3.S8.` |
| `10000` | `INVALID0.INVALID2.` |
| `10001` | `INVALID1.INVALID2.` |
| `10010` | `INVALID0.S8.INVALID2.` |
| `10011` | `INVALID1.S8.INVALID2.` |
| `10100` | `INVALID0.INVALID2.INVALID2.` |
| `10101` | `INVALID1.INVALID2.INVALID2.` |
| `10110` | `INVALID0.INVALID3.INVALID2.` |
| `10111` | `INVALID1.INVALID3.INVALID2.` |
| `11000` | `INVALID0.INVALID3.` |
| `11001` | `INVALID1.INVALID3.` |
| `11010` | `INVALID0.S8.INVALID3.` |
| `11011` | `INVALID1.S8.INVALID3.` |
| `11100` | `INVALID0.INVALID2.INVALID3.` |
| `11101` | `INVALID1.INVALID2.INVALID3.` |
| `11110` | `INVALID0.INVALID3.INVALID3.` |
| `11111` | `INVALID1.INVALID3.INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U4.` |
| `10` | `U4.` |
| `11` | `U4.U4.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `INVALID0.` |
| `01` | `8832.` |
| `10` | `INVALID4.` |
| `11` | `16864.` |

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

