# LEA (SM89 SASS)

**NVIDIA:** LOAD Effective Address (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Load effective address: (a << s) + b, with .HI for 64-bit addresses (category: Integer)

Typically emitted for: address arithmetic `base + (idx << k)`; array indexing `p[i]`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x11, 0x91 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1923)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [lea](../verify/RESULTS.md#lea): `shl.b32 + add.s32`
- [lea64](../verify/RESULTS.md#lea64): `pointer + (sign-extended s32 index << 2)`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 74 | `LEA R0, R7, 0xc0800000, 0x17`<br>`LEA R4, P0, R6, R4, 0x2`<br>`LEA R5, R0, R1, 0x2` |
| 80 | `LEA R0, R7, 0xc0800000, 0x17`<br>`LEA R4, P0, R6, R4, 0x2`<br>`LEA R5, R0, R1, 0x2` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/LEA.html> (machine-derived by fuzzing the assembler; no semantics).

44 encoding variant(s):

- [LEA_R_P_R_R_I_I](#v1)
- [LEA_R_P_R_R_I_I_P](#v2)
- [LEA_R_R_R_I_I](#v3)
- [LEA_R_R_R_I_I_P](#v4)
- [LEA_R_P_R_I_I](#v5)
- [LEA_R_P_R_I_I_P](#v6)
- [LEA_R_P_R_I_R_I](#v7)
- [LEA_R_P_R_I_R_I_P](#v8)
- [LEA_R_R_I_I](#v9)
- [LEA_R_R_I_I_P](#v10)
- [LEA_R_R_I_R_I](#v11)
- [LEA_R_R_I_R_I_P](#v12)
- [LEA_R_P_R_c[I][I]_I](#v13)
- [LEA_R_P_R_c[I][I]_I_P](#v14)
- [LEA_R_P_R_c[I][I]_R_I](#v15)
- [LEA_R_P_R_c[I][I]_R_I_P](#v16)
- [LEA_R_P_R_cx[UR][I]_I](#v17)
- [LEA_R_P_R_cx[UR][I]_I_P](#v18)
- [LEA_R_P_R_cx[UR][I]_R_I](#v19)
- [LEA_R_P_R_cx[UR][I]_R_I_P](#v20)
- [LEA_R_R_c[I][I]_I](#v21)
- [LEA_R_R_c[I][I]_I_P](#v22)
- [LEA_R_R_c[I][I]_R_I](#v23)
- [LEA_R_R_c[I][I]_R_I_P](#v24)
- [LEA_R_R_cx[UR][I]_I](#v25)
- [LEA_R_R_cx[UR][I]_I_P](#v26)
- [LEA_R_R_cx[UR][I]_R_I](#v27)
- [LEA_R_R_cx[UR][I]_R_I_P](#v28)
- [LEA_R_P_R_UR_I](#v29)
- [LEA_R_P_R_UR_I_P](#v30)
- [LEA_R_P_R_UR_R_I](#v31)
- [LEA_R_P_R_UR_R_I_P](#v32)
- [LEA_R_R_UR_I](#v33)
- [LEA_R_R_UR_I_P](#v34)
- [LEA_R_R_UR_R_I](#v35)
- [LEA_R_R_UR_R_I_P](#v36)
- [LEA_R_P_R_R_I](#v37)
- [LEA_R_P_R_R_I_P](#v38)
- [LEA_R_P_R_R_R_I](#v39)
- [LEA_R_P_R_R_R_I_P](#v40)
- [LEA_R_R_R_I](#v41)
- [LEA_R_R_R_I_P](#v42)
- [LEA_R_R_R_R_I](#v43)
- [LEA_R_R_R_R_I_P](#v44)

<a id="v1"></a>
## 1. `LEA_R_P_R_R_I_I`

Syntax: `LEA R, P, R, R, INT_IMM, INT_IMM`  
Example: `@P0 LEA.???0 R0, P0, R0, R0, 0x0, 0x0;`

Register access: WRITE R (1 slots); WRITE P (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-63 |
| operand 3 | 64-71 |
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
100010000010....................................................
.........00.........000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `HI.` |

<a id="v2"></a>
## 2. `LEA_R_P_R_R_I_I_P`

Syntax: `LEA.X R, P, R, R, INT_IMM, INT_IMM, P`  
Example: `@P0 LEA.???0.X R0, P0, R0, R0, 0x0, 0x0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-63 |
| operand 3 | 64-71 |
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
100010000010....................................................
.........01.........00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `HI.` |

<a id="v3"></a>
## 3. `LEA_R_R_R_I_I`

Syntax: `LEA R, R, R, INT_IMM, INT_IMM`  
Example: `@P0 LEA.???0 R0, R0, R0, 0x0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-63 |
| operand 2 | 64-71 |
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
100010000010....................................................
.........00......111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `HI.` |

<a id="v4"></a>
## 4. `LEA_R_R_R_I_I_P`

Syntax: `LEA.X R, R, R, INT_IMM, INT_IMM, P`  
Example: `@P0 LEA.???0.X R0, R0, R0, 0x0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-63 |
| operand 2 | 64-71 |
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
100010000010....................................................
.........01......11100.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `HI.` |

<a id="v5"></a>
## 5. `LEA_R_P_R_I_I`

Syntax: `LEA R, P, R, INT_IMM, INT_IMM`  
Example: `@P0 LEA R0, P0, R0, 0x0, 0x0;`

Register access: WRITE R (1 slots); WRITE P (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
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
100010000001....................................................
00000000.00.....0...000000000000000000000.....................00
```

<a id="v6"></a>
## 6. `LEA_R_P_R_I_I_P`

Syntax: `LEA.X R, P, R, INT_IMM, INT_IMM, P`  
Example: `@P0 LEA.X R0, P0, R0, 0x0, 0x0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
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
100010000001....................................................
00000000.01.....0...00.....00000000000000.....................00
```

<a id="v7"></a>
## 7. `LEA_R_P_R_I_R_I`

Syntax: `LEA.HI R, P, R, INT_IMM, R, INT_IMM`  
Example: `@P0 LEA.HI R0, P0, R0, 0x0, R0, 0x0;`

Register access: WRITE R (1 slots); WRITE P (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| operand 4 | 64-71 |
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
100010000001....................................................
.........00.....1...000000000000000000000.....................00
```

<a id="v8"></a>
## 8. `LEA_R_P_R_I_R_I_P`

Syntax: `LEA.HI.X R, P, R, INT_IMM, R, INT_IMM, P`  
Example: `@P0 LEA.HI.X R0, P0, R0, 0x0, R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| operand 4 | 64-71 |
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
100010000001....................................................
.........01.....1...00.....00000000000000.....................00
```

<a id="v9"></a>
## 9. `LEA_R_R_I_I`

Syntax: `LEA R, R, INT_IMM, INT_IMM`  
Example: `@P0 LEA R0, R0, 0x0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
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
100010000001....................................................
00000000.00.....0111000000000000000000000.....................00
```

<a id="v10"></a>
## 10. `LEA_R_R_I_I_P`

Syntax: `LEA.SX32.HI.X R, R, INT_IMM, INT_IMM, P`  
Example: `@P0 LEA.HI.X.SX32 R0, R0, 0x0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
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
100010000001....................................................
00000000.11.....111100.....00000000000000.....................00
```

<a id="v11"></a>
## 11. `LEA_R_R_I_R_I`

Syntax: `LEA.HI R, R, INT_IMM, R, INT_IMM`  
Example: `@P0 LEA.HI R0, R0, 0x0, R0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
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
100010000001....................................................
.........00.....1111000000000000000000000.....................00
```

<a id="v12"></a>
## 12. `LEA_R_R_I_R_I_P`

Syntax: `LEA.HI.X R, R, INT_IMM, R, INT_IMM, P`  
Example: `@P0 LEA.HI.X R0, R0, 0x0, R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
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
100010000001....................................................
.........01.....111100.....00000000000000.....................00
```

<a id="v13"></a>
## 13. `LEA_R_P_R_c[I][I]_I`

Syntax: `LEA R, P, R, c[INT_IMM][INT_IMM], INT_IMM`  
Example: `@P0 LEA R0, P0, R0, c[0x0][0x0], 0x0;`

Register access: WRITE R (1 slots); WRITE P (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
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
100010000101....................00000000...................00000
00000000.00.....0...000000000000000000000.....................00
```

<a id="v14"></a>
## 14. `LEA_R_P_R_c[I][I]_I_P`

Syntax: `LEA.X R, P, R, c[INT_IMM][INT_IMM], INT_IMM, P`  
Example: `@P0 LEA.X R0, P0, R0, c[0x0][0x0], 0x0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
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
100010000101....................00000000...................00000
00000000.01.....0...00.....00000000000000.....................00
```

<a id="v15"></a>
## 15. `LEA_R_P_R_c[I][I]_R_I`

Syntax: `LEA.HI R, P, R, c[INT_IMM][INT_IMM], R, INT_IMM`  
Example: `@P0 LEA.HI R0, P0, R0, c[0x0][0x0], R0, 0x0;`

Register access: WRITE R (1 slots); WRITE P (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 64-71 |
| cNEG (op 2) | 72 |
| operand 6 | 75-79 |
| operand 1 | 81-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010000101....................00000000...................00000
.........00.....1...000000000000000000000.....................00
```

<a id="v16"></a>
## 16. `LEA_R_P_R_c[I][I]_R_I_P`

Syntax: `LEA.HI.X R, P, R, c[INT_IMM][INT_IMM], R, INT_IMM, P`  
Example: `@P0 LEA.HI.X R0, P0, R0, c[0x0][0x0], R0, 0x0, P0;`

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
| operand 6 | 75-79 |
| operand 1 | 81-83 |
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
100010000101....................00000000...................00000
.........01.....1...00.....00000000000000.....................00
```

<a id="v17"></a>
## 17. `LEA_R_P_R_cx[UR][I]_I`

Syntax: `LEA R, P, R, cx[UR][INT_IMM], INT_IMM`  
Example: `@P0 LEA R0, P0, R0, cx[UR0][0x0], 0x0;`

Register access: WRITE R (1 slots); WRITE P (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
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
100010000101...........................0...............000000000
00000000.00.....0...000000010000000000000.....................00
```

<a id="v18"></a>
## 18. `LEA_R_P_R_cx[UR][I]_I_P`

Syntax: `LEA.X R, P, R, cx[UR][INT_IMM], INT_IMM, P`  
Example: `@P0 LEA.X R0, P0, R0, cx[UR0][0x0], 0x0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
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
100010000101...........................0...............000000000
00000000.01.....0...00.....10000000000000.....................00
```

<a id="v19"></a>
## 19. `LEA_R_P_R_cx[UR][I]_R_I`

Syntax: `LEA.HI R, P, R, cx[UR][INT_IMM], R, INT_IMM`  
Example: `@P0 LEA.HI R0, P0, R0, cx[UR0][0x0], R0, 0x0;`

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
| operand 6 | 75-79 |
| operand 1 | 81-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010000101...........................0...............000000000
.........00.....1...000000010000000000000.....................00
```

<a id="v20"></a>
## 20. `LEA_R_P_R_cx[UR][I]_R_I_P`

Syntax: `LEA.HI.X R, P, R, cx[UR][INT_IMM], R, INT_IMM, P`  
Example: `@P0 LEA.HI.X R0, P0, R0, cx[UR0][0x0], R0, 0x0, P0;`

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
| operand 6 | 75-79 |
| operand 1 | 81-83 |
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
100010000101...........................0...............000000000
.........01.....1...00.....10000000000000.....................00
```

<a id="v21"></a>
## 21. `LEA_R_R_c[I][I]_I`

Syntax: `LEA.HI.SX32 R, R, c[INT_IMM][INT_IMM], INT_IMM`  
Example: `@P0 LEA.HI.SX32 R0, R0, c[0x0][0x0], 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
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
100010000101....................00000000...................00000
00000000.10.....1111000000000000000000000.....................00
```

<a id="v22"></a>
## 22. `LEA_R_R_c[I][I]_I_P`

Syntax: `LEA.SX32.HI.X R, R, c[INT_IMM][INT_IMM], INT_IMM, P`  
Example: `@P0 LEA.HI.X.SX32 R0, R0, c[0x0][0x0], 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
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
100010000101....................00000000...................00000
00000000.11.....111100.....00000000000000.....................00
```

<a id="v23"></a>
## 23. `LEA_R_R_c[I][I]_R_I`

Syntax: `LEA.HI R, R, c[INT_IMM][INT_IMM], R, INT_IMM`  
Example: `@P0 LEA.HI R0, R0, c[0x0][0x0], R0, 0x0;`

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
| operand 5 | 75-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010000101....................00000000...................00000
.........00.....1111000000000000000000000.....................00
```

<a id="v24"></a>
## 24. `LEA_R_R_c[I][I]_R_I_P`

Syntax: `LEA.HI.X R, R, c[INT_IMM][INT_IMM], R, INT_IMM, P`  
Example: `@P0 LEA.HI.X R0, R0, c[0x0][0x0], R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| cINV (op 1) | 72 |
| operand 5 | 75-79 |
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
100010000101....................00000000...................00000
.........01.....111100.....00000000000000.....................00
```

<a id="v25"></a>
## 25. `LEA_R_R_cx[UR][I]_I`

Syntax: `LEA R, R, cx[UR][INT_IMM], INT_IMM`  
Example: `@P0 LEA R0, R0, cx[UR0][0x0], 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
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
100010000101...........................0...............000000000
00000000.00.....0111000000010000000000000.....................00
```

<a id="v26"></a>
## 26. `LEA_R_R_cx[UR][I]_I_P`

Syntax: `LEA.X R, R, cx[UR][INT_IMM], INT_IMM, P`  
Example: `@P0 LEA.X R0, R0, cx[UR0][0x0], 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
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
100010000101...........................0...............000000000
00000000.01.....011100.....10000000000000.....................00
```

<a id="v27"></a>
## 27. `LEA_R_R_cx[UR][I]_R_I`

Syntax: `LEA.HI R, R, cx[UR][INT_IMM], R, INT_IMM`  
Example: `@P0 LEA.HI R0, R0, cx[UR0][0x0], R0, 0x0;`

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
| operand 5 | 75-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010000101...........................0...............000000000
.........00.....1111000000010000000000000.....................00
```

<a id="v28"></a>
## 28. `LEA_R_R_cx[UR][I]_R_I_P`

Syntax: `LEA.HI.X R, R, cx[UR][INT_IMM], R, INT_IMM, P`  
Example: `@P0 LEA.HI.X R0, R0, cx[UR0][0x0], R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| cINV (op 1) | 72 |
| operand 5 | 75-79 |
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
100010000101...........................0...............000000000
.........01.....111100.....10000000000000.....................00
```

<a id="v29"></a>
## 29. `LEA_R_P_R_UR_I`

Syntax: `LEA R, P, R, UR, INT_IMM`  
Example: `@P0 LEA R0, P0, R0, UR0, 0x0;`

Register access: WRITE R (1 slots); WRITE P (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
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
100010000011...........................000000000000000000000000.
00000000.00.....0...000000010000000000000.....................00
```

<a id="v30"></a>
## 30. `LEA_R_P_R_UR_I_P`

Syntax: `LEA.X R, P, R, UR, INT_IMM, P`  
Example: `@P0 LEA.X R0, P0, R0, UR0, 0x0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
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
100010000011...........................000000000000000000000000.
00000000.01.....0...00.....10000000000000.....................00
```

<a id="v31"></a>
## 31. `LEA_R_P_R_UR_R_I`

Syntax: `LEA.HI R, P, R, UR, R, INT_IMM`  
Example: `@P0 LEA.HI R0, P0, R0, UR0, R0, 0x0;`

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
100010000011...........................000000000000000000000000.
.........00.....1...000000010000000000000.....................00
```

<a id="v32"></a>
## 32. `LEA_R_P_R_UR_R_I_P`

Syntax: `LEA.HI.X R, P, R, UR, R, INT_IMM, P`  
Example: `@P0 LEA.HI.X R0, P0, R0, UR0, R0, 0x0, P0;`

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
100010000011...........................000000000000000000000000.
.........01.....1...00.....10000000000000.....................00
```

<a id="v33"></a>
## 33. `LEA_R_R_UR_I`

Syntax: `LEA R, R, UR, INT_IMM`  
Example: `@P0 LEA R0, R0, UR0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
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
100010000011...........................000000000000000000000000.
00000000.00.....0111000000010000000000000.....................00
```

<a id="v34"></a>
## 34. `LEA_R_R_UR_I_P`

Syntax: `LEA.X R, R, UR, INT_IMM, P`  
Example: `@P0 LEA.X R0, R0, UR0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
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
100010000011...........................000000000000000000000000.
00000000.01.....011100.....10000000000000.....................00
```

<a id="v35"></a>
## 35. `LEA_R_R_UR_R_I`

Syntax: `LEA.HI R, R, UR, R, INT_IMM`  
Example: `@P0 LEA.HI R0, R0, UR0, R0, 0x0;`

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
| operand 4 | 75-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010000011...........................000000000000000000000000.
.........00.....1111000000010000000000000.....................00
```

<a id="v36"></a>
## 36. `LEA_R_R_UR_R_I_P`

Syntax: `LEA.HI.X R, R, UR, R, INT_IMM, P`  
Example: `@P0 LEA.HI.X R0, R0, UR0, R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| cINV (op 2) | 63 |
| operand 3 | 64-71 |
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
100010000011...........................000000000000000000000000.
.........01.....111100.....10000000000000.....................00
```

<a id="v37"></a>
## 37. `LEA_R_P_R_R_I`

Syntax: `LEA R, P, R, R, INT_IMM`  
Example: `@P0 LEA R0, P0, R0, R0, 0x0;`

Register access: WRITE R (1 slots); WRITE P (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
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
100010000100............................00000000000000000000000.
00000000.00.....0...000000000000000000000.....................00
```

<a id="v38"></a>
## 38. `LEA_R_P_R_R_I_P`

Syntax: `LEA.X R, P, R, R, INT_IMM, P`  
Example: `@P0 LEA.X R0, P0, R0, R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ_WRITE P (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
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
100010000100............................00000000000000000000000.
00000000.01.....0...00.....00000000000000.....................00
```

<a id="v39"></a>
## 39. `LEA_R_P_R_R_R_I`

Syntax: `LEA.HI R, P, R, R, R, INT_IMM`  
Example: `@P0 LEA.HI R0, P0, R0, R0, R0, 0x0;`

Register access: WRITE R (1 slots); WRITE P (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| cNEG (op 3) | 63 |
| operand 4 | 64-71 |
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
100010000100............................00000000000000000000000.
.........00.....1...000000000000000000000.....................00
```

<a id="v40"></a>
## 40. `LEA_R_P_R_R_R_I_P`

Syntax: `LEA.HI.X R, P, R, R, R, INT_IMM, P`  
Example: `@P0 LEA.HI.X R0, P0, R0, R0, R0, 0x0, P0;`

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
100010000100............................00000000000000000000000.
.........01.....1...00.....00000000000000.....................00
```

<a id="v41"></a>
## 41. `LEA_R_R_R_I`

Syntax: `LEA R, R, R, INT_IMM`  
Example: `@P0 LEA R0, R0, R0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
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
100010000100............................00000000000000000000000.
00000000.00.....0111000000000000000000000.....................00
```

<a id="v42"></a>
## 42. `LEA_R_R_R_I_P`

Syntax: `LEA.SX32.HI.X R, R, R, INT_IMM, P`  
Example: `@P0 LEA.HI.X.SX32 R0, R0, R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
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
100010000100............................00000000000000000000000.
00000000.11.....111100.....00000000000000.....................00
```

<a id="v43"></a>
## 43. `LEA_R_R_R_R_I`

Syntax: `LEA.HI R, R, R, R, INT_IMM`  
Example: `@P0 LEA.HI R0, R0, R0, R0, 0x0;`

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
| operand 4 | 75-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100010000100............................00000000000000000000000.
.........00.....1111000000000000000000000.....................00
```

<a id="v44"></a>
## 44. `LEA_R_R_R_R_I_P`

Syntax: `LEA.HI.X R, R, R, R, INT_IMM, P`  
Example: `@P0 LEA.HI.X R0, R0, R0, R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cINV (op 2) | 63 |
| operand 3 | 64-71 |
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
100010000100............................00000000000000000000000.
.........01.....111100.....00000000000000.....................00
```

