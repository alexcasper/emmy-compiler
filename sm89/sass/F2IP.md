# F2IP (SM89 SASS)

**NVIDIA:** FP32 Down-Convert to Integer and Pack (Conversion Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: FP32 to packed narrow integer conversion (category: Conversion)

Typically emitted for: per NVIDIA: FP32 down-convert to integer and pack; no PTX source found (`cvt.rni.sat.s8.f32` gives F2I)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/F2IP.html> (machine-derived by fuzzing the assembler; no semantics).

9 encoding variant(s):

- [F2IP_R_R_R_FI](#v1)
- [F2IP_R_R_R_c[I][I]](#v2)
- [F2IP_R_R_R_cx[UR][I]](#v3)
- [F2IP_R_R_FI_R](#v4)
- [F2IP_R_R_c[I][I]_R](#v5)
- [F2IP_R_R_cx[UR][I]_R](#v6)
- [F2IP_R_R_UR_R](#v7)
- [F2IP_R_R_R_UR](#v8)
- [F2IP_R_R_R_R](#v9)

<a id="v1"></a>
## 1. `F2IP_R_R_R_FI`

Syntax: `F2IP.F32 R, R, R, FIMM`  
Example: `@P0 F2IP.U8.F32 R0, R0, R0, 0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-63, 72-73 |
| operand 2 | 64-71 |
| NTZ | 74 |
| RELU | 75 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000100010....................................................
................0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `TRUNC.` |

<a id="v2"></a>
## 2. `F2IP_R_R_R_c[I][I]`

Syntax: `F2IP.F32 R, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 F2IP.U8.F32 R0, R0, R0, c[0x0] [0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 2 | 64-71 |
| NTZ | 74 |
| RELU | 75 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000100110....................00000000...................00000
........00......0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `TRUNC.` |

<a id="v3"></a>
## 3. `F2IP_R_R_R_cx[UR][I]`

Syntax: `F2IP.F32 R, R, R, cx[UR][INT_IMM]`  
Example: `@P0 F2IP.U8.F32 R0, R0, R0, cx[UR0] [0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 2 | 64-71 |
| NTZ | 74 |
| RELU | 75 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000100110...........................0...............000000000
........00......0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `TRUNC.` |

<a id="v4"></a>
## 4. `F2IP_R_R_FI_R`

Syntax: `F2IP.F32 R, R, FIMM, R`  
Example: `@P0 F2IP.U8.F32 R0, R0, 0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
| H1 (op 3) | 72 |
| NTZ | 74 |
| RELU | 75 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000100001....................................................
.........0......0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `TRUNC.` |

<a id="v5"></a>
## 5. `F2IP_R_R_c[I][I]_R`

Syntax: `F2IP.F32 R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 F2IP.U8.F32 R0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| H1 (op 4) | 72 |
| NTZ | 74 |
| RELU | 75 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000100101....................00000000...................00000
.........0......0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `TRUNC.` |

<a id="v6"></a>
## 6. `F2IP_R_R_cx[UR][I]_R`

Syntax: `F2IP.F32 R, R, cx[UR][INT_IMM], R`  
Example: `@P0 F2IP.U8.F32 R0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| H1 (op 4) | 72 |
| NTZ | 74 |
| RELU | 75 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000100101...........................0...............000000000
.........0......0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `TRUNC.` |

<a id="v7"></a>
## 7. `F2IP_R_R_UR_R`

Syntax: `F2IP.F32 R, R, UR, R`  
Example: `@P0 F2IP.U8.F32 R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
| H1 (op 3) | 72 |
| NTZ | 74 |
| RELU | 75 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000100011...........................0000000000000000000000000
.........0......0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `TRUNC.` |

<a id="v8"></a>
## 8. `F2IP_R_R_R_UR`

Syntax: `F2IP.F32 R, R, R, UR`  
Example: `@P0 F2IP.U8.F32 R0, R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| operand 2 | 64-71 |
| H1 (op 3) | 72 |
| NTZ | 74 |
| RELU | 75 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000100111...........................0000000000000000000000000
.........0......0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `TRUNC.` |

<a id="v9"></a>
## 9. `F2IP_R_R_R_R`

Syntax: `F2IP.F32 R, R, R, R`  
Example: `@P0 F2IP.U8.F32 R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
| H1 (op 3) | 72 |
| NTZ | 74 |
| RELU | 75 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000100100............................000000000000000000000000
.........0......0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `INVALID2.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `TRUNC.` |

