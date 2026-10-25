# PLOP3 (SM89 SASS)

**NVIDIA:** Predicate Logic Operation (Predicate Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Arbitrary 3-input predicate logic (category: Predicate / compare)

Typically emitted for: predicate logic (`and/or/xor/not.pred`); simple combinations are folded into ISETP/FSETP's built-in `.AND/.OR/.XOR` (probe `plop3_folded`), standalone PLOP3 shows up in loop/branch control

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x81c, 0x89c ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2616)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [s2ur_loop](../verify/RESULTS.md#s2ur_loop): `%ctaid.x as a loop bound (warp-uniform)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/PLOP3.html> (machine-derived by fuzzing the assembler; no semantics).

14 encoding variant(s):

- [PLOP3_P_P_P_P_P_I_I](#v1)
- [PLOP3_P_P_P_P_UP_I_I](#v2)
- [PLOP3_P_P_P_c[I][I]_P_I_I](#v3)
- [PLOP3_P_P_P_cx[UR][I]_P_I_I](#v4)
- [PLOP3_P_P_P_c[I][I]_R_I_I](#v5)
- [PLOP3_P_P_P_cx[UR][I]_R_I_I](#v6)
- [PLOP3_P_P_R_c[I][I]_R_I_I](#v7)
- [PLOP3_P_P_R_cx[UR][I]_R_I_I](#v8)
- [PLOP3_P_P_P_UR_P_I_I](#v9)
- [PLOP3_P_P_P_UR_R_I_I](#v10)
- [PLOP3_P_P_R_UR_R_I_I](#v11)
- [PLOP3_P_P_P_R_P_I_I](#v12)
- [PLOP3_P_P_P_R_R_I_I](#v13)
- [PLOP3_P_P_R_R_R_I_I](#v14)

<a id="v1"></a>
## 1. `PLOP3_P_P_P_P_P_I_I`

Syntax: `PLOP3.LUT P, P, P, P, P, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, P0, P0, P0, 0x0, 0x0;`

Register access: READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 5 | 64-66, 72-75, 77 |
| operand 4 | 68-70 |
| cNOT (op 4) | 71 |
| operand 3 | 76, 78-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001110000001............0000000000000000000000000000000000000000
...0.......................00000000000000.....................00
```

<a id="v2"></a>
## 2. `PLOP3_P_P_P_P_UP_I_I`

Syntax: `PLOP3.LUT P, P, P, P, UP, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, P0, P0, UP0, 0x0, 0x0;`

Register access: READ UP (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 5 | 64-66, 72-75, 77 |
| operand 4 | 68-70 |
| cNOT (op 4) | 71 |
| operand 3 | 76, 78-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001110000001............0000000000000000000000000000000000000000
...1.......................00000000000000.....................00
```

<a id="v3"></a>
## 3. `PLOP3_P_P_P_c[I][I]_P_I_I`

Syntax: `PLOP3.LUT P, P, P, c[INT_IMM][INT_IMM], P, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, P0, c[0x0] [0x0].SIGN, P0, 0x0, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 7 | 16-23 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 67-70 |
| cNOT (op 5) | 71 |
| operand 6 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110000101............0000000000000000...................00000
000........................00000000000000.....................00
```

<a id="v4"></a>
## 4. `PLOP3_P_P_P_cx[UR][I]_P_I_I`

Syntax: `PLOP3.LUT P, P, P, cx[UR][INT_IMM], P, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, P0, cx[UR0] [0x0].SIGN, P0, 0x0, 0x0;`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 7 | 16-23 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 5 | 67-70 |
| cNOT (op 5) | 71 |
| operand 6 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110000101............00000000.......0...............000000000
000........................10000000000000.....................00
```

<a id="v5"></a>
## 5. `PLOP3_P_P_P_c[I][I]_R_I_I`

Syntax: `PLOP3.LUT P, P, P, c[INT_IMM][INT_IMM], R, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, P0, c[0x0] [0x0].SIGN, R0.SIGN, 0x0, 0x0;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 7 | 16-23 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 64-71 |
| operand 6 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011110000101............0000000000000000...................00000
...........................00000000000000.....................00
```

<a id="v6"></a>
## 6. `PLOP3_P_P_P_cx[UR][I]_R_I_I`

Syntax: `PLOP3.LUT P, P, P, cx[UR][INT_IMM], R, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, P0, cx[UR0] [0x0].SIGN, R0.SIGN, 0x0, 0x0;`

Register access: READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 7 | 16-23 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 5 | 64-71 |
| operand 6 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011110000101............00000000.......0...............000000000
...........................10000000000000.....................00
```

<a id="v7"></a>
## 7. `PLOP3_P_P_R_c[I][I]_R_I_I`

Syntax: `PLOP3.LUT P, P, R, c[INT_IMM][INT_IMM], R, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, R0.SIGN, c[0x0] [0x0].SIGN, R0.SIGN, 0x0, 0x0;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 7 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 5 | 64-71 |
| operand 6 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111110000101....................00000000...................00000
.......................000000000000000000.....................00
```

<a id="v8"></a>
## 8. `PLOP3_P_P_R_cx[UR][I]_R_I_I`

Syntax: `PLOP3.LUT P, P, R, cx[UR][INT_IMM], R, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, R0.SIGN, cx[UR0] [0x0].SIGN, R0.SIGN, 0x0, 0x0;`

Register access: READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 7 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 5 | 64-71 |
| operand 6 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111110000101...........................0...............000000000
.......................000010000000000000.....................00
```

<a id="v9"></a>
## 9. `PLOP3_P_P_P_UR_P_I_I`

Syntax: `PLOP3.LUT P, P, P, UR, P, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, P0, UR0.SIGN, P0, 0x0, 0x0;`

Register access: READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 3 | 32-38 |
| operand 4 | 67-70 |
| cNOT (op 4) | 71 |
| operand 5 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110000011............00000000.......0000000000000000000000000
000........................10000000000000.....................00
```

<a id="v10"></a>
## 10. `PLOP3_P_P_P_UR_R_I_I`

Syntax: `PLOP3.LUT P, P, P, UR, R, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, P0, UR0.SIGN, R0.SIGN, 0x0, 0x0;`

Register access: READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 3 | 32-38 |
| operand 4 | 64-71 |
| operand 5 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011110000011............00000000.......0000000000000000000000000
...........................10000000000000.....................00
```

<a id="v11"></a>
## 11. `PLOP3_P_P_R_UR_R_I_I`

Syntax: `PLOP3.LUT P, P, R, UR, R, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, R0.SIGN, UR0.SIGN, R0.SIGN, 0x0, 0x0;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 64-71 |
| operand 5 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111110000011...........................0000000000000000000000000
.......................000010000000000000.....................00
```

<a id="v12"></a>
## 12. `PLOP3_P_P_P_R_P_I_I`

Syntax: `PLOP3.LUT P, P, P, R, P, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, P0, R0.SIGN, P0, 0x0, 0x0;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 3 | 32-39 |
| operand 4 | 67-70 |
| cNOT (op 4) | 71 |
| operand 5 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110000100............00000000........000000000000000000000000
000........................00000000000000.....................00
```

<a id="v13"></a>
## 13. `PLOP3_P_P_P_R_R_I_I`

Syntax: `PLOP3.LUT P, P, P, R, R, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, P0, R0.SIGN, R0.SIGN, 0x0, 0x0;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 3 | 32-39 |
| operand 4 | 64-71 |
| operand 5 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011110000100............00000000........000000000000000000000000
...........................00000000000000.....................00
```

<a id="v14"></a>
## 14. `PLOP3_P_P_R_R_R_I_I`

Syntax: `PLOP3.LUT P, P, R, R, R, INT_IMM, INT_IMM`  
Example: `@P0 PLOP3.LUT P0, P0, R0.SIGN, R0.SIGN, R0.SIGN, 0x0, 0x0;`

Register access: READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 64-71 |
| operand 5 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111110000100............................000000000000000000000000
.......................000000000000000000.....................00
```

