# JMX (SM89 SASS)

**NVIDIA:** Absolute Jump Indirect (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Indirect absolute jump (category: Control flow)

Typically emitted for: absolute indirect jumps (rare)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/JMX.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [JMX_P_R](#v1)
- [JMX_P_R_I](#v2)
- [JMX_R](#v3)
- [JMX_R_I](#v4)

<a id="v1"></a>
## 1. `JMX_P_R`

Syntax: `JMX P, R`  
Example: `@P0 JMX P0, R0;`

Register access: READ P (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| modi 1 | 85-86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100101001....00000000........00000000000000000000000000000000
000000000000000000000......00000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v2"></a>
## 2. `JMX_P_R_I`

Syntax: `JMX P, R, INT_IMM`  
Example: `@P0 JMX P0, R0 0x10;`

Register access: READ P (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 33-81 |
| modi 1 | 85-86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100101001....00000000........0...............................
..................000......00000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v3"></a>
## 3. `JMX_R`

Syntax: `JMX R`  
Example: `@P0 JMX R0;`

Register access: READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| modi 1 | 85-86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100101001....00000000........00000000000000000000000000000000
000000000000000000000..111000000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v4"></a>
## 4. `JMX_R_I`

Syntax: `JMX R, INT_IMM`  
Example: `@P0 JMX R0 0x10;`

Register access: READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 33-81 |
| modi 1 | 85-86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100101001....00000000........0...............................
..................000..111000000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

