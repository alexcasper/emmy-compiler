# BRX (SM89 SASS)

**NVIDIA:** Relative Branch Indirect (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Indirect relative branch (category: Control flow)

Typically emitted for: `brx.idx`; switch jump tables

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [brx](../verify/RESULTS.md#brx): `brx.idx (jump table)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/BRX.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [BRX_P_R](#v1)
- [BRX_P_R_I](#v2)
- [BRX_R](#v3)
- [BRX_R_I](#v4)

<a id="v1"></a>
## 1. `BRX_P_R`

Syntax: `BRX P, R`  
Example: `@P0 BRX P0, R0;`

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
100100101001....00000000........00000000000000000000000000000000
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
## 2. `BRX_P_R_I`

Syntax: `BRX P, R, INT_IMM`  
Example: `@P0 BRX P0, R0 0x10;`

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
100100101001....00000000........0...............................
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
## 3. `BRX_R`

Syntax: `BRX R`  
Example: `@P0 BRX R0;`

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
100100101001....00000000........00000000000000000000000000000000
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
## 4. `BRX_R_I`

Syntax: `BRX R, INT_IMM`  
Example: `@P0 BRX R0 0x10;`

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
100100101001....00000000........0...............................
..................000..111000000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

