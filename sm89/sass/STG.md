# STG (SM89 SASS)

**NVIDIA:** Store to Global Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Store to global memory (category: Load / store)

Typically emitted for: `st.global` (vector forms -> STG.E.64/.128)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [prologue](../verify/RESULTS.md#prologue): `empty kernel body: param pointer + %tid.x load/store`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 66 | `STG.E [R2.64+0x4], R7`<br>`STG.E [R2.64], R11`<br>`STG.E [R2.64], R5` |
| 76 | `STG.E [R2.64], R5` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/STG.html> (machine-derived by fuzzing the assembler; no semantics).

11 encoding variant(s):

- [STG_RI_R](#v1)
- [STG_RURI_R](#v2)
- [STG_RUR_R](#v3)
- [STG_R_R](#v4)
- [STG_URI_R](#v5)
- [STG_UR_R](#v6)
- [STG_desc[UR][RI]_R](#v7)
- [STG_desc[UR][R]_R](#v8)
- [STG_I_R](#v9)
- [STG_RI_R](#v10)
- [STG_R_R](#v11)

<a id="v1"></a>
## 1. `STG_RI_R`

Syntax: `STG [R+INT_IMM], R`  
Example: `@P0 STG.???0.EF.U8 [R0.64+0x4], R0 ;`

Register access: READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 2 | 32-39 |
| operand 1 | 40-63 |
| modi 1 | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000011001....00000000........................................
00000000....1....000...000110000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v2"></a>
## 2. `STG_RURI_R`

Syntax: `STG [R+UR+INT_IMM], R`  
Example: `@P0 STG.EF.U8 [R0.U32+UR0+0x4], R0 ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 3 | 32-39 |
| operand 2 | 40-63 |
| operand 1 | 64-70 |
| E | 72 |
| modi 1 | 73-75 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| modi (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000011001....00000000........................................
.......0....0....000...000.10000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v3"></a>
## 3. `STG_RUR_R`

Syntax: `STG [R+UR], R`  
Example: `@P0 STG.EF.U8 [R0.U32+UR0], R0 ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 2 | 32-39 |
| operand 1 | 64-70 |
| E | 72 |
| modi 1 | 73-75 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| modi (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000011001....00000000................000000000000000000000000
.......0....0....000...000.10000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v4"></a>
## 4. `STG_R_R`

Syntax: `STG [R], R`  
Example: `@P0 STG.???0.EF.U8 [R0.64], R0 ;`

Register access: READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 32-39 |
| modi 1 | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000011001....00000000................000000000000000000000000
00000000....1....000...000110000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v5"></a>
## 5. `STG_URI_R`

Syntax: `STG [UR+INT_IMM], R`  
Example: `@P0 STG.EF.U8 [UR0+0x20], R0 ;`

Register access: READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 32-39 |
| operand 1 | 40-63 |
| operand 0 | 64-70 |
| E | 72 |
| modi 1 | 73-75 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000011001....0000000011111111................................
.......0....0....000...000010000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v6"></a>
## 6. `STG_UR_R`

Syntax: `STG [UR], R`  
Example: `@P0 STG.EF.U8 [UR0], R0 ;`

Register access: READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| operand 0 | 64-70 |
| E | 72 |
| modi 1 | 73-75 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000011001....0000000011111111........000000000000000000000000
.......0....0....000...000010000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v7"></a>
## 7. `STG_desc[UR][RI]_R`

Syntax: `STG desc[UR][R+INT_IMM], R`  
Example: `@P0 STG.???0.EF.U8 desc[UR0][R0.64+0x4], R0 ;`

Register access: READ UR (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 3 | 32-39 |
| operand 2 | 40-63 |
| operand 0 | 64-70 |
| modi 1 | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000011001....00000000........................................
.......0....1....000...000110000000001000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v8"></a>
## 8. `STG_desc[UR][R]_R`

Syntax: `STG desc[UR][R], R`  
Example: `@P0 STG.???0.EF.U8 desc[UR0][R0.64], R0 ;`

Register access: READ UR (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 0 | 64-70 |
| modi 1 | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000011001....00000000................000000000000000000000000
.......0....1....000...000110000000001000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v9"></a>
## 9. `STG_I_R`

Syntax: `STG [INT_IMM], R`  
Example: `@P0 STG.EF.U8 [0x20], R0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| operand 0 | 40-63 |
| E | 72 |
| modi 1 | 73-75 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000011100....0000000011111111................................
00000000....0....000...000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v10"></a>
## 10. `STG_RI_R`

Syntax: `STG [R+INT_IMM], R`  
Example: `@P0 STG.EF.U8 [R0+0x10], R0 ;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 2 | 32-39 |
| operand 1 | 40-63 |
| E | 72 |
| modi 1 | 73-75 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000011100....00000000........................................
00000000....0....000...000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v11"></a>
## 11. `STG_R_R`

Syntax: `STG [R], R`  
Example: `@P0 STG.EF.U8 [R0], R0 ;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 32-39 |
| E | 72 |
| modi 1 | 73-75 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000011100....00000000................000000000000000000000000
00000000....0....000...000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

