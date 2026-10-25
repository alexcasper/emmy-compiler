# JMP (SM89 SASS)

**NVIDIA:** Absolute Jump (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Absolute jump (category: Control flow)

Typically emitted for: absolute jumps (rare)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/JMP.html> (machine-derived by fuzzing the assembler; no semantics).

8 encoding variant(s):

- [JMP_I](#v1)
- [JMP_P_I](#v2)
- [JMP_P_UR_I](#v3)
- [JMP_UR_I](#v4)
- [JMP_P_UR_c[I][I]](#v5)
- [JMP_P_c[I][I]](#v6)
- [JMP_UR_c[I][I]](#v7)
- [JMP_c[I][I]](#v8)

<a id="v1"></a>
## 1. `JMP_I`

Syntax: `JMP INT_IMM`  
Example: `@P0 JMP 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| modi 1 | 32-33 |
| operand 0 | 34-80 |
| modi 2 | 85-86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100101001....0000000000000000................................
.................0000..111000000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `U.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v2"></a>
## 2. `JMP_P_I`

Syntax: `JMP P, INT_IMM`  
Example: `@P0 JMP P0, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| modi 1 | 32-33 |
| operand 1 | 34-80 |
| modi 2 | 85-86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100101001....0000000000000000................................
.................0000......00000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `U.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v3"></a>
## 3. `JMP_P_UR_I`

Syntax: `JMP P, UR, INT_IMM`  
Example: `@P0 JMP.INVALID0 P0, UR0, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
| modi 1 | 32-33 |
| operand 2 | 34-80 |
| modi 2 | 85-86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100101001....00000000.......0................................
.................0000......10000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `INVALID0.` |
| `01` | `INVALID1.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v4"></a>
## 4. `JMP_UR_I`

Syntax: `JMP UR, INT_IMM`  
Example: `@P0 JMP.INVALID0 UR0, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-30 |
| modi 1 | 32-33 |
| operand 1 | 34-80 |
| modi 2 | 85-86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100101001....00000000.......0................................
.................0000..111010000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `INVALID0.` |
| `01` | `INVALID1.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v5"></a>
## 5. `JMP_P_UR_c[I][I]`

Syntax: `JMP P, UR, c[INT_IMM][INT_IMM]`  
Example: `@P0 JMP.INVALID0 P0, UR0, c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
| modi 1 | 32-33 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| modi 2 | 85-86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100101101....00000000.......0..000000...................00000
000000000000000000000......10000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `INVALID0.` |
| `01` | `INVALID1.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v6"></a>
## 6. `JMP_P_c[I][I]`

Syntax: `JMP P, c[INT_IMM][INT_IMM]`  
Example: `@P0 JMP P0, c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| modi 1 | 32-33 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| modi 2 | 85-86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100101101....0000000000000000..000000...................00000
000000000000000000000......00000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `U.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v7"></a>
## 7. `JMP_UR_c[I][I]`

Syntax: `JMP UR, c[INT_IMM][INT_IMM]`  
Example: `@P0 JMP.INVALID0 UR0, c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-30 |
| modi 1 | 32-33 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| modi 2 | 85-86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100101101....00000000.......0..000000...................00000
000000000000000000000..111010000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `INVALID0.` |
| `01` | `INVALID1.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v8"></a>
## 8. `JMP_c[I][I]`

Syntax: `JMP c[INT_IMM][INT_IMM]`  
Example: `@P0 JMP c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| modi 1 | 32-33 |
| operand 1 | 40-52, 54 |
| operand 0 | 53, 55-58 |
| modi 2 | 85-86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100101101....0000000000000000..000000...................00000
000000000000000000000..111000000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `U.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

