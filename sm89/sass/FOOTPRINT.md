# FOOTPRINT (SM89 SASS)

**NVIDIA:** not listed in the official Ampere/Ada opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)).

Notes: Texture footprint query (category: Texture / surface)

Typically emitted for: texture footprint query (`__nv_tex_footprint`)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/FOOTPRINT.html> (machine-derived by fuzzing the assembler; no semantics).

102 encoding variant(s):

- [FOOTPRINT_P_R_R_R_I_I_D](#v1)
- [FOOTPRINT_P_R_R_R_I_I_SNOWFLAKE](#v2)
- [FOOTPRINT_P_R_R_R_R_I_I_D](#v3)
- [FOOTPRINT_P_R_R_R_R_I_I_SNOWFLAKE](#v4)
- [FOOTPRINT_P_R_R_R_SNOWFLAKE_I_I_D](#v5)
- [FOOTPRINT_P_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE](#v6)
- [FOOTPRINT_P_R_R_SNOWFLAKE_R_I_I_D](#v7)
- [FOOTPRINT_P_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE](#v8)
- [FOOTPRINT_P_SNOWFLAKE_R_R_I_I_D](#v9)
- [FOOTPRINT_P_SNOWFLAKE_R_R_I_I_SNOWFLAKE](#v10)
- [FOOTPRINT_P_SNOWFLAKE_R_R_R_I_I_D](#v11)
- [FOOTPRINT_P_SNOWFLAKE_R_R_R_I_I_SNOWFLAKE](#v12)
- [FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_I_I_D](#v13)
- [FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_I_I_SNOWFLAKE](#v14)
- [FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_I_I_D](#v15)
- [FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_I_I_SNOWFLAKE](#v16)
- [FOOTPRINT_R_R_R_I_I_D](#v17)
- [FOOTPRINT_R_R_R_I_I_SNOWFLAKE](#v18)
- [FOOTPRINT_R_R_R_R_I_I_D](#v19)
- [FOOTPRINT_R_R_R_R_I_I_SNOWFLAKE](#v20)
- [FOOTPRINT_R_R_R_SNOWFLAKE_I_I_D](#v21)
- [FOOTPRINT_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE](#v22)
- [FOOTPRINT_R_R_SNOWFLAKE_R_I_I_D](#v23)
- [FOOTPRINT_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE](#v24)
- [FOOTPRINT_SNOWFLAKE_R_R_I_I_D](#v25)
- [FOOTPRINT_SNOWFLAKE_R_R_I_I_SNOWFLAKE](#v26)
- [FOOTPRINT_SNOWFLAKE_R_R_R_I_I_D](#v27)
- [FOOTPRINT_SNOWFLAKE_R_R_R_I_I_SNOWFLAKE](#v28)
- [FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_I_I_D](#v29)
- [FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_I_I_SNOWFLAKE](#v30)
- [FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_I_I_D](#v31)
- [FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_I_I_SNOWFLAKE](#v32)
- [FOOTPRINT_P_R_R_R_R_I_I_I_D](#v33)
- [FOOTPRINT_P_R_R_R_R_I_I_I_SNOWFLAKE](#v34)
- [FOOTPRINT_P_R_R_R_SNOWFLAKE_I_I_I_D](#v35)
- [FOOTPRINT_P_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE](#v36)
- [FOOTPRINT_P_R_R_SNOWFLAKE_R_I_I_I_D](#v37)
- [FOOTPRINT_P_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE](#v38)
- [FOOTPRINT_P_SNOWFLAKE_R_R_R_I_I_I_D](#v39)
- [FOOTPRINT_P_SNOWFLAKE_R_R_R_I_I_I_SNOWFLAKE](#v40)
- [FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_I_I_I_D](#v41)
- [FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE](#v42)
- [FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_I_I_I_D](#v43)
- [FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE](#v44)
- [FOOTPRINT_R_R_R_R_I_I_I_D](#v45)
- [FOOTPRINT_R_R_R_R_I_I_I_SNOWFLAKE](#v46)
- [FOOTPRINT_R_R_R_SNOWFLAKE_I_I_I_D](#v47)
- [FOOTPRINT_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE](#v48)
- [FOOTPRINT_R_R_SNOWFLAKE_R_I_I_I_D](#v49)
- [FOOTPRINT_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE](#v50)
- [FOOTPRINT_SNOWFLAKE_R_R_R_I_I_I_D](#v51)
- [FOOTPRINT_SNOWFLAKE_R_R_R_I_I_I_SNOWFLAKE](#v52)
- [FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_I_I_I_D](#v53)
- [FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE](#v54)
- [FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_I_I_I_D](#v55)
- [FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE](#v56)
- [FOOTPRINT_P_R_R_R_R_SNOWFLAKE_I_D](#v57)
- [FOOTPRINT_P_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE](#v58)
- [FOOTPRINT_P_R_R_R_R_UR_I_D](#v59)
- [FOOTPRINT_P_R_R_R_R_UR_I_SNOWFLAKE](#v60)
- [FOOTPRINT_P_R_R_R_SNOWFLAKE_I_D](#v61)
- [FOOTPRINT_P_R_R_R_SNOWFLAKE_I_SNOWFLAKE](#v62)
- [FOOTPRINT_P_R_R_R_UR_I_D](#v63)
- [FOOTPRINT_P_R_R_R_UR_I_SNOWFLAKE](#v64)
- [FOOTPRINT_P_R_R_SNOWFLAKE_R_UR_I_D](#v65)
- [FOOTPRINT_P_R_R_SNOWFLAKE_R_UR_I_SNOWFLAKE](#v66)
- [FOOTPRINT_P_SNOWFLAKE_R_R_R_UR_I_D](#v67)
- [FOOTPRINT_P_SNOWFLAKE_R_R_R_UR_I_SNOWFLAKE](#v68)
- [FOOTPRINT_R_R_R_R_SNOWFLAKE_I_D](#v69)
- [FOOTPRINT_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE](#v70)
- [FOOTPRINT_R_R_R_R_UR_I_D](#v71)
- [FOOTPRINT_R_R_R_R_UR_I_SNOWFLAKE](#v72)
- [FOOTPRINT_R_R_R_SNOWFLAKE_I_D](#v73)
- [FOOTPRINT_R_R_R_SNOWFLAKE_I_SNOWFLAKE](#v74)
- [FOOTPRINT_R_R_R_UR_I_D](#v75)
- [FOOTPRINT_R_R_R_UR_I_SNOWFLAKE](#v76)
- [FOOTPRINT_SNOWFLAKE_R_R_R_UR_I_D](#v77)
- [FOOTPRINT_SNOWFLAKE_R_R_R_UR_I_SNOWFLAKE](#v78)
- [FOOTPRINT_P_R_R_R_R_D](#v79)
- [FOOTPRINT_P_R_R_R_R_SNOWFLAKE](#v80)
- [FOOTPRINT_P_R_R_R_SNOWFLAKE_D](#v81)
- [FOOTPRINT_P_R_R_R_SNOWFLAKE_SNOWFLAKE](#v82)
- [FOOTPRINT_P_R_R_SNOWFLAKE_R_D](#v83)
- [FOOTPRINT_P_R_R_SNOWFLAKE_R_SNOWFLAKE](#v84)
- [FOOTPRINT_P_SNOWFLAKE_R_R_R_D](#v85)
- [FOOTPRINT_P_SNOWFLAKE_R_R_R_SNOWFLAKE](#v86)
- [FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_D](#v87)
- [FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_SNOWFLAKE](#v88)
- [FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_D](#v89)
- [FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_SNOWFLAKE](#v90)
- [FOOTPRINT_R_R_R_R_D](#v91)
- [FOOTPRINT_R_R_R_R_SNOWFLAKE](#v92)
- [FOOTPRINT_R_R_R_SNOWFLAKE_D](#v93)
- [FOOTPRINT_R_R_R_SNOWFLAKE_SNOWFLAKE](#v94)
- [FOOTPRINT_R_R_SNOWFLAKE_R_D](#v95)
- [FOOTPRINT_R_R_SNOWFLAKE_R_SNOWFLAKE](#v96)
- [FOOTPRINT_SNOWFLAKE_R_R_R_D](#v97)
- [FOOTPRINT_SNOWFLAKE_R_R_R_SNOWFLAKE](#v98)
- [FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_D](#v99)
- [FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_SNOWFLAKE](#v100)
- [FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_D](#v101)
- [FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_SNOWFLAKE](#v102)

<a id="v1"></a>
## 1. `FOOTPRINT_P_R_R_R_I_I_D`

Syntax: `FOOTPRINT P, R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................0.100
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v2"></a>
## 2. `FOOTPRINT_P_R_R_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................0.0..
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v3"></a>
## 3. `FOOTPRINT_P_R_R_R_R_I_I_D`

Syntax: `FOOTPRINT P, R, R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101.................................................100
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v4"></a>
## 4. `FOOTPRINT_P_R_R_R_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0, R0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

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
| operand 7 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101.................................................0..
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v5"></a>
## 5. `FOOTPRINT_P_R_R_R_SNOWFLAKE_I_I_D`

Syntax: `FOOTPRINT.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.B.TEX P0, R0, R0, R0,     ???255, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| SCR | 60 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................1.100
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v6"></a>
## 6. `FOOTPRINT_P_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT.B P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.B.TEX P0, R0, R0, R0,     ???255, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| SCR | 60 |
| operand 7 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................1.1..
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v7"></a>
## 7. `FOOTPRINT_P_R_R_SNOWFLAKE_R_I_I_D`

Syntax: `FOOTPRINT P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0,     ???255, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101............11111111.............................100
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v8"></a>
## 8. `FOOTPRINT_P_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0,     ???255, R0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 7 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101............11111111.............................0..
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v9"></a>
## 9. `FOOTPRINT_P_SNOWFLAKE_R_R_I_I_D`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0,     ???255, R0, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................0.100
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v10"></a>
## 10. `FOOTPRINT_P_SNOWFLAKE_R_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0,     ???255, R0, R0, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................0.1..
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v11"></a>
## 11. `FOOTPRINT_P_SNOWFLAKE_R_R_R_I_I_D`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0,     ???255, R0, R0, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101.................................................100
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v12"></a>
## 12. `FOOTPRINT_P_SNOWFLAKE_R_R_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0,     ???255, R0, R0, R0, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

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
| operand 7 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101.................................................1..
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v13"></a>
## 13. `FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_I_I_D`

Syntax: `FOOTPRINT.B P, SNOWFLAKE, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.B.TEX P0,     ???255, R0, R0, ???255, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................1.100
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v14"></a>
## 14. `FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT.B P, SNOWFLAKE, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.B.TEX P0,     ???255, R0, R0, ???255, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| SCR | 60 |
| operand 7 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................1.1..
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v15"></a>
## 15. `FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_I_I_D`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, SNOWFLAKE, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0,     ???255, R0, ???255, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101............11111111.............................100
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v16"></a>
## 16. `FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, SNOWFLAKE, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0,     ???255, R0, ???255, R0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 6 | 40-52, 54 |
| operand 5 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 7 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
010011101101............11111111.............................0..
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v17"></a>
## 17. `FOOTPRINT_R_R_R_I_I_D`

Syntax: `FOOTPRINT R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| SCR | 60 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................0.100
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v18"></a>
## 18. `FOOTPRINT_R_R_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| SCR | 60 |
| operand 5 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................0.0..
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v19"></a>
## 19. `FOOTPRINT_R_R_R_R_I_I_D`

Syntax: `FOOTPRINT R, R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101.................................................100
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v20"></a>
## 20. `FOOTPRINT_R_R_R_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0, R0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

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
| operand 6 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101.................................................0..
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v21"></a>
## 21. `FOOTPRINT_R_R_R_SNOWFLAKE_I_I_D`

Syntax: `FOOTPRINT.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.B.TEX R0, R0, R0,     ???255, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................1.100
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v22"></a>
## 22. `FOOTPRINT_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.B.TEX R0, R0, R0,     ???255, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................1.1..
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v23"></a>
## 23. `FOOTPRINT_R_R_SNOWFLAKE_R_I_I_D`

Syntax: `FOOTPRINT R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX R0, R0,     ???255, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101............11111111.............................100
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v24"></a>
## 24. `FOOTPRINT_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX R0, R0,     ???255, R0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 6 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101............11111111.............................0..
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v25"></a>
## 25. `FOOTPRINT_SNOWFLAKE_R_R_I_I_D`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX     ???255, R0, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................0.100
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v26"></a>
## 26. `FOOTPRINT_SNOWFLAKE_R_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX     ???255, R0, R0, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| SCR | 60 |
| operand 5 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................0.1..
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v27"></a>
## 27. `FOOTPRINT_SNOWFLAKE_R_R_R_I_I_D`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX     ???255, R0, R0, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101.................................................100
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v28"></a>
## 28. `FOOTPRINT_SNOWFLAKE_R_R_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX     ???255, R0, R0, R0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

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
| operand 6 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101.................................................0..
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v29"></a>
## 29. `FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_I_I_D`

Syntax: `FOOTPRINT.B SNOWFLAKE, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.B.TEX     ???255, R0, R0, ???255, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................1.100
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v30"></a>
## 30. `FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT.B SNOWFLAKE, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.B.TEX     ???255, R0, R0, ???255, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| SCR | 60 |
| operand 6 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101....................11111111...................1.1..
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v31"></a>
## 31. `FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_I_I_D`

Syntax: `FOOTPRINT SNOWFLAKE, R, SNOWFLAKE, R, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX     ???255, R0, ???255, R0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101............11111111.............................100
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v32"></a>
## 32. `FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT SNOWFLAKE, R, SNOWFLAKE, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX     ???255, R0, ???255, R0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| SCR | 60 |
| operand 6 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
010011101101............11111111.............................0..
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v33"></a>
## 33. `FOOTPRINT_P_R_R_R_R_I_I_I_D`

Syntax: `FOOTPRINT P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101.................................................100
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v34"></a>
## 34. `FOOTPRINT_P_R_R_R_R_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0, R0, R0, 0x0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

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
| operand 8 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101.................................................0..
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v35"></a>
## 35. `FOOTPRINT_P_R_R_R_SNOWFLAKE_I_I_I_D`

Syntax: `FOOTPRINT P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101....................11111111.....................100
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v36"></a>
## 36. `FOOTPRINT_P_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0, R0,     ???255, 0x0, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

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
| operand 8 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101....................11111111.....................1..
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v37"></a>
## 37. `FOOTPRINT_P_R_R_SNOWFLAKE_R_I_I_I_D`

Syntax: `FOOTPRINT P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0,     ???255, R0, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101............11111111.............................100
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v38"></a>
## 38. `FOOTPRINT_P_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0,     ???255, R0, 0x0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

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
| operand 8 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101............11111111.............................0..
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v39"></a>
## 39. `FOOTPRINT_P_SNOWFLAKE_R_R_R_I_I_I_D`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, R0, R0, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101.................................................100
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v40"></a>
## 40. `FOOTPRINT_P_SNOWFLAKE_R_R_R_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, R0, R0, 0x0, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

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
| operand 8 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101.................................................1..
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v41"></a>
## 41. `FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_I_I_I_D`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, R0, ???255, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101....................11111111.....................100
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v42"></a>
## 42. `FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, R0, ???255, 0x0, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); READ R (3 slots)

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
| operand 8 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101....................11111111.....................1..
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v43"></a>
## 43. `FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_I_I_I_D`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, ???255, R0, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101............11111111.............................100
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v44"></a>
## 44. `FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, ???255, R0, 0x0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); READ R (1 slots)

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
| operand 8 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101101............11111111.............................0..
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v45"></a>
## 45. `FOOTPRINT_R_R_R_R_I_I_I_D`

Syntax: `FOOTPRINT R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0, R0, R0, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101.................................................100
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v46"></a>
## 46. `FOOTPRINT_R_R_R_R_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0, R0, R0, 0x0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

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
| operand 7 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101.................................................0..
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v47"></a>
## 47. `FOOTPRINT_R_R_R_SNOWFLAKE_I_I_I_D`

Syntax: `FOOTPRINT R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0, R0,     ???255, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101....................11111111.....................100
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v48"></a>
## 48. `FOOTPRINT_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0, R0,     ???255, 0x0, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

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
| operand 7 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101....................11111111.....................1..
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v49"></a>
## 49. `FOOTPRINT_R_R_SNOWFLAKE_R_I_I_I_D`

Syntax: `FOOTPRINT R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0,     ???255, R0, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101............11111111.............................100
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v50"></a>
## 50. `FOOTPRINT_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0,     ???255, R0, 0x0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

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
| operand 7 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101............11111111.............................0..
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v51"></a>
## 51. `FOOTPRINT_SNOWFLAKE_R_R_R_I_I_I_D`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, R0, R0, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101.................................................100
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v52"></a>
## 52. `FOOTPRINT_SNOWFLAKE_R_R_R_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, R0, R0, 0x0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

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
| operand 7 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101.................................................0..
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v53"></a>
## 53. `FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_I_I_I_D`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, R0, ???255, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101....................11111111.....................100
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v54"></a>
## 54. `FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, R0, ???255, 0x0, 0x0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); READ R (3 slots)

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
| operand 7 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101....................11111111.....................1..
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v55"></a>
## 55. `FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_I_I_I_D`

Syntax: `FOOTPRINT SNOWFLAKE, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, ???255, R0, 0x0, 0x0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (1 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101............11111111.............................100
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v56"></a>
## 56. `FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE`

Syntax: `FOOTPRINT SNOWFLAKE, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, ???255, R0, 0x0, 0x0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); READ R (1 slots)

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
| operand 7 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101101............11111111.............................0..
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v57"></a>
## 57. `FOOTPRINT_P_R_R_R_R_SNOWFLAKE_I_D`

Syntax: `FOOTPRINT P, R, R, R, R, SNOWFLAKE, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0, R0,     ???63, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 46-53 |
| SCR | 60 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111............................111111........000000.100
........0000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v58"></a>
## 58. `FOOTPRINT_P_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0, R0,     ???63, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 6 | 46-53 |
| SCR | 60 |
| operand 7 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111............................111111........000000.1..
........0000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v59"></a>
## 59. `FOOTPRINT_P_R_R_R_R_UR_I_D`

Syntax: `FOOTPRINT P, R, R, R, R, UR, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0, R0, UR0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots); READ UR (2 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111..........................................000000.100
........0000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v60"></a>
## 60. `FOOTPRINT_P_R_R_R_R_UR_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, R, R, UR, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0, R0, UR0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 7 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111..........................................000000.0..
........0000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v61"></a>
## 61. `FOOTPRINT_P_R_R_R_SNOWFLAKE_I_D`

Syntax: `FOOTPRINT P, R, R, R, SNOWFLAKE, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0,     ???63, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111....................11111111111111........000000.100
........0000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v62"></a>
## 62. `FOOTPRINT_P_R_R_R_SNOWFLAKE_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0,     ???63, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 6 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111....................11111111111111........000000.1..
........0000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v63"></a>
## 63. `FOOTPRINT_P_R_R_R_UR_I_D`

Syntax: `FOOTPRINT P, R, R, R, UR, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0, UR0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111....................11111111..............000000.100
........0000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v64"></a>
## 64. `FOOTPRINT_P_R_R_R_UR_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, R, UR, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0, R0, UR0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| operand 6 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111....................11111111..............000000.1..
........0000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v65"></a>
## 65. `FOOTPRINT_P_R_R_SNOWFLAKE_R_UR_I_D`

Syntax: `FOOTPRINT P, R, R, SNOWFLAKE, R, UR, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0,     ???255, R0, UR0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111............11111111......................000000.100
........0000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v66"></a>
## 66. `FOOTPRINT_P_R_R_SNOWFLAKE_R_UR_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, SNOWFLAKE, R, UR, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0, R0, R0,     ???255, R0, UR0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 7 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111............11111111......................000000.0..
........0000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v67"></a>
## 67. `FOOTPRINT_P_SNOWFLAKE_R_R_R_UR_I_D`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, R, UR, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX P0,     ???255, R0, R0, R0, UR0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111..........................................000000.100
111111110000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v68"></a>
## 68. `FOOTPRINT_P_SNOWFLAKE_R_R_R_UR_I_SNOWFLAKE`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, R, UR, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX P0,     ???255, R0, R0, R0, UR0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-53 |
| SCR | 60 |
| operand 7 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
001011101111..........................................000000.0..
111111110000...0....000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v69"></a>
## 69. `FOOTPRINT_R_R_R_R_SNOWFLAKE_I_D`

Syntax: `FOOTPRINT R, R, R, R, SNOWFLAKE, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0, R0,     ???63, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101111............................111111........000000.100
........0000...00111000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v70"></a>
## 70. `FOOTPRINT_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0, R0,     ???63, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| SCR | 60 |
| operand 6 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101111............................111111........000000.1..
........0000...00111000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v71"></a>
## 71. `FOOTPRINT_R_R_R_R_UR_I_D`

Syntax: `FOOTPRINT R, R, R, R, UR, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0, R0, UR0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots); READ UR (2 slots)

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
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101111..........................................000000.100
........0000...00111000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v72"></a>
## 72. `FOOTPRINT_R_R_R_R_UR_I_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, R, R, UR, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0, R0, UR0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| operand 6 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101111..........................................000000.0..
........0000...00111000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v73"></a>
## 73. `FOOTPRINT_R_R_R_SNOWFLAKE_I_D`

Syntax: `FOOTPRINT R, R, R, SNOWFLAKE, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0,     ???63, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 46-53 |
| SCR | 60 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101111....................11111111111111........000000.100
........0000...00111000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v74"></a>
## 74. `FOOTPRINT_R_R_R_SNOWFLAKE_I_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0,     ???63, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 46-53 |
| SCR | 60 |
| operand 5 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101111....................11111111111111........000000.1..
........0000...00111000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v75"></a>
## 75. `FOOTPRINT_R_R_R_UR_I_D`

Syntax: `FOOTPRINT R, R, R, UR, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0, UR0, 0x0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| SCR | 60 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101111....................11111111..............000000.100
........0000...00111000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v76"></a>
## 76. `FOOTPRINT_R_R_R_UR_I_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, R, UR, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX R0, R0, R0, UR0, 0x0, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| SCR | 60 |
| operand 5 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101111....................11111111..............000000.1..
........0000...00111000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v77"></a>
## 77. `FOOTPRINT_SNOWFLAKE_R_R_R_UR_I_D`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, R, UR, INT_IMM, D`  
Example: `@P0 FOOTPRINT.TEX     ???255, R0, R0, R0, UR0, 0x0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101111..........................................000000.100
111111110000...00111000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v78"></a>
## 78. `FOOTPRINT_SNOWFLAKE_R_R_R_UR_I_SNOWFLAKE`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, R, UR, INT_IMM, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.TEX     ???255, R0, R0, R0, UR0, 0x0, INVALID0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| SCR | 60 |
| operand 6 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
001011101111..........................................000000.0..
111111110000...00111000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v79"></a>
## 79. `FOOTPRINT_P_R_R_R_R_D`

Syntax: `FOOTPRINT P, R, R, R, R, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0, R0, R0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100............................0000000000000000000..100
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v80"></a>
## 80. `FOOTPRINT_P_R_R_R_R_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, R, R, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0, R0, R0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100............................0000000000000000000..0..
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v81"></a>
## 81. `FOOTPRINT_P_R_R_R_SNOWFLAKE_D`

Syntax: `FOOTPRINT P, R, R, R, SNOWFLAKE, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0, R0,     ???255, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100....................111111110000000000000000000..100
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v82"></a>
## 82. `FOOTPRINT_P_R_R_R_SNOWFLAKE_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, R, SNOWFLAKE, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0, R0,     ???255, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100....................111111110000000000000000000..1..
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v83"></a>
## 83. `FOOTPRINT_P_R_R_SNOWFLAKE_R_D`

Syntax: `FOOTPRINT P, R, R, SNOWFLAKE, R, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0,     ???255, R0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100............11111111........0000000000000000000..100
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v84"></a>
## 84. `FOOTPRINT_P_R_R_SNOWFLAKE_R_SNOWFLAKE`

Syntax: `FOOTPRINT P, R, R, SNOWFLAKE, R, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0, R0, R0,     ???255, R0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 62-63 |
| operand 1 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100............11111111........0000000000000000000..0..
........0000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v85"></a>
## 85. `FOOTPRINT_P_SNOWFLAKE_R_R_R_D`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, R, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, R0, R0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100............................0000000000000000000..100
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v86"></a>
## 86. `FOOTPRINT_P_SNOWFLAKE_R_R_R_SNOWFLAKE`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, R, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, R0, R0, INVALID3 ;`

Register access: WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100............................0000000000000000000..1..
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v87"></a>
## 87. `FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_D`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, SNOWFLAKE, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, R0, ???255, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100....................111111110000000000000000000..100
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v88"></a>
## 88. `FOOTPRINT_P_SNOWFLAKE_R_R_SNOWFLAKE_SNOWFLAKE`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, R, SNOWFLAKE, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, R0, ???255, INVALID3 ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 3 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100....................111111110000000000000000000..1..
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v89"></a>
## 89. `FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_D`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, SNOWFLAKE, R, D`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, ???255, R0, 2D ;`

Register access: WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100............11111111........0000000000000000000..100
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v90"></a>
## 90. `FOOTPRINT_P_SNOWFLAKE_R_SNOWFLAKE_R_SNOWFLAKE`

Syntax: `FOOTPRINT P, SNOWFLAKE, R, SNOWFLAKE, R, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX P0,     ???255, R0, ???255, R0, INVALID0 ;`

Register access: WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 16-23 |
| operand 4 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 5 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| operand 0 | 80-83 |
| modi 3 | 87-88 |
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
110011101100............11111111........0000000000000000000..0..
111111110000...0....000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v91"></a>
## 91. `FOOTPRINT_R_R_R_R_D`

Syntax: `FOOTPRINT R, R, R, R, D`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0, R0, R0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100............................0000000000000000000..100
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v92"></a>
## 92. `FOOTPRINT_R_R_R_R_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, R, R, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0, R0, R0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100............................0000000000000000000..0..
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v93"></a>
## 93. `FOOTPRINT_R_R_R_SNOWFLAKE_D`

Syntax: `FOOTPRINT R, R, R, SNOWFLAKE, D`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0, R0,     ???255, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100....................111111110000000000000000000..100
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v94"></a>
## 94. `FOOTPRINT_R_R_R_SNOWFLAKE_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, R, SNOWFLAKE, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0, R0,     ???255, INVALID3 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100....................111111110000000000000000000..1..
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v95"></a>
## 95. `FOOTPRINT_R_R_SNOWFLAKE_R_D`

Syntax: `FOOTPRINT R, R, SNOWFLAKE, R, D`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0,     ???255, R0, 2D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100............11111111........0000000000000000000..100
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v96"></a>
## 96. `FOOTPRINT_R_R_SNOWFLAKE_R_SNOWFLAKE`

Syntax: `FOOTPRINT R, R, SNOWFLAKE, R, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX R0, R0,     ???255, R0, INVALID0 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 62-63 |
| operand 0 | 64-71 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100............11111111........0000000000000000000..0..
........0000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v97"></a>
## 97. `FOOTPRINT_SNOWFLAKE_R_R_R_D`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, R, D`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, R0, R0, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100............................0000000000000000000..100
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v98"></a>
## 98. `FOOTPRINT_SNOWFLAKE_R_R_R_SNOWFLAKE`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, R, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, R0, R0, INVALID0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100............................0000000000000000000..0..
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v99"></a>
## 99. `FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_D`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, SNOWFLAKE, D`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, R0, ???255, 2D ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100....................111111110000000000000000000..100
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v100"></a>
## 100. `FOOTPRINT_SNOWFLAKE_R_R_SNOWFLAKE_SNOWFLAKE`

Syntax: `FOOTPRINT SNOWFLAKE, R, R, SNOWFLAKE, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, R0, ???255, INVALID3 ;`

Register access: WRITE R (2 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100....................111111110000000000000000000..1..
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v101"></a>
## 101. `FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_D`

Syntax: `FOOTPRINT SNOWFLAKE, R, SNOWFLAKE, R, D`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, ???255, R0, 2D ;`

Register access: WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100............11111111........0000000000000000000..100
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

<a id="v102"></a>
## 102. `FOOTPRINT_SNOWFLAKE_R_SNOWFLAKE_R_SNOWFLAKE`

Syntax: `FOOTPRINT SNOWFLAKE, R, SNOWFLAKE, R, SNOWFLAKE`  
Example: `@P0 FOOTPRINT.???0.TEX     ???255, R0, ???255, R0, INVALID0 ;`

Register access: WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| SCR | 60 |
| operand 4 | 62-63 |
| COARSE | 76 |
| NDV | 77 |
| modi 2 | 78 |
| modi 3 | 87-88 |
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
110011101100............11111111........0000000000000000000..0..
111111110000...00111000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `TEX.` |
| `1` | `TXD.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LZ.` |
| `10` | `LB.` |
| `11` | `LL.` |

