# CALL (SM89 SASS)

**NVIDIA:** Call Function (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Call subroutine (category: Control flow)

Typically emitted for: `call` (non-inlined device functions, printf, slow-path div/sqrt)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [fdiv_rn](../verify/RESULTS.md#fdiv_rn): `div.rn.f32 (IEEE division)`
- [call](../verify/RESULTS.md#call): `.func .noinline call`

Encodings: <https://kuterdinel.com/nv_isa_sm89/CALL.html> (machine-derived by fuzzing the assembler; no semantics).

16 encoding variant(s):

- [CALL_I](#v1)
- [CALL_P_I](#v2)
- [CALL_P_UR](#v3)
- [CALL_P_UR_I](#v4)
- [CALL_UR](#v5)
- [CALL_UR_I](#v6)
- [CALL_I](#v7)
- [CALL_P_I](#v8)
- [CALL_P_UR_I](#v9)
- [CALL_UR_I](#v10)
- [CALL_P_c[I][I]](#v11)
- [CALL_c[I][I]](#v12)
- [CALL_P_R](#v13)
- [CALL_P_R_I](#v14)
- [CALL_R](#v15)
- [CALL_R_I](#v16)

<a id="v1"></a>
## 1. `CALL_I`

Syntax: `CALL.ABS INT_IMM`  
Example: `@P0 CALL.ABS 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 33-80 |
| NOINC | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101001....00000000000000000...............................
.................00000.111000000000000000.....111111..........00
```

<a id="v2"></a>
## 2. `CALL_P_I`

Syntax: `CALL.ABS P, INT_IMM`  
Example: `@P0 CALL.ABS P0, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 33-80 |
| NOINC | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101001....00000000000000000...............................
.................00000.....00000000000000.....111111..........00
```

<a id="v3"></a>
## 3. `CALL_P_UR`

Syntax: `CALL.ABS P, UR`  
Example: `@P0 CALL.ABS P0, UR0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
| NOINC | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101001....00000000.......000000000000000000000000000000000
0000000000000000000000.....10000000000000.....111111..........00
```

<a id="v4"></a>
## 4. `CALL_P_UR_I`

Syntax: `CALL.ABS P, UR, INT_IMM`  
Example: `@P0 CALL.ABS P0, UR0 0x4;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
| operand 2 | 34-81 |
| NOINC | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101001....00000000.......000..............................
..................0000.....10000000000000.....111111..........00
```

<a id="v5"></a>
## 5. `CALL_UR`

Syntax: `CALL.ABS UR`  
Example: `@P0 CALL.ABS UR0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-30 |
| NOINC | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101001....00000000.......000000000000000000000000000000000
0000000000000000000000.111010000000000000.....111111..........00
```

<a id="v6"></a>
## 6. `CALL_UR_I`

Syntax: `CALL.ABS UR, INT_IMM`  
Example: `@P0 CALL.ABS UR0 0x20;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-30 |
| operand 1 | 33-81 |
| NOINC | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101001....00000000.......00...............................
..................0000.111010000000000000.....111111..........00
```

<a id="v7"></a>
## 7. `CALL_I`

Syntax: `CALL.REL INT_IMM`  
Example: `@P0 CALL.REL 0x10;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 33-81 |
| NOINC | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000101001....00000000000000000...............................
..................0000.111000000000000000.....111111..........00
```

<a id="v8"></a>
## 8. `CALL_P_I`

Syntax: `CALL.REL P, INT_IMM`  
Example: `@P0 CALL.REL P0, 0x10;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 33-81 |
| NOINC | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000101001....00000000000000000...............................
..................0000.....00000000000000.....111111..........00
```

<a id="v9"></a>
## 9. `CALL_P_UR_I`

Syntax: `CALL.REL P, UR, INT_IMM`  
Example: `@P0 CALL.REL P0, UR0 0x10;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
| operand 2 | 33-81 |
| NOINC | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000101001....00000000.......00...............................
..................0000.....10000000000000.....111111..........00
```

<a id="v10"></a>
## 10. `CALL_UR_I`

Syntax: `CALL.REL UR, INT_IMM`  
Example: `@P0 CALL.REL UR0 0x10;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-30 |
| operand 1 | 33-81 |
| NOINC | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000101001....00000000.......00...............................
..................0000.111010000000000000.....111111..........00
```

<a id="v11"></a>
## 11. `CALL_P_c[I][I]`

Syntax: `CALL.ABS P, c[INT_IMM][INT_IMM]`  
Example: `@P0 CALL.ABS P0, c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| NOINC | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101101....000000000000000000000000...................00000
0000000000000000000000.....00000000000000.....111111..........00
```

<a id="v12"></a>
## 12. `CALL_c[I][I]`

Syntax: `CALL.ABS c[INT_IMM][INT_IMM]`  
Example: `@P0 CALL.ABS c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 40-52, 54 |
| operand 0 | 53, 55-58 |
| NOINC | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101101....000000000000000000000000...................00000
0000000000000000000000.111000000000000000.....111111..........00
```

<a id="v13"></a>
## 13. `CALL_P_R`

Syntax: `CALL.ABS P, R`  
Example: `@P0 CALL.ABS P0, R0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| NOINC | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101100....00000000........00000000000000000000000000000000
0000000000000000000000.....00000000000000.....111111..........00
```

<a id="v14"></a>
## 14. `CALL_P_R_I`

Syntax: `CALL.ABS P, R, INT_IMM`  
Example: `@P0 CALL.ABS P0, R0 0x4;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 34-81 |
| NOINC | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101100....00000000........00..............................
..................0000.....00000000000000.....111111..........00
```

<a id="v15"></a>
## 15. `CALL_R`

Syntax: `CALL.ABS R`  
Example: `@P0 CALL.ABS R0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| NOINC | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101100....00000000........00000000000000000000000000000000
0000000000000000000000.111000000000000000.....111111..........00
```

<a id="v16"></a>
## 16. `CALL_R_I`

Syntax: `CALL.ABS R, INT_IMM`  
Example: `@P0 CALL.ABS R0 0x4;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 34-81 |
| NOINC | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000101100....00000000........00..............................
..................0000.111000000000000000.....111111..........00
```

