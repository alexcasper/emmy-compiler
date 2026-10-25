# TXQ (SM89 SASS)

**NVIDIA:** Texture Query (Texture Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Texture query (category: Texture / surface)

Typically emitted for: `txq` (texture dims)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x370, 0xb6f ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3198)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [txq](../verify/RESULTS.md#txq): `txq.width.b32`
- [suq](../verify/RESULTS.md#suq): `suq.width.b32 (lowers to TXQ, not SUQUERY)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/TXQ.html> (machine-derived by fuzzing the assembler; no semantics).

14 encoding variant(s):

- [TXQ_R_R_R_SNOWFLAKE_I_I_I](#v1)
- [TXQ_R_R_R_TEX_I_I_I](#v2)
- [TXQ_R_R_R_SNOWFLAKE_I_I_I_I](#v3)
- [TXQ_R_R_R_TEX_I_I_I_I](#v4)
- [TXQ_R_R_SNOWFLAKE_SNOWFLAKE_I_I_I_I](#v5)
- [TXQ_R_R_SNOWFLAKE_TEX_I_I_I_I](#v6)
- [TXQ_R_R_R_SNOWFLAKE_SNOWFLAKE_I_I](#v7)
- [TXQ_R_R_R_SNOWFLAKE_UR_I_I](#v8)
- [TXQ_R_R_R_TEX_SNOWFLAKE_I_I](#v9)
- [TXQ_R_R_R_TEX_UR_I_I](#v10)
- [TXQ_R_R_R_SNOWFLAKE_I](#v11)
- [TXQ_R_R_R_TEX_I](#v12)
- [TXQ_R_R_SNOWFLAKE_SNOWFLAKE_I](#v13)
- [TXQ_R_R_SNOWFLAKE_TEX_I](#v14)

<a id="v1"></a>
## 1. `TXQ_R_R_R_SNOWFLAKE_I_I_I`

Syntax: `TXQ R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 TXQ R0, R0, R0, INVALID3, 0x0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111101101101....................00000000....................0011
.............0000000000000.00000000000000.....................00
```

<a id="v2"></a>
## 2. `TXQ_R_R_R_TEX_I_I_I`

Syntax: `TXQ R, R, R, TEX, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 TXQ R0, R0, R0, TEX_HEADER_DIMENSION, 0x0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| B | 59 |
| operand 3 | 61-63 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111101101101....................00000000....................0...
.............0000000000000.00000000000000.....................00
```

<a id="v3"></a>
## 3. `TXQ_R_R_R_SNOWFLAKE_I_I_I_I`

Syntax: `TXQ R, R, R, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 TXQ.???0 R0, R0, R0, INVALID3, 0x0, 0x0, 0x0, 0x0 ;`

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
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011101101....................00000000....................0011
.............0000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v4"></a>
## 4. `TXQ_R_R_R_TEX_I_I_I_I`

Syntax: `TXQ R, R, R, TEX, INT_IMM, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 TXQ.???0 R0, R0, R0, TEX_HEADER_DIMENSION, 0x0, 0x0, 0x0, 0x0 ;`

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
| operand 3 | 61-63 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011101101....................00000000....................0...
.............0000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v5"></a>
## 5. `TXQ_R_R_SNOWFLAKE_SNOWFLAKE_I_I_I_I`

Syntax: `TXQ R, R, SNOWFLAKE, SNOWFLAKE, INT_IMM, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 TXQ.???0 R0, R0,     ???255, INVALID3, 0x0, 0x0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011101101............1111111100000000....................0011
.............0000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v6"></a>
## 6. `TXQ_R_R_SNOWFLAKE_TEX_I_I_I_I`

Syntax: `TXQ R, R, SNOWFLAKE, TEX, INT_IMM, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 TXQ.???0 R0, R0,     ???255, TEX_HEADER_DIMENSION, 0x0, 0x0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59 |
| operand 3 | 61-63 |
| operand 0 | 64-71 |
| operand 7 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011101101............1111111100000000....................0...
.............0000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v7"></a>
## 7. `TXQ_R_R_R_SNOWFLAKE_SNOWFLAKE_I_I`

Syntax: `TXQ R, R, R, SNOWFLAKE, SNOWFLAKE, INT_IMM, INT_IMM`  
Example: `@P0 TXQ R0, R0, R0, INVALID3,     ???63, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 46-53 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111101101111....................00000000111111........0000000011
.............0000000000000.10000000000000.....................00
```

<a id="v8"></a>
## 8. `TXQ_R_R_R_SNOWFLAKE_UR_I_I`

Syntax: `TXQ R, R, R, SNOWFLAKE, UR, INT_IMM, INT_IMM`  
Example: `@P0 TXQ R0, R0, R0, INVALID3, UR0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111101101111....................00000000..............0000000011
.............0000000000000.10000000000000.....................00
```

<a id="v9"></a>
## 9. `TXQ_R_R_R_TEX_SNOWFLAKE_I_I`

Syntax: `TXQ R, R, R, TEX, SNOWFLAKE, INT_IMM, INT_IMM`  
Example: `@P0 TXQ R0, R0, R0, TEX_HEADER_DIMENSION,     ???63, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 46-53 |
| operand 3 | 61-63 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111101101111....................00000000111111........0000000...
.............0000000000000.10000000000000.....................00
```

<a id="v10"></a>
## 10. `TXQ_R_R_R_TEX_UR_I_I`

Syntax: `TXQ R, R, R, TEX, UR, INT_IMM, INT_IMM`  
Example: `@P0 TXQ R0, R0, R0, TEX_HEADER_DIMENSION, UR0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| operand 3 | 61-63 |
| operand 0 | 64-71 |
| operand 6 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111101101111....................00000000..............0000000...
.............0000000000000.10000000000000.....................00
```

<a id="v11"></a>
## 11. `TXQ_R_R_R_SNOWFLAKE_I`

Syntax: `TXQ R, R, R, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXQ.???0 R0, R0, R0, INVALID3, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| operand 0 | 64-71 |
| operand 4 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000011101100....................000000000000000000000000000.0011
.............0000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v12"></a>
## 12. `TXQ_R_R_R_TEX_I`

Syntax: `TXQ R, R, R, TEX, INT_IMM`  
Example: `@P0 TXQ.???0 R0, R0, R0, TEX_HEADER_DIMENSION, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59 |
| operand 3 | 61-63 |
| operand 0 | 64-71 |
| operand 4 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000011101100....................000000000000000000000000000.0...
.............0000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v13"></a>
## 13. `TXQ_R_R_SNOWFLAKE_SNOWFLAKE_I`

Syntax: `TXQ R, R, SNOWFLAKE, SNOWFLAKE, INT_IMM`  
Example: `@P0 TXQ.???0 R0, R0,     ???255, INVALID3, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| modi 1 | 59 |
| operand 0 | 64-71 |
| operand 4 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000011101100............11111111000000000000000000000000000.0011
.............0000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

<a id="v14"></a>
## 14. `TXQ_R_R_SNOWFLAKE_TEX_I`

Syntax: `TXQ R, R, SNOWFLAKE, TEX, INT_IMM`  
Example: `@P0 TXQ.???0 R0, R0,     ???255, TEX_HEADER_DIMENSION, 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| modi 1 | 59 |
| operand 3 | 61-63 |
| operand 0 | 64-71 |
| operand 4 | 72-76 |
| NODEP | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000011101100............11111111000000000000000000000000000.0...
.............0000000000000.00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `B.` |

