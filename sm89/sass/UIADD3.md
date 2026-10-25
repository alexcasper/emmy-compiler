# UIADD3 (SM89 SASS)

**NVIDIA:** Uniform Integer Addition (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform 3-input integer add (category: Uniform datapath)

Typically emitted for: warp-uniform integer adds (loop counters, base pointers)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [uniform_loop](../verify/RESULTS.md#uniform_loop): `loop with trip count from kernel param (uniform datapath)`
- [s2ur_loop](../verify/RESULTS.md#s2ur_loop): `%ctaid.x as a loop bound (warp-uniform)`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 74 | `UIADD3 UR4, UP0, UR4, UR6, URZ`<br>`UIADD3 UR4, UR4, -0x3, URZ`<br>`UIADD3 UR7, UR6, -0x3, URZ` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/UIADD3.html> (machine-derived by fuzzing the assembler; no semantics).

24 encoding variant(s):

- [UIADD3_UR_UP_UP_UR_I_UR](#v1)
- [UIADD3_UR_UP_UP_UR_I_UR_UP_UP](#v2)
- [UIADD3_UR_UP_UR_I_UR](#v3)
- [UIADD3_UR_UP_UR_I_UR_UP_UP](#v4)
- [UIADD3_UR_UR_I_UR](#v5)
- [UIADD3_UR_UR_I_UR_UP_UP](#v6)
- [UIADD3_UR_UP_UP_UR_I_UR](#v7)
- [UIADD3_UR_UP_UP_UR_I_UR_UP_UP](#v8)
- [UIADD3_UR_UP_UR_I_UR](#v9)
- [UIADD3_UR_UP_UR_I_UR_UP_UP](#v10)
- [UIADD3_UR_UR_I_UR](#v11)
- [UIADD3_UR_UR_I_UR_UP_UP](#v12)
- [UIADD3_UR_UP_UP_UR_UR_UR](#v13)
- [UIADD3_UR_UP_UP_UR_UR_UR_UP_UP](#v14)
- [UIADD3_UR_UP_UR_UR_UR](#v15)
- [UIADD3_UR_UP_UR_UR_UR_UP_UP](#v16)
- [UIADD3_UR_UR_UR_UR](#v17)
- [UIADD3_UR_UR_UR_UR_UP_UP](#v18)
- [UIADD3_UR_UP_UP_UR_UR_UR](#v19)
- [UIADD3_UR_UP_UP_UR_UR_UR_UP_UP](#v20)
- [UIADD3_UR_UP_UR_UR_UR](#v21)
- [UIADD3_UR_UP_UR_UR_UR_UP_UP](#v22)
- [UIADD3_UR_UR_UR_UR](#v23)
- [UIADD3_UR_UR_UR_UR_UP_UP](#v24)

<a id="v1"></a>
## 1. `UIADD3_UR_UP_UP_UR_I_UR`

Syntax: `UIADD3 UR, UP, UP, UR, INT_IMM, UR`  
Example: `@UP0 UIADD3 UR0, UP0, UP0, UR0, 0x0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 3 | 24-30 |
| operand 4 | 32-63 |
| operand 5 | 64-70 |
| cNEG (op 3) | 72 |
| cNEG (op 5) | 75 |
| operand 1 | 80-82 |
| operand 2 | 83-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010010001...........0.......0................................
.......0.00.0000.......000010000000000000.....................00
```

<a id="v2"></a>
## 2. `UIADD3_UR_UP_UP_UR_I_UR_UP_UP`

Syntax: `UIADD3.X UR, UP, UP, UR, INT_IMM, UR, UP, UP`  
Example: `@UP0 UIADD3.X UR0, UP0, UP0, UR0, 0x0, UR0, UP0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 3 | 24-30 |
| operand 4 | 32-63 |
| operand 5 | 64-70 |
| cINV (op 3) | 72 |
| cINV (op 5) | 75 |
| operand 7 | 76-79 |
| operand 1 | 80-82 |
| operand 2 | 83-85 |
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
000010010001...........0.......0................................
.......0.01................10000000000000.....................00
```

<a id="v3"></a>
## 3. `UIADD3_UR_UP_UR_I_UR`

Syntax: `UIADD3 UR, UP, UR, INT_IMM, UR`  
Example: `@UP0 UIADD3 UR0, UP0, UR0, 0x0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| operand 4 | 64-70 |
| cNEG (op 2) | 72 |
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
000010010001...........0.......0................................
.......0.00.0000....111000010000000000000.....................00
```

<a id="v4"></a>
## 4. `UIADD3_UR_UP_UR_I_UR_UP_UP`

Syntax: `UIADD3.X UR, UP, UR, INT_IMM, UR, UP, UP`  
Example: `@UP0 UIADD3.X UR0, UP0, UR0, 0x0, UR0, UP0, UP0;`

Register access: WRITE UR (1 slots); READ_WRITE UP (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| operand 4 | 64-70 |
| cINV (op 2) | 72 |
| cINV (op 4) | 75 |
| operand 6 | 76-79 |
| cNOT (op 6) | 80 |
| operand 1 | 84-85 |
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
000010010001...........0.......0................................
.......0.01......111.......10000000000000.....................00
```

<a id="v5"></a>
## 5. `UIADD3_UR_UR_I_UR`

Syntax: `UIADD3 UR, UR, INT_IMM, UR`  
Example: `@UP0 UIADD3 UR0, UR0, 0x0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| cNEG (op 1) | 72 |
| cNEG (op 3) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010010001...........0.......0................................
.......0.00.00000111111000010000000000000.....................00
```

<a id="v6"></a>
## 6. `UIADD3_UR_UR_I_UR_UP_UP`

Syntax: `UIADD3.X UR, UR, INT_IMM, UR, UP, UP`  
Example: `@UP0 UIADD3.X UR0, UR0, 0x0, UR0, UP0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UP (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| cINV (op 1) | 72 |
| cINV (op 3) | 75 |
| operand 5 | 76-79 |
| cNOT (op 5) | 80 |
| operand 4 | 87-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010010001...........0.......0................................
.......0.01......111111....10000000000000.....................00
```

<a id="v7"></a>
## 7. `UIADD3_UR_UP_UP_UR_I_UR`

Syntax: `UIADD3.64 UR, UP, UP, UR, INT_IMM, UR`  
Example: `@UP0 UIADD3.64 UR0, UP0, UP0, UR0, 0x0, UR0;`

Register access: WRITE UR (2 slots); READ UR (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 3 | 24-30 |
| operand 4 | 32-63 |
| operand 5 | 64-70 |
| cNEG (op 3) | 72 |
| cNEG (op 5) | 75 |
| operand 1 | 80-82 |
| operand 2 | 83-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010010001...........0.......0................................
.......0.00.0000.......000010000000000000.....................00
```

<a id="v8"></a>
## 8. `UIADD3_UR_UP_UP_UR_I_UR_UP_UP`

Syntax: `UIADD3.64.X UR, UP, UP, UR, INT_IMM, UR, UP, UP`  
Example: `@UP0 UIADD3.64.X UR0, UP0, UP0, UR0, 0x0, UR0, UP0, UP0;`

Register access: WRITE UR (2 slots); READ UR (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 3 | 24-30 |
| operand 4 | 32-63 |
| operand 5 | 64-70 |
| cINV (op 3) | 72 |
| cINV (op 5) | 75 |
| operand 7 | 76-79 |
| operand 1 | 80-82 |
| operand 2 | 83-85 |
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
111010010001...........0.......0................................
.......0.01................10000000000000.....................00
```

<a id="v9"></a>
## 9. `UIADD3_UR_UP_UR_I_UR`

Syntax: `UIADD3.64 UR, UP, UR, INT_IMM, UR`  
Example: `@UP0 UIADD3.64 UR0, UP0, UR0, 0x0, UR0;`

Register access: WRITE UR (2 slots); WRITE UP (1 slots); READ UR (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| operand 4 | 64-70 |
| cNEG (op 2) | 72 |
| cNEG (op 4) | 75 |
| operand 1 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010010001...........0.......0................................
.......0.00.00000111...000010000000000000.....................00
```

<a id="v10"></a>
## 10. `UIADD3_UR_UP_UR_I_UR_UP_UP`

Syntax: `UIADD3.64.X UR, UP, UR, INT_IMM, UR, UP, UP`  
Example: `@UP0 UIADD3.64.X UR0, UP0, UR0, 0x0, UR0, UP0, UP0;`

Register access: WRITE UR (2 slots); READ_WRITE UP (1 slots); READ UR (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| operand 4 | 64-70 |
| cINV (op 2) | 72 |
| cINV (op 4) | 75 |
| operand 6 | 76-79 |
| cNOT (op 6) | 80 |
| operand 1 | 84-85 |
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
111010010001...........0.......0................................
.......0.01......111.......10000000000000.....................00
```

<a id="v11"></a>
## 11. `UIADD3_UR_UR_I_UR`

Syntax: `UIADD3.64 UR, UR, INT_IMM, UR`  
Example: `@UP0 UIADD3.64 UR0, UR0, 0x0, UR0;`

Register access: WRITE UR (2 slots); READ UR (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| cNEG (op 1) | 72 |
| cNEG (op 3) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010010001...........0.......0................................
.......0.00.00000111111000010000000000000.....................00
```

<a id="v12"></a>
## 12. `UIADD3_UR_UR_I_UR_UP_UP`

Syntax: `UIADD3.64.X UR, UR, INT_IMM, UR, UP, UP`  
Example: `@UP0 UIADD3.64.X UR0, UR0, 0x0, UR0, UP0, UP0;`

Register access: WRITE UR (2 slots); READ UR (2 slots); READ UR (2 slots); READ UP (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| cINV (op 1) | 72 |
| cINV (op 3) | 75 |
| operand 5 | 76-79 |
| cNOT (op 5) | 80 |
| operand 4 | 87-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010010001...........0.......0................................
.......0.01......111111....10000000000000.....................00
```

<a id="v13"></a>
## 13. `UIADD3_UR_UP_UP_UR_UR_UR`

Syntax: `UIADD3 UR, UP, UP, UR, UR, UR`  
Example: `@UP0 UIADD3 UR0, UP0, UP0, UR0, UR0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 3 | 24-30 |
| operand 4 | 32-38 |
| cNEG (op 4) | 63 |
| operand 5 | 64-70 |
| cNEG (op 3) | 72 |
| cNEG (op 5) | 75 |
| operand 1 | 80-82 |
| operand 2 | 83-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010010100...........0.......0.......000000000000000000000000.
.......0.00.0000.......000010000000000000.....................00
```

<a id="v14"></a>
## 14. `UIADD3_UR_UP_UP_UR_UR_UR_UP_UP`

Syntax: `UIADD3.X UR, UP, UP, UR, UR, UR, UP, UP`  
Example: `@UP0 UIADD3.X UR0, UP0, UP0, UR0, UR0, UR0, UP0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 3 | 24-30 |
| operand 4 | 32-38 |
| cINV (op 4) | 63 |
| operand 5 | 64-70 |
| cINV (op 3) | 72 |
| cINV (op 5) | 75 |
| operand 7 | 76-79 |
| operand 1 | 80-82 |
| operand 2 | 83-85 |
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
000010010100...........0.......0.......000000000000000000000000.
.......0.01................10000000000000.....................00
```

<a id="v15"></a>
## 15. `UIADD3_UR_UP_UR_UR_UR`

Syntax: `UIADD3 UR, UP, UR, UR, UR`  
Example: `@UP0 UIADD3 UR0, UP0, UR0, UR0, UR0;`

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
| cNEG (op 4) | 75 |
| operand 1 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010010100...........0.......0.......000000000000000000000000.
.......0.00.00000111...000010000000000000.....................00
```

<a id="v16"></a>
## 16. `UIADD3_UR_UP_UR_UR_UR_UP_UP`

Syntax: `UIADD3.X UR, UP, UR, UR, UR, UP, UP`  
Example: `@UP0 UIADD3.X UR0, UP0, UR0, UR0, UR0, UP0, UP0;`

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
| cINV (op 4) | 75 |
| operand 6 | 76-79 |
| cNOT (op 6) | 80 |
| operand 1 | 84-85 |
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
000010010100...........0.......0.......000000000000000000000000.
.......0.01......111.......10000000000000.....................00
```

<a id="v17"></a>
## 17. `UIADD3_UR_UR_UR_UR`

Syntax: `UIADD3 UR, UR, UR, UR`  
Example: `@UP0 UIADD3 UR0, UR0, UR0, UR0;`

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
| cNEG (op 3) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010010100...........0.......0.......000000000000000000000000.
.......0.00.00000111111000010000000000000.....................00
```

<a id="v18"></a>
## 18. `UIADD3_UR_UR_UR_UR_UP_UP`

Syntax: `UIADD3.X UR, UR, UR, UR, UP, UP`  
Example: `@UP0 UIADD3.X UR0, UR0, UR0, UR0, UP0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UP (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| cINV (op 2) | 63 |
| operand 3 | 64-70 |
| cINV (op 1) | 72 |
| cINV (op 3) | 75 |
| operand 5 | 76-79 |
| cNOT (op 5) | 80 |
| operand 4 | 87-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010010100...........0.......0.......000000000000000000000000.
.......0.01......111111....10000000000000.....................00
```

<a id="v19"></a>
## 19. `UIADD3_UR_UP_UP_UR_UR_UR`

Syntax: `UIADD3.64 UR, UP, UP, UR, UR, UR`  
Example: `@UP0 UIADD3.64 UR0, UP0, UP0, UR0, UR0, UR0;`

Register access: WRITE UR (2 slots); READ UR (2 slots); READ UR (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 3 | 24-30 |
| operand 4 | 32-38 |
| cNEG (op 4) | 63 |
| operand 5 | 64-70 |
| cNEG (op 3) | 72 |
| cNEG (op 5) | 75 |
| operand 1 | 80-82 |
| operand 2 | 83-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010010100...........0.......0.......000000000000000000000000.
.......0.00.0000.......000010000000000000.....................00
```

<a id="v20"></a>
## 20. `UIADD3_UR_UP_UP_UR_UR_UR_UP_UP`

Syntax: `UIADD3.64.X UR, UP, UP, UR, UR, UR, UP, UP`  
Example: `@UP0 UIADD3.64.X UR0, UP0, UP0, UR0, UR0, UR0, UP0, UP0;`

Register access: WRITE UR (2 slots); READ UR (2 slots); READ UR (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 3 | 24-30 |
| operand 4 | 32-38 |
| cINV (op 4) | 63 |
| operand 5 | 64-70 |
| cINV (op 3) | 72 |
| cINV (op 5) | 75 |
| operand 7 | 76-79 |
| operand 1 | 80-82 |
| operand 2 | 83-85 |
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
111010010100...........0.......0.......000000000000000000000000.
.......0.01................10000000000000.....................00
```

<a id="v21"></a>
## 21. `UIADD3_UR_UP_UR_UR_UR`

Syntax: `UIADD3.64 UR, UP, UR, UR, UR`  
Example: `@UP0 UIADD3.64 UR0, UP0, UR0, UR0, UR0;`

Register access: WRITE UR (2 slots); WRITE UP (1 slots); READ UR (2 slots); READ UR (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| cNEG (op 3) | 63 |
| operand 4 | 64-70 |
| cNEG (op 2) | 72 |
| cNEG (op 4) | 75 |
| operand 1 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010010100...........0.......0.......000000000000000000000000.
.......0.00.00000111...000010000000000000.....................00
```

<a id="v22"></a>
## 22. `UIADD3_UR_UP_UR_UR_UR_UP_UP`

Syntax: `UIADD3.64.X UR, UP, UR, UR, UR, UP, UP`  
Example: `@UP0 UIADD3.64.X UR0, UP0, UR0, UR0, UR0, UP0, UP0;`

Register access: WRITE UR (2 slots); READ_WRITE UP (1 slots); READ UR (2 slots); READ UR (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| cINV (op 3) | 63 |
| operand 4 | 64-70 |
| cINV (op 2) | 72 |
| cINV (op 4) | 75 |
| operand 6 | 76-79 |
| cNOT (op 6) | 80 |
| operand 1 | 84-85 |
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
111010010100...........0.......0.......000000000000000000000000.
.......0.01......111.......10000000000000.....................00
```

<a id="v23"></a>
## 23. `UIADD3_UR_UR_UR_UR`

Syntax: `UIADD3.64 UR, UR, UR, UR`  
Example: `@UP0 UIADD3.64 UR0, UR0, UR0, UR0;`

Register access: WRITE UR (2 slots); READ UR (2 slots); READ UR (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| cNEG (op 2) | 63 |
| operand 3 | 64-70 |
| cNEG (op 1) | 72 |
| cNEG (op 3) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010010100...........0.......0.......000000000000000000000000.
.......0.00.00000111111000010000000000000.....................00
```

<a id="v24"></a>
## 24. `UIADD3_UR_UR_UR_UR_UP_UP`

Syntax: `UIADD3.64.X UR, UR, UR, UR, UP, UP`  
Example: `@UP0 UIADD3.64.X UR0, UR0, UR0, UR0, UP0, UP0;`

Register access: WRITE UR (2 slots); READ UR (2 slots); READ UR (2 slots); READ UR (2 slots); READ UP (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| cINV (op 2) | 63 |
| operand 3 | 64-70 |
| cINV (op 1) | 72 |
| cINV (op 3) | 75 |
| operand 5 | 76-79 |
| cNOT (op 5) | 80 |
| operand 4 | 87-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010010100...........0.......0.......000000000000000000000000.
.......0.01......111111....10000000000000.....................00
```

