# LOP3 (SM89 SASS)

**NVIDIA:** Logic Operation (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Arbitrary 3-input bitwise logic (8-bit LUT) (category: Integer)

Typically emitted for: `and/or/xor/not`, `lop3.b32`; any bitwise expression of up to 3 inputs

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x12, 0x92 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2064)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [lop3](../verify/RESULTS.md#lop3): `and/xor/or of 3 values`

Encodings: <https://kuterdinel.com/nv_isa_sm89/LOP3.html> (machine-derived by fuzzing the assembler; no semantics).

10 encoding variant(s):

- [LOP3_P_R_R_I_R_I_P](#v1)
- [LOP3_R_R_I_R_I_P](#v2)
- [LOP3_P_R_R_c[I][I]_R_I_P](#v3)
- [LOP3_P_R_R_cx[UR][I]_R_I_P](#v4)
- [LOP3_R_R_c[I][I]_R_I_P](#v5)
- [LOP3_R_R_cx[UR][I]_R_I_P](#v6)
- [LOP3_P_R_R_UR_R_I_P](#v7)
- [LOP3_R_R_UR_R_I_P](#v8)
- [LOP3_P_R_R_R_R_I_P](#v9)
- [LOP3_R_R_R_R_I_P](#v10)

<a id="v1"></a>
## 1. `LOP3_P_R_R_I_R_I_P`

Syntax: `LOP3.LUT P, R, R, INT_IMM, R, INT_IMM, P`  
Example: `@P0 LOP3.LUT P0, R0, R0, 0x0, R0, 0x0, P0;`

Register access: READ_WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| operand 4 | 64-71 |
| operand 5 | 72-79 |
| PAND | 80 |
| operand 0 | 81-83 |
| operand 6 | 86-89 |
| cNOT (op 6) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010000001....................................................
....................00.....00000000000000.....................00
```

<a id="v2"></a>
## 2. `LOP3_R_R_I_R_I_P`

Syntax: `LOP3.LUT R, R, INT_IMM, R, INT_IMM, P`  
Example: `@P0 LOP3.LUT R0, R0, 0x0, R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
| operand 4 | 72-79 |
| PAND | 80 |
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
010010000001....................................................
.................11100.....00000000000000.....................00
```

<a id="v3"></a>
## 3. `LOP3_P_R_R_c[I][I]_R_I_P`

Syntax: `LOP3.LUT P, R, R, c[INT_IMM][INT_IMM], R, INT_IMM, P`  
Example: `@P0 LOP3.LUT P0, R0, R0, c[0x0][0x0], R0, 0x0, P0;`

Register access: READ_WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 64-71 |
| operand 6 | 72-79 |
| PAND | 80 |
| operand 0 | 81-83 |
| operand 7 | 86-89 |
| cNOT (op 7) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010000101....................00000000...................00000
....................00.....00000000000000.....................00
```

<a id="v4"></a>
## 4. `LOP3_P_R_R_cx[UR][I]_R_I_P`

Syntax: `LOP3.LUT P, R, R, cx[UR][INT_IMM], R, INT_IMM, P`  
Example: `@P0 LOP3.LUT P0, R0, R0, cx[UR0][0x0], R0, 0x0, P0;`

Register access: READ_WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 5 | 64-71 |
| operand 6 | 72-79 |
| PAND | 80 |
| operand 0 | 81-83 |
| operand 7 | 86-89 |
| cNOT (op 7) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010000101...........................0...............000000000
....................00.....10000000000000.....................00
```

<a id="v5"></a>
## 5. `LOP3_R_R_c[I][I]_R_I_P`

Syntax: `LOP3.LUT R, R, c[INT_IMM][INT_IMM], R, INT_IMM, P`  
Example: `@P0 LOP3.LUT R0, R0, c[0x0][0x0], R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| operand 5 | 72-79 |
| PAND | 80 |
| operand 6 | 86-89 |
| cNOT (op 6) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010000101....................00000000...................00000
.................11100.....00000000000000.....................00
```

<a id="v6"></a>
## 6. `LOP3_R_R_cx[UR][I]_R_I_P`

Syntax: `LOP3.LUT R, R, cx[UR][INT_IMM], R, INT_IMM, P`  
Example: `@P0 LOP3.LUT R0, R0, cx[UR0][0x0], R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| operand 5 | 72-79 |
| PAND | 80 |
| operand 6 | 86-89 |
| cNOT (op 6) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010000101...........................0...............000000000
.................11100.....10000000000000.....................00
```

<a id="v7"></a>
## 7. `LOP3_P_R_R_UR_R_I_P`

Syntax: `LOP3.LUT P, R, R, UR, R, INT_IMM, P`  
Example: `@P0 LOP3.LUT P0, R0, R0, UR0, R0, 0x0, P0;`

Register access: READ_WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 64-71 |
| operand 5 | 72-79 |
| PAND | 80 |
| operand 0 | 81-83 |
| operand 6 | 86-89 |
| cNOT (op 6) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010000011...........................0000000000000000000000000
....................00.....10000000000000.....................00
```

<a id="v8"></a>
## 8. `LOP3_R_R_UR_R_I_P`

Syntax: `LOP3.LUT R, R, UR, R, INT_IMM, P`  
Example: `@P0 LOP3.LUT R0, R0, UR0, R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
| operand 4 | 72-79 |
| PAND | 80 |
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
010010000011...........................0000000000000000000000000
.................11100.....10000000000000.....................00
```

<a id="v9"></a>
## 9. `LOP3_P_R_R_R_R_I_P`

Syntax: `LOP3.LUT P, R, R, R, R, INT_IMM, P`  
Example: `@P0 LOP3.LUT P0, R0, R0, R0, R0, 0x0, P0;`

Register access: READ_WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 64-71 |
| operand 5 | 72-79 |
| PAND | 80 |
| operand 0 | 81-83 |
| operand 6 | 86-89 |
| cNOT (op 6) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010000100............................000000000000000000000000
....................00.....00000000000000.....................00
```

<a id="v10"></a>
## 10. `LOP3_R_R_R_R_I_P`

Syntax: `LOP3.LUT R, R, R, R, INT_IMM, P`  
Example: `@P0 LOP3.LUT R0, R0, R0, R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
| operand 4 | 72-79 |
| PAND | 80 |
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
010010000100............................000000000000000000000000
.................11100.....00000000000000.....................00
```

