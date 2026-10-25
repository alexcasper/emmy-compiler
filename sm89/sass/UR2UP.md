# UR2UP (SM89 SASS)

**NVIDIA:** Uniform Register to Uniform Predicate (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform register to uniform predicates (category: Uniform datapath)

Typically emitted for: uniform predicate restore

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/UR2UP.html> (machine-derived by fuzzing the assembler; no semantics).

3 encoding variant(s):

- [UR2UP_UP_UR](#v1)
- [UR2UP_UP_UR_I](#v2)
- [UR2UP_UP_UR_UR](#v3)

<a id="v1"></a>
## 1. `UR2UP_UP_UR`

Syntax: `UR2UP UP, UR`  
Example: `@UP0 UR2UP UPR, UR0;`

Register access: READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
| modi (op 1) | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000010001....00000000.......011111111000000000000000000000000
000000000000..000000000000010000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v2"></a>
## 2. `UR2UP_UP_UR_I`

Syntax: `UR2UP UP, UR, INT_IMM`  
Example: `@UP0 UR2UP UPR, UR0, 0x0;`

Register access: READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
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
001000010001....00000000.......0................................
000000000000..000000000000010000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

<a id="v3"></a>
## 3. `UR2UP_UP_UR_UR`

Syntax: `UR2UP UP, UR, UR`  
Example: `@UP0 UR2UP UPR, UR0, UR0;`

Register access: READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
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
001000010011....00000000.......0.......0000000000000000000000000
000000000000..000000000000010000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `B1.` |
| `10` | `B2.` |
| `11` | `B3.` |

