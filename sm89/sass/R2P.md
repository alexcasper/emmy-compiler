# R2P (SM89 SASS)

**NVIDIA:** Move Register To Predicate Register (Predicate Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Unpack register bits into predicates (category: Movement)

Typically emitted for: restoring predicates (compiler-generated)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/R2P.html> (machine-derived by fuzzing the assembler; no semantics).

6 encoding variant(s):

- [R2P_P_R](#v1)
- [R2P_P_R_I](#v2)
- [R2P_P_R_c[I][I]](#v3)
- [R2P_P_R_cx[UR][I]](#v4)
- [R2P_P_R_UR](#v5)
- [R2P_P_R_R](#v6)

<a id="v1"></a>
## 1. `R2P_P_R`

Syntax: `R2P P, R`  
Example: `@P0 R2P PR, R0;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| modi (op 1) | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000000001....00000000........11111111000000000000000000000000
000000000000..000000000000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v2"></a>
## 2. `R2P_P_R_I`

Syntax: `R2P P, R, INT_IMM`  
Example: `@P0 R2P PR, R0, 0x0;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| modi (op 1) | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000000001....00000000........................................
000000000000..000000000000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v3"></a>
## 3. `R2P_P_R_c[I][I]`

Syntax: `R2P P, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 R2P PR, R0, c[0x0][0x0];`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| modi (op 1) | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000000101....00000000........00000000...................00000
000000000000..000000000000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v4"></a>
## 4. `R2P_P_R_cx[UR][I]`

Syntax: `R2P P, R, cx[UR][INT_IMM]`  
Example: `@P0 R2P PR, R0, cx[UR0][0x0];`

Register access: READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| modi (op 1) | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000000101....00000000...............0...............000000000
000000000000..000000000000010000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v5"></a>
## 5. `R2P_P_R_UR`

Syntax: `R2P P, R, UR`  
Example: `@P0 R2P PR, R0, UR0;`

Register access: READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| modi (op 1) | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000000011....00000000...............0000000000000000000000000
000000000000..000000000000010000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v6"></a>
## 6. `R2P_P_R_R`

Syntax: `R2P P, R, R`  
Example: `@P0 R2P PR, R0, R0;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi (op 1) | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000000100....00000000................000000000000000000000000
000000000000..000000000000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

