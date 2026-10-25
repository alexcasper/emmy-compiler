# SUQUERY (SM89 SASS)

**NVIDIA:** not listed in the official Ampere/Ada opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)).

Notes: Surface query (category: Texture / surface)

Typically emitted for: unclear: PTX `suq.width` lowers to TXQ on sm_89 (probe `suq`)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/SUQUERY.html> (machine-derived by fuzzing the assembler; no semantics).

10 encoding variant(s):

- [SUQUERY_P_R_R_SNOWFLAKE_I_I_I](#v1)
- [SUQUERY_R_R_SNOWFLAKE_I_I_I](#v2)
- [SUQUERY_P_R_R_SNOWFLAKE_R](#v3)
- [SUQUERY_P_R_R_SNOWFLAKE_SNOWFLAKE](#v4)
- [SUQUERY_R_R_SNOWFLAKE_R](#v5)
- [SUQUERY_R_R_SNOWFLAKE_SNOWFLAKE](#v6)
- [SUQUERY_P_R_R_SNOWFLAKE_I_I](#v7)
- [SUQUERY_R_R_SNOWFLAKE_I_I](#v8)
- [SUQUERY_P_R_R_SNOWFLAKE_UR_I](#v9)
- [SUQUERY_R_R_SNOWFLAKE_UR_I](#v10)

<a id="v1"></a>
## 1. `SUQUERY_P_R_R_SNOWFLAKE_I_I_I`

Syntax: `SUQUERY P, R, [R], SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 SUQUERY.1D P0, R0, [R0], COMP_STATUS, 0x0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 61-63 |
| BA | 72 |
| operand 0 | 80-83 |
| operand 3 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110011011110....................00000000...................00...
00000000.0000000....00..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v2"></a>
## 2. `SUQUERY_R_R_SNOWFLAKE_I_I_I`

Syntax: `SUQUERY R, [R], SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 SUQUERY.1D R0, [R0], COMP_STATUS, 0x0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-52 |
| operand 3 | 53-58 |
| modi 1 | 61-63 |
| BA | 72 |
| operand 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110011011110....................00000000...................00...
00000000.0000000011100..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v3"></a>
## 3. `SUQUERY_P_R_R_SNOWFLAKE_R`

Syntax: `SUQUERY P, R, [R], SNOWFLAKE, R`  
Example: `@P0 SUQUERY.1D P0, R0, [R0], COMP_STATUS, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 61-63 |
| operand 4 | 64-71 |
| BA | 72 |
| operand 0 | 80-83 |
| operand 3 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110011011001....................00000000000000000000000000000...
.........0000000....00..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v4"></a>
## 4. `SUQUERY_P_R_R_SNOWFLAKE_SNOWFLAKE`

Syntax: `SUQUERY P, R, [R], SNOWFLAKE, SNOWFLAKE`  
Example: `@P0 SUQUERY.1D P0, R0, [R0], COMP_STATUS,     ???255 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 61-63 |
| BA | 72 |
| operand 0 | 80-83 |
| operand 3 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110011011001....................00000000000000000000000000000...
11111111.0000000....00..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v5"></a>
## 5. `SUQUERY_R_R_SNOWFLAKE_R`

Syntax: `SUQUERY R, [R], SNOWFLAKE, R`  
Example: `@P0 SUQUERY.1D R0, [R0], COMP_STATUS, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 61-63 |
| operand 3 | 64-71 |
| BA | 72 |
| operand 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110011011001....................00000000000000000000000000000...
.........0000000011100..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v6"></a>
## 6. `SUQUERY_R_R_SNOWFLAKE_SNOWFLAKE`

Syntax: `SUQUERY R, [R], SNOWFLAKE, SNOWFLAKE`  
Example: `@P0 SUQUERY.1D R0, [R0], COMP_STATUS,     ???255 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 61-63 |
| BA | 72 |
| operand 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110011011001....................00000000000000000000000000000...
11111111.0000000011100..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v7"></a>
## 7. `SUQUERY_P_R_R_SNOWFLAKE_I_I`

Syntax: `SUQUERY P, R, [R], SNOWFLAKE, INT_IMM, INT_IMM`  
Example: `@P0 SUQUERY.1D P0, R0, [R0], COMP_STATUS, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| modi 1 | 61-63 |
| BA | 72 |
| operand 0 | 80-83 |
| operand 3 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110011011101....................00000000...................00...
00000000.0000000....00..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v8"></a>
## 8. `SUQUERY_R_R_SNOWFLAKE_I_I`

Syntax: `SUQUERY R, [R], SNOWFLAKE, INT_IMM, INT_IMM`  
Example: `@P0 SUQUERY.1D R0, [R0], COMP_STATUS, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| modi 1 | 61-63 |
| BA | 72 |
| operand 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110011011101....................00000000...................00...
00000000.0000000011100..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v9"></a>
## 9. `SUQUERY_P_R_R_SNOWFLAKE_UR_I`

Syntax: `SUQUERY P, R, [R], SNOWFLAKE, UR, INT_IMM`  
Example: `@P0 SUQUERY.1D P0, R0, [R0], COMP_STATUS, UR0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| modi 1 | 61-63 |
| BA | 72 |
| operand 0 | 80-83 |
| operand 3 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110011011111....................00000000..............0000000...
00000000.0000000....00..00010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v10"></a>
## 10. `SUQUERY_R_R_SNOWFLAKE_UR_I`

Syntax: `SUQUERY R, [R], SNOWFLAKE, UR, INT_IMM`  
Example: `@P0 SUQUERY.1D R0, [R0], COMP_STATUS, UR0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| modi 1 | 61-63 |
| BA | 72 |
| operand 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110011011111....................00000000..............0000000...
00000000.0000000011100..00010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

