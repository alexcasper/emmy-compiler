# TMML (SM89 SASS)

**NVIDIA:** Texture MipMap Level (Texture Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Texture mip-map level query (category: Texture / surface)

Typically emitted for: texture LOD query (`__nv_tex_lod`-style); not reproduced

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x36a, 0xb69 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3092)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/TMML.html> (machine-derived by fuzzing the assembler; no semantics).

69 encoding variant(s):

- [TMML_R_R_R_I_I_ARRAY_D](#v1)
- [TMML_R_R_R_I_I_ARRAY_D_I](#v2)
- [TMML_R_R_R_I_I_D](#v3)
- [TMML_R_R_R_I_I_D_I](#v4)
- [TMML_R_R_R_I_I_SNOWFLAKE](#v5)
- [TMML_R_R_R_I_I_SNOWFLAKE_I](#v6)
- [TMML_R_R_R_R_I_I_ARRAY_D](#v7)
- [TMML_R_R_R_R_I_I_ARRAY_D_I](#v8)
- [TMML_R_R_R_R_I_I_D](#v9)
- [TMML_R_R_R_R_I_I_D_I](#v10)
- [TMML_R_R_R_R_I_I_SNOWFLAKE](#v11)
- [TMML_R_R_R_R_I_I_SNOWFLAKE_I](#v12)
- [TMML_R_R_R_SNOWFLAKE_I_I_ARRAY_D](#v13)
- [TMML_R_R_R_SNOWFLAKE_I_I_ARRAY_D_I](#v14)
- [TMML_R_R_R_SNOWFLAKE_I_I_D](#v15)
- [TMML_R_R_R_SNOWFLAKE_I_I_D_I](#v16)
- [TMML_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE](#v17)
- [TMML_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE_I](#v18)
- [TMML_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I](#v19)
- [TMML_R_R_SNOWFLAKE_R_I_I_D_I](#v20)
- [TMML_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I](#v21)
- [TMML_R_R_R_R_I_I_I_ARRAY_D](#v22)
- [TMML_R_R_R_R_I_I_I_ARRAY_D_I](#v23)
- [TMML_R_R_R_R_I_I_I_D](#v24)
- [TMML_R_R_R_R_I_I_I_D_I](#v25)
- [TMML_R_R_R_R_I_I_I_SNOWFLAKE](#v26)
- [TMML_R_R_R_R_I_I_I_SNOWFLAKE_I](#v27)
- [TMML_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D](#v28)
- [TMML_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D_I](#v29)
- [TMML_R_R_R_SNOWFLAKE_I_I_I_D](#v30)
- [TMML_R_R_R_SNOWFLAKE_I_I_I_D_I](#v31)
- [TMML_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE](#v32)
- [TMML_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE_I](#v33)
- [TMML_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I](#v34)
- [TMML_R_R_SNOWFLAKE_R_I_I_I_D_I](#v35)
- [TMML_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I](#v36)
- [TMML_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v37)
- [TMML_R_R_R_R_SNOWFLAKE_I_D_I](#v38)
- [TMML_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v39)
- [TMML_R_R_R_R_UR_I_ARRAY_D](#v40)
- [TMML_R_R_R_R_UR_I_ARRAY_D_I](#v41)
- [TMML_R_R_R_R_UR_I_D](#v42)
- [TMML_R_R_R_R_UR_I_D_I](#v43)
- [TMML_R_R_R_R_UR_I_SNOWFLAKE](#v44)
- [TMML_R_R_R_R_UR_I_SNOWFLAKE_I](#v45)
- [TMML_R_R_R_SNOWFLAKE_I_ARRAY_D_I](#v46)
- [TMML_R_R_R_SNOWFLAKE_I_D_I](#v47)
- [TMML_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I](#v48)
- [TMML_R_R_R_UR_I_ARRAY_D_I](#v49)
- [TMML_R_R_R_UR_I_D_I](#v50)
- [TMML_R_R_R_UR_I_SNOWFLAKE_I](#v51)
- [TMML_R_R_SNOWFLAKE_R_UR_I_ARRAY_D_I](#v52)
- [TMML_R_R_SNOWFLAKE_R_UR_I_D_I](#v53)
- [TMML_R_R_SNOWFLAKE_R_UR_I_SNOWFLAKE_I](#v54)
- [TMML_R_R_R_R_ARRAY_D](#v55)
- [TMML_R_R_R_R_ARRAY_D_I](#v56)
- [TMML_R_R_R_R_D](#v57)
- [TMML_R_R_R_R_D_I](#v58)
- [TMML_R_R_R_R_SNOWFLAKE](#v59)
- [TMML_R_R_R_R_SNOWFLAKE_I](#v60)
- [TMML_R_R_R_SNOWFLAKE_ARRAY_D](#v61)
- [TMML_R_R_R_SNOWFLAKE_ARRAY_D_I](#v62)
- [TMML_R_R_R_SNOWFLAKE_D](#v63)
- [TMML_R_R_R_SNOWFLAKE_D_I](#v64)
- [TMML_R_R_R_SNOWFLAKE_SNOWFLAKE](#v65)
- [TMML_R_R_R_SNOWFLAKE_SNOWFLAKE_I](#v66)
- [TMML_R_R_SNOWFLAKE_R_ARRAY_D_I](#v67)
- [TMML_R_R_SNOWFLAKE_R_D_I](#v68)
- [TMML_R_R_SNOWFLAKE_R_SNOWFLAKE_I](#v69)

<a id="v1"></a>
## 1. `TMML_R_R_R_I_I_ARRAY_D`

Syntax: `TMML.LOD R, R, R, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TMML.LOD R0, R0, R0, 0x0, 0x0, ARRAY_1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 60-61 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................0..01
........11110.000000000000.00000000000000.....................00
```

<a id="v2"></a>
## 2. `TMML_R_R_R_I_I_ARRAY_D_I`

Syntax: `TMML.LOD R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 60-61 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................0..01
..............000000000000.00000000000000.....................00
```

<a id="v3"></a>
## 3. `TMML_R_R_R_I_I_D`

Syntax: `TMML.LOD R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 TMML.LOD R0, R0, R0, 0x0, 0x0, 1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 60-62 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................0...0
........11110.000000000000.00000000000000.....................00
```

<a id="v4"></a>
## 4. `TMML_R_R_R_I_I_D_I`

Syntax: `TMML.LOD R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 60-62 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................0...0
..............000000000000.00000000000000.....................00
```

<a id="v5"></a>
## 5. `TMML_R_R_R_I_I_SNOWFLAKE`

Syntax: `TMML.LOD R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TMML.LOD R0, R0, R0, 0x0, 0x0, INVALID6 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................00011
........11110.000000000000.00000000000000.....................00
```

<a id="v6"></a>
## 6. `TMML_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, 0x0, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................00110
..............000000000000.00000000000000.....................00
```

<a id="v7"></a>
## 7. `TMML_R_R_R_R_I_I_ARRAY_D`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, 0x0, 0x0, ARRAY_1D ;`

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
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101..................................................01
........11110.000000000000.00000000000000.....................00
```

<a id="v8"></a>
## 8. `TMML_R_R_R_R_I_I_ARRAY_D_I`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101..................................................01
..............000000000000.00000000000000.....................00
```

<a id="v9"></a>
## 9. `TMML_R_R_R_R_I_I_D`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, D`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, 0x0, 0x0, 1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| operand 6 | 60-62 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101...................................................0
........11110.000000000000.00000000000000.....................00
```

<a id="v10"></a>
## 10. `TMML_R_R_R_R_I_I_D_I`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, 0x0, 0x0, 1D, 0x0 ;`

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
| operand 6 | 60-62 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101...................................................0
..............000000000000.00000000000000.....................00
```

<a id="v11"></a>
## 11. `TMML_R_R_R_R_I_I_SNOWFLAKE`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, 0x0, 0x0, CUBE ;`

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
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101................................................0110
........11110.000000000000.00000000000000.....................00
```

<a id="v12"></a>
## 12. `TMML_R_R_R_R_I_I_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, 0x0, 0x0, INVALID6, 0x0 ;`

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
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101................................................0011
..............000000000000.00000000000000.....................00
```

<a id="v13"></a>
## 13. `TMML_R_R_R_SNOWFLAKE_I_I_ARRAY_D`

Syntax: `TMML.LOD.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TMML.B.LOD R0, R0, R0,     ???255, 0x0, 0x0, ARRAY_1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................1..01
........11110.000000000000.00000000000000.....................00
```

<a id="v14"></a>
## 14. `TMML_R_R_R_SNOWFLAKE_I_I_ARRAY_D_I`

Syntax: `TMML.LOD.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.B.LOD R0, R0, R0,     ???255, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................1..01
..............000000000000.00000000000000.....................00
```

<a id="v15"></a>
## 15. `TMML_R_R_R_SNOWFLAKE_I_I_D`

Syntax: `TMML.LOD.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D`  
Example: `@P0 TMML.B.LOD R0, R0, R0,     ???255, 0x0, 0x0, 1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 6 | 60-62 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................1...0
........11110.000000000000.00000000000000.....................00
```

<a id="v16"></a>
## 16. `TMML_R_R_R_SNOWFLAKE_I_I_D_I`

Syntax: `TMML.LOD.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.B.LOD R0, R0, R0,     ???255, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 6 | 60-62 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................1...0
..............000000000000.00000000000000.....................00
```

<a id="v17"></a>
## 17. `TMML_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE`

Syntax: `TMML.LOD.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TMML.B.LOD R0, R0, R0,     ???255, 0x0, 0x0, INVALID6 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................10011
........11110.000000000000.00000000000000.....................00
```

<a id="v18"></a>
## 18. `TMML_R_R_R_SNOWFLAKE_I_I_SNOWFLAKE_I`

Syntax: `TMML.LOD.B R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.B.LOD R0, R0, R0,     ???255, 0x0, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101....................11111111...................10110
..............000000000000.00000000000000.....................00
```

<a id="v19"></a>
## 19. `TMML_R_R_SNOWFLAKE_R_I_I_ARRAY_D_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0,     ???255, R0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

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
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101............11111111..............................01
..............000000000000.00000000000000.....................00
```

<a id="v20"></a>
## 20. `TMML_R_R_SNOWFLAKE_R_I_I_D_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0,     ???255, R0, 0x0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| operand 6 | 60-62 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101............11111111...............................0
..............000000000000.00000000000000.....................00
```

<a id="v21"></a>
## 21. `TMML_R_R_SNOWFLAKE_R_I_I_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0,     ???255, R0, 0x0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101101............11111111............................0011
..............000000000000.00000000000000.....................00
```

<a id="v22"></a>
## 22. `TMML_R_R_R_R_I_I_I_ARRAY_D`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, 0x0, 0x0, 0x0, ARRAY_1D ;`

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
| operand 7 | 60-61 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101..................................................01
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v23"></a>
## 23. `TMML_R_R_R_R_I_I_I_ARRAY_D_I`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| operand 7 | 60-61 |
| operand 0 | 64-71 |
| operand 8 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101..................................................01
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v24"></a>
## 24. `TMML_R_R_R_R_I_I_I_D`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, 0x0, 0x0, 0x0, 1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (1 slots)

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
| operand 7 | 60-62 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101...................................................0
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v25"></a>
## 25. `TMML_R_R_R_R_I_I_I_D_I`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

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
| operand 7 | 60-62 |
| operand 0 | 64-71 |
| operand 8 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101...................................................0
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v26"></a>
## 26. `TMML_R_R_R_R_I_I_I_SNOWFLAKE`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, 0x0, 0x0, 0x0, CUBE ;`

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
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101................................................0110
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v27"></a>
## 27. `TMML_R_R_R_R_I_I_I_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, R, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, 0x0, 0x0, 0x0, INVALID6, 0x0 ;`

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
| operand 0 | 64-71 |
| operand 8 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101................................................0011
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v28"></a>
## 28. `TMML_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, ARRAY_D`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, 0x0, 0x0, 0x0, ARRAY_1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| operand 7 | 60-61 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101....................11111111......................01
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v29"></a>
## 29. `TMML_R_R_R_SNOWFLAKE_I_I_I_ARRAY_D_I`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| operand 7 | 60-61 |
| operand 0 | 64-71 |
| operand 8 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101....................11111111......................01
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v30"></a>
## 30. `TMML_R_R_R_SNOWFLAKE_I_I_I_D`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, 0x0, 0x0, 0x0, 1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| operand 7 | 60-62 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101....................11111111.......................0
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v31"></a>
## 31. `TMML_R_R_R_SNOWFLAKE_I_I_I_D_I`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, 0x0, 0x0, 0x0, 1D, 0x0 ;`

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
| operand 7 | 60-62 |
| operand 0 | 64-71 |
| operand 8 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101....................11111111.......................0
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v32"></a>
## 32. `TMML_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, 0x0, 0x0, 0x0, INVALID6 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101....................11111111....................0011
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v33"></a>
## 33. `TMML_R_R_R_SNOWFLAKE_I_I_I_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, 0x0, 0x0, 0x0, CUBE, 0x0 ;`

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
| operand 0 | 64-71 |
| operand 8 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101....................11111111....................0110
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v34"></a>
## 34. `TMML_R_R_SNOWFLAKE_R_I_I_I_ARRAY_D_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0,     ???255, R0, 0x0, 0x0, 0x0, ARRAY_1D, 0x0 ;`

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
| operand 7 | 60-61 |
| operand 0 | 64-71 |
| operand 8 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101............11111111..............................01
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v35"></a>
## 35. `TMML_R_R_SNOWFLAKE_R_I_I_I_D_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0,     ???255, R0, 0x0, 0x0, 0x0, 1D, 0x0 ;`

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
| operand 7 | 60-62 |
| operand 0 | 64-71 |
| operand 8 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101............11111111...............................0
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v36"></a>
## 36. `TMML_R_R_SNOWFLAKE_R_I_I_I_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, INT_IMM, INT_IMM, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0,     ???255, R0, 0x0, 0x0, 0x0, INVALID6, 0x0 ;`

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
| operand 0 | 64-71 |
| operand 8 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101101101............11111111............................0011
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v37"></a>
## 37. `TMML_R_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TMML.LOD R, R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111............................111111........000000..01
..............000000000000.10000000000000.....................00
```

<a id="v38"></a>
## 38. `TMML_R_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TMML.LOD R, R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| operand 6 | 60-62 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111............................111111........000000...0
..............000000000000.10000000000000.....................00
```

<a id="v39"></a>
## 39. `TMML_R_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, R0,     ???63, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 46-53 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111............................111111........0000000110
..............000000000000.10000000000000.....................00
```

<a id="v40"></a>
## 40. `TMML_R_R_R_R_UR_I_ARRAY_D`

Syntax: `TMML.LOD R, R, R, R, UR, INT_IMM, ARRAY_D`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, UR0, 0x0, ARRAY_1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots); READ UR (2 slots)

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
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111..........................................000000..01
........11110.000000000000.10000000000000.....................00
```

<a id="v41"></a>
## 41. `TMML_R_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TMML.LOD R, R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots); READ UR (2 slots)

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
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111..........................................000000..01
..............000000000000.10000000000000.....................00
```

<a id="v42"></a>
## 42. `TMML_R_R_R_R_UR_I_D`

Syntax: `TMML.LOD R, R, R, R, UR, INT_IMM, D`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, UR0, 0x0, 1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 6 | 60-62 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111..........................................000000...0
........11110.000000000000.10000000000000.....................00
```

<a id="v43"></a>
## 43. `TMML_R_R_R_R_UR_I_D_I`

Syntax: `TMML.LOD R, R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 6 | 60-62 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111..........................................000000...0
..............000000000000.10000000000000.....................00
```

<a id="v44"></a>
## 44. `TMML_R_R_R_R_UR_I_SNOWFLAKE`

Syntax: `TMML.LOD R, R, R, R, UR, INT_IMM, SNOWFLAKE`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, UR0, 0x0, INVALID6 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111..........................................0000000011
........11110.000000000000.10000000000000.....................00
```

<a id="v45"></a>
## 45. `TMML_R_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, R0, UR0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111..........................................0000000011
..............000000000000.10000000000000.....................00
```

<a id="v46"></a>
## 46. `TMML_R_R_R_SNOWFLAKE_I_ARRAY_D_I`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0,     ???63, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 46-53 |
| operand 5 | 60-61 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111....................11111111111111........000000..01
..............000000000000.10000000000000.....................00
```

<a id="v47"></a>
## 47. `TMML_R_R_R_SNOWFLAKE_I_D_I`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0,     ???63, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 46-53 |
| operand 5 | 60-62 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111....................11111111111111........000000...0
..............000000000000.10000000000000.....................00
```

<a id="v48"></a>
## 48. `TMML_R_R_R_SNOWFLAKE_I_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0,     ???63, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 46-53 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111....................11111111111111........0000000110
..............000000000000.10000000000000.....................00
```

<a id="v49"></a>
## 49. `TMML_R_R_R_UR_I_ARRAY_D_I`

Syntax: `TMML.LOD R, R, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| operand 5 | 60-61 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111....................11111111..............000000..01
..............000000000000.10000000000000.....................00
```

<a id="v50"></a>
## 50. `TMML_R_R_R_UR_I_D_I`

Syntax: `TMML.LOD R, R, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, UR0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| operand 5 | 60-62 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111....................11111111..............000000...0
..............000000000000.10000000000000.....................00
```

<a id="v51"></a>
## 51. `TMML_R_R_R_UR_I_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0, R0, UR0, 0x0, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111....................11111111..............0000000110
..............000000000000.10000000000000.....................00
```

<a id="v52"></a>
## 52. `TMML_R_R_SNOWFLAKE_R_UR_I_ARRAY_D_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, UR, INT_IMM, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0,     ???255, R0, UR0, 0x0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 6 | 60-61 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111............11111111......................000000..01
..............000000000000.10000000000000.....................00
```

<a id="v53"></a>
## 53. `TMML_R_R_SNOWFLAKE_R_UR_I_D_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, UR, INT_IMM, D, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0,     ???255, R0, UR0, 0x0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 6 | 60-62 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111............11111111......................000000...0
..............000000000000.10000000000000.....................00
```

<a id="v54"></a>
## 54. `TMML_R_R_SNOWFLAKE_R_UR_I_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, UR, INT_IMM, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.LOD R0, R0,     ???255, R0, UR0, 0x0, INVALID6, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101101111............11111111......................0000000011
..............000000000000.10000000000000.....................00
```

<a id="v55"></a>
## 55. `TMML_R_R_R_R_ARRAY_D`

Syntax: `TMML.LOD R, R, R, R, ARRAY_D`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, ARRAY_1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-61 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100............................0000000000000000000...01
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v56"></a>
## 56. `TMML_R_R_R_R_ARRAY_D_I`

Syntax: `TMML.LOD R, R, R, R, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-61 |
| operand 0 | 64-71 |
| operand 5 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100............................0000000000000000000...01
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v57"></a>
## 57. `TMML_R_R_R_R_D`

Syntax: `TMML.LOD R, R, R, R, D`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, 1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-62 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100............................0000000000000000000....0
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v58"></a>
## 58. `TMML_R_R_R_R_D_I`

Syntax: `TMML.LOD R, R, R, R, D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-62 |
| operand 0 | 64-71 |
| operand 5 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100............................0000000000000000000....0
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v59"></a>
## 59. `TMML_R_R_R_R_SNOWFLAKE`

Syntax: `TMML.LOD R, R, R, R, SNOWFLAKE`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, CUBE ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (3 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100............................0000000000000000000.0110
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v60"></a>
## 60. `TMML_R_R_R_R_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, R, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0, R0, INVALID6, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 0 | 64-71 |
| operand 5 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100............................0000000000000000000.0011
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v61"></a>
## 61. `TMML_R_R_R_SNOWFLAKE_ARRAY_D`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, ARRAY_D`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, ARRAY_1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| operand 4 | 60-61 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100....................111111110000000000000000000...01
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v62"></a>
## 62. `TMML_R_R_R_SNOWFLAKE_ARRAY_D_I`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| operand 4 | 60-61 |
| operand 0 | 64-71 |
| operand 5 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100....................111111110000000000000000000...01
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v63"></a>
## 63. `TMML_R_R_R_SNOWFLAKE_D`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, D`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, 1D ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| operand 4 | 60-62 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100....................111111110000000000000000000....0
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v64"></a>
## 64. `TMML_R_R_R_SNOWFLAKE_D_I`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| operand 4 | 60-62 |
| operand 0 | 64-71 |
| operand 5 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100....................111111110000000000000000000....0
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v65"></a>
## 65. `TMML_R_R_R_SNOWFLAKE_SNOWFLAKE`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, SNOWFLAKE`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, INVALID6 ;`

Register access: WRITE R (2 slots); WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| operand 0 | 64-71 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100....................111111110000000000000000000.0011
........11110.000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v66"></a>
## 66. `TMML_R_R_R_SNOWFLAKE_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, R, SNOWFLAKE, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0, R0,     ???255, CUBE, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (3 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| operand 0 | 64-71 |
| operand 5 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100....................111111110000000000000000000.0110
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v67"></a>
## 67. `TMML_R_R_SNOWFLAKE_R_ARRAY_D_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, ARRAY_D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0,     ???255, R0, ARRAY_1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-61 |
| operand 0 | 64-71 |
| operand 5 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100............11111111........0000000000000000000...01
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v68"></a>
## 68. `TMML_R_R_SNOWFLAKE_R_D_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, D, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0,     ???255, R0, 1D, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 4 | 60-62 |
| operand 0 | 64-71 |
| operand 5 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100............11111111........0000000000000000000....0
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v69"></a>
## 69. `TMML_R_R_SNOWFLAKE_R_SNOWFLAKE_I`

Syntax: `TMML.LOD R, R, SNOWFLAKE, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TMML.???0.LOD R0, R0,     ???255, R0, INVALID6, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| modi 1 | 59 |
| operand 0 | 64-71 |
| operand 5 | 72-76 |
| NDV | 77 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101101100............11111111........0000000000000000000.0011
..............000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

