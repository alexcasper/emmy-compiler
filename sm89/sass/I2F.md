# I2F (SM89 SASS)

**NVIDIA:** Integer To Floating Point Conversion (Conversion Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Integer to float conversion (category: Conversion)

Typically emitted for: `cvt.rn.f32.s32` etc. (64-bit / FP64 forms)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x5a, 0x106, 0x112 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2329)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [i2f](../verify/RESULTS.md#i2f): `cvt.rn.f64.s32`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 84 | `I2F.F64 R4, R4` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/I2F.html> (machine-derived by fuzzing the assembler; no semantics).

10 encoding variant(s):

- [I2F_R_I](#v1)
- [I2F_R_I](#v2)
- [I2F_R_c[I][I]](#v3)
- [I2F_R_cx[UR][I]](#v4)
- [I2F_R_c[I][I]](#v5)
- [I2F_R_cx[UR][I]](#v6)
- [I2F_R_UR](#v7)
- [I2F_R_UR](#v8)
- [I2F_R_R](#v9)
- [I2F_R_R](#v10)

<a id="v1"></a>
## 1. `I2F_R_I`

Syntax: `I2F.???0 R, INT_IMM`  
Example: `@P0 I2F.???0.U32 R0, 0x0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| modi 1 | 74-76 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000001001............00000000................................
0000000000...0..0000010000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `F16.U32.` |
| `011` | `F16.` |
| `100` | `U32.` |
| `101` | `(default)` |
| `110` | `???3.U32.` |
| `111` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v2"></a>
## 2. `I2F_R_I`

Syntax: `I2F R, INT_IMM`  
Example: `@P0 I2F.U64 R0, 0x0 ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| modi 1 | 74 |
| modi 2 | 75-76 |
| modi 3 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010001001............00000000................................
0000000000...0..0000110000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U64.` |
| `1` | `S64.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v3"></a>
## 3. `I2F_R_c[I][I]`

Syntax: `I2F R, c[INT_IMM][INT_IMM]`  
Example: `@P0 I2F.???0.U8 R0, c[0x0] [0x0] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| modi 1 | 74 |
| modi 2 | 75-76 |
| modi 3 | 78-79 |
| modi 4 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000001101............0000000000000000...................00000
0000000000...0..0000..0000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `F16.` |
| `10` | `(default)` |
| `11` | `???3.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U16.` |
| `10` | `U32.` |

<a id="v4"></a>
## 4. `I2F_R_cx[UR][I]`

Syntax: `I2F R, cx[UR][INT_IMM]`  
Example: `@P0 I2F.???0.U8 R0, cx[UR0] [0x0] ;`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| modi 1 | 74 |
| modi 2 | 75-76 |
| modi 3 | 78-79 |
| modi 4 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000001101............00000000.......0...............000000000
0000000000...0..0000..0000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `F16.` |
| `10` | `(default)` |
| `11` | `???3.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U16.` |
| `10` | `U32.` |

<a id="v5"></a>
## 5. `I2F_R_c[I][I]`

Syntax: `I2F R, c[INT_IMM][INT_IMM]`  
Example: `@P0 I2F.U64 R0, c[0x0][0x0] ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| modi 1 | 74 |
| modi 2 | 75-76 |
| modi 3 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010001101............0000000000000000...................00000
0000000000...0..0000110000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U64.` |
| `1` | `S64.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v6"></a>
## 6. `I2F_R_cx[UR][I]`

Syntax: `I2F R, cx[UR][INT_IMM]`  
Example: `@P0 I2F.U64 R0, cx[UR0][0x0] ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| modi 1 | 74 |
| modi 2 | 75-76 |
| modi 3 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010001101............00000000.......0...............000000000
0000000000...0..0000110000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U64.` |
| `1` | `S64.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v7"></a>
## 7. `I2F_R_UR`

Syntax: `I2F R, UR`  
Example: `@P0 I2F.???0.U8 R0, UR0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| modi (op 1) | 60-61 |
| modi 1 | 74 |
| modi 2 | 75-76 |
| modi 3 | 78-79 |
| modi 4 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000001011............00000000.......000000000000000000000..00
0000000000...0..0000..0000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `F16.` |
| `10` | `(default)` |
| `11` | `???3.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U16.` |
| `10` | `U32.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v8"></a>
## 8. `I2F_R_UR`

Syntax: `I2F R, UR`  
Example: `@P0 I2F.U64 R0, UR0 ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| modi 1 | 74 |
| modi 2 | 75-76 |
| modi 3 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010001011............00000000.......0000000000000000000000000
0000000000...0..0000110000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U64.` |
| `1` | `S64.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v9"></a>
## 9. `I2F_R_R`

Syntax: `I2F R, R`  
Example: `@P0 I2F.???0.U8 R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| modi (op 1) | 60-61 |
| modi 1 | 74 |
| modi 2 | 75-76 |
| modi 3 | 78-79 |
| modi 4 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000001100............00000000........00000000000000000000..00
0000000000...0..0000..0000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `F16.` |
| `10` | `(default)` |
| `11` | `???3.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U16.` |
| `10` | `U32.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v10"></a>
## 10. `I2F_R_R`

Syntax: `I2F R, R`  
Example: `@P0 I2F.U64 R0, R0 ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| modi 1 | 74 |
| modi 2 | 75-76 |
| modi 3 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010001100............00000000........000000000000000000000000
0000000000...0..0000110000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U64.` |
| `1` | `S64.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

