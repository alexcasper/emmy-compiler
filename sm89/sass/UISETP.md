# UISETP (SM89 SASS)

**NVIDIA:** Integer Compare and Set Uniform Predicate (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform integer compare to uniform predicate (category: Uniform datapath)

Typically emitted for: warp-uniform compares (uniform loop exits)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/UISETP.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [UISETP_UP_UP_UR_I_UP](#v1)
- [UISETP_UP_UP_UR_I_UP_UP](#v2)
- [UISETP_UP_UP_UR_UR_UP](#v3)
- [UISETP_UP_UP_UR_UR_UP_UP](#v4)

<a id="v1"></a>
## 1. `UISETP_UP_UP_UR_I_UP`

Syntax: `UISETP.AND UP, UP, UR, INT_IMM, UP`  
Example: `@UP0 UISETP.F.U32.AND UP0, UP0, UR0, 0x0, UP0;`

Register access: READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100010001....00000000.......0................................
000000000......0...........10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v2"></a>
## 2. `UISETP_UP_UP_UR_I_UP_UP`

Syntax: `UISETP.AND.EX UP, UP, UR, INT_IMM, UP, UP`  
Example: `@UP0 UISETP.F.U32.AND.EX UP0, UP0, UR0, 0x0, UP0, UP0;`

Register access: READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| operand 5 | 67-70 |
| cNOT (op 5) | 71 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100010001....00000000.......0................................
000.....1......0...........10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v3"></a>
## 3. `UISETP_UP_UP_UR_UR_UP`

Syntax: `UISETP.AND UP, UP, UR, UR, UP`  
Example: `@UP0 UISETP.F.U32.AND UP0, UP0, UR0, UR0, UP0;`

Register access: READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100010100....00000000.......0.......0000000000000000000000000
000000000......0...........10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

<a id="v4"></a>
## 4. `UISETP_UP_UP_UR_UR_UP_UP`

Syntax: `UISETP.AND.EX UP, UP, UR, UR, UP, UP`  
Example: `@UP0 UISETP.F.U32.AND.EX UP0, UP0, UR0, UR0, UP0, UP0;`

Register access: READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| operand 5 | 67-70 |
| cNOT (op 5) | 71 |
| modi 1 | 73-75 |
| modi 2 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100010100....00000000.......0.......0000000000000000000000000
000.....1......0...........10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U32.` |
| `001` | `(default)` |
| `010` | `U32.OR.` |
| `011` | `OR.` |
| `100` | `U32.XOR.` |
| `101` | `XOR.` |
| `110` | `U32.INVALID3.` |
| `111` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `LT.` |
| `010` | `EQ.` |
| `011` | `LE.` |
| `100` | `GT.` |
| `101` | `NE.` |
| `110` | `GE.` |
| `111` | `T.` |

