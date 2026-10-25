# P2R (SM89 SASS)

**NVIDIA:** Move Predicate Register To Register (Predicate Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Pack predicates into a register (category: Movement)

Typically emitted for: spilling/packing predicates (compiler-generated)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/P2R.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [P2R_R_P_R_I](#v1)
- [P2R_R_P_R_c[I][I]](#v2)
- [P2R_R_P_R_cx[UR][I]](#v3)
- [P2R_R_P_R_UR](#v4)
- [P2R_R_P_R_R](#v5)

<a id="v1"></a>
## 1. `P2R_R_P_R_I`

Syntax: `P2R R, P, R, INT_IMM`  
Example: `@P0 P2R R0, PR, R0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-63 |
| modi 1 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000000001....................................................
000000000000..000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v2"></a>
## 2. `P2R_R_P_R_c[I][I]`

Syntax: `P2R R, P, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 P2R R0, PR, R0, c[0x0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| modi 1 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000000101....................00000000...................00000
000000000000..000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v3"></a>
## 3. `P2R_R_P_R_cx[UR][I]`

Syntax: `P2R R, P, R, cx[UR][INT_IMM]`  
Example: `@P0 P2R R0, PR, R0, cx[UR0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| modi 1 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000000101...........................0...............000000000
000000000000..000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v4"></a>
## 4. `P2R_R_P_R_UR`

Syntax: `P2R R, P, R, UR`  
Example: `@P0 P2R R0, PR, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| modi 1 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000000011...........................0000000000000000000000000
000000000000..000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v5"></a>
## 5. `P2R_R_P_R_R`

Syntax: `P2R R, P, R, R`  
Example: `@P0 P2R R0, PR, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000000100............................000000000000000000000000
000000000000..000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

