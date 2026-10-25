# ISETP (SM89 SASS)

**NVIDIA:** Integer Compare And Set Predicate (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Integer compare, write predicate (category: Integer)

Typically emitted for: `setp.<cmp>.s32/u32/s64`; integer comparisons, loop bounds

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0xc, 0x8c ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1866)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [isetp_pred](../verify/RESULTS.md#isetp_pred): `setp.lt.s32 + selp.b32 (ptxas if-converts to a predicated op, no SEL)`
- [plop3_folded](../verify/RESULTS.md#plop3_folded): `xor.pred of two compares (folded into FSETP's combine op, no PLOP3)`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 72 | `ISETP.EQ.U32.AND P0, PT, R0, R3, PT`<br>`ISETP.EQ.U32.AND P0, PT, R0, UR5, PT`<br>`ISETP.EQ.U32.AND P0, PT, R4, -0x1, PT` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/ISETP.html> (machine-derived by fuzzing the assembler; no semantics).

10 encoding variant(s):

- [ISETP_P_P_R_I_P](#v1)
- [ISETP_P_P_R_I_P_P](#v2)
- [ISETP_P_P_R_c[I][I]_P](#v3)
- [ISETP_P_P_R_c[I][I]_P_P](#v4)
- [ISETP_P_P_R_cx[UR][I]_P](#v5)
- [ISETP_P_P_R_cx[UR][I]_P_P](#v6)
- [ISETP_P_P_R_UR_P](#v7)
- [ISETP_P_P_R_UR_P_P](#v8)
- [ISETP_P_P_R_R_P](#v9)
- [ISETP_P_P_R_R_P_P](#v10)

<a id="v1"></a>
## 1. `ISETP_P_P_R_I_P`

Syntax: `ISETP.AND P, P, R, INT_IMM, P`  
Example: `@P0 ISETP.F.U32.AND P0, P0, R0, 0x0, P0;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100000001....00000000........................................
000000000......0...........00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v2"></a>
## 2. `ISETP_P_P_R_I_P_P`

Syntax: `ISETP.AND.EX P, P, R, INT_IMM, P, P`  
Example: `@P0 ISETP.F.U32.AND.EX P0, P0, R0, 0x0, P0, P0;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| operand 5 | 67-70 |
| cNOT (op 5) | 71 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100000001....00000000........................................
000.....1......0...........00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v3"></a>
## 3. `ISETP_P_P_R_c[I][I]_P`

Syntax: `ISETP.AND P, P, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 ISETP.F.U32.AND P0, P0, R0, c[0x0][0x0], P0;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100000101....00000000........00000000...................00000
000000000......0...........00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v4"></a>
## 4. `ISETP_P_P_R_c[I][I]_P_P`

Syntax: `ISETP.AND.EX P, P, R, c[INT_IMM][INT_IMM], P, P`  
Example: `@P0 ISETP.F.U32.AND.EX P0, P0, R0, c[0x0][0x0], P0, P0;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 6 | 67-70 |
| cNOT (op 6) | 71 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100000101....00000000........00000000...................00000
000.....1......0...........00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v5"></a>
## 5. `ISETP_P_P_R_cx[UR][I]_P`

Syntax: `ISETP.AND P, P, R, cx[UR][INT_IMM], P`  
Example: `@P0 ISETP.F.U32.AND P0, P0, R0, cx[UR0][0x0], P0;`

Register access: READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100000101....00000000...............0...............000000000
000000000......0...........10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v6"></a>
## 6. `ISETP_P_P_R_cx[UR][I]_P_P`

Syntax: `ISETP.AND.EX P, P, R, cx[UR][INT_IMM], P, P`  
Example: `@P0 ISETP.F.U32.AND.EX P0, P0, R0, cx[UR0][0x0], P0, P0;`

Register access: READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 6 | 67-70 |
| cNOT (op 6) | 71 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100000101....00000000...............0...............000000000
000.....1......0...........10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v7"></a>
## 7. `ISETP_P_P_R_UR_P`

Syntax: `ISETP.AND P, P, R, UR, P`  
Example: `@P0 ISETP.F.U32.AND P0, P0, R0, UR0, P0;`

Register access: READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100000011....00000000...............0000000000000000000000000
000000000......0...........10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v8"></a>
## 8. `ISETP_P_P_R_UR_P_P`

Syntax: `ISETP.AND.EX P, P, R, UR, P, P`  
Example: `@P0 ISETP.F.U32.AND.EX P0, P0, R0, UR0, P0, P0;`

Register access: READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 5 | 67-70 |
| cNOT (op 5) | 71 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100000011....00000000...............0000000000000000000000000
000.....1......0...........10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v9"></a>
## 9. `ISETP_P_P_R_R_P`

Syntax: `ISETP.AND P, P, R, R, P`  
Example: `@P0 ISETP.F.U32.AND P0, P0, R0, R0, P0;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100000100....00000000................000000000000000000000000
000000000......0...........00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v10"></a>
## 10. `ISETP_P_P_R_R_P_P`

Syntax: `ISETP.AND.EX P, P, R, R, P, P`  
Example: `@P0 ISETP.F.U32.AND.EX P0, P0, R0, R0, P0, P0;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 67-70 |
| cNOT (op 5) | 71 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100000100....00000000................000000000000000000000000
000.....1......0...........00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

