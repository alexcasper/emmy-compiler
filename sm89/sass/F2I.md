# F2I (SM89 SASS)

**NVIDIA:** Floating Point To Integer Conversion (Conversion Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Float to integer conversion (category: Conversion)

Typically emitted for: `cvt.rzi.s32.f32` etc.; `(int)f`, `__float2int_rn`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x5c, 0x105, 0x111 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2282)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [f2i](../verify/RESULTS.md#f2i): `cvt.rzi.s32.f32`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 84 | `F2I.S8.NTZ R5, R0`<br>`F2I.TRUNC.NTZ R5, R0` |
| 85 | `F2I.S8.NTZ R5, R0`<br>`F2I.TRUNC.NTZ R5, R0` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/F2I.html> (machine-derived by fuzzing the assembler; no semantics).

9 encoding variant(s):

- [F2I_R_FI](#v1)
- [F2I_R_FI](#v2)
- [F2I_R_c[I][I]](#v3)
- [F2I_R_cx[UR][I]](#v4)
- [F2I_R_c[I][I]](#v5)
- [F2I_R_cx[UR][I]](#v6)
- [F2I_R_UR](#v7)
- [F2I_R_R](#v8)
- [F2I_R_R](#v9)

<a id="v1"></a>
## 1. `F2I_R_FI`

Syntax: `F2I.F16 R, FIMM`  
Example: `@P0 F2I.U8.F16 R0, 0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-47 |
| modi 1 | 72 |
| modi 2 | 75-76, 78-79 |
| NTZ | 77 |
| FTZ | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000001001............00000000................0000000000000000
00000000.00......000100000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U16.` |
| `10` | `U32.` |
| `11` | `???6.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

<a id="v2"></a>
## 2. `F2I_R_FI`

Syntax: `F2I R, FIMM`  
Example: `@P0 F2I.U64 R0, 0 ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| modi 1 | 72 |
| NTZ | 77 |
| modi 2 | 78-79 |
| FTZ | 80 |
| modi 3 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010001001............00000000................................
00000000.0011....000..0000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U64.` |
| `1` | `S64.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

<a id="v3"></a>
## 3. `F2I_R_c[I][I]`

Syntax: `F2I.F16 R, c[INT_IMM][INT_IMM]`  
Example: `@P0 F2I.U8.F16 R0, c[0x0] [0x0] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| modi 1 | 72 |
| modi 2 | 75-76, 78-79 |
| NTZ | 77 |
| FTZ | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000001101............0000000000000000...................00000
00000000.00......000100000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U16.` |
| `10` | `U32.` |
| `11` | `???6.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

<a id="v4"></a>
## 4. `F2I_R_cx[UR][I]`

Syntax: `F2I.F16 R, cx[UR][INT_IMM]`  
Example: `@P0 F2I.U8.F16 R0, cx[UR0] [0x0] ;`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| modi 1 | 72 |
| modi 2 | 75-76, 78-79 |
| NTZ | 77 |
| FTZ | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000001101............00000000.......0...............000000000
00000000.00......000100000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U16.` |
| `10` | `U32.` |
| `11` | `???6.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

<a id="v5"></a>
## 5. `F2I_R_c[I][I]`

Syntax: `F2I R, c[INT_IMM][INT_IMM]`  
Example: `@P0 F2I.U64 R0, c[0x0][0x0] ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| modi 1 | 72 |
| NTZ | 77 |
| modi 2 | 78-79 |
| FTZ | 80 |
| modi 3 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010001101............0000000000000000...................00000
00000000.0011....000..0000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U64.` |
| `1` | `S64.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

<a id="v6"></a>
## 6. `F2I_R_cx[UR][I]`

Syntax: `F2I R, cx[UR][INT_IMM]`  
Example: `@P0 F2I.U64 R0, cx[UR0][0x0] ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| modi 1 | 72 |
| NTZ | 77 |
| modi 2 | 78-79 |
| FTZ | 80 |
| modi 3 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010001101............00000000.......0...............000000000
00000000.0011....000..0000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U64.` |
| `1` | `S64.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

<a id="v7"></a>
## 7. `F2I_R_UR`

Syntax: `F2I.F64 R, UR`  
Example: `@P0 F2I.U8.F64 R0, UR0 ;`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| cABS (op 1) | 62 |
| cNEG (op 1) | 63 |
| modi 1 | 72 |
| modi 2 | 75-76, 78-79 |
| NTZ | 77 |
| FTZ | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010001011............00000000.......00000000000000000000000..
00000000.00......000110000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U16.` |
| `10` | `U32.` |
| `11` | `U64.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

<a id="v8"></a>
## 8. `F2I_R_R`

Syntax: `F2I.F16 R, R`  
Example: `@P0 F2I.U8.F16 R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| modi (op 1) | 60-61 |
| cABS (op 1) | 62 |
| cNEG (op 1) | 63 |
| modi 1 | 72 |
| modi 2 | 75-76, 78-79 |
| NTZ | 77 |
| FTZ | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000001100............00000000........00000000000000000000....
00000000.00......000100000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `U16.` |
| `10` | `U32.` |
| `11` | `???6.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `H1.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

<a id="v9"></a>
## 9. `F2I_R_R`

Syntax: `F2I R, R`  
Example: `@P0 F2I.U64 R0, R0 ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| cABS (op 1) | 62 |
| cNEG (op 1) | 63 |
| modi 1 | 72 |
| NTZ | 77 |
| modi 2 | 78-79 |
| FTZ | 80 |
| modi 3 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010001100............00000000........0000000000000000000000..
00000000.0011....000..0000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U64.` |
| `1` | `S64.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

