# UIMAD (SM89 SASS)

**NVIDIA:** Uniform Integer Multiplication (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform integer multiply-add (category: Uniform datapath)

Typically emitted for: warp-uniform multiply (e.g. `blockIdx.x * blockDim.x`)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [uniform_txq](../verify/RESULTS.md#uniform_txq): `txq.num_mipmap_levels (handle arithmetic runs on uniform datapath)`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 74 | `UIMAD UR4, UR4, UR5, 0x2c` |
| 81 | `UIMAD UR4, UR4, UR5, 0x2c` |
| 82 | `UIMAD UR4, UR4, UR5, 0x2c` |
| 83 | `UIMAD UR4, UR4, UR5, 0x2c` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/UIMAD.html> (machine-derived by fuzzing the assembler; no semantics).

14 encoding variant(s):

- [UIMAD_UR_UR_UR_I](#v1)
- [UIMAD_UR_UR_UR_I_UP](#v2)
- [UIMAD_UR_UR_I_UR](#v3)
- [UIMAD_UR_UR_I_UR_UP](#v4)
- [UIMAD_UR_UP_UR_I_UR](#v5)
- [UIMAD_UR_UP_UR_I_UR_UP](#v6)
- [UIMAD_UR_UR_I_UR](#v7)
- [UIMAD_UR_UR_I_UR_UP](#v8)
- [UIMAD_UR_UR_UR_UR](#v9)
- [UIMAD_UR_UR_UR_UR_UP](#v10)
- [UIMAD_UR_UP_UR_UR_UR](#v11)
- [UIMAD_UR_UP_UR_UR_UR_UP](#v12)
- [UIMAD_UR_UR_UR_UR](#v13)
- [UIMAD_UR_UR_UR_UR_UP](#v14)

<a id="v1"></a>
## 1. `UIMAD_UR_UR_UR_I`

Syntax: `UIMAD UR, UR, UR, INT_IMM`  
Example: `@UP0 UIMAD.U32 UR0, UR0, UR0, 0x0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 3 | 32-63 |
| operand 2 | 64-70 |
| modi 1 | 73 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001010010...........0.......0................................
.......00.0000000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v2"></a>
## 2. `UIMAD_UR_UR_UR_I_UP`

Syntax: `UIMAD.X UR, UR, UR, INT_IMM, UP`  
Example: `@UP0 UIMAD.U32.X UR0, UR0, UR0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 3 | 32-63 |
| operand 2 | 64-70 |
| modi 1 | 73 |
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
001001010010...........0.......0................................
.......00.100000000000.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v3"></a>
## 3. `UIMAD_UR_UR_I_UR`

Syntax: `UIMAD UR, UR, INT_IMM, UR`  
Example: `@UP0 UIMAD.U32 UR0, UR0, 0x0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| modi 1 | 73 |
| cNEG (op 3) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001010001...........0.......0................................
.......00.0.00000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v4"></a>
## 4. `UIMAD_UR_UR_I_UR_UP`

Syntax: `UIMAD.X UR, UR, INT_IMM, UR, UP`  
Example: `@UP0 UIMAD.U32.X UR0, UR0, 0x0, UR0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| modi 1 | 73 |
| cINV (op 3) | 75 |
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
001001010001...........0.......0................................
.......00.1.0000000000.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v5"></a>
## 5. `UIMAD_UR_UP_UR_I_UR`

Syntax: `UIMAD.WIDE UR, UP, UR, INT_IMM, UR`  
Example: `@UP0 UIMAD.WIDE.U32 UR0, UP0, UR0, 0x0, UR0;`

Register access: WRITE UR (2 slots); READ UR (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| operand 4 | 64-70 |
| modi 1 | 73 |
| cNEG (op 4) | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101001010001...........0.......0................................
.......00.0.0000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v6"></a>
## 6. `UIMAD_UR_UP_UR_I_UR_UP`

Syntax: `UIMAD.WIDE.X UR, UP, UR, INT_IMM, UR, UP`  
Example: `@UP0 UIMAD.WIDE.U32.X UR0, UP0, UR0, 0x0, UR0, UP0;`

Register access: WRITE UR (2 slots); READ UP (1 slots); READ UR (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| operand 4 | 64-70 |
| modi 1 | 73 |
| cINV (op 4) | 75 |
| operand 1 | 80-83 |
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
101001010001...........0.......0................................
.......00.1.0000....00.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v7"></a>
## 7. `UIMAD_UR_UR_I_UR`

Syntax: `UIMAD UR, UR, INT_IMM, UR`  
Example: `@UP0 UIMAD.U32 UR0, UR0, 0x0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| modi 1 | 73 |
| cNEG (op 3) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001010001...........0.......0................................
.......00.0.00000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v8"></a>
## 8. `UIMAD_UR_UR_I_UR_UP`

Syntax: `UIMAD.X UR, UR, INT_IMM, UR, UP`  
Example: `@UP0 UIMAD.U32.X UR0, UR0, 0x0, UR0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| modi 1 | 73 |
| cINV (op 3) | 75 |
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
001001010001...........0.......0................................
.......00.1.0000011100.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v9"></a>
## 9. `UIMAD_UR_UR_UR_UR`

Syntax: `UIMAD UR, UR, UR, UR`  
Example: `@UP0 UIMAD.U32 UR0, UR0, UR0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| operand 3 | 64-70 |
| modi 1 | 73 |
| cNEG (op 3) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001010100...........0.......0.......0000000000000000000000000
.......00.0.00000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v10"></a>
## 10. `UIMAD_UR_UR_UR_UR_UP`

Syntax: `UIMAD.X UR, UR, UR, UR, UP`  
Example: `@UP0 UIMAD.U32.X UR0, UR0, UR0, UR0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| operand 3 | 64-70 |
| modi 1 | 73 |
| cINV (op 3) | 75 |
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
001001010100...........0.......0.......0000000000000000000000000
.......00.1.0000000000.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v11"></a>
## 11. `UIMAD_UR_UP_UR_UR_UR`

Syntax: `UIMAD.WIDE UR, UP, UR, UR, UR`  
Example: `@UP0 UIMAD.WIDE.U32 UR0, UP0, UR0, UR0, UR0;`

Register access: WRITE UR (2 slots); READ UR (1 slots); READ UR (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| operand 4 | 64-70 |
| modi 1 | 73 |
| cNEG (op 4) | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101001010100...........0.......0.......0000000000000000000000000
.......00.0.0000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v12"></a>
## 12. `UIMAD_UR_UP_UR_UR_UR_UP`

Syntax: `UIMAD.WIDE.X UR, UP, UR, UR, UR, UP`  
Example: `@UP0 UIMAD.WIDE.U32.X UR0, UP0, UR0, UR0, UR0, UP0;`

Register access: WRITE UR (2 slots); READ UP (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| operand 4 | 64-70 |
| modi 1 | 73 |
| cINV (op 4) | 75 |
| operand 1 | 80-83 |
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
101001010100...........0.......0.......0000000000000000000000000
.......00.1.0000....00.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v13"></a>
## 13. `UIMAD_UR_UR_UR_UR`

Syntax: `UIMAD UR, UR, UR, UR`  
Example: `@UP0 UIMAD.U32 UR0, UR0, UR0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| operand 3 | 64-70 |
| modi 1 | 73 |
| cNEG (op 3) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001010100...........0.......0.......0000000000000000000000000
.......00.0.00000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v14"></a>
## 14. `UIMAD_UR_UR_UR_UR_UP`

Syntax: `UIMAD.X UR, UR, UR, UR, UP`  
Example: `@UP0 UIMAD.U32.X UR0, UR0, UR0, UR0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| operand 3 | 64-70 |
| modi 1 | 73 |
| cINV (op 3) | 75 |
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
001001010100...........0.......0.......0000000000000000000000000
.......00.1.0000011100.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

