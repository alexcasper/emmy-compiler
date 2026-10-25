# BMOV (SM89 SASS)

**NVIDIA:** Move Convergence Barrier State (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Move to/from convergence barrier registers (category: Movement)

Typically emitted for: convergence barrier save/restore (compiler-generated, deep divergence/recursion)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x355, 0x356 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4128)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/BMOV.html> (machine-derived by fuzzing the assembler; no semantics).

16 encoding variant(s):

- [BMOV_B_I](#v1)
- [BMOV_SNOWFLAKE_I](#v2)
- [BMOV_SNOWFLAKE_I](#v3)
- [BMOV_B_c[I][I]](#v4)
- [BMOV_B_cx[UR][I]](#v5)
- [BMOV_SNOWFLAKE_c[I][I]](#v6)
- [BMOV_SNOWFLAKE_cx[UR][I]](#v7)
- [BMOV_SNOWFLAKE_c[I][I]](#v8)
- [BMOV_SNOWFLAKE_cx[UR][I]](#v9)
- [BMOV_B_B](#v10)
- [BMOV_SNOWFLAKE_B](#v11)
- [BMOV_R_B](#v12)
- [BMOV_R_SNOWFLAKE](#v13)
- [BMOV_B_R](#v14)
- [BMOV_SNOWFLAKE_R](#v15)
- [BMOV_SNOWFLAKE_R](#v16)

<a id="v1"></a>
## 1. `BMOV_B_I`

Syntax: `BMOV.32 B, INT_IMM`  
Example: `@P0 BMOV.32 B0, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-27 |
| operand 1 | 32-63 |
| PQUAD | 84 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010101001....00000000....0000................................
00000000000000000000.00000000000000000000.....111111..........00
```

<a id="v2"></a>
## 2. `BMOV_SNOWFLAKE_I`

Syntax: `BMOV.32 SNOWFLAKE, INT_IMM`  
Example: `@P0 BMOV.32 THREAD_STATE_ENUM.0, 0x0;`

| field | bits |
|---|---|
| operand 0 | 0, 26-29 |
| predicate | 12-15 |
| modi (op 0) | 24-25 |
| operand 1 | 32-63 |
| PQUAD | 84 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
.11010101001....00000000......00................................
00000000000000000000.00000000000000000000.....111111..........00
```

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `(default)` |
| `10` | `(default)` |
| `11` | `(default)` |

<a id="v3"></a>
## 3. `BMOV_SNOWFLAKE_I`

Syntax: `BMOV.64 SNOWFLAKE, INT_IMM`  
Example: `@P0 BMOV.64 ATEXIT_PC, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 33-80 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010101001....00000000000000000...............................
.................000000000000000000000000.....111111..........00
```

<a id="v4"></a>
## 4. `BMOV_B_c[I][I]`

Syntax: `BMOV.32 B, c[INT_IMM][INT_IMM]`  
Example: `@P0 BMOV.32 B0, c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-27 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| PQUAD | 84 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010101101....00000000....000000000000...................00000
00000000000000000000.00000000000000000000.....111111..........00
```

<a id="v5"></a>
## 5. `BMOV_B_cx[UR][I]`

Syntax: `BMOV.32 B, cx[UR][INT_IMM]`  
Example: `@P0 BMOV.32 B0, cx[UR0][0x0];`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-27 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| PQUAD | 84 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010101101....00000000....0000.......0...............000000000
00000000000000000000.00000010000000000000.....111111..........00
```

<a id="v6"></a>
## 6. `BMOV_SNOWFLAKE_c[I][I]`

Syntax: `BMOV.32 SNOWFLAKE, c[INT_IMM][INT_IMM]`  
Example: `@P0 BMOV.32 THREAD_STATE_ENUM.0, c[0x0][0x0];`

| field | bits |
|---|---|
| operand 0 | 0, 26-29 |
| predicate | 12-15 |
| modi (op 0) | 24-25 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| PQUAD | 84 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
.11010101101....00000000......0000000000...................00000
00000000000000000000.00000000000000000000.....111111..........00
```

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `(default)` |
| `10` | `(default)` |
| `11` | `(default)` |

<a id="v7"></a>
## 7. `BMOV_SNOWFLAKE_cx[UR][I]`

Syntax: `BMOV.32 SNOWFLAKE, cx[UR][INT_IMM]`  
Example: `@P0 BMOV.32 THREAD_STATE_ENUM.0, cx[UR0][0x0];`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| operand 0 | 0, 26-29 |
| predicate | 12-15 |
| modi (op 0) | 24-25 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| PQUAD | 84 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
.11010101101....00000000......00.......0...............000000000
00000000000000000000.00000010000000000000.....111111..........00
```

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `(default)` |
| `10` | `(default)` |
| `11` | `(default)` |

<a id="v8"></a>
## 8. `BMOV_SNOWFLAKE_c[I][I]`

Syntax: `BMOV.64 SNOWFLAKE, c[INT_IMM][INT_IMM]`  
Example: `@P0 BMOV.64 ATEXIT_PC, c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010101101....000000000000000000000000...................00000
00000000000000000000000000000000000000000.....111111..........00
```

<a id="v9"></a>
## 9. `BMOV_SNOWFLAKE_cx[UR][I]`

Syntax: `BMOV.64 SNOWFLAKE, cx[UR][INT_IMM]`  
Example: `@P0 BMOV.64 ATEXIT_PC, cx[UR0][0x0];`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010101101....0000000000000000.......0...............000000000
00000000000000000000000000010000000000000.....111111..........00
```

<a id="v10"></a>
## 10. `BMOV_B_B`

Syntax: `BMOV.32 B, B`  
Example: `@P0 BMOV.32 B0, B0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-20 |
| operand 0 | 24-27 |
| PQUAD | 84 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010101111.........000....000000000000000000000000000000000000
00000000000000000000.00000000000000000000.....111111..........00
```

<a id="v11"></a>
## 11. `BMOV_SNOWFLAKE_B`

Syntax: `BMOV.32 SNOWFLAKE, B`  
Example: `@P0 BMOV.32 THREAD_STATE_ENUM.0, B0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-20 |
| modi (op 0) | 24-25 |
| operand 0 | 26-29 |
| PQUAD | 84 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010101111.........000......0000000000000000000000000000000000
00000000000000000000.00000000000000000000.....111111..........00
```

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `(default)` |
| `10` | `(default)` |
| `11` | `(default)` |

<a id="v12"></a>
## 12. `BMOV_R_B`

Syntax: `BMOV.32 R, B`  
Example: `@P0 BMOV.32 R0, B0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-27 |
| CLEAR | 84 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010101100................000000000000000000000000000000000000
00000000000000000000.00000000000000000000........111..........00
```

<a id="v13"></a>
## 13. `BMOV_R_SNOWFLAKE`

Syntax: `BMOV.32 R, SNOWFLAKE`  
Example: `@P0 BMOV.32 R0, THREAD_STATE_ENUM.0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| modi (op 1) | 24-25 |
| operand 1 | 26-29 |
| CLEAR | 84 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101010101100..................0000000000000000000000000000000000
00000000000000000000.00000000000000000000........111..........00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `(default)` |
| `10` | `(default)` |
| `11` | `(default)` |

<a id="v14"></a>
## 14. `BMOV_B_R`

Syntax: `BMOV.32 B, R`  
Example: `@P0 BMOV.32 B0, R0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-27 |
| operand 1 | 32-39 |
| PQUAD | 84 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010101100....00000000....0000........000000000000000000000000
00000000000000000000.00000000000000000000.....111.............00
```

<a id="v15"></a>
## 15. `BMOV_SNOWFLAKE_R`

Syntax: `BMOV.32 SNOWFLAKE, R`  
Example: `@P0 BMOV.32 THREAD_STATE_ENUM.0, R0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| operand 0 | 0, 26-29 |
| predicate | 12-15 |
| modi (op 0) | 24-25 |
| operand 1 | 32-39 |
| PQUAD | 84 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
.11010101100....00000000......00........000000000000000000000000
00000000000000000000.00000000000000000000.....111.............00
```

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `(default)` |
| `10` | `(default)` |
| `11` | `(default)` |

<a id="v16"></a>
## 16. `BMOV_SNOWFLAKE_R`

Syntax: `BMOV.64 SNOWFLAKE, R`  
Example: `@P0 BMOV.64 ATEXIT_PC, R0 ;`

Register access: READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010101100....0000000000000000........000000000000000000000000
00000000000000000000000000000000000000000.....111.............00
```

