# IADD3 (SM89 SASS)

**NVIDIA:** 3-input Integer Addition (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: 3-input 32-bit integer add (carry in/out via predicates) (category: Integer)

Typically emitted for: `add/sub.s32/u32`, `add.cc`/`addc` chains, 64-bit `add.s64` (pair of IADD3 with carry)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x10, 0x90 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1595)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [iadd](../verify/RESULTS.md#iadd): `add.s32 / sub.s32`
- [iadd64](../verify/RESULTS.md#iadd64): `add.s64`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 74 | `@!P1 IADD3 R10, R10, 0x40, RZ`<br>`@!P1 IADD3 R4, R4, 0x2, RZ`<br>`@!P1 IADD3 R5, R0, R5, R0` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/IADD3.html> (machine-derived by fuzzing the assembler; no semantics).

30 encoding variant(s):

- [IADD3_R_P_P_R_I_R](#v1)
- [IADD3_R_P_P_R_I_R_P_P](#v2)
- [IADD3_R_P_R_I_R](#v3)
- [IADD3_R_P_R_I_R_P_P](#v4)
- [IADD3_R_R_I_R](#v5)
- [IADD3_R_R_I_R_P_P](#v6)
- [IADD3_R_P_P_R_c[I][I]_R](#v7)
- [IADD3_R_P_P_R_c[I][I]_R_P_P](#v8)
- [IADD3_R_P_P_R_cx[UR][I]_R](#v9)
- [IADD3_R_P_P_R_cx[UR][I]_R_P_P](#v10)
- [IADD3_R_P_R_c[I][I]_R](#v11)
- [IADD3_R_P_R_c[I][I]_R_P_P](#v12)
- [IADD3_R_P_R_cx[UR][I]_R](#v13)
- [IADD3_R_P_R_cx[UR][I]_R_P_P](#v14)
- [IADD3_R_R_c[I][I]_R](#v15)
- [IADD3_R_R_c[I][I]_R_P_P](#v16)
- [IADD3_R_R_cx[UR][I]_R](#v17)
- [IADD3_R_R_cx[UR][I]_R_P_P](#v18)
- [IADD3_R_P_P_R_UR_R](#v19)
- [IADD3_R_P_P_R_UR_R_P_P](#v20)
- [IADD3_R_P_R_UR_R](#v21)
- [IADD3_R_P_R_UR_R_P_P](#v22)
- [IADD3_R_R_UR_R](#v23)
- [IADD3_R_R_UR_R_P_P](#v24)
- [IADD3_R_P_P_R_R_R](#v25)
- [IADD3_R_P_P_R_R_R_P_P](#v26)
- [IADD3_R_P_R_R_R](#v27)
- [IADD3_R_P_R_R_R_P_P](#v28)
- [IADD3_R_R_R_R](#v29)
- [IADD3_R_R_R_R_P_P](#v30)

<a id="v1"></a>
## 1. `IADD3_R_P_P_R_I_R`

Syntax: `IADD3 R, P, P, R, INT_IMM, R`  
Example: `@P0 IADD3 R0, P0, P0, R0, 0x0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-63 |
| operand 5 | 64-71 |
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
000010000001....................................................
.........00.0000.......000000000000000000.....................00
```

<a id="v2"></a>
## 2. `IADD3_R_P_P_R_I_R_P_P`

Syntax: `IADD3.X R, P, P, R, INT_IMM, R, P, P`  
Example: `@P0 IADD3.X R0, P0, P0, R0, 0x0, R0, P0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-63 |
| operand 5 | 64-71 |
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
000010000001....................................................
.........01................00000000000000.....................00
```

<a id="v3"></a>
## 3. `IADD3_R_P_R_I_R`

Syntax: `IADD3 R, P, R, INT_IMM, R`  
Example: `@P0 IADD3 R0, P0, R0, 0x0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| operand 4 | 64-71 |
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
000010000001....................................................
.........00.0000....111000000000000000000.....................00
```

<a id="v4"></a>
## 4. `IADD3_R_P_R_I_R_P_P`

Syntax: `IADD3.X R, P, R, INT_IMM, R, P, P`  
Example: `@P0 IADD3.X R0, P0, R0, 0x0, R0, P0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| operand 4 | 64-71 |
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
000010000001....................................................
.........01......111.......00000000000000.....................00
```

<a id="v5"></a>
## 5. `IADD3_R_R_I_R`

Syntax: `IADD3 R, R, INT_IMM, R`  
Example: `@P0 IADD3 R0, R0, 0x0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
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
000010000001....................................................
.........00.00000111111000000000000000000.....................00
```

<a id="v6"></a>
## 6. `IADD3_R_R_I_R_P_P`

Syntax: `IADD3.X R, R, INT_IMM, R, P, P`  
Example: `@P0 IADD3.X R0, R0, 0x0, R0, P0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
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
000010000001....................................................
.........01......111111....00000000000000.....................00
```

<a id="v7"></a>
## 7. `IADD3_R_P_P_R_c[I][I]_R`

Syntax: `IADD3 R, P, P, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 IADD3 R0, P0, P0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 6 | 64-71 |
| cNEG (op 3) | 72 |
| cNEG (op 6) | 75 |
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
000010000101....................00000000...................00000
.........00.0000.......000000000000000000.....................00
```

<a id="v8"></a>
## 8. `IADD3_R_P_P_R_c[I][I]_R_P_P`

Syntax: `IADD3.X R, P, P, R, c[INT_IMM][INT_IMM], R, P, P`  
Example: `@P0 IADD3.X R0, P0, P0, R0, c[0x0][0x0], R0, P0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 6 | 64-71 |
| cINV (op 3) | 72 |
| cINV (op 6) | 75 |
| operand 8 | 76-79 |
| operand 1 | 80-82 |
| operand 2 | 83-85 |
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
000010000101....................00000000...................00000
.........01................00000000000000.....................00
```

<a id="v9"></a>
## 9. `IADD3_R_P_P_R_cx[UR][I]_R`

Syntax: `IADD3 R, P, P, R, cx[UR][INT_IMM], R`  
Example: `@P0 IADD3 R0, P0, P0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-38 |
| operand 5 | 40-54 |
| operand 6 | 64-71 |
| cNEG (op 3) | 72 |
| cNEG (op 6) | 75 |
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
000010000101...........................0...............000000000
.........00.0000.......000010000000000000.....................00
```

<a id="v10"></a>
## 10. `IADD3_R_P_P_R_cx[UR][I]_R_P_P`

Syntax: `IADD3.X R, P, P, R, cx[UR][INT_IMM], R, P, P`  
Example: `@P0 IADD3.X R0, P0, P0, R0, cx[UR0][0x0], R0, P0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-38 |
| operand 5 | 40-54 |
| operand 6 | 64-71 |
| cINV (op 3) | 72 |
| cINV (op 6) | 75 |
| operand 8 | 76-79 |
| operand 1 | 80-82 |
| operand 2 | 83-85 |
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
000010000101...........................0...............000000000
.........01................10000000000000.....................00
```

<a id="v11"></a>
## 11. `IADD3_R_P_R_c[I][I]_R`

Syntax: `IADD3 R, P, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 IADD3 R0, P0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 64-71 |
| cNEG (op 2) | 72 |
| cNEG (op 5) | 75 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010000101....................00000000...................00000
.........00.0000....111000000000000000000.....................00
```

<a id="v12"></a>
## 12. `IADD3_R_P_R_c[I][I]_R_P_P`

Syntax: `IADD3.X R, P, R, c[INT_IMM][INT_IMM], R, P, P`  
Example: `@P0 IADD3.X R0, P0, R0, c[0x0][0x0], R0, P0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 64-71 |
| cINV (op 2) | 72 |
| cINV (op 5) | 75 |
| operand 7 | 76-79 |
| cNOT (op 7) | 80 |
| operand 1 | 84-85 |
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
000010000101....................00000000...................00000
.........01......111.......00000000000000.....................00
```

<a id="v13"></a>
## 13. `IADD3_R_P_R_cx[UR][I]_R`

Syntax: `IADD3 R, P, R, cx[UR][INT_IMM], R`  
Example: `@P0 IADD3 R0, P0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); WRITE P (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 5 | 64-71 |
| cNEG (op 2) | 72 |
| cNEG (op 5) | 75 |
| operand 1 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010000101...........................0...............000000000
.........00.00000111...000010000000000000.....................00
```

<a id="v14"></a>
## 14. `IADD3_R_P_R_cx[UR][I]_R_P_P`

Syntax: `IADD3.X R, P, R, cx[UR][INT_IMM], R, P, P`  
Example: `@P0 IADD3.X R0, P0, R0, cx[UR0][0x0], R0, P0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 5 | 64-71 |
| cINV (op 2) | 72 |
| cINV (op 5) | 75 |
| operand 7 | 76-79 |
| cNOT (op 7) | 80 |
| operand 1 | 84-85 |
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
000010000101...........................0...............000000000
.........01......111.......10000000000000.....................00
```

<a id="v15"></a>
## 15. `IADD3_R_R_c[I][I]_R`

Syntax: `IADD3 R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 IADD3 R0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| cNEG (op 1) | 72 |
| cNEG (op 4) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010000101....................00000000...................00000
.........00.00000111111000000000000000000.....................00
```

<a id="v16"></a>
## 16. `IADD3_R_R_c[I][I]_R_P_P`

Syntax: `IADD3.X R, R, c[INT_IMM][INT_IMM], R, P, P`  
Example: `@P0 IADD3.X R0, R0, c[0x0][0x0], R0, P0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| cINV (op 1) | 72 |
| cINV (op 4) | 75 |
| operand 6 | 76-79 |
| cNOT (op 6) | 80 |
| operand 5 | 87-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010000101....................00000000...................00000
.........01......111111....00000000000000.....................00
```

<a id="v17"></a>
## 17. `IADD3_R_R_cx[UR][I]_R`

Syntax: `IADD3 R, R, cx[UR][INT_IMM], R`  
Example: `@P0 IADD3 R0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| cNEG (op 1) | 72 |
| cNEG (op 4) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010000101...........................0...............000000000
.........00.00000111111000010000000000000.....................00
```

<a id="v18"></a>
## 18. `IADD3_R_R_cx[UR][I]_R_P_P`

Syntax: `IADD3.X R, R, cx[UR][INT_IMM], R, P, P`  
Example: `@P0 IADD3.X R0, R0, cx[UR0][0x0], R0, P0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots); READ P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| cINV (op 1) | 72 |
| cINV (op 4) | 75 |
| operand 6 | 76-79 |
| cNOT (op 6) | 80 |
| operand 5 | 87-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010000101...........................0...............000000000
.........01......111111....10000000000000.....................00
```

<a id="v19"></a>
## 19. `IADD3_R_P_P_R_UR_R`

Syntax: `IADD3 R, P, P, R, UR, R`  
Example: `@P0 IADD3 R0, P0, P0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-38 |
| cNEG (op 4) | 63 |
| operand 5 | 64-71 |
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
000010000011...........................000000000000000000000000.
.........00.0000.......000010000000000000.....................00
```

<a id="v20"></a>
## 20. `IADD3_R_P_P_R_UR_R_P_P`

Syntax: `IADD3.X R, P, P, R, UR, R, P, P`  
Example: `@P0 IADD3.X R0, P0, P0, R0, UR0, R0, P0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-38 |
| cINV (op 4) | 63 |
| operand 5 | 64-71 |
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
000010000011...........................000000000000000000000000.
.........01................10000000000000.....................00
```

<a id="v21"></a>
## 21. `IADD3_R_P_R_UR_R`

Syntax: `IADD3 R, P, R, UR, R`  
Example: `@P0 IADD3 R0, P0, R0, UR0, R0;`

Register access: WRITE R (1 slots); WRITE P (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| cNEG (op 3) | 63 |
| operand 4 | 64-71 |
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
000010000011...........................000000000000000000000000.
.........00.00000111...000010000000000000.....................00
```

<a id="v22"></a>
## 22. `IADD3_R_P_R_UR_R_P_P`

Syntax: `IADD3.X R, P, R, UR, R, P, P`  
Example: `@P0 IADD3.X R0, P0, R0, UR0, R0, P0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| cINV (op 3) | 63 |
| operand 4 | 64-71 |
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
000010000011...........................000000000000000000000000.
.........01......111.......10000000000000.....................00
```

<a id="v23"></a>
## 23. `IADD3_R_R_UR_R`

Syntax: `IADD3 R, R, UR, R`  
Example: `@P0 IADD3 R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
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
000010000011...........................000000000000000000000000.
.........00.00000111111000010000000000000.....................00
```

<a id="v24"></a>
## 24. `IADD3_R_R_UR_R_P_P`

Syntax: `IADD3.X R, R, UR, R, P, P`  
Example: `@P0 IADD3.X R0, R0, UR0, R0, P0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots); READ P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| cINV (op 2) | 63 |
| operand 3 | 64-71 |
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
000010000011...........................000000000000000000000000.
.........01......111111....10000000000000.....................00
```

<a id="v25"></a>
## 25. `IADD3_R_P_P_R_R_R`

Syntax: `IADD3 R, P, P, R, R, R`  
Example: `@P0 IADD3 R0, P0, P0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| cNEG (op 4) | 63 |
| operand 5 | 64-71 |
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
000010000100............................00000000000000000000000.
.........00.0000.......000000000000000000.....................00
```

<a id="v26"></a>
## 26. `IADD3_R_P_P_R_R_R_P_P`

Syntax: `IADD3.X R, P, P, R, R, R, P, P`  
Example: `@P0 IADD3.X R0, P0, P0, R0, R0, R0, P0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| cINV (op 4) | 63 |
| operand 5 | 64-71 |
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
000010000100............................00000000000000000000000.
.........01................00000000000000.....................00
```

<a id="v27"></a>
## 27. `IADD3_R_P_R_R_R`

Syntax: `IADD3 R, P, R, R, R`  
Example: `@P0 IADD3 R0, P0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| cNEG (op 3) | 63 |
| operand 4 | 64-71 |
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
000010000100............................00000000000000000000000.
.........00.0000....111000000000000000000.....................00
```

<a id="v28"></a>
## 28. `IADD3_R_P_R_R_R_P_P`

Syntax: `IADD3.X R, P, R, R, R, P, P`  
Example: `@P0 IADD3.X R0, P0, R0, R0, R0, P0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| cINV (op 3) | 63 |
| operand 4 | 64-71 |
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
000010000100............................00000000000000000000000.
.........01......111.......00000000000000.....................00
```

<a id="v29"></a>
## 29. `IADD3_R_R_R_R`

Syntax: `IADD3 R, R, R, R`  
Example: `@P0 IADD3 R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
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
000010000100............................00000000000000000000000.
.........00.00000111111000000000000000000.....................00
```

<a id="v30"></a>
## 30. `IADD3_R_R_R_R_P_P`

Syntax: `IADD3.X R, R, R, R, P, P`  
Example: `@P0 IADD3.X R0, R0, R0, R0, P0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots); READ P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cINV (op 2) | 63 |
| operand 3 | 64-71 |
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
000010000100............................00000000000000000000000.
.........01......111111....00000000000000.....................00
```

