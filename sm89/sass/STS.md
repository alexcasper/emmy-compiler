# STS (SM89 SASS)

**NVIDIA:** Store to Shared Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Store to shared memory (category: Load / store)

Typically emitted for: `st.shared`

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [lds_sts](../verify/RESULTS.md#lds_sts): `ld.shared / st.shared`

Encodings: <https://kuterdinel.com/nv_isa_sm89/STS.html> (machine-derived by fuzzing the assembler; no semantics).

3 encoding variant(s):

- [STS_I_R](#v1)
- [STS_RI_R](#v2)
- [STS_R_R](#v3)

<a id="v1"></a>
## 1. `STS_I_R`

Syntax: `STS [INT_IMM], R`  
Example: `@P0 STS.U8 [0x20], R0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| operand 0 | 40-63 |
| modi 1 | 73-75 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100011100....0000000011111111................................
000000000...00000000000000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

<a id="v2"></a>
## 2. `STS_RI_R`

Syntax: `STS [R+INT_IMM], R`  
Example: `@P0 STS.U8 [R0+0x20], R0 ;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 2 | 32-39 |
| operand 1 | 40-63 |
| modi 1 | 73-75 |
| modi (op 0) | 78-79 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100011100....00000000........................................
000000000...00..0000000000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

<a id="v3"></a>
## 3. `STS_R_R`

Syntax: `STS [R], R`  
Example: `@P0 STS.U8 [R0], R0 ;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 32-39 |
| modi 1 | 73-75 |
| modi (op 0) | 78-79 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100011100....00000000................000000000000000000000000
000000000...00..0000000000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

