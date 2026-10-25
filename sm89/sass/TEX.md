# TEX (SM89 SASS)

**NVIDIA:** Texture Fetch (Texture Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Texture fetch (category: Texture / surface)

Typically emitted for: `tex.*`; `tex2D` etc.

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x361, 0xb60, 0xd61 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2887)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [tex](../verify/RESULTS.md#tex): `tex.2d.v4.f32.f32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/TEX.html> (machine-derived by fuzzing the assembler; no semantics).

111 encoding variant(s):

- [TEX_P_R_R_R_I_I_ARRAY_D](#v1)
- [TEX_P_R_R_R_I_I_ARRAY_D_I](#v2)
- [TEX_P_R_R_R_I_I_D](#v3)
- [TEX_P_R_R_R_I_I_D_I](#v4)
- [TEX_P_R_R_R_I_I_SNOWFLAKE](#v5)
- [TEX_P_R_R_R_I_I_SNOWFLAKE_I](#v6)
- [TEX_P_R_R_R_R_I_I_ARRAY_D](#v7)
- [TEX_P_R_R_R_R_I_I_ARRAY_D_I](#v8)
- [TEX_P_R_R_R_R_I_I_D](#v9)
- [TEX_P_R_R_R_R_I_I_D_I](#v10)
- [TEX_P_R_R_R_R_I_I_SNOWFLAKE](#v11)
- [TEX_P_R_R_R_R_I_I_SNOWFLAKE_I](#v12)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_ARRAY_D](#v13)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_ARRAY_D_I](#v14)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_D](#v15)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_D_I](#v16)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE](#v17)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE_I](#v18)
- [TEX_P_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I](#v19)
- [TEX_P_R_R_SNOWFLAKE_R_I_I_D_I](#v20)
- [TEX_P_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I](#v21)
- [TEX_R_R_R_I_I_ARRAY_D_I](#v22)
- [TEX_R_R_R_I_I_D_I](#v23)
- [TEX_R_R_R_I_I_SNOWFLAKE_I](#v24)
- [TEX_R_R_R_R_I_I_ARRAY_D_I](#v25)
- [TEX_R_R_R_R_I_I_D_I](#v26)
- [TEX_R_R_R_R_I_I_SNOWFLAKE_I](#v27)
- [TEX_R_R_R_SNOWFLAKE_I_I_ARRAY_D_I](#v28)
- [TEX_R_R_R_SNOWFLAKE_I_I_D_I](#v29)
- [TEX_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE_I](#v30)
- [TEX_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I](#v31)
- [TEX_R_R_SNOWFLAKE_R_I_I_D_I](#v32)
- [TEX_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I](#v33)
- [TEX_P_R_R_R_R_I_I_I_ARRAY_D](#v34)
- [TEX_P_R_R_R_R_I_I_I_ARRAY_D_I](#v35)
- [TEX_P_R_R_R_R_I_I_I_D](#v36)
- [TEX_P_R_R_R_R_I_I_I_D_I](#v37)
- [TEX_P_R_R_R_R_I_I_I_SNOWFLAKE](#v38)
- [TEX_P_R_R_R_R_I_I_I_SNOWFLAKE_I](#v39)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D](#v40)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D_I](#v41)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_I_D](#v42)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_I_D_I](#v43)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE](#v44)
- [TEX_P_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE_I](#v45)
- [TEX_P_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I](#v46)
- [TEX_P_R_R_SNOWFLAKE_R_I_I_I_D_I](#v47)
- [TEX_P_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I](#v48)
- [TEX_R_R_R_R_I_I_I_ARRAY_D_I](#v49)
- [TEX_R_R_R_R_I_I_I_D_I](#v50)
- [TEX_R_R_R_R_I_I_I_SNOWFLAKE_I](#v51)
- [TEX_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D_I](#v52)
- [TEX_R_R_R_SNOWFLAKE_I_I_I_D_I](#v53)
- [TEX_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE_I](#v54)
- [TEX_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I](#v55)
- [TEX_R_R_SNOWFLAKE_R_I_I_I_D_I](#v56)
- [TEX_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I](#v57)
- [TEX_P_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v58)
- [TEX_P_R_R_R_R_SNOWFLAKE_I_D_I](#v59)
- [TEX_P_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v60)
- [TEX_P_R_R_R_R_UR_I_ARRAY_D](#v61)
- [TEX_P_R_R_R_R_UR_I_ARRAY_D_I](#v62)
- [TEX_P_R_R_R_R_UR_I_D](#v63)
- [TEX_P_R_R_R_R_UR_I_D_I](#v64)
- [TEX_P_R_R_R_R_UR_I_SNOWFLAKE](#v65)
- [TEX_P_R_R_R_R_UR_I_SNOWFLAKE_I](#v66)
- [TEX_P_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v67)
- [TEX_P_R_R_R_SNOWFLAKE_I_D_I](#v68)
- [TEX_P_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v69)
- [TEX_P_R_R_R_UR_I_ARRAY_D_I](#v70)
- [TEX_P_R_R_R_UR_I_D_I](#v71)
- [TEX_P_R_R_R_UR_I_SNOWFLAKE_I](#v72)
- [TEX_P_R_R_SNOWFLAKE_R_UR_I_ARRAY_D_I](#v73)
- [TEX_P_R_R_SNOWFLAKE_R_UR_I_D_I](#v74)
- [TEX_P_R_R_SNOWFLAKE_R_UR_I_SNOWFLAKE_I](#v75)
- [TEX_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v76)
- [TEX_R_R_R_R_SNOWFLAKE_I_D_I](#v77)
- [TEX_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v78)
- [TEX_R_R_R_R_UR_I_ARRAY_D_I](#v79)
- [TEX_R_R_R_R_UR_I_D_I](#v80)
- [TEX_R_R_R_R_UR_I_SNOWFLAKE_I](#v81)
- [TEX_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v82)
- [TEX_R_R_R_SNOWFLAKE_I_D_I](#v83)
- [TEX_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v84)
- [TEX_R_R_R_UR_I_ARRAY_D_I](#v85)
- [TEX_R_R_R_UR_I_D_I](#v86)
- [TEX_R_R_R_UR_I_SNOWFLAKE_I](#v87)
- [TEX_P_R_R_R_R_ARRAY_D](#v88)
- [TEX_P_R_R_R_R_ARRAY_D_I](#v89)
- [TEX_P_R_R_R_R_D](#v90)
- [TEX_P_R_R_R_R_D_I](#v91)
- [TEX_P_R_R_R_R_SNOWFLAKE](#v92)
- [TEX_P_R_R_R_R_SNOWFLAKE_I](#v93)
- [TEX_P_R_R_R_SNOWFLAKE_ARRAY_D](#v94)
- [TEX_P_R_R_R_SNOWFLAKE_ARRAY_D_I](#v95)
- [TEX_P_R_R_R_SNOWFLAKE_D](#v96)
- [TEX_P_R_R_R_SNOWFLAKE_D_I](#v97)
- [TEX_P_R_R_R_SNOWFLAKE_SNOWFLAKE](#v98)
- [TEX_P_R_R_R_SNOWFLAKE_SNOWFLAKE_I](#v99)
- [TEX_P_R_R_SNOWFLAKE_R_ARRAY_D_I](#v100)
- [TEX_P_R_R_SNOWFLAKE_R_D_I](#v101)
- [TEX_P_R_R_SNOWFLAKE_R_SNOWFLAKE_I](#v102)
- [TEX_R_R_R_R_ARRAY_D_I](#v103)
- [TEX_R_R_R_R_D_I](#v104)
- [TEX_R_R_R_R_SNOWFLAKE_I](#v105)
- [TEX_R_R_R_SNOWFLAKE_ARRAY_D_I](#v106)
- [TEX_R_R_R_SNOWFLAKE_D_I](#v107)
- [TEX_R_R_R_SNOWFLAKE_SNOWFLAKE_I](#v108)
- [TEX_R_R_SNOWFLAKE_R_ARRAY_D_I](#v109)
- [TEX_R_R_SNOWFLAKE_R_D_I](#v110)
- [TEX_R_R_SNOWFLAKE_R_SNOWFLAKE_I](#v111)

<a id="v1"></a>
## 1. `TEX_P_R_R_R_I_I_ARRAY_D`

Syntax: `TEX P, R, R, R, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TEX.EF P0, R0, R0, R0, 0x0, 0x0, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................0..01
........1111...............00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v2"></a>
## 2. `TEX_P_R_R_R_I_I_ARRAY_D_I`

Syntax: `TEX P, R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 61 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................0..01
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v3"></a>
## 3. `TEX_P_R_R_R_I_I_D`

Syntax: `TEX P, R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 TEX.EF P0, R0, R0, R0, 0x0, 0x0, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 61-62 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................0...0
........1111...............00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v4"></a>
## 4. `TEX_P_R_R_R_I_I_D_I`

Syntax: `TEX P, R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 61-62 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................0...0
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v5"></a>
## 5. `TEX_P_R_R_R_I_I_SNOWFLAKE`

Syntax: `TEX P, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TEX.EF P0, R0, R0, R0, 0x0, 0x0, INVALID6 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................0.011
........1111...............00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v6"></a>
## 6. `TEX_P_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TEX P, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, 0x0, 0x0, CUBE, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................0.110
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v7"></a>
## 7. `TEX_P_R_R_R_R_I_I_ARRAY_D`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, 0x0, 0x0, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 7 | 61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101..................................................01
........1111...............00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v8"></a>
## 8. `TEX_P_R_R_R_R_I_I_ARRAY_D_I`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 7 | 61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101..................................................01
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v9"></a>
## 9. `TEX_P_R_R_R_R_I_I_D`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, 0x0, 0x0, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 7 | 61-62 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101...................................................0
........1111...............00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v10"></a>
## 10. `TEX_P_R_R_R_R_I_I_D_I`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 7 | 61-62 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101...................................................0
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v11"></a>
## 11. `TEX_P_R_R_R_R_I_I_SNOWFLAKE`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, 0x0, 0x0, CUBE ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101.................................................110
........1111...............00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v12"></a>
## 12. `TEX_P_R_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, 0x0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101.................................................011
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v13"></a>
## 13. `TEX_P_R_R_R_SNOWFLAKE_I_I_ARRAY_D`

Syntax: `TEX.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TEX.B.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| SCR | 60 |
| operand 7 | 61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................1..01
........1111...............00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v14"></a>
## 14. `TEX_P_R_R_R_SNOWFLAKE_I_I_ARRAY_D_I`

Syntax: `TEX.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.B.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| SCR | 60 |
| operand 7 | 61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................1..01
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v15"></a>
## 15. `TEX_P_R_R_R_SNOWFLAKE_I_I_D`

Syntax: `TEX.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D`  
Example: `@P0 TEX.B.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| SCR | 60 |
| operand 7 | 61-62 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................1...0
........1111...............00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v16"></a>
## 16. `TEX_P_R_R_R_SNOWFLAKE_I_I_D_I`

Syntax: `TEX.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.B.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| SCR | 60 |
| operand 7 | 61-62 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................1...0
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v17"></a>
## 17. `TEX_P_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE`

Syntax: `TEX.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TEX.B.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, INVALID6 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| SCR | 60 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................1.011
........1111...............00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v18"></a>
## 18. `TEX_P_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE_I`

Syntax: `TEX.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.B.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, CUBE, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................1.110
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v19"></a>
## 19. `TEX_P_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 7 | 61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101............11111111..............................01
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v20"></a>
## 20. `TEX_P_R_R_SNOWFLAKE_R_I_I_D_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 7 | 61-62 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101............11111111...............................0
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v21"></a>
## 21. `TEX_P_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101............11111111.............................011
...........................00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v22"></a>
## 22. `TEX_R_R_R_I_I_ARRAY_D_I`

Syntax: `TEX R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| SCR | 60 |
| operand 5 | 61 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................0..01
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v23"></a>
## 23. `TEX_R_R_R_I_I_D_I`

Syntax: `TEX R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| SCR | 60 |
| operand 5 | 61-62 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................0...0
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v24"></a>
## 24. `TEX_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TEX R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, 0x0, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................0.110
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v25"></a>
## 25. `TEX_R_R_R_R_I_I_ARRAY_D_I`

Syntax: `TEX R, R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 6 | 61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101..................................................01
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v26"></a>
## 26. `TEX_R_R_R_R_I_I_D_I`

Syntax: `TEX R, R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 6 | 61-62 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101...................................................0
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v27"></a>
## 27. `TEX_R_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TEX R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, R0, 0x0, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101.................................................110
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v28"></a>
## 28. `TEX_R_R_R_SNOWFLAKE_I_I_ARRAY_D_I`

Syntax: `TEX.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.B.EF R0, R0, R0,     ???255, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................1..01
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v29"></a>
## 29. `TEX_R_R_R_SNOWFLAKE_I_I_D_I`

Syntax: `TEX.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.B.EF R0, R0, R0,     ???255, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 61-62 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................1...0
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v30"></a>
## 30. `TEX_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE_I`

Syntax: `TEX.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.B.EF R0, R0, R0,     ???255, 0x0, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101....................11111111...................1.110
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v31"></a>
## 31. `TEX_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I`

Syntax: `TEX R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0,     ???255, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 6 | 61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101............11111111..............................01
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v32"></a>
## 32. `TEX_R_R_SNOWFLAKE_R_I_I_D_I`

Syntax: `TEX R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0,     ???255, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 6 | 61-62 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101............11111111...............................0
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v33"></a>
## 33. `TEX_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I`

Syntax: `TEX R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF R0, R0,     ???255, R0, 0x0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101101............11111111.............................011
.................111.......00000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v34"></a>
## 34. `TEX_P_R_R_R_R_I_I_I_ARRAY_D`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

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
| SCR | 60 |
| operand 8 | 61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101..................................................01
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v35"></a>
## 35. `TEX_P_R_R_R_R_I_I_I_ARRAY_D_I`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

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
| SCR | 60 |
| operand 8 | 61 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101..................................................01
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v36"></a>
## 36. `TEX_P_R_R_R_R_I_I_I_D`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (1 slots)

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
| SCR | 60 |
| operand 8 | 61-62 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101...................................................0
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v37"></a>
## 37. `TEX_P_R_R_R_R_I_I_I_D_I`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| SCR | 60 |
| operand 8 | 61-62 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101...................................................0
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v38"></a>
## 38. `TEX_P_R_R_R_R_I_I_I_SNOWFLAKE`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, CUBE ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

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
| SCR | 60 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101.................................................110
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v39"></a>
## 39. `TEX_P_R_R_R_R_I_I_I_SNOWFLAKE_I`

Syntax: `TEX P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| SCR | 60 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101.................................................011
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v40"></a>
## 40. `TEX_P_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D`

Syntax: `TEX P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 8 | 61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101....................11111111......................01
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v41"></a>
## 41. `TEX_P_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D_I`

Syntax: `TEX P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 8 | 61 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101....................11111111......................01
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v42"></a>
## 42. `TEX_P_R_R_R_SNOWFLAKE_I_I_I_D`

Syntax: `TEX P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 8 | 61-62 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101....................11111111.......................0
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v43"></a>
## 43. `TEX_P_R_R_R_SNOWFLAKE_I_I_I_D_I`

Syntax: `TEX P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 8 | 61-62 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101....................11111111.......................0
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v44"></a>
## 44. `TEX_P_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE`

Syntax: `TEX P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, INVALID6 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101....................11111111.....................011
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v45"></a>
## 45. `TEX_P_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE_I`

Syntax: `TEX P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, CUBE, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101....................11111111.....................110
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v46"></a>
## 46. `TEX_P_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 8 | 61 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101............11111111..............................01
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v47"></a>
## 47. `TEX_P_R_R_SNOWFLAKE_R_I_I_I_D_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 8 | 61-62 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101............11111111...............................0
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v48"></a>
## 48. `TEX_P_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-44, 46 |
| operand 7 | 45, 47-52 |
| operand 5 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101............11111111.............................011
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v49"></a>
## 49. `TEX_R_R_R_R_I_I_I_ARRAY_D_I`

Syntax: `TEX R, R, R, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

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
| SCR | 60 |
| operand 7 | 61 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101..................................................01
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v50"></a>
## 50. `TEX_R_R_R_R_I_I_I_D_I`

Syntax: `TEX R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| SCR | 60 |
| operand 7 | 61-62 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101...................................................0
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v51"></a>
## 51. `TEX_R_R_R_R_I_I_I_SNOWFLAKE_I`

Syntax: `TEX R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0, R0, 0x0, 0x0, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ R (1 slots)

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
| SCR | 60 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101.................................................110
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v52"></a>
## 52. `TEX_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D_I`

Syntax: `TEX R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0,     ???255, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 7 | 61 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101....................11111111......................01
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v53"></a>
## 53. `TEX_R_R_R_SNOWFLAKE_I_I_I_D_I`

Syntax: `TEX R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0,     ???255, 0x0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 7 | 61-62 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101....................11111111.......................0
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v54"></a>
## 54. `TEX_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE_I`

Syntax: `TEX R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0,     ???255, 0x0, 0x0, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101....................11111111.....................110
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v55"></a>
## 55. `TEX_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I`

Syntax: `TEX R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0,     ???255, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 7 | 61 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101............11111111..............................01
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v56"></a>
## 56. `TEX_R_R_SNOWFLAKE_R_I_I_I_D_I`

Syntax: `TEX R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0,     ???255, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 7 | 61-62 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101............11111111...............................0
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v57"></a>
## 57. `TEX_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I`

Syntax: `TEX R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0,     ???255, R0, 0x0, 0x0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001101101............11111111.............................011
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v58"></a>
## 58. `TEX_P_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TEX P, R, R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 46-53 |
| SCR | 60 |
| operand 7 | 61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111............................111111........000000..01
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v59"></a>
## 59. `TEX_P_R_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TEX P, R, R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 46-53 |
| SCR | 60 |
| operand 7 | 61-62 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111............................111111........000000...0
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v60"></a>
## 60. `TEX_P_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TEX P, R, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0,     ???63, 0x0, CUBE, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 46-53 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111............................111111........000000.110
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v61"></a>
## 61. `TEX_P_R_R_R_R_UR_I_ARRAY_D`

Syntax: `TEX P, R, R, R, R, UR, INT_IMM, ARRAY_D`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, UR0, 0x0, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 7 | 61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111..........................................000000..01
........1111...............10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v62"></a>
## 62. `TEX_P_R_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TEX P, R, R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 7 | 61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111..........................................000000..01
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v63"></a>
## 63. `TEX_P_R_R_R_R_UR_I_D`

Syntax: `TEX P, R, R, R, R, UR, INT_IMM, D`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, UR0, 0x0, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 7 | 61-62 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111..........................................000000...0
........1111...............10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v64"></a>
## 64. `TEX_P_R_R_R_R_UR_I_D_I`

Syntax: `TEX P, R, R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 7 | 61-62 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111..........................................000000...0
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v65"></a>
## 65. `TEX_P_R_R_R_R_UR_I_SNOWFLAKE`

Syntax: `TEX P, R, R, R, R, UR, INT_IMM, SNOWFLAKE`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, UR0, 0x0, INVALID6 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111..........................................000000.011
........1111...............10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v66"></a>
## 66. `TEX_P_R_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TEX P, R, R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, R0, UR0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111..........................................000000.011
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v67"></a>
## 67. `TEX_P_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TEX P, R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 6 | 61 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111111111........000000..01
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v68"></a>
## 68. `TEX_P_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TEX P, R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 6 | 61-62 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111111111........000000...0
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v69"></a>
## 69. `TEX_P_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TEX P, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0,     ???63, 0x0, CUBE, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111111111........000000.110
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v70"></a>
## 70. `TEX_P_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TEX P, R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| operand 6 | 61 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111..............000000..01
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v71"></a>
## 71. `TEX_P_R_R_R_UR_I_D_I`

Syntax: `TEX P, R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| operand 6 | 61-62 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111..............000000...0
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v72"></a>
## 72. `TEX_P_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TEX P, R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0, R0, UR0, 0x0, CUBE, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111..............000000.110
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v73"></a>
## 73. `TEX_P_R_R_SNOWFLAKE_R_UR_I_ARRAY_D_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0,     ???255, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 7 | 61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111............11111111......................000000..01
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v74"></a>
## 74. `TEX_P_R_R_SNOWFLAKE_R_UR_I_D_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0,     ???255, R0, UR0, 0x0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 7 | 61-62 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111............11111111......................000000...0
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v75"></a>
## 75. `TEX_P_R_R_SNOWFLAKE_R_UR_I_SNOWFLAKE_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF P0, R0, R0,     ???255, R0, UR0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111............11111111......................000000.011
...........................10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v76"></a>
## 76. `TEX_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TEX R, R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 6 | 61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111............................111111........000000..01
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v77"></a>
## 77. `TEX_R_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TEX R, R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 6 | 61-62 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111............................111111........000000...0
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v78"></a>
## 78. `TEX_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TEX R, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, R0,     ???63, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111............................111111........000000.110
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v79"></a>
## 79. `TEX_R_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TEX R, R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| operand 6 | 61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111..........................................000000..01
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v80"></a>
## 80. `TEX_R_R_R_R_UR_I_D_I`

Syntax: `TEX R, R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| operand 6 | 61-62 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111..........................................000000...0
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v81"></a>
## 81. `TEX_R_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TEX R, R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, R0, UR0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111..........................................000000.011
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v82"></a>
## 82. `TEX_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TEX R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 46-53 |
| SCR | 60 |
| operand 5 | 61 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111111111........000000..01
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v83"></a>
## 83. `TEX_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TEX R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 46-53 |
| SCR | 60 |
| operand 5 | 61-62 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111111111........000000...0
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v84"></a>
## 84. `TEX_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TEX R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0,     ???63, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 46-53 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111111111........000000.110
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v85"></a>
## 85. `TEX_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TEX R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| SCR | 60 |
| operand 5 | 61 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111..............000000..01
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v86"></a>
## 86. `TEX_R_R_R_UR_I_D_I`

Syntax: `TEX R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| SCR | 60 |
| operand 5 | 61-62 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111..............000000...0
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v87"></a>
## 87. `TEX_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TEX R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.EF R0, R0, R0, UR0, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001101111....................11111111..............000000.110
.................111.......10000000000000.....................00
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

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v88"></a>
## 88. `TEX_P_R_R_R_R_ARRAY_D`

Syntax: `TEX P, R, R, R, R, ARRAY_D`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............................0000000000000000000...01
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v89"></a>
## 89. `TEX_P_R_R_R_R_ARRAY_D_I`

Syntax: `TEX P, R, R, R, R, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 61 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............................0000000000000000000...01
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v90"></a>
## 90. `TEX_P_R_R_R_R_D`

Syntax: `TEX P, R, R, R, R, D`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 61-62 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............................0000000000000000000....0
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v91"></a>
## 91. `TEX_P_R_R_R_R_D_I`

Syntax: `TEX P, R, R, R, R, D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 61-62 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............................0000000000000000000....0
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v92"></a>
## 92. `TEX_P_R_R_R_R_SNOWFLAKE`

Syntax: `TEX P, R, R, R, R, SNOWFLAKE`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, CUBE ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............................0000000000000000000..110
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v93"></a>
## 93. `TEX_P_R_R_R_R_SNOWFLAKE_I`

Syntax: `TEX P, R, R, R, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0, R0, INVALID6, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............................0000000000000000000..011
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v94"></a>
## 94. `TEX_P_R_R_R_SNOWFLAKE_ARRAY_D`

Syntax: `TEX P, R, R, R, SNOWFLAKE, ARRAY_D`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, ARRAY_1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100....................111111110000000000000000000...01
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v95"></a>
## 95. `TEX_P_R_R_R_SNOWFLAKE_ARRAY_D_I`

Syntax: `TEX P, R, R, R, SNOWFLAKE, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 61 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100....................111111110000000000000000000...01
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v96"></a>
## 96. `TEX_P_R_R_R_SNOWFLAKE_D`

Syntax: `TEX P, R, R, R, SNOWFLAKE, D`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, 1D ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 61-62 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100....................111111110000000000000000000....0
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v97"></a>
## 97. `TEX_P_R_R_R_SNOWFLAKE_D_I`

Syntax: `TEX P, R, R, R, SNOWFLAKE, D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 61-62 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100....................111111110000000000000000000....0
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v98"></a>
## 98. `TEX_P_R_R_R_SNOWFLAKE_SNOWFLAKE`

Syntax: `TEX P, R, R, R, SNOWFLAKE, SNOWFLAKE`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, INVALID6 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100....................111111110000000000000000000..011
........1111...............00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v99"></a>
## 99. `TEX_P_R_R_R_SNOWFLAKE_SNOWFLAKE_I`

Syntax: `TEX P, R, R, R, SNOWFLAKE, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0, R0,     ???255, CUBE, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100....................111111110000000000000000000..110
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v100"></a>
## 100. `TEX_P_R_R_SNOWFLAKE_R_ARRAY_D_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0,     ???255, R0, ARRAY_1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 61 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............11111111........0000000000000000000...01
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v101"></a>
## 101. `TEX_P_R_R_SNOWFLAKE_R_D_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, D, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0,     ???255, R0, 1D, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 61-62 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............11111111........0000000000000000000....0
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v102"></a>
## 102. `TEX_P_R_R_SNOWFLAKE_R_SNOWFLAKE_I`

Syntax: `TEX P, R, R, SNOWFLAKE, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF P0, R0, R0,     ???255, R0, INVALID6, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............11111111........0000000000000000000..011
...........................00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v103"></a>
## 103. `TEX_R_R_R_R_ARRAY_D_I`

Syntax: `TEX R, R, R, R, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0, R0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 61 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............................0000000000000000000...01
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v104"></a>
## 104. `TEX_R_R_R_R_D_I`

Syntax: `TEX R, R, R, R, D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0, R0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 61-62 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............................0000000000000000000....0
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v105"></a>
## 105. `TEX_R_R_R_R_SNOWFLAKE_I`

Syntax: `TEX R, R, R, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0, R0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............................0000000000000000000..110
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v106"></a>
## 106. `TEX_R_R_R_SNOWFLAKE_ARRAY_D_I`

Syntax: `TEX R, R, R, SNOWFLAKE, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0,     ???255, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 61 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100....................111111110000000000000000000...01
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v107"></a>
## 107. `TEX_R_R_R_SNOWFLAKE_D_I`

Syntax: `TEX R, R, R, SNOWFLAKE, D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0,     ???255, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 61-62 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100....................111111110000000000000000000....0
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v108"></a>
## 108. `TEX_R_R_R_SNOWFLAKE_SNOWFLAKE_I`

Syntax: `TEX R, R, R, SNOWFLAKE, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0, R0,     ???255, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100....................111111110000000000000000000..110
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v109"></a>
## 109. `TEX_R_R_SNOWFLAKE_R_ARRAY_D_I`

Syntax: `TEX R, R, SNOWFLAKE, R, ARRAY_D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0,     ???255, R0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 61 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............11111111........0000000000000000000...01
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v110"></a>
## 110. `TEX_R_R_SNOWFLAKE_R_D_I`

Syntax: `TEX R, R, SNOWFLAKE, R, D, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0,     ???255, R0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 61-62 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............11111111........0000000000000000000....0
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v111"></a>
## 111. `TEX_R_R_SNOWFLAKE_R_SNOWFLAKE_I`

Syntax: `TEX R, R, SNOWFLAKE, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TEX.???0.EF R0, R0,     ???255, R0, INVALID6, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| NDV | 77 |
| DC | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-88 |
| LC | 89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001101100............11111111........0000000000000000000..011
.................111.......00000000000000.....................00
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

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

