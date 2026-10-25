# VABSDIFF4 (SM89 SASS)

**NVIDIA:** Absolute Difference (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: 4-way byte absolute difference (SIMD video op) (category: Integer)

Typically emitted for: `vabsdiff4` (verified)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [vabsdiff4](../verify/RESULTS.md#vabsdiff4): `vabsdiff4.u32.u32.u32.add`

Encodings: <https://kuterdinel.com/nv_isa_sm89/VABSDIFF4.html> (machine-derived by fuzzing the assembler; no semantics).

18 encoding variant(s):

- [VABSDIFF4_R_P_R_R_I](#v1)
- [VABSDIFF4_R_R_R_I](#v2)
- [VABSDIFF4_R_P_R_R_c[I][I]](#v3)
- [VABSDIFF4_R_P_R_R_cx[UR][I]](#v4)
- [VABSDIFF4_R_R_R_c[I][I]](#v5)
- [VABSDIFF4_R_R_R_cx[UR][I]](#v6)
- [VABSDIFF4_R_P_R_I_R](#v7)
- [VABSDIFF4_R_R_I_R](#v8)
- [VABSDIFF4_R_P_R_c[I][I]_R](#v9)
- [VABSDIFF4_R_P_R_cx[UR][I]_R](#v10)
- [VABSDIFF4_R_R_c[I][I]_R](#v11)
- [VABSDIFF4_R_R_cx[UR][I]_R](#v12)
- [VABSDIFF4_R_P_R_UR_R](#v13)
- [VABSDIFF4_R_R_UR_R](#v14)
- [VABSDIFF4_R_P_R_R_UR](#v15)
- [VABSDIFF4_R_R_R_UR](#v16)
- [VABSDIFF4_R_P_R_R_R](#v17)
- [VABSDIFF4_R_R_R_R](#v18)

<a id="v1"></a>
## 1. `VABSDIFF4_R_P_R_R_I`

Syntax: `VABSDIFF4 R, P, R, R, INT_IMM`  
Example: `@P0 VABSDIFF4.U8 R0, P0, R0, R0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-63 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000010....................................................
........0.0.0000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v2"></a>
## 2. `VABSDIFF4_R_R_R_I`

Syntax: `VABSDIFF4 R, R, R, INT_IMM`  
Example: `@P0 VABSDIFF4.U8 R0, R0, R0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-63 |
| operand 2 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000010....................................................
........0.0.00000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v3"></a>
## 3. `VABSDIFF4_R_P_R_R_c[I][I]`

Syntax: `VABSDIFF4 R, P, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 VABSDIFF4.U8 R0, P0, R0, R0, c[0x0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000110....................00000000...................00000
........0.0.0000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v4"></a>
## 4. `VABSDIFF4_R_P_R_R_cx[UR][I]`

Syntax: `VABSDIFF4 R, P, R, R, cx[UR][INT_IMM]`  
Example: `@P0 VABSDIFF4.U8 R0, P0, R0, R0, cx[UR0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-38 |
| operand 5 | 40-54 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000110...........................0...............000000000
........0.0.0000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v5"></a>
## 5. `VABSDIFF4_R_R_R_c[I][I]`

Syntax: `VABSDIFF4 R, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 VABSDIFF4.U8 R0, R0, R0, c[0x0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 2 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000110....................00000000...................00000
........0.0.00000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v6"></a>
## 6. `VABSDIFF4_R_R_R_cx[UR][I]`

Syntax: `VABSDIFF4 R, R, R, cx[UR][INT_IMM]`  
Example: `@P0 VABSDIFF4.U8 R0, R0, R0, cx[UR0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 2 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000110...........................0...............000000000
........0.0.00000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v7"></a>
## 7. `VABSDIFF4_R_P_R_I_R`

Syntax: `VABSDIFF4 R, P, R, INT_IMM, R`  
Example: `@P0 VABSDIFF4.U8 R0, P0, R0, 0x0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| operand 4 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000001....................................................
........0.0.0000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v8"></a>
## 8. `VABSDIFF4_R_R_I_R`

Syntax: `VABSDIFF4 R, R, INT_IMM, R`  
Example: `@P0 VABSDIFF4.U8 R0, R0, 0x0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000001....................................................
........0.0.00000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v9"></a>
## 9. `VABSDIFF4_R_P_R_c[I][I]_R`

Syntax: `VABSDIFF4 R, P, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 VABSDIFF4.U8 R0, P0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000101....................00000000...................00000
........0.0.0000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v10"></a>
## 10. `VABSDIFF4_R_P_R_cx[UR][I]_R`

Syntax: `VABSDIFF4 R, P, R, cx[UR][INT_IMM], R`  
Example: `@P0 VABSDIFF4.U8 R0, P0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 5 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000101...........................0...............000000000
........0.0.0000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v11"></a>
## 11. `VABSDIFF4_R_R_c[I][I]_R`

Syntax: `VABSDIFF4 R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 VABSDIFF4.U8 R0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000101....................00000000...................00000
........0.0.00000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v12"></a>
## 12. `VABSDIFF4_R_R_cx[UR][I]_R`

Syntax: `VABSDIFF4 R, R, cx[UR][INT_IMM], R`  
Example: `@P0 VABSDIFF4.U8 R0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000101...........................0...............000000000
........0.0.00000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v13"></a>
## 13. `VABSDIFF4_R_P_R_UR_R`

Syntax: `VABSDIFF4 R, P, R, UR, R`  
Example: `@P0 VABSDIFF4.U8 R0, P0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000011...........................0000000000000000000000000
........0.0.0000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v14"></a>
## 14. `VABSDIFF4_R_R_UR_R`

Syntax: `VABSDIFF4 R, R, UR, R`  
Example: `@P0 VABSDIFF4.U8 R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000011...........................0000000000000000000000000
........0.0.00000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v15"></a>
## 15. `VABSDIFF4_R_P_R_R_UR`

Syntax: `VABSDIFF4 R, P, R, R, UR`  
Example: `@P0 VABSDIFF4.U8 R0, P0, R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-38 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000111...........................0000000000000000000000000
........0.0.0000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v16"></a>
## 16. `VABSDIFF4_R_R_R_UR`

Syntax: `VABSDIFF4 R, R, R, UR`  
Example: `@P0 VABSDIFF4.U8 R0, R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| operand 2 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000111...........................0000000000000000000000000
........0.0.00000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v17"></a>
## 17. `VABSDIFF4_R_P_R_R_R`

Syntax: `VABSDIFF4 R, P, R, R, R`  
Example: `@P0 VABSDIFF4.U8 R0, P0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000100............................000000000000000000000000
........0.0.0000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

<a id="v18"></a>
## 18. `VABSDIFF4_R_R_R_R`

Syntax: `VABSDIFF4 R, R, R, R`  
Example: `@P0 VABSDIFF4.U8 R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| ACC | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010000100............................000000000000000000000000
........0.0.00000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U8.` |
| `1` | `(default)` |

