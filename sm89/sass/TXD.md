# TXD (SM89 SASS)

**NVIDIA:** Texture Fetch With Derivatives (Texture Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Texture fetch with explicit derivatives (category: Texture / surface)

Typically emitted for: `tex.grad`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x36d, 0xb6c, 0xd6d ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3137)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [txd](../verify/RESULTS.md#txd): `tex.grad.2d.v4.f32.f32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/TXD.html> (machine-derived by fuzzing the assembler; no semantics).

63 encoding variant(s):

- [TXD_P_R_R_R_R_I_I_ARRAY_D](#v1)
- [TXD_P_R_R_R_R_I_I_ARRAY_D_I](#v2)
- [TXD_P_R_R_R_R_I_I_D](#v3)
- [TXD_P_R_R_R_R_I_I_D_I](#v4)
- [TXD_P_R_R_R_R_I_I_SNOWFLAKE](#v5)
- [TXD_P_R_R_R_R_I_I_SNOWFLAKE_I](#v6)
- [TXD_P_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I](#v7)
- [TXD_P_R_R_SNOWFLAKE_R_I_I_D_I](#v8)
- [TXD_P_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I](#v9)
- [TXD_R_R_R_R_I_I_ARRAY_D_I](#v10)
- [TXD_R_R_R_R_I_I_D_I](#v11)
- [TXD_R_R_R_R_I_I_SNOWFLAKE_I](#v12)
- [TXD_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I](#v13)
- [TXD_R_R_SNOWFLAKE_R_I_I_D_I](#v14)
- [TXD_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I](#v15)
- [TXD_P_R_R_R_R_I_I_I_ARRAY_D](#v16)
- [TXD_P_R_R_R_R_I_I_I_ARRAY_D_I](#v17)
- [TXD_P_R_R_R_R_I_I_I_D](#v18)
- [TXD_P_R_R_R_R_I_I_I_D_I](#v19)
- [TXD_P_R_R_R_R_I_I_I_SNOWFLAKE](#v20)
- [TXD_P_R_R_R_R_I_I_I_SNOWFLAKE_I](#v21)
- [TXD_P_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I](#v22)
- [TXD_P_R_R_SNOWFLAKE_R_I_I_I_D_I](#v23)
- [TXD_P_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I](#v24)
- [TXD_R_R_R_R_I_I_I_ARRAY_D_I](#v25)
- [TXD_R_R_R_R_I_I_I_D_I](#v26)
- [TXD_R_R_R_R_I_I_I_SNOWFLAKE_I](#v27)
- [TXD_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I](#v28)
- [TXD_R_R_SNOWFLAKE_R_I_I_I_D_I](#v29)
- [TXD_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I](#v30)
- [TXD_P_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v31)
- [TXD_P_R_R_R_R_SNOWFLAKE_I_D_I](#v32)
- [TXD_P_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v33)
- [TXD_P_R_R_R_R_UR_I_ARRAY_D](#v34)
- [TXD_P_R_R_R_R_UR_I_ARRAY_D_I](#v35)
- [TXD_P_R_R_R_R_UR_I_D](#v36)
- [TXD_P_R_R_R_R_UR_I_D_I](#v37)
- [TXD_P_R_R_R_R_UR_I_SNOWFLAKE](#v38)
- [TXD_P_R_R_R_R_UR_I_SNOWFLAKE_I](#v39)
- [TXD_P_R_R_SNOWFLAKE_R_UR_I_ARRAY_D_I](#v40)
- [TXD_P_R_R_SNOWFLAKE_R_UR_I_D_I](#v41)
- [TXD_P_R_R_SNOWFLAKE_R_UR_I_SNOWFLAKE_I](#v42)
- [TXD_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v43)
- [TXD_R_R_R_R_SNOWFLAKE_I_D_I](#v44)
- [TXD_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v45)
- [TXD_R_R_R_R_UR_I_ARRAY_D_I](#v46)
- [TXD_R_R_R_R_UR_I_D_I](#v47)
- [TXD_R_R_R_R_UR_I_SNOWFLAKE_I](#v48)
- [TXD_P_R_R_R_R_ARRAY_D](#v49)
- [TXD_P_R_R_R_R_ARRAY_D_I](#v50)
- [TXD_P_R_R_R_R_D](#v51)
- [TXD_P_R_R_R_R_D_I](#v52)
- [TXD_P_R_R_R_R_SNOWFLAKE](#v53)
- [TXD_P_R_R_R_R_SNOWFLAKE_I](#v54)
- [TXD_P_R_R_SNOWFLAKE_R_ARRAY_D_I](#v55)
- [TXD_P_R_R_SNOWFLAKE_R_D_I](#v56)
- [TXD_P_R_R_SNOWFLAKE_R_SNOWFLAKE_I](#v57)
- [TXD_R_R_R_R_ARRAY_D_I](#v58)
- [TXD_R_R_R_R_D_I](#v59)
- [TXD_R_R_R_R_SNOWFLAKE_I](#v60)
- [TXD_R_R_SNOWFLAKE_R_ARRAY_D_I](#v61)
- [TXD_R_R_SNOWFLAKE_R_D_I](#v62)
- [TXD_R_R_SNOWFLAKE_R_SNOWFLAKE_I](#v63)

<a id="v1"></a>
## 1. `TXD_P_R_R_R_R_I_I_ARRAY_D`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, 0x0, 0x0, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101..................................................01
........1111.00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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
## 2. `TXD_P_R_R_R_R_I_I_ARRAY_D_I`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101..................................................01
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v3"></a>
## 3. `TXD_P_R_R_R_R_I_I_D`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, 0x0, 0x0, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101..................................................00
........1111.00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v4"></a>
## 4. `TXD_P_R_R_R_R_I_I_D_I`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101..................................................00
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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
## 5. `TXD_P_R_R_R_R_I_I_SNOWFLAKE`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, 0x0, 0x0, INVALID2 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| operand 7 | 60-61, 63 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101..................................................1.
........1111.00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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
## 6. `TXD_P_R_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, 0x0, 0x0, INVALID2, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| operand 7 | 60-61, 63 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101..................................................1.
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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
## 7. `TXD_P_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101............11111111..............................01
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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
## 8. `TXD_P_R_R_SNOWFLAKE_R_I_I_D_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101............11111111..............................00
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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
## 9. `TXD_P_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, INVALID2, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| operand 7 | 60-61, 63 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101............11111111..............................1.
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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
## 10. `TXD_R_R_R_R_I_I_ARRAY_D_I`

Syntax: `TXD R, R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.EF R0, R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101..................................................01
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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
## 11. `TXD_R_R_R_R_I_I_D_I`

Syntax: `TXD R, R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.EF R0, R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101..................................................00
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v12"></a>
## 12. `TXD_R_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TXD R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.EF R0, R0, R0, R0, 0x0, 0x0, INVALID2, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| operand 6 | 60-61, 63 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101..................................................1.
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v13"></a>
## 13. `TXD_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I`

Syntax: `TXD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.EF R0, R0,     ???255, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101............11111111..............................01
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v14"></a>
## 14. `TXD_R_R_SNOWFLAKE_R_I_I_D_I`

Syntax: `TXD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.EF R0, R0,     ???255, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101............11111111..............................00
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v15"></a>
## 15. `TXD_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I`

Syntax: `TXD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.EF R0, R0,     ???255, R0, 0x0, 0x0, INVALID2, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| operand 6 | 60-61, 63 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101101............11111111..............................1.
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v16"></a>
## 16. `TXD_P_R_R_R_R_I_I_I_ARRAY_D`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| operand 8 | 60-61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101..................................................01
........1111.00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v17"></a>
## 17. `TXD_P_R_R_R_R_I_I_I_ARRAY_D_I`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| operand 8 | 60-61 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101..................................................01
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v18"></a>
## 18. `TXD_P_R_R_R_R_I_I_I_D`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| operand 8 | 60-61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101..................................................00
........1111.00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v19"></a>
## 19. `TXD_P_R_R_R_R_I_I_I_D_I`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| operand 8 | 60-61 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101..................................................00
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v20"></a>
## 20. `TXD_P_R_R_R_R_I_I_I_SNOWFLAKE`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, INVALID2 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| operand 8 | 60-61, 63 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101..................................................1.
........1111.00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v21"></a>
## 21. `TXD_P_R_R_R_R_I_I_I_SNOWFLAKE_I`

Syntax: `TXD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, INVALID2, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| operand 8 | 60-61, 63 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101..................................................1.
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v22"></a>
## 22. `TXD_P_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| operand 8 | 60-61 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101............11111111..............................01
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v23"></a>
## 23. `TXD_P_R_R_SNOWFLAKE_R_I_I_I_D_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| operand 8 | 60-61 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101............11111111..............................00
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v24"></a>
## 24. `TXD_P_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 0x0, INVALID2, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| operand 8 | 60-61, 63 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101............11111111..............................1.
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v25"></a>
## 25. `TXD_R_R_R_R_I_I_I_ARRAY_D_I`

Syntax: `TXD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0, R0, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| operand 7 | 60-61 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101..................................................01
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v26"></a>
## 26. `TXD_R_R_R_R_I_I_I_D_I`

Syntax: `TXD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0, R0, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| operand 7 | 60-61 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101..................................................00
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v27"></a>
## 27. `TXD_R_R_R_R_I_I_I_SNOWFLAKE_I`

Syntax: `TXD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0, R0, R0, 0x0, 0x0, 0x0, INVALID2, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| operand 7 | 60-61, 63 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101..................................................1.
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v28"></a>
## 28. `TXD_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I`

Syntax: `TXD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0,     ???255, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| operand 7 | 60-61 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101............11111111..............................01
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v29"></a>
## 29. `TXD_R_R_SNOWFLAKE_R_I_I_I_D_I`

Syntax: `TXD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0,     ???255, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| operand 7 | 60-61 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101............11111111..............................00
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v30"></a>
## 30. `TXD_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I`

Syntax: `TXD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0,     ???255, R0, 0x0, 0x0, 0x0, INVALID2, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| operand 7 | 60-61, 63 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101101101............11111111..............................1.
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v31"></a>
## 31. `TXD_P_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TXD P, R, R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 46-53 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111............................111111........000000..01
.............00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v32"></a>
## 32. `TXD_P_R_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TXD P, R, R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 46-53 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111............................111111........000000..00
.............00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v33"></a>
## 33. `TXD_P_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TXD P, R, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0,     ???63, 0x0, INVALID2, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 46-53 |
| operand 7 | 60-61, 63 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111............................111111........000000..1.
.............00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v34"></a>
## 34. `TXD_P_R_R_R_R_UR_I_ARRAY_D`

Syntax: `TXD P, R, R, R, R, UR, INT_IMM, ARRAY_D`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, UR0, 0x0, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111..........................................000000..01
........1111.00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v35"></a>
## 35. `TXD_P_R_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TXD P, R, R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111..........................................000000..01
.............00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v36"></a>
## 36. `TXD_P_R_R_R_R_UR_I_D`

Syntax: `TXD P, R, R, R, R, UR, INT_IMM, D`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, UR0, 0x0, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111..........................................000000..00
........1111.00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v37"></a>
## 37. `TXD_P_R_R_R_R_UR_I_D_I`

Syntax: `TXD P, R, R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111..........................................000000..00
.............00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v38"></a>
## 38. `TXD_P_R_R_R_R_UR_I_SNOWFLAKE`

Syntax: `TXD P, R, R, R, R, UR, INT_IMM, SNOWFLAKE`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, UR0, 0x0, INVALID2 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| operand 7 | 60-61, 63 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111..........................................000000..1.
........1111.00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v39"></a>
## 39. `TXD_P_R_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TXD P, R, R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0, R0, R0, UR0, 0x0, INVALID2, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| operand 7 | 60-61, 63 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111..........................................000000..1.
.............00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v40"></a>
## 40. `TXD_P_R_R_SNOWFLAKE_R_UR_I_ARRAY_D_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0,     ???255, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111............11111111......................000000..01
.............00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v41"></a>
## 41. `TXD_P_R_R_SNOWFLAKE_R_UR_I_D_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0,     ???255, R0, UR0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| operand 7 | 60-61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111............11111111......................000000..00
.............00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v42"></a>
## 42. `TXD_P_R_R_SNOWFLAKE_R_UR_I_SNOWFLAKE_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.EF P0, R0, R0,     ???255, R0, UR0, 0x0, INVALID2, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| operand 7 | 60-61, 63 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111............11111111......................000000..1.
.............00.........00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v43"></a>
## 43. `TXD_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TXD R, R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.EF R0, R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111............................111111........000000..01
.............00..111....00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v44"></a>
## 44. `TXD_R_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TXD R, R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.EF R0, R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111............................111111........000000..00
.............00..111....00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v45"></a>
## 45. `TXD_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TXD R, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.EF R0, R0, R0, R0,     ???63, 0x0, INVALID2, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| operand 6 | 60-61, 63 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111............................111111........000000..1.
.............00..111....00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v46"></a>
## 46. `TXD_R_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TXD R, R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.EF R0, R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111..........................................000000..01
.............00..111....00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v47"></a>
## 47. `TXD_R_R_R_R_UR_I_D_I`

Syntax: `TXD R, R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TXD.EF R0, R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111..........................................000000..00
.............00..111....00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v48"></a>
## 48. `TXD_R_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TXD R, R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.EF R0, R0, R0, R0, UR0, 0x0, INVALID2, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 6 | 60-61, 63 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001101101111..........................................000000..1.
.............00..111....00.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

Modifier Group 2:

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

<a id="v49"></a>
## 49. `TXD_P_R_R_R_R_ARRAY_D`

Syntax: `TXD P, R, R, R, R, ARRAY_D`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| operand 5 | 60-61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............................0000000000000000000...01
........1111.00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v50"></a>
## 50. `TXD_P_R_R_R_R_ARRAY_D_I`

Syntax: `TXD P, R, R, R, R, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| operand 5 | 60-61 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............................0000000000000000000...01
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v51"></a>
## 51. `TXD_P_R_R_R_R_D`

Syntax: `TXD P, R, R, R, R, D`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| operand 5 | 60-61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............................0000000000000000000...00
........1111.00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v52"></a>
## 52. `TXD_P_R_R_R_R_D_I`

Syntax: `TXD P, R, R, R, R, D, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| operand 5 | 60-61 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............................0000000000000000000...00
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v53"></a>
## 53. `TXD_P_R_R_R_R_SNOWFLAKE`

Syntax: `TXD P, R, R, R, R, SNOWFLAKE`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, INVALID2 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| operand 5 | 60-61, 63 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............................0000000000000000000...1.
........1111.00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v54"></a>
## 54. `TXD_P_R_R_R_R_SNOWFLAKE_I`

Syntax: `TXD P, R, R, R, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0, R0, R0, INVALID2, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| operand 5 | 60-61, 63 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............................0000000000000000000...1.
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v55"></a>
## 55. `TXD_P_R_R_SNOWFLAKE_R_ARRAY_D_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0,     ???255, R0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| operand 5 | 60-61 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............11111111........0000000000000000000...01
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v56"></a>
## 56. `TXD_P_R_R_SNOWFLAKE_R_D_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, D, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0,     ???255, R0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| operand 5 | 60-61 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............11111111........0000000000000000000...00
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v57"></a>
## 57. `TXD_P_R_R_SNOWFLAKE_R_SNOWFLAKE_I`

Syntax: `TXD P, R, R, SNOWFLAKE, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.???0.EF P0, R0, R0,     ???255, R0, INVALID2, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| operand 5 | 60-61, 63 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............11111111........0000000000000000000...1.
.............00.........00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v58"></a>
## 58. `TXD_R_R_R_R_ARRAY_D_I`

Syntax: `TXD R, R, R, R, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0, R0, R0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-61 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............................0000000000000000000...01
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v59"></a>
## 59. `TXD_R_R_R_R_D_I`

Syntax: `TXD R, R, R, R, D, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0, R0, R0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-61 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............................0000000000000000000...00
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v60"></a>
## 60. `TXD_R_R_R_R_SNOWFLAKE_I`

Syntax: `TXD R, R, R, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0, R0, R0, INVALID2, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-61, 63 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............................0000000000000000000...1.
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v61"></a>
## 61. `TXD_R_R_SNOWFLAKE_R_ARRAY_D_I`

Syntax: `TXD R, R, SNOWFLAKE, R, ARRAY_D, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0,     ???255, R0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-61 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............11111111........0000000000000000000...01
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v62"></a>
## 62. `TXD_R_R_SNOWFLAKE_R_D_I`

Syntax: `TXD R, R, SNOWFLAKE, R, D, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0,     ???255, R0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-61 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............11111111........0000000000000000000...00
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

<a id="v63"></a>
## 63. `TXD_R_R_SNOWFLAKE_R_SNOWFLAKE_I`

Syntax: `TXD R, R, SNOWFLAKE, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXD.???0.EF R0, R0,     ???255, R0, INVALID2, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-61, 63 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| modi 3 | 79-80 |
| modi 4 | 84-86 |
| LC | 87 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101101100............11111111........0000000000000000000...1.
.............00..111....00.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F16.RN.` |
| `10` | `F16.RZ.` |
| `11` | `INVALID3.` |

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

