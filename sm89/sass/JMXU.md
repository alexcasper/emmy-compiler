# JMXU (SM89 SASS)

**NVIDIA:** Absolute Jump with Uniform Register Based Offset (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Indirect absolute jump via uniform register (category: Control flow)

Typically emitted for: uniform absolute indirect jump

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/JMXU.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [JMXU_P_UR](#v1)
- [JMXU_P_UR_I](#v2)
- [JMXU_UR](#v3)
- [JMXU_UR_I](#v4)

<a id="v1"></a>
## 1. `JMXU_P_UR`

Syntax: `JMXU P, UR`  
Example: `@P0 JMXU P0, UR0;`

Register access: READ P (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
| modi 1 | 32-33 |
| modi 2 | 85-86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110101001....00000000.......0..000000000000000000000000000000
000000000000000000000......10000000000000.....111111..........00
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
## 2. `JMXU_P_UR_I`

Syntax: `JMXU P, UR, INT_IMM`  
Example: `@P0 JMXU P0, UR0 0x4;`

Register access: READ P (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
| modi 1 | 32-33 |
| operand 2 | 34-81 |
| modi 2 | 85-86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110101001....00000000.......0................................
..................000......10000000000000.....111111..........00
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
## 3. `JMXU_UR`

Syntax: `JMXU UR`  
Example: `@P0 JMXU UR0;`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-30 |
| modi 1 | 32-33 |
| modi 2 | 85-86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110101001....00000000.......0..000000000000000000000000000000
000000000000000000000..111010000000000000.....111111..........00
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

<a id="v4"></a>
## 4. `JMXU_UR_I`

Syntax: `JMXU UR, INT_IMM`  
Example: `@P0 JMXU UR0 0x4;`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-30 |
| modi 1 | 32-33 |
| operand 1 | 34-81 |
| modi 2 | 85-86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110101001....00000000.......0................................
..................000..111010000000000000.....111111..........00
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

