# TLD (SM89 SASS)

**NVIDIA:** Texture Load (Texture Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Texture load (texel fetch, no filtering) (category: Texture / surface)

Typically emitted for: unfiltered texel fetch with integer coords: `tex.1d.v4.s32.s32` / `tex1Dfetch`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x367, 0xb66, 0xd67 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2956)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [tld](../verify/RESULTS.md#tld): `tex.1d.v4.s32.s32 (integer coords, tex1Dfetch)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/TLD.html> (machine-derived by fuzzing the assembler; no semantics).

111 encoding variant(s):

- [TLD_P_R_R_R_I_I_ARRAY_D](#v1)
- [TLD_P_R_R_R_I_I_ARRAY_D_I](#v2)
- [TLD_P_R_R_R_I_I_D](#v3)
- [TLD_P_R_R_R_I_I_D_I](#v4)
- [TLD_P_R_R_R_I_I_SNOWFLAKE](#v5)
- [TLD_P_R_R_R_I_I_SNOWFLAKE_I](#v6)
- [TLD_P_R_R_R_R_I_I_ARRAY_D](#v7)
- [TLD_P_R_R_R_R_I_I_ARRAY_D_I](#v8)
- [TLD_P_R_R_R_R_I_I_D](#v9)
- [TLD_P_R_R_R_R_I_I_D_I](#v10)
- [TLD_P_R_R_R_R_I_I_SNOWFLAKE](#v11)
- [TLD_P_R_R_R_R_I_I_SNOWFLAKE_I](#v12)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_ARRAY_D](#v13)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_ARRAY_D_I](#v14)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_D](#v15)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_D_I](#v16)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE](#v17)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE_I](#v18)
- [TLD_P_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I](#v19)
- [TLD_P_R_R_SNOWFLAKE_R_I_I_D_I](#v20)
- [TLD_P_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I](#v21)
- [TLD_R_R_R_I_I_ARRAY_D_I](#v22)
- [TLD_R_R_R_I_I_D_I](#v23)
- [TLD_R_R_R_I_I_SNOWFLAKE_I](#v24)
- [TLD_R_R_R_R_I_I_ARRAY_D_I](#v25)
- [TLD_R_R_R_R_I_I_D_I](#v26)
- [TLD_R_R_R_R_I_I_SNOWFLAKE_I](#v27)
- [TLD_R_R_R_SNOWFLAKE_I_I_ARRAY_D_I](#v28)
- [TLD_R_R_R_SNOWFLAKE_I_I_D_I](#v29)
- [TLD_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE_I](#v30)
- [TLD_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I](#v31)
- [TLD_R_R_SNOWFLAKE_R_I_I_D_I](#v32)
- [TLD_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I](#v33)
- [TLD_P_R_R_R_R_I_I_I_ARRAY_D](#v34)
- [TLD_P_R_R_R_R_I_I_I_ARRAY_D_I](#v35)
- [TLD_P_R_R_R_R_I_I_I_D](#v36)
- [TLD_P_R_R_R_R_I_I_I_D_I](#v37)
- [TLD_P_R_R_R_R_I_I_I_SNOWFLAKE](#v38)
- [TLD_P_R_R_R_R_I_I_I_SNOWFLAKE_I](#v39)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D](#v40)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D_I](#v41)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_I_D](#v42)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_I_D_I](#v43)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE](#v44)
- [TLD_P_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE_I](#v45)
- [TLD_P_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I](#v46)
- [TLD_P_R_R_SNOWFLAKE_R_I_I_I_D_I](#v47)
- [TLD_P_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I](#v48)
- [TLD_R_R_R_R_I_I_I_ARRAY_D_I](#v49)
- [TLD_R_R_R_R_I_I_I_D_I](#v50)
- [TLD_R_R_R_R_I_I_I_SNOWFLAKE_I](#v51)
- [TLD_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D_I](#v52)
- [TLD_R_R_R_SNOWFLAKE_I_I_I_D_I](#v53)
- [TLD_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE_I](#v54)
- [TLD_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I](#v55)
- [TLD_R_R_SNOWFLAKE_R_I_I_I_D_I](#v56)
- [TLD_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I](#v57)
- [TLD_P_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v58)
- [TLD_P_R_R_R_R_SNOWFLAKE_I_D_I](#v59)
- [TLD_P_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v60)
- [TLD_P_R_R_R_R_UR_I_ARRAY_D](#v61)
- [TLD_P_R_R_R_R_UR_I_ARRAY_D_I](#v62)
- [TLD_P_R_R_R_R_UR_I_D](#v63)
- [TLD_P_R_R_R_R_UR_I_D_I](#v64)
- [TLD_P_R_R_R_R_UR_I_SNOWFLAKE](#v65)
- [TLD_P_R_R_R_R_UR_I_SNOWFLAKE_I](#v66)
- [TLD_P_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v67)
- [TLD_P_R_R_R_SNOWFLAKE_I_D_I](#v68)
- [TLD_P_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v69)
- [TLD_P_R_R_R_UR_I_ARRAY_D_I](#v70)
- [TLD_P_R_R_R_UR_I_D_I](#v71)
- [TLD_P_R_R_R_UR_I_SNOWFLAKE_I](#v72)
- [TLD_P_R_R_SNOWFLAKE_R_UR_I_ARRAY_D_I](#v73)
- [TLD_P_R_R_SNOWFLAKE_R_UR_I_D_I](#v74)
- [TLD_P_R_R_SNOWFLAKE_R_UR_I_SNOWFLAKE_I](#v75)
- [TLD_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v76)
- [TLD_R_R_R_R_SNOWFLAKE_I_D_I](#v77)
- [TLD_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v78)
- [TLD_R_R_R_R_UR_I_ARRAY_D_I](#v79)
- [TLD_R_R_R_R_UR_I_D_I](#v80)
- [TLD_R_R_R_R_UR_I_SNOWFLAKE_I](#v81)
- [TLD_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v82)
- [TLD_R_R_R_SNOWFLAKE_I_D_I](#v83)
- [TLD_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v84)
- [TLD_R_R_R_UR_I_ARRAY_D_I](#v85)
- [TLD_R_R_R_UR_I_D_I](#v86)
- [TLD_R_R_R_UR_I_SNOWFLAKE_I](#v87)
- [TLD_P_R_R_R_R_ARRAY_D](#v88)
- [TLD_P_R_R_R_R_ARRAY_D_I](#v89)
- [TLD_P_R_R_R_R_D](#v90)
- [TLD_P_R_R_R_R_D_I](#v91)
- [TLD_P_R_R_R_R_SNOWFLAKE](#v92)
- [TLD_P_R_R_R_R_SNOWFLAKE_I](#v93)
- [TLD_P_R_R_R_SNOWFLAKE_ARRAY_D](#v94)
- [TLD_P_R_R_R_SNOWFLAKE_ARRAY_D_I](#v95)
- [TLD_P_R_R_R_SNOWFLAKE_D](#v96)
- [TLD_P_R_R_R_SNOWFLAKE_D_I](#v97)
- [TLD_P_R_R_R_SNOWFLAKE_SNOWFLAKE](#v98)
- [TLD_P_R_R_R_SNOWFLAKE_SNOWFLAKE_I](#v99)
- [TLD_P_R_R_SNOWFLAKE_R_ARRAY_D_I](#v100)
- [TLD_P_R_R_SNOWFLAKE_R_D_I](#v101)
- [TLD_P_R_R_SNOWFLAKE_R_SNOWFLAKE_I](#v102)
- [TLD_R_R_R_R_ARRAY_D_I](#v103)
- [TLD_R_R_R_R_D_I](#v104)
- [TLD_R_R_R_R_SNOWFLAKE_I](#v105)
- [TLD_R_R_R_SNOWFLAKE_ARRAY_D_I](#v106)
- [TLD_R_R_R_SNOWFLAKE_D_I](#v107)
- [TLD_R_R_R_SNOWFLAKE_SNOWFLAKE_I](#v108)
- [TLD_R_R_SNOWFLAKE_R_ARRAY_D_I](#v109)
- [TLD_R_R_SNOWFLAKE_R_D_I](#v110)
- [TLD_R_R_SNOWFLAKE_R_SNOWFLAKE_I](#v111)

<a id="v1"></a>
## 1. `TLD_P_R_R_R_I_I_ARRAY_D`

Syntax: `TLD P, R, R, R, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, 0x0, 0x0, ARRAY_1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................0..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v2"></a>
## 2. `TLD_P_R_R_R_I_I_ARRAY_D_I`

Syntax: `TLD P, R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................0..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v3"></a>
## 3. `TLD_P_R_R_R_I_I_D`

Syntax: `TLD P, R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, 0x0, 0x0, 1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................0...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v4"></a>
## 4. `TLD_P_R_R_R_I_I_D_I`

Syntax: `TLD P, R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................0...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v5"></a>
## 5. `TLD_P_R_R_R_I_I_SNOWFLAKE`

Syntax: `TLD P, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, 0x0, 0x0, INVALID6 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................0..11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v6"></a>
## 6. `TLD_P_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TLD P, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, 0x0, 0x0, INVALID3, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 63 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................0.11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v7"></a>
## 7. `TLD_P_R_R_R_R_I_I_ARRAY_D`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, ARRAY_1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101..................................................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v8"></a>
## 8. `TLD_P_R_R_R_R_I_I_ARRAY_D_I`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101..................................................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v9"></a>
## 9. `TLD_P_R_R_R_R_I_I_D`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101...................................................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v10"></a>
## 10. `TLD_P_R_R_R_R_I_I_D_I`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101...................................................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v11"></a>
## 11. `TLD_P_R_R_R_R_I_I_SNOWFLAKE`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, INVALID3 ;`

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
| operand 7 | 63 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101.................................................11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v12"></a>
## 12. `TLD_P_R_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, INVALID6, 0x0 ;`

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
| operand 7 | 61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101..................................................11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v13"></a>
## 13. `TLD_P_R_R_R_SNOWFLAKE_I_I_ARRAY_D`

Syntax: `TLD.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TLD.B.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, ARRAY_1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................1..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v14"></a>
## 14. `TLD_P_R_R_R_SNOWFLAKE_I_I_ARRAY_D_I`

Syntax: `TLD.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.B.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................1..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v15"></a>
## 15. `TLD_P_R_R_R_SNOWFLAKE_I_I_D`

Syntax: `TLD.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D`  
Example: `@P0 TLD.B.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................1...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v16"></a>
## 16. `TLD_P_R_R_R_SNOWFLAKE_I_I_D_I`

Syntax: `TLD.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.B.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................1...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v17"></a>
## 17. `TLD_P_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE`

Syntax: `TLD.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TLD.B.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, INVALID6 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................1..11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v18"></a>
## 18. `TLD_P_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE_I`

Syntax: `TLD.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.B.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, INVALID3, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| SCR | 60 |
| operand 7 | 63 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................1.11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v19"></a>
## 19. `TLD_P_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101............11111111..............................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v20"></a>
## 20. `TLD_P_R_R_SNOWFLAKE_R_I_I_D_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101............11111111...............................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v21"></a>
## 21. `TLD_P_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, INVALID6, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101............11111111..............................11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v22"></a>
## 22. `TLD_R_R_R_I_I_ARRAY_D_I`

Syntax: `TLD R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................0..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v23"></a>
## 23. `TLD_R_R_R_I_I_D_I`

Syntax: `TLD R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................0...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v24"></a>
## 24. `TLD_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TLD R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, 0x0, 0x0, INVALID3, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| SCR | 60 |
| operand 5 | 63 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................0.11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v25"></a>
## 25. `TLD_R_R_R_R_I_I_ARRAY_D_I`

Syntax: `TLD R, R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101..................................................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v26"></a>
## 26. `TLD_R_R_R_R_I_I_D_I`

Syntax: `TLD R, R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101...................................................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v27"></a>
## 27. `TLD_R_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TLD R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, R0, 0x0, 0x0, INVALID3, 0x0 ;`

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
| operand 6 | 63 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101.................................................11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v28"></a>
## 28. `TLD_R_R_R_SNOWFLAKE_I_I_ARRAY_D_I`

Syntax: `TLD.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.B.INVALID0.EF R0, R0, R0,     ???255, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................1..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v29"></a>
## 29. `TLD_R_R_R_SNOWFLAKE_I_I_D_I`

Syntax: `TLD.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.B.INVALID0.EF R0, R0, R0,     ???255, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................1...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v30"></a>
## 30. `TLD_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE_I`

Syntax: `TLD.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.B.INVALID0.EF R0, R0, R0,     ???255, 0x0, 0x0, INVALID3, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 63 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101....................11111111...................1.11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v31"></a>
## 31. `TLD_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I`

Syntax: `TLD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0,     ???255, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101............11111111..............................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v32"></a>
## 32. `TLD_R_R_SNOWFLAKE_R_I_I_D_I`

Syntax: `TLD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0,     ???255, R0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101............11111111...............................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v33"></a>
## 33. `TLD_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I`

Syntax: `TLD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0,     ???255, R0, 0x0, 0x0, INVALID6, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101101............11111111..............................11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v34"></a>
## 34. `TLD_P_R_R_R_R_I_I_I_ARRAY_D`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, ARRAY_1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101..................................................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v35"></a>
## 35. `TLD_P_R_R_R_R_I_I_I_ARRAY_D_I`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101..................................................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v36"></a>
## 36. `TLD_P_R_R_R_R_I_I_I_D`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, 1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101...................................................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v37"></a>
## 37. `TLD_P_R_R_R_R_I_I_I_D_I`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101...................................................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v38"></a>
## 38. `TLD_P_R_R_R_R_I_I_I_SNOWFLAKE`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, INVALID3 ;`

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
| operand 8 | 63 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101.................................................11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v39"></a>
## 39. `TLD_P_R_R_R_R_I_I_I_SNOWFLAKE_I`

Syntax: `TLD P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, INVALID6, 0x0 ;`

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
| operand 8 | 61 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101..................................................11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v40"></a>
## 40. `TLD_P_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D`

Syntax: `TLD P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, ARRAY_1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101....................11111111......................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v41"></a>
## 41. `TLD_P_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D_I`

Syntax: `TLD P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101....................11111111......................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v42"></a>
## 42. `TLD_P_R_R_R_SNOWFLAKE_I_I_I_D`

Syntax: `TLD P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, 1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101....................11111111.......................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v43"></a>
## 43. `TLD_P_R_R_R_SNOWFLAKE_I_I_I_D_I`

Syntax: `TLD P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101....................11111111.......................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v44"></a>
## 44. `TLD_P_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE`

Syntax: `TLD P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, INVALID6 ;`

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
| operand 8 | 61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101....................11111111......................11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v45"></a>
## 45. `TLD_P_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE_I`

Syntax: `TLD P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, INVALID3, 0x0 ;`

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
| operand 8 | 63 |
| operand 1 | 64-71 |
| operand 9 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101....................11111111.....................11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v46"></a>
## 46. `TLD_P_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101............11111111..............................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v47"></a>
## 47. `TLD_P_R_R_SNOWFLAKE_R_I_I_I_D_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101............11111111...............................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v48"></a>
## 48. `TLD_P_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0,     ???255, R0, 0x0, 0x0, 0x0, INVALID6, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101............11111111..............................11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v49"></a>
## 49. `TLD_R_R_R_R_I_I_I_ARRAY_D_I`

Syntax: `TLD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101..................................................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v50"></a>
## 50. `TLD_R_R_R_R_I_I_I_D_I`

Syntax: `TLD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101...................................................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v51"></a>
## 51. `TLD_R_R_R_R_I_I_I_SNOWFLAKE_I`

Syntax: `TLD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0, R0, 0x0, 0x0, 0x0, INVALID3, 0x0 ;`

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
| operand 7 | 63 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101.................................................11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v52"></a>
## 52. `TLD_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D_I`

Syntax: `TLD R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0,     ???255, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101....................11111111......................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v53"></a>
## 53. `TLD_R_R_R_SNOWFLAKE_I_I_I_D_I`

Syntax: `TLD R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0,     ???255, 0x0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101....................11111111.......................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v54"></a>
## 54. `TLD_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE_I`

Syntax: `TLD R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0,     ???255, 0x0, 0x0, 0x0, INVALID3, 0x0 ;`

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
| operand 7 | 63 |
| operand 0 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101....................11111111.....................11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v55"></a>
## 55. `TLD_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I`

Syntax: `TLD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0,     ???255, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101............11111111..............................01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v56"></a>
## 56. `TLD_R_R_SNOWFLAKE_R_I_I_I_D_I`

Syntax: `TLD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0,     ???255, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101............11111111...............................0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v57"></a>
## 57. `TLD_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I`

Syntax: `TLD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0,     ???255, R0, 0x0, 0x0, 0x0, INVALID6, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000101101101............11111111..............................11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v58"></a>
## 58. `TLD_P_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TLD P, R, R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111............................111111........000000..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v59"></a>
## 59. `TLD_P_R_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TLD P, R, R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111............................111111........000000...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v60"></a>
## 60. `TLD_P_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TLD P, R, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0,     ???63, 0x0, INVALID3, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 46-53 |
| SCR | 60 |
| operand 7 | 63 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111............................111111........000000.11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v61"></a>
## 61. `TLD_P_R_R_R_R_UR_I_ARRAY_D`

Syntax: `TLD P, R, R, R, R, UR, INT_IMM, ARRAY_D`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, UR0, 0x0, ARRAY_1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111..........................................000000..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v62"></a>
## 62. `TLD_P_R_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TLD P, R, R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111..........................................000000..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v63"></a>
## 63. `TLD_P_R_R_R_R_UR_I_D`

Syntax: `TLD P, R, R, R, R, UR, INT_IMM, D`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, UR0, 0x0, 1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111..........................................000000...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v64"></a>
## 64. `TLD_P_R_R_R_R_UR_I_D_I`

Syntax: `TLD P, R, R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111..........................................000000...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v65"></a>
## 65. `TLD_P_R_R_R_R_UR_I_SNOWFLAKE`

Syntax: `TLD P, R, R, R, R, UR, INT_IMM, SNOWFLAKE`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, UR0, 0x0, INVALID6 ;`

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
| operand 7 | 61 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111..........................................000000..11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v66"></a>
## 66. `TLD_P_R_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TLD P, R, R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, R0, UR0, 0x0, INVALID6, 0x0 ;`

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
| operand 7 | 61 |
| operand 1 | 64-71 |
| operand 8 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111..........................................000000..11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v67"></a>
## 67. `TLD_P_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TLD P, R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111111111........000000..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v68"></a>
## 68. `TLD_P_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TLD P, R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111111111........000000...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v69"></a>
## 69. `TLD_P_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TLD P, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0,     ???63, 0x0, INVALID3, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 6 | 63 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111111111........000000.11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v70"></a>
## 70. `TLD_P_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TLD P, R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111..............000000..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v71"></a>
## 71. `TLD_P_R_R_R_UR_I_D_I`

Syntax: `TLD P, R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111..............000000...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v72"></a>
## 72. `TLD_P_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TLD P, R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0, R0, UR0, 0x0, INVALID3, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| operand 6 | 63 |
| operand 1 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111..............000000.11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v73"></a>
## 73. `TLD_P_R_R_SNOWFLAKE_R_UR_I_ARRAY_D_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0,     ???255, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111............11111111......................000000..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v74"></a>
## 74. `TLD_P_R_R_SNOWFLAKE_R_UR_I_D_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0,     ???255, R0, UR0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111............11111111......................000000...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v75"></a>
## 75. `TLD_P_R_R_SNOWFLAKE_R_UR_I_SNOWFLAKE_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF P0, R0, R0,     ???255, R0, UR0, 0x0, INVALID6, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111............11111111......................000000..11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v76"></a>
## 76. `TLD_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TLD R, R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111............................111111........000000..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v77"></a>
## 77. `TLD_R_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TLD R, R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111............................111111........000000...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v78"></a>
## 78. `TLD_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TLD R, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, R0,     ???63, 0x0, INVALID3, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 6 | 63 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111............................111111........000000.11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v79"></a>
## 79. `TLD_R_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TLD R, R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111..........................................000000..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v80"></a>
## 80. `TLD_R_R_R_R_UR_I_D_I`

Syntax: `TLD R, R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111..........................................000000...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v81"></a>
## 81. `TLD_R_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TLD R, R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, R0, UR0, 0x0, INVALID6, 0x0 ;`

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
| operand 6 | 61 |
| operand 0 | 64-71 |
| operand 7 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111..........................................000000..11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v82"></a>
## 82. `TLD_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TLD R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111111111........000000..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v83"></a>
## 83. `TLD_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TLD R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111111111........000000...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v84"></a>
## 84. `TLD_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TLD R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0,     ???63, 0x0, INVALID3, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 46-53 |
| SCR | 60 |
| operand 5 | 63 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111111111........000000.11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v85"></a>
## 85. `TLD_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TLD R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111..............000000..01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v86"></a>
## 86. `TLD_R_R_R_UR_I_D_I`

Syntax: `TLD R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111..............000000...0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v87"></a>
## 87. `TLD_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TLD R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.INVALID0.EF R0, R0, R0, UR0, 0x0, INVALID3, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| SCR | 60 |
| operand 5 | 63 |
| operand 0 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001101111....................11111111..............000000.11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v88"></a>
## 88. `TLD_P_R_R_R_R_ARRAY_D`

Syntax: `TLD P, R, R, R, R, ARRAY_D`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, ARRAY_1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............................0000000000000000000...01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v89"></a>
## 89. `TLD_P_R_R_R_R_ARRAY_D_I`

Syntax: `TLD P, R, R, R, R, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............................0000000000000000000...01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v90"></a>
## 90. `TLD_P_R_R_R_R_D`

Syntax: `TLD P, R, R, R, R, D`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, 1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............................0000000000000000000....0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v91"></a>
## 91. `TLD_P_R_R_R_R_D_I`

Syntax: `TLD P, R, R, R, R, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............................0000000000000000000....0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v92"></a>
## 92. `TLD_P_R_R_R_R_SNOWFLAKE`

Syntax: `TLD P, R, R, R, R, SNOWFLAKE`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, INVALID3 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 63 |
| operand 1 | 64-71 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............................0000000000000000000..11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v93"></a>
## 93. `TLD_P_R_R_R_R_SNOWFLAKE_I`

Syntax: `TLD P, R, R, R, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0, R0, INVALID6, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............................0000000000000000000...11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v94"></a>
## 94. `TLD_P_R_R_R_SNOWFLAKE_ARRAY_D`

Syntax: `TLD P, R, R, R, SNOWFLAKE, ARRAY_D`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, ARRAY_1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100....................111111110000000000000000000...01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v95"></a>
## 95. `TLD_P_R_R_R_SNOWFLAKE_ARRAY_D_I`

Syntax: `TLD P, R, R, R, SNOWFLAKE, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100....................111111110000000000000000000...01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v96"></a>
## 96. `TLD_P_R_R_R_SNOWFLAKE_D`

Syntax: `TLD P, R, R, R, SNOWFLAKE, D`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, 1D ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100....................111111110000000000000000000....0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v97"></a>
## 97. `TLD_P_R_R_R_SNOWFLAKE_D_I`

Syntax: `TLD P, R, R, R, SNOWFLAKE, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100....................111111110000000000000000000....0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v98"></a>
## 98. `TLD_P_R_R_R_SNOWFLAKE_SNOWFLAKE`

Syntax: `TLD P, R, R, R, SNOWFLAKE, SNOWFLAKE`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, INVALID6 ;`

Register access: WRITE P (1 slots); WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100....................111111110000000000000000000...11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v99"></a>
## 99. `TLD_P_R_R_R_SNOWFLAKE_SNOWFLAKE_I`

Syntax: `TLD P, R, R, R, SNOWFLAKE, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0, R0,     ???255, INVALID3, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 63 |
| operand 1 | 64-71 |
| operand 6 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100....................111111110000000000000000000..11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v100"></a>
## 100. `TLD_P_R_R_SNOWFLAKE_R_ARRAY_D_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0,     ???255, R0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............11111111........0000000000000000000...01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v101"></a>
## 101. `TLD_P_R_R_SNOWFLAKE_R_D_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0,     ???255, R0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............11111111........0000000000000000000....0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v102"></a>
## 102. `TLD_P_R_R_SNOWFLAKE_R_SNOWFLAKE_I`

Syntax: `TLD P, R, R, SNOWFLAKE, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF P0, R0, R0,     ???255, R0, INVALID6, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............11111111........0000000000000000000...11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v103"></a>
## 103. `TLD_R_R_R_R_ARRAY_D_I`

Syntax: `TLD R, R, R, R, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0, R0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............................0000000000000000000...01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v104"></a>
## 104. `TLD_R_R_R_R_D_I`

Syntax: `TLD R, R, R, R, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0, R0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............................0000000000000000000....0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v105"></a>
## 105. `TLD_R_R_R_R_SNOWFLAKE_I`

Syntax: `TLD R, R, R, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0, R0, INVALID3, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 63 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............................0000000000000000000..11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v106"></a>
## 106. `TLD_R_R_R_SNOWFLAKE_ARRAY_D_I`

Syntax: `TLD R, R, R, SNOWFLAKE, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0,     ???255, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100....................111111110000000000000000000...01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v107"></a>
## 107. `TLD_R_R_R_SNOWFLAKE_D_I`

Syntax: `TLD R, R, R, SNOWFLAKE, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0,     ???255, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100....................111111110000000000000000000....0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v108"></a>
## 108. `TLD_R_R_R_SNOWFLAKE_SNOWFLAKE_I`

Syntax: `TLD R, R, R, SNOWFLAKE, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0, R0,     ???255, INVALID3, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 63 |
| operand 0 | 64-71 |
| operand 5 | 72-75 |
| AOFFI | 76 |
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100....................111111110000000000000000000..11.
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v109"></a>
## 109. `TLD_R_R_SNOWFLAKE_R_ARRAY_D_I`

Syntax: `TLD R, R, SNOWFLAKE, R, ARRAY_D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0,     ???255, R0, ARRAY_1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............11111111........0000000000000000000...01
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v110"></a>
## 110. `TLD_R_R_SNOWFLAKE_R_D_I`

Syntax: `TLD R, R, SNOWFLAKE, R, D, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0,     ???255, R0, 1D, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............11111111........0000000000000000000....0
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v111"></a>
## 111. `TLD_R_R_SNOWFLAKE_R_SNOWFLAKE_I`

Syntax: `TLD R, R, SNOWFLAKE, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TLD.???0.INVALID0.EF R0, R0,     ???255, R0, INVALID6, 0x0 ;`

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
| CL | 77 |
| MS | 78 |
| modi 2 | 79-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111001101100............11111111........0000000000000000000...11
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
| `000` | `INVALID0.` |
| `001` | `LZ.` |
| `010` | `INVALID2.` |
| `011` | `LL.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

