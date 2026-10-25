# ULEA (SM89 SASS)

**NVIDIA:** Uniform Load Effective Address (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform load-effective-address (category: Uniform datapath)

Typically emitted for: warp-uniform address computation

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/ULEA.html> (machine-derived by fuzzing the assembler; no semantics).

20 encoding variant(s):

- [ULEA_UR_UP_UR_UR_I_I](#v1)
- [ULEA_UR_UP_UR_UR_I_I_UP](#v2)
- [ULEA_UR_UR_UR_I_I](#v3)
- [ULEA_UR_UR_UR_I_I_UP](#v4)
- [ULEA_UR_UP_UR_I_I](#v5)
- [ULEA_UR_UP_UR_I_I_UP](#v6)
- [ULEA_UR_UP_UR_I_UR_I](#v7)
- [ULEA_UR_UP_UR_I_UR_I_UP](#v8)
- [ULEA_UR_UR_I_I](#v9)
- [ULEA_UR_UR_I_I_UP](#v10)
- [ULEA_UR_UR_I_UR_I](#v11)
- [ULEA_UR_UR_I_UR_I_UP](#v12)
- [ULEA_UR_UP_UR_UR_I](#v13)
- [ULEA_UR_UP_UR_UR_I_UP](#v14)
- [ULEA_UR_UP_UR_UR_UR_I](#v15)
- [ULEA_UR_UP_UR_UR_UR_I_UP](#v16)
- [ULEA_UR_UR_UR_I](#v17)
- [ULEA_UR_UR_UR_I_UP](#v18)
- [ULEA_UR_UR_UR_UR_I](#v19)
- [ULEA_UR_UR_UR_UR_I_UP](#v20)

<a id="v1"></a>
## 1. `ULEA_UR_UP_UR_UR_I_I`

Syntax: `ULEA UR, UP, UR, UR, INT_IMM, INT_IMM`  
Example: `@UP0 ULEA.???0 UR0, UP0, UR0, UR0, 0x0, 0x0;`

Register access: WRITE UR (1 slots); WRITE UP (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 4 | 32-63 |
| operand 3 | 64-70 |
| cNEG (op 2) | 72 |
| operand 5 | 75-79 |
| modi 1 | 80 |
| operand 1 | 81-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010010...........0.......0................................
.......0.00.........000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `HI.` |

<a id="v2"></a>
## 2. `ULEA_UR_UP_UR_UR_I_I_UP`

Syntax: `ULEA.X UR, UP, UR, UR, INT_IMM, INT_IMM, UP`  
Example: `@UP0 ULEA.???0.X UR0, UP0, UR0, UR0, 0x0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ_WRITE UP (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 4 | 32-63 |
| operand 3 | 64-70 |
| cINV (op 2) | 72 |
| operand 5 | 75-79 |
| modi 1 | 80 |
| operand 1 | 81-83 |
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
100010010010...........0.......0................................
.......0.01.........00.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `HI.` |

<a id="v3"></a>
## 3. `ULEA_UR_UR_UR_I_I`

Syntax: `ULEA UR, UR, UR, INT_IMM, INT_IMM`  
Example: `@UP0 ULEA.???0 UR0, UR0, UR0, 0x0, 0x0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 3 | 32-63 |
| operand 2 | 64-70 |
| cNEG (op 1) | 72 |
| operand 4 | 75-79 |
| modi 1 | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010010...........0.......0................................
.......0.00......111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `HI.` |

<a id="v4"></a>
## 4. `ULEA_UR_UR_UR_I_I_UP`

Syntax: `ULEA.X UR, UR, UR, INT_IMM, INT_IMM, UP`  
Example: `@UP0 ULEA.???0.X UR0, UR0, UR0, 0x0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 3 | 32-63 |
| operand 2 | 64-70 |
| cINV (op 1) | 72 |
| operand 4 | 75-79 |
| modi 1 | 80 |
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
100010010010...........0.......0................................
.......0.01......11100.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `HI.` |

<a id="v5"></a>
## 5. `ULEA_UR_UP_UR_I_I`

Syntax: `ULEA UR, UP, UR, INT_IMM, INT_IMM`  
Example: `@UP0 ULEA UR0, UP0, UR0, 0x0, 0x0;`

Register access: WRITE UR (1 slots); WRITE UP (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| cNEG (op 2) | 72 |
| operand 4 | 75-79 |
| operand 1 | 81-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010001...........0.......0................................
00000000.00.....0...000000010000000000000.....................00
```

<a id="v6"></a>
## 6. `ULEA_UR_UP_UR_I_I_UP`

Syntax: `ULEA.X UR, UP, UR, INT_IMM, INT_IMM, UP`  
Example: `@UP0 ULEA.X UR0, UP0, UR0, 0x0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ_WRITE UP (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| cINV (op 2) | 72 |
| operand 4 | 75-79 |
| operand 1 | 81-83 |
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
100010010001...........0.......0................................
00000000.01.....0...00.....10000000000000.....................00
```

<a id="v7"></a>
## 7. `ULEA_UR_UP_UR_I_UR_I`

Syntax: `ULEA.HI UR, UP, UR, INT_IMM, UR, INT_IMM`  
Example: `@UP0 ULEA.HI UR0, UP0, UR0, 0x0, UR0, 0x0;`

Register access: WRITE UR (1 slots); WRITE UP (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| operand 4 | 64-70 |
| cNEG (op 2) | 72 |
| operand 5 | 75-79 |
| operand 1 | 81-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010001...........0.......0................................
.......0.00.....1...000000010000000000000.....................00
```

<a id="v8"></a>
## 8. `ULEA_UR_UP_UR_I_UR_I_UP`

Syntax: `ULEA.HI.X UR, UP, UR, INT_IMM, UR, INT_IMM, UP`  
Example: `@UP0 ULEA.HI.X UR0, UP0, UR0, 0x0, UR0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ_WRITE UP (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| operand 4 | 64-70 |
| cINV (op 2) | 72 |
| operand 5 | 75-79 |
| operand 1 | 81-83 |
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
100010010001...........0.......0................................
.......0.01.....1...00.....10000000000000.....................00
```

<a id="v9"></a>
## 9. `ULEA_UR_UR_I_I`

Syntax: `ULEA UR, UR, INT_IMM, INT_IMM`  
Example: `@UP0 ULEA UR0, UR0, 0x0, 0x0;`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| cNEG (op 1) | 72 |
| operand 3 | 75-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010001...........0.......0................................
00000000.00.....0111000000010000000000000.....................00
```

<a id="v10"></a>
## 10. `ULEA_UR_UR_I_I_UP`

Syntax: `ULEA.X UR, UR, INT_IMM, INT_IMM, UP`  
Example: `@UP0 ULEA.X UR0, UR0, 0x0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| cINV (op 1) | 72 |
| operand 3 | 75-79 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010001...........0.......0................................
00000000.01.....011100.....10000000000000.....................00
```

<a id="v11"></a>
## 11. `ULEA_UR_UR_I_UR_I`

Syntax: `ULEA.HI UR, UR, INT_IMM, UR, INT_IMM`  
Example: `@UP0 ULEA.HI UR0, UR0, 0x0, UR0, 0x0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| cNEG (op 1) | 72 |
| operand 4 | 75-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010001...........0.......0................................
.......0.00.....1111000000010000000000000.....................00
```

<a id="v12"></a>
## 12. `ULEA_UR_UR_I_UR_I_UP`

Syntax: `ULEA.HI.X UR, UR, INT_IMM, UR, INT_IMM, UP`  
Example: `@UP0 ULEA.HI.X UR0, UR0, 0x0, UR0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| cINV (op 1) | 72 |
| operand 4 | 75-79 |
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
100010010001...........0.......0................................
.......0.01.....111100.....10000000000000.....................00
```

<a id="v13"></a>
## 13. `ULEA_UR_UP_UR_UR_I`

Syntax: `ULEA UR, UP, UR, UR, INT_IMM`  
Example: `@UP0 ULEA UR0, UP0, UR0, UR0, 0x0;`

Register access: WRITE UR (1 slots); WRITE UP (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| cNEG (op 3) | 63 |
| cNEG (op 2) | 72 |
| operand 4 | 75-79 |
| operand 1 | 81-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010100...........0.......0.......000000000000000000000000.
00000000.00.....0...000000010000000000000.....................00
```

<a id="v14"></a>
## 14. `ULEA_UR_UP_UR_UR_I_UP`

Syntax: `ULEA.X UR, UP, UR, UR, INT_IMM, UP`  
Example: `@UP0 ULEA.X UR0, UP0, UR0, UR0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ_WRITE UP (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| cINV (op 3) | 63 |
| cINV (op 2) | 72 |
| operand 4 | 75-79 |
| operand 1 | 81-83 |
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
100010010100...........0.......0.......000000000000000000000000.
00000000.01.....0...00.....10000000000000.....................00
```

<a id="v15"></a>
## 15. `ULEA_UR_UP_UR_UR_UR_I`

Syntax: `ULEA.HI UR, UP, UR, UR, UR, INT_IMM`  
Example: `@UP0 ULEA.HI UR0, UP0, UR0, UR0, UR0, 0x0;`

Register access: WRITE UR (1 slots); WRITE UP (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| cNEG (op 3) | 63 |
| operand 4 | 64-70 |
| cNEG (op 2) | 72 |
| operand 5 | 75-79 |
| operand 1 | 81-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010100...........0.......0.......000000000000000000000000.
.......0.00.....1...000000010000000000000.....................00
```

<a id="v16"></a>
## 16. `ULEA_UR_UP_UR_UR_UR_I_UP`

Syntax: `ULEA.HI.X UR, UP, UR, UR, UR, INT_IMM, UP`  
Example: `@UP0 ULEA.HI.X UR0, UP0, UR0, UR0, UR0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ_WRITE UP (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| cINV (op 3) | 63 |
| operand 4 | 64-70 |
| cINV (op 2) | 72 |
| operand 5 | 75-79 |
| operand 1 | 81-83 |
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
100010010100...........0.......0.......000000000000000000000000.
.......0.01.....1...00.....10000000000000.....................00
```

<a id="v17"></a>
## 17. `ULEA_UR_UR_UR_I`

Syntax: `ULEA.HI.SX32 UR, UR, UR, INT_IMM`  
Example: `@UP0 ULEA.HI.SX32 UR0, UR0, UR0, 0x0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| cNEG (op 2) | 63 |
| cNEG (op 1) | 72 |
| operand 3 | 75-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010100...........0.......0.......000000000000000000000000.
00000000.10.....1111000000010000000000000.....................00
```

<a id="v18"></a>
## 18. `ULEA_UR_UR_UR_I_UP`

Syntax: `ULEA.SX32.HI.X UR, UR, UR, INT_IMM, UP`  
Example: `@UP0 ULEA.HI.X.SX32 UR0, UR0, UR0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| cINV (op 2) | 63 |
| cINV (op 1) | 72 |
| operand 3 | 75-79 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010100...........0.......0.......000000000000000000000000.
00000000.11.....111100.....10000000000000.....................00
```

<a id="v19"></a>
## 19. `ULEA_UR_UR_UR_UR_I`

Syntax: `ULEA.HI UR, UR, UR, UR, INT_IMM`  
Example: `@UP0 ULEA.HI UR0, UR0, UR0, UR0, 0x0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| cNEG (op 2) | 63 |
| operand 3 | 64-70 |
| cNEG (op 1) | 72 |
| operand 4 | 75-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010010100...........0.......0.......000000000000000000000000.
.......0.00.....1111000000010000000000000.....................00
```

<a id="v20"></a>
## 20. `ULEA_UR_UR_UR_UR_I_UP`

Syntax: `ULEA.HI.X UR, UR, UR, UR, INT_IMM, UP`  
Example: `@UP0 ULEA.HI.X UR0, UR0, UR0, UR0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| cINV (op 2) | 63 |
| operand 3 | 64-70 |
| cINV (op 1) | 72 |
| operand 4 | 75-79 |
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
100010010100...........0.......0.......000000000000000000000000.
.......0.01.....111100.....10000000000000.....................00
```

