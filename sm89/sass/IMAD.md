# IMAD (SM89 SASS)

**NVIDIA:** Integer Multiply And Add (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Integer multiply-add (IMAD.WIDE for 64-bit result; IMAD.MOV/SHL idioms) (category: Integer)

Typically emitted for: `mul.lo`, `mad.lo`, `mul.wide` (IMAD.WIDE), `mul.hi` (IMAD.HI); also `IMAD.MOV.U32` / `IMAD.IADD` as moves/adds that ptxas balances against MOV/IADD3

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x24, 0xa4 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1751)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [imad](../verify/RESULTS.md#imad): `mad.lo.s32`
- [imad_wide](../verify/RESULTS.md#imad_wide): `mul.wide.s32`
- [imad_hi](../verify/RESULTS.md#imad_hi): `mul.hi.u32`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 74 | `@!P0 IMAD.IADD R5, R0, 0x1, R5`<br>`@!P0 IMAD.IADD R5, R5, 0x1, R4`<br>`@!P0 IMAD.MOV.U32 R10, RZ, RZ, -0x40` |
| 81 | `@!P0 IMAD.MOV.U32 R10, RZ, RZ, -0x40`<br>`@P2 IMAD.MOV.U32 R4, RZ, RZ, 0x1`<br>`IMAD.MOV.U32 R3, RZ, RZ, 0x0` |
| 82 | `@!P0 IMAD.MOV.U32 R10, RZ, RZ, -0x40`<br>`@P2 IMAD.MOV.U32 R4, RZ, RZ, 0x1`<br>`IMAD.MOV.U32 R3, RZ, RZ, 0x0` |
| 83 | `@!P0 IMAD.MOV.U32 R10, RZ, RZ, -0x40`<br>`@P2 IMAD.MOV.U32 R4, RZ, RZ, 0x1`<br>`IMAD.MOV.U32 R3, RZ, RZ, 0x0` |

Real encodings whose 12-bit opcode field matches **no** variant on the source page (form missing from the site): `IMAD.HI.U32 R5, R0, R5, RZ`

Encodings: <https://kuterdinel.com/nv_isa_sm89/IMAD.html> (machine-derived by fuzzing the assembler; no semantics).

82 encoding variant(s):

- [IMAD_R_R_R_I](#v1)
- [IMAD_R_R_R_I_P](#v2)
- [IMAD_R_R_R_c[I][I]](#v3)
- [IMAD_R_R_R_c[I][I]_P](#v4)
- [IMAD_R_R_R_cx[UR][I]](#v5)
- [IMAD_R_R_R_cx[UR][I]_P](#v6)
- [IMAD_R_P_R_R_c[I][I]](#v7)
- [IMAD_R_P_R_R_c[I][I]_P](#v8)
- [IMAD_R_P_R_R_cx[UR][I]](#v9)
- [IMAD_R_P_R_R_cx[UR][I]_P](#v10)
- [IMAD_R_R_R_c[I][I]](#v11)
- [IMAD_R_R_R_c[I][I]_P](#v12)
- [IMAD_R_R_R_cx[UR][I]](#v13)
- [IMAD_R_R_R_cx[UR][I]_P](#v14)
- [IMAD_R_P_R_R_c[I][I]](#v15)
- [IMAD_R_P_R_R_c[I][I]_P](#v16)
- [IMAD_R_P_R_R_cx[UR][I]](#v17)
- [IMAD_R_P_R_R_cx[UR][I]_P](#v18)
- [IMAD_R_R_R_c[I][I]](#v19)
- [IMAD_R_R_R_c[I][I]_P](#v20)
- [IMAD_R_R_R_cx[UR][I]](#v21)
- [IMAD_R_R_R_cx[UR][I]_P](#v22)
- [IMAD_R_R_I_R](#v23)
- [IMAD_R_R_I_R_P](#v24)
- [IMAD_R_P_R_I_R](#v25)
- [IMAD_R_P_R_I_R_P](#v26)
- [IMAD_R_R_I_R](#v27)
- [IMAD_R_R_I_R_P](#v28)
- [IMAD_R_P_R_I_R](#v29)
- [IMAD_R_P_R_I_R_P](#v30)
- [IMAD_R_R_I_R](#v31)
- [IMAD_R_R_I_R_P](#v32)
- [IMAD_R_R_c[I][I]_R](#v33)
- [IMAD_R_R_c[I][I]_R_P](#v34)
- [IMAD_R_R_cx[UR][I]_R](#v35)
- [IMAD_R_R_cx[UR][I]_R_P](#v36)
- [IMAD_R_P_R_c[I][I]_R](#v37)
- [IMAD_R_P_R_c[I][I]_R_P](#v38)
- [IMAD_R_P_R_cx[UR][I]_R](#v39)
- [IMAD_R_P_R_cx[UR][I]_R_P](#v40)
- [IMAD_R_R_c[I][I]_R](#v41)
- [IMAD_R_R_c[I][I]_R_P](#v42)
- [IMAD_R_R_cx[UR][I]_R](#v43)
- [IMAD_R_R_cx[UR][I]_R_P](#v44)
- [IMAD_R_P_R_c[I][I]_R](#v45)
- [IMAD_R_P_R_c[I][I]_R_P](#v46)
- [IMAD_R_P_R_cx[UR][I]_R](#v47)
- [IMAD_R_P_R_cx[UR][I]_R_P](#v48)
- [IMAD_R_R_c[I][I]_R](#v49)
- [IMAD_R_R_c[I][I]_R_P](#v50)
- [IMAD_R_R_cx[UR][I]_R](#v51)
- [IMAD_R_R_cx[UR][I]_R_P](#v52)
- [IMAD_R_R_UR_R](#v53)
- [IMAD_R_R_UR_R_P](#v54)
- [IMAD_R_P_R_UR_R](#v55)
- [IMAD_R_P_R_UR_R_P](#v56)
- [IMAD_R_R_UR_R](#v57)
- [IMAD_R_R_UR_R_P](#v58)
- [IMAD_R_P_R_UR_R](#v59)
- [IMAD_R_P_R_UR_R_P](#v60)
- [IMAD_R_R_UR_R](#v61)
- [IMAD_R_R_UR_R_P](#v62)
- [IMAD_R_R_R_UR](#v63)
- [IMAD_R_R_R_UR_P](#v64)
- [IMAD_R_P_R_R_UR](#v65)
- [IMAD_R_P_R_R_UR_P](#v66)
- [IMAD_R_R_R_UR](#v67)
- [IMAD_R_R_R_UR_P](#v68)
- [IMAD_R_P_R_R_UR](#v69)
- [IMAD_R_P_R_R_UR_P](#v70)
- [IMAD_R_R_R_UR](#v71)
- [IMAD_R_R_R_UR_P](#v72)
- [IMAD_R_R_R_R](#v73)
- [IMAD_R_R_R_R_P](#v74)
- [IMAD_R_P_R_R_R](#v75)
- [IMAD_R_P_R_R_R_P](#v76)
- [IMAD_R_R_R_R](#v77)
- [IMAD_R_R_R_R_P](#v78)
- [IMAD_R_P_R_R_R](#v79)
- [IMAD_R_P_R_R_R_P](#v80)
- [IMAD_R_R_R_R](#v81)
- [IMAD_R_R_R_R_P](#v82)

<a id="v1"></a>
## 1. `IMAD_R_R_R_I`

Syntax: `IMAD R, R, R, INT_IMM`  
Example: `@P0 IMAD.U32 R0, R0, R0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-63 |
| operand 2 | 64-71 |
| modi 1 | 73 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000010....................................................
........0.0000000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v2"></a>
## 2. `IMAD_R_R_R_I_P`

Syntax: `IMAD.X R, R, R, INT_IMM, P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-63 |
| operand 2 | 64-71 |
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
001001000010....................................................
........0.100000000000.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v3"></a>
## 3. `IMAD_R_R_R_c[I][I]`

Syntax: `IMAD R, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 IMAD.U32 R0, R0, R0, c[0x0][0x0];`

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
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000110....................00000000...................00000
........0.0000000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v4"></a>
## 4. `IMAD_R_R_R_c[I][I]_P`

Syntax: `IMAD.X R, R, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, c[0x0][0x0], P0;`

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
001001000110....................00000000...................00000
........0.100000000000.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v5"></a>
## 5. `IMAD_R_R_R_cx[UR][I]`

Syntax: `IMAD R, R, R, cx[UR][INT_IMM]`  
Example: `@P0 IMAD.U32 R0, R0, R0, cx[UR0][0x0];`

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
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000110...........................0...............000000000
........0.0000000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v6"></a>
## 6. `IMAD_R_R_R_cx[UR][I]_P`

Syntax: `IMAD.X R, R, R, cx[UR][INT_IMM], P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, cx[UR0][0x0], P0;`

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
001001000110...........................0...............000000000
........0.100000000000.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v7"></a>
## 7. `IMAD_R_P_R_R_c[I][I]`

Syntax: `IMAD.WIDE R, P, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, R0, c[0x0][0x0];`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101001000110....................00000000...................00000
........0.000000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v8"></a>
## 8. `IMAD_R_P_R_R_c[I][I]_P`

Syntax: `IMAD.WIDE.X R, P, R, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, R0, c[0x0][0x0], P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| operand 1 | 80-83 |
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
101001000110....................00000000...................00000
........0.100000....00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v9"></a>
## 9. `IMAD_R_P_R_R_cx[UR][I]`

Syntax: `IMAD.WIDE R, P, R, R, cx[UR][INT_IMM]`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, R0, cx[UR0][0x0];`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-38 |
| operand 5 | 40-54 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101001000110...........................0...............000000000
........0.000000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v10"></a>
## 10. `IMAD_R_P_R_R_cx[UR][I]_P`

Syntax: `IMAD.WIDE.X R, P, R, R, cx[UR][INT_IMM], P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, R0, cx[UR0][0x0], P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-38 |
| operand 5 | 40-54 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| operand 1 | 80-83 |
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
101001000110...........................0...............000000000
........0.100000....00.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v11"></a>
## 11. `IMAD_R_R_R_c[I][I]`

Syntax: `IMAD R, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 IMAD.U32 R0, R0, R0, c[0x0][0x0];`

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
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000110....................00000000...................00000
........0.0000000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v12"></a>
## 12. `IMAD_R_R_R_c[I][I]_P`

Syntax: `IMAD.X R, R, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, c[0x0][0x0], P0;`

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
001001000110....................00000000...................00000
........0.100000011100.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v13"></a>
## 13. `IMAD_R_R_R_cx[UR][I]`

Syntax: `IMAD R, R, R, cx[UR][INT_IMM]`  
Example: `@P0 IMAD.U32 R0, R0, R0, cx[UR0][0x0];`

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
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000110...........................0...............000000000
........0.0000000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v14"></a>
## 14. `IMAD_R_R_R_cx[UR][I]_P`

Syntax: `IMAD.X R, R, R, cx[UR][INT_IMM], P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, cx[UR0][0x0], P0;`

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
001001000110...........................0...............000000000
........0.100000011100.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v15"></a>
## 15. `IMAD_R_P_R_R_c[I][I]`

Syntax: `IMAD.WIDE R, P, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, R0, c[0x0][0x0];`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101001000110....................00000000...................00000
........0.000000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v16"></a>
## 16. `IMAD_R_P_R_R_c[I][I]_P`

Syntax: `IMAD.WIDE.X R, P, R, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, R0, c[0x0][0x0], P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| operand 1 | 80-83 |
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
101001000110....................00000000...................00000
........0.100000....00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v17"></a>
## 17. `IMAD_R_P_R_R_cx[UR][I]`

Syntax: `IMAD.WIDE R, P, R, R, cx[UR][INT_IMM]`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, R0, cx[UR0][0x0];`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-38 |
| operand 5 | 40-54 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101001000110...........................0...............000000000
........0.000000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v18"></a>
## 18. `IMAD_R_P_R_R_cx[UR][I]_P`

Syntax: `IMAD.WIDE.X R, P, R, R, cx[UR][INT_IMM], P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, R0, cx[UR0][0x0], P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-38 |
| operand 5 | 40-54 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| operand 1 | 80-83 |
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
101001000110...........................0...............000000000
........0.100000....00.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v19"></a>
## 19. `IMAD_R_R_R_c[I][I]`

Syntax: `IMAD R, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 IMAD.U32 R0, R0, R0, c[0x0][0x0];`

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
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000110....................00000000...................00000
........0.0000000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v20"></a>
## 20. `IMAD_R_R_R_c[I][I]_P`

Syntax: `IMAD.X R, R, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, c[0x0][0x0], P0;`

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
001001000110....................00000000...................00000
........0.100000011100.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v21"></a>
## 21. `IMAD_R_R_R_cx[UR][I]`

Syntax: `IMAD R, R, R, cx[UR][INT_IMM]`  
Example: `@P0 IMAD.U32 R0, R0, R0, cx[UR0][0x0];`

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
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000110...........................0...............000000000
........0.0000000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v22"></a>
## 22. `IMAD_R_R_R_cx[UR][I]_P`

Syntax: `IMAD.X R, R, R, cx[UR][INT_IMM], P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, cx[UR0][0x0], P0;`

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
001001000110...........................0...............000000000
........0.100000011100.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v23"></a>
## 23. `IMAD_R_R_I_R`

Syntax: `IMAD.MOV R, R, INT_IMM, R`  
Example: `@P0 IMAD.MOV.U32 R0, R0, 0x0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
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
001001000001....................................................
........0.0.00000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v24"></a>
## 24. `IMAD_R_R_I_R_P`

Syntax: `IMAD.X R, R, INT_IMM, R, P`  
Example: `@P0 IMAD.U32.X R0, R0, 0x0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
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
001001000001....................................................
........0.1.0000000000.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v25"></a>
## 25. `IMAD_R_P_R_I_R`

Syntax: `IMAD.WIDE R, P, R, INT_IMM, R`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, 0x0, R0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| operand 4 | 64-71 |
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
101001000001....................................................
........0.0.0000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v26"></a>
## 26. `IMAD_R_P_R_I_R_P`

Syntax: `IMAD.WIDE.X R, P, R, INT_IMM, R, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, 0x0, R0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| operand 4 | 64-71 |
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
101001000001....................................................
........0.1.0000....00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v27"></a>
## 27. `IMAD_R_R_I_R`

Syntax: `IMAD.MOV R, R, INT_IMM, R`  
Example: `@P0 IMAD.MOV.U32 R0, R0, 0x0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
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
001001000001....................................................
........0.0.00000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v28"></a>
## 28. `IMAD_R_R_I_R_P`

Syntax: `IMAD.X R, R, INT_IMM, R, P`  
Example: `@P0 IMAD.U32.X R0, R0, 0x0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
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
001001000001....................................................
........0.1.0000011100.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v29"></a>
## 29. `IMAD_R_P_R_I_R`

Syntax: `IMAD.WIDE R, P, R, INT_IMM, R`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, 0x0, R0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| operand 4 | 64-71 |
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
101001000001....................................................
........0.0.0000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v30"></a>
## 30. `IMAD_R_P_R_I_R_P`

Syntax: `IMAD.WIDE.X R, P, R, INT_IMM, R, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, 0x0, R0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| operand 4 | 64-71 |
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
101001000001....................................................
........0.1.0000....00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v31"></a>
## 31. `IMAD_R_R_I_R`

Syntax: `IMAD.MOV R, R, INT_IMM, R`  
Example: `@P0 IMAD.MOV.U32 R0, R0, 0x0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
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
001001000001....................................................
........0.0.00000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v32"></a>
## 32. `IMAD_R_R_I_R_P`

Syntax: `IMAD.X R, R, INT_IMM, R, P`  
Example: `@P0 IMAD.U32.X R0, R0, 0x0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
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
001001000001....................................................
........0.1.0000011100.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v33"></a>
## 33. `IMAD_R_R_c[I][I]_R`

Syntax: `IMAD R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 IMAD.U32 R0, R0, c[0x0][0x0], R0;`

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
| cNEG (op 4) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000101....................00000000...................00000
........0.0.00000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v34"></a>
## 34. `IMAD_R_R_c[I][I]_R_P`

Syntax: `IMAD.X R, R, c[INT_IMM][INT_IMM], R, P`  
Example: `@P0 IMAD.U32.X R0, R0, c[0x0][0x0], R0, P0;`

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
| cINV (op 4) | 75 |
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
001001000101....................00000000...................00000
........0.1.0000000000.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v35"></a>
## 35. `IMAD_R_R_cx[UR][I]_R`

Syntax: `IMAD R, R, cx[UR][INT_IMM], R`  
Example: `@P0 IMAD.U32 R0, R0, cx[UR0][0x0], R0;`

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
| cNEG (op 4) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000101...........................0...............000000000
........0.0.00000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v36"></a>
## 36. `IMAD_R_R_cx[UR][I]_R_P`

Syntax: `IMAD.X R, R, cx[UR][INT_IMM], R, P`  
Example: `@P0 IMAD.U32.X R0, R0, cx[UR0][0x0], R0, P0;`

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
| cINV (op 4) | 75 |
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
001001000101...........................0...............000000000
........0.1.0000000000.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v37"></a>
## 37. `IMAD_R_P_R_c[I][I]_R`

Syntax: `IMAD.WIDE R, P, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 64-71 |
| modi 1 | 73 |
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
101001000101....................00000000...................00000
........0.0.0000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v38"></a>
## 38. `IMAD_R_P_R_c[I][I]_R_P`

Syntax: `IMAD.WIDE.X R, P, R, c[INT_IMM][INT_IMM], R, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, c[0x0][0x0], R0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 64-71 |
| modi 1 | 73 |
| cINV (op 5) | 75 |
| operand 1 | 80-83 |
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
101001000101....................00000000...................00000
........0.1.0000....00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v39"></a>
## 39. `IMAD_R_P_R_cx[UR][I]_R`

Syntax: `IMAD.WIDE R, P, R, cx[UR][INT_IMM], R`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 5 | 64-71 |
| modi 1 | 73 |
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
101001000101...........................0...............000000000
........0.0.0000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v40"></a>
## 40. `IMAD_R_P_R_cx[UR][I]_R_P`

Syntax: `IMAD.WIDE.X R, P, R, cx[UR][INT_IMM], R, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, cx[UR0][0x0], R0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 5 | 64-71 |
| modi 1 | 73 |
| cINV (op 5) | 75 |
| operand 1 | 80-83 |
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
101001000101...........................0...............000000000
........0.1.0000....00.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v41"></a>
## 41. `IMAD_R_R_c[I][I]_R`

Syntax: `IMAD R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 IMAD.U32 R0, R0, c[0x0][0x0], R0;`

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
| cNEG (op 4) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000101....................00000000...................00000
........0.0.00000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v42"></a>
## 42. `IMAD_R_R_c[I][I]_R_P`

Syntax: `IMAD.X R, R, c[INT_IMM][INT_IMM], R, P`  
Example: `@P0 IMAD.U32.X R0, R0, c[0x0][0x0], R0, P0;`

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
| cINV (op 4) | 75 |
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
001001000101....................00000000...................00000
........0.1.0000011100.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v43"></a>
## 43. `IMAD_R_R_cx[UR][I]_R`

Syntax: `IMAD R, R, cx[UR][INT_IMM], R`  
Example: `@P0 IMAD.U32 R0, R0, cx[UR0][0x0], R0;`

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
| cNEG (op 4) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000101...........................0...............000000000
........0.0.00000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v44"></a>
## 44. `IMAD_R_R_cx[UR][I]_R_P`

Syntax: `IMAD.X R, R, cx[UR][INT_IMM], R, P`  
Example: `@P0 IMAD.U32.X R0, R0, cx[UR0][0x0], R0, P0;`

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
| cINV (op 4) | 75 |
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
001001000101...........................0...............000000000
........0.1.0000011100.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v45"></a>
## 45. `IMAD_R_P_R_c[I][I]_R`

Syntax: `IMAD.WIDE R, P, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 64-71 |
| modi 1 | 73 |
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
101001000101....................00000000...................00000
........0.0.0000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v46"></a>
## 46. `IMAD_R_P_R_c[I][I]_R_P`

Syntax: `IMAD.WIDE.X R, P, R, c[INT_IMM][INT_IMM], R, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, c[0x0][0x0], R0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 64-71 |
| modi 1 | 73 |
| cINV (op 5) | 75 |
| operand 1 | 80-83 |
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
101001000101....................00000000...................00000
........0.1.0000....00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v47"></a>
## 47. `IMAD_R_P_R_cx[UR][I]_R`

Syntax: `IMAD.WIDE R, P, R, cx[UR][INT_IMM], R`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 5 | 64-71 |
| modi 1 | 73 |
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
101001000101...........................0...............000000000
........0.0.0000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v48"></a>
## 48. `IMAD_R_P_R_cx[UR][I]_R_P`

Syntax: `IMAD.WIDE.X R, P, R, cx[UR][INT_IMM], R, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, cx[UR0][0x0], R0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 5 | 64-71 |
| modi 1 | 73 |
| cINV (op 5) | 75 |
| operand 1 | 80-83 |
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
101001000101...........................0...............000000000
........0.1.0000....00.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v49"></a>
## 49. `IMAD_R_R_c[I][I]_R`

Syntax: `IMAD R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 IMAD.U32 R0, R0, c[0x0][0x0], R0;`

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
| cNEG (op 4) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000101....................00000000...................00000
........0.0.00000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v50"></a>
## 50. `IMAD_R_R_c[I][I]_R_P`

Syntax: `IMAD.X R, R, c[INT_IMM][INT_IMM], R, P`  
Example: `@P0 IMAD.U32.X R0, R0, c[0x0][0x0], R0, P0;`

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
| cINV (op 4) | 75 |
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
001001000101....................00000000...................00000
........0.1.0000011100.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v51"></a>
## 51. `IMAD_R_R_cx[UR][I]_R`

Syntax: `IMAD R, R, cx[UR][INT_IMM], R`  
Example: `@P0 IMAD.U32 R0, R0, cx[UR0][0x0], R0;`

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
| cNEG (op 4) | 75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000101...........................0...............000000000
........0.0.00000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v52"></a>
## 52. `IMAD_R_R_cx[UR][I]_R_P`

Syntax: `IMAD.X R, R, cx[UR][INT_IMM], R, P`  
Example: `@P0 IMAD.U32.X R0, R0, cx[UR0][0x0], R0, P0;`

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
| cINV (op 4) | 75 |
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
001001000101...........................0...............000000000
........0.1.0000011100.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v53"></a>
## 53. `IMAD_R_R_UR_R`

Syntax: `IMAD R, R, UR, R`  
Example: `@P0 IMAD.U32 R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
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
001001000011...........................0000000000000000000000000
........0.0.00000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v54"></a>
## 54. `IMAD_R_R_UR_R_P`

Syntax: `IMAD.X R, R, UR, R, P`  
Example: `@P0 IMAD.U32.X R0, R0, UR0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
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
001001000011...........................0000000000000000000000000
........0.1.0000000000.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v55"></a>
## 55. `IMAD_R_P_R_UR_R`

Syntax: `IMAD.WIDE R, P, R, UR, R`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, UR0, R0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ UR (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 64-71 |
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
101001000011...........................0000000000000000000000000
........0.0.0000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v56"></a>
## 56. `IMAD_R_P_R_UR_R_P`

Syntax: `IMAD.WIDE.X R, P, R, UR, R, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, UR0, R0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ UR (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 64-71 |
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
101001000011...........................0000000000000000000000000
........0.1.0000....00.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v57"></a>
## 57. `IMAD_R_R_UR_R`

Syntax: `IMAD R, R, UR, R`  
Example: `@P0 IMAD.U32 R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
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
001001000011...........................0000000000000000000000000
........0.0.00000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v58"></a>
## 58. `IMAD_R_R_UR_R_P`

Syntax: `IMAD.X R, R, UR, R, P`  
Example: `@P0 IMAD.U32.X R0, R0, UR0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
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
001001000011...........................0000000000000000000000000
........0.1.0000011100.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v59"></a>
## 59. `IMAD_R_P_R_UR_R`

Syntax: `IMAD.WIDE R, P, R, UR, R`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, UR0, R0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ UR (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 64-71 |
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
101001000011...........................0000000000000000000000000
........0.0.0000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v60"></a>
## 60. `IMAD_R_P_R_UR_R_P`

Syntax: `IMAD.WIDE.X R, P, R, UR, R, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, UR0, R0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ UR (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 64-71 |
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
101001000011...........................0000000000000000000000000
........0.1.0000....00.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v61"></a>
## 61. `IMAD_R_R_UR_R`

Syntax: `IMAD R, R, UR, R`  
Example: `@P0 IMAD.U32 R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
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
001001000011...........................0000000000000000000000000
........0.0.00000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v62"></a>
## 62. `IMAD_R_R_UR_R_P`

Syntax: `IMAD.X R, R, UR, R, P`  
Example: `@P0 IMAD.U32.X R0, R0, UR0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
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
001001000011...........................0000000000000000000000000
........0.1.0000011100.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v63"></a>
## 63. `IMAD_R_R_R_UR`

Syntax: `IMAD R, R, R, UR`  
Example: `@P0 IMAD.U32 R0, R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| cNEG (op 3) | 63 |
| operand 2 | 64-71 |
| modi 1 | 73 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000111...........................000000000000000000000000.
........0.0000000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v64"></a>
## 64. `IMAD_R_R_R_UR_P`

Syntax: `IMAD.X R, R, R, UR, P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, UR0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| cINV (op 3) | 63 |
| operand 2 | 64-71 |
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
001001000111...........................000000000000000000000000.
........0.100000000000.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v65"></a>
## 65. `IMAD_R_P_R_R_UR`

Syntax: `IMAD.WIDE R, P, R, R, UR`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, R0, UR0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-38 |
| cNEG (op 4) | 63 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101001000111...........................000000000000000000000000.
........0.000000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v66"></a>
## 66. `IMAD_R_P_R_R_UR_P`

Syntax: `IMAD.WIDE.X R, P, R, R, UR, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, R0, UR0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-38 |
| cINV (op 4) | 63 |
| operand 3 | 64-71 |
| modi 1 | 73 |
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
101001000111...........................000000000000000000000000.
........0.100000....00.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v67"></a>
## 67. `IMAD_R_R_R_UR`

Syntax: `IMAD R, R, R, UR`  
Example: `@P0 IMAD.U32 R0, R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| cNEG (op 3) | 63 |
| operand 2 | 64-71 |
| modi 1 | 73 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000111...........................000000000000000000000000.
........0.0000000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v68"></a>
## 68. `IMAD_R_R_R_UR_P`

Syntax: `IMAD.X R, R, R, UR, P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, UR0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| cINV (op 3) | 63 |
| operand 2 | 64-71 |
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
001001000111...........................000000000000000000000000.
........0.100000011100.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v69"></a>
## 69. `IMAD_R_P_R_R_UR`

Syntax: `IMAD.WIDE R, P, R, R, UR`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, R0, UR0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-38 |
| cNEG (op 4) | 63 |
| operand 3 | 64-71 |
| modi 1 | 73 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101001000111...........................000000000000000000000000.
........0.000000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v70"></a>
## 70. `IMAD_R_P_R_R_UR_P`

Syntax: `IMAD.WIDE.X R, P, R, R, UR, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, R0, UR0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-38 |
| cINV (op 4) | 63 |
| operand 3 | 64-71 |
| modi 1 | 73 |
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
101001000111...........................000000000000000000000000.
........0.100000....00.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v71"></a>
## 71. `IMAD_R_R_R_UR`

Syntax: `IMAD R, R, R, UR`  
Example: `@P0 IMAD.U32 R0, R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| cNEG (op 3) | 63 |
| operand 2 | 64-71 |
| modi 1 | 73 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001000111...........................000000000000000000000000.
........0.0000000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v72"></a>
## 72. `IMAD_R_R_R_UR_P`

Syntax: `IMAD.X R, R, R, UR, P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, UR0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| cINV (op 3) | 63 |
| operand 2 | 64-71 |
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
001001000111...........................000000000000000000000000.
........0.100000011100.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v73"></a>
## 73. `IMAD_R_R_R_R`

Syntax: `IMAD R, R, R, R`  
Example: `@P0 IMAD.U32 R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
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
001001000100............................000000000000000000000000
........0.0.00000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v74"></a>
## 74. `IMAD_R_R_R_R_P`

Syntax: `IMAD.X R, R, R, R, P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
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
001001000100............................000000000000000000000000
........0.1.0000000000.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v75"></a>
## 75. `IMAD_R_P_R_R_R`

Syntax: `IMAD.WIDE R, P, R, R, R`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, R0, R0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 64-71 |
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
101001000100............................000000000000000000000000
........0.0.0000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v76"></a>
## 76. `IMAD_R_P_R_R_R_P`

Syntax: `IMAD.WIDE.X R, P, R, R, R, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, R0, R0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 64-71 |
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
101001000100............................000000000000000000000000
........0.1.0000....00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v77"></a>
## 77. `IMAD_R_R_R_R`

Syntax: `IMAD R, R, R, R`  
Example: `@P0 IMAD.U32 R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
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
001001000100............................000000000000000000000000
........0.0.00000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v78"></a>
## 78. `IMAD_R_R_R_R_P`

Syntax: `IMAD.X R, R, R, R, P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
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
001001000100............................000000000000000000000000
........0.1.0000011100.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v79"></a>
## 79. `IMAD_R_P_R_R_R`

Syntax: `IMAD.WIDE R, P, R, R, R`  
Example: `@P0 IMAD.WIDE.U32 R0, P0, R0, R0, R0;`

Register access: WRITE R (2 slots); READ R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 64-71 |
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
101001000100............................000000000000000000000000
........0.0.0000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v80"></a>
## 80. `IMAD_R_P_R_R_R_P`

Syntax: `IMAD.WIDE.X R, P, R, R, R, P`  
Example: `@P0 IMAD.WIDE.U32.X R0, P0, R0, R0, R0, P0;`

Register access: WRITE R (2 slots); READ P (1 slots); READ R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 64-71 |
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
101001000100............................000000000000000000000000
........0.1.0000....00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v81"></a>
## 81. `IMAD_R_R_R_R`

Syntax: `IMAD R, R, R, R`  
Example: `@P0 IMAD.U32 R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
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
001001000100............................000000000000000000000000
........0.0.00000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v82"></a>
## 82. `IMAD_R_R_R_R_P`

Syntax: `IMAD.X R, R, R, R, P`  
Example: `@P0 IMAD.U32.X R0, R0, R0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
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
001001000100............................000000000000000000000000
........0.1.0000011100.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

