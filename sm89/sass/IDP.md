# IDP (SM89 SASS)

**NVIDIA:** Integer Dot Product and Accumulate (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Integer dot product (dp4a / dp2a) (category: Integer)

Typically emitted for: `dp4a`, `dp2a` (`__dp4a`)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [idp](../verify/RESULTS.md#idp): `dp4a.s32.s32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/IDP.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [IDP_R_R_c[I][I]_R](#v1)
- [IDP_R_R_cx[UR][I]_R](#v2)
- [IDP_R_R_UR_R](#v3)
- [IDP_R_R_R_R](#v4)

<a id="v1"></a>
## 1. `IDP_R_R_c[I][I]_R`

Syntax: `IDP.4A R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 IDP.4A.U8.U8 R0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| modi 1 | 73-74 |
| cNEG (op 4) | 75 |
| modi 2 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001000101....................00000000...................00000
........0.....000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `S8.` |
| `11` | `S8.S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `4A.U8.` |
| `01` | `2A.LO.U16.` |
| `11` | `2A.HI.U16.` |

<a id="v2"></a>
## 2. `IDP_R_R_cx[UR][I]_R`

Syntax: `IDP.4A R, R, cx[UR][INT_IMM], R`  
Example: `@P0 IDP.4A.U8.U8 R0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| modi 1 | 73-74 |
| cNEG (op 4) | 75 |
| modi 2 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001000101...........................0...............000000000
........0.....000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `S8.` |
| `11` | `S8.S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `4A.U8.` |
| `01` | `2A.LO.U16.` |
| `11` | `2A.HI.U16.` |

<a id="v3"></a>
## 3. `IDP_R_R_UR_R`

Syntax: `IDP.4A R, R, UR, R`  
Example: `@P0 IDP.4A.U8.U8 R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
| modi 1 | 73-74 |
| cNEG (op 3) | 75 |
| modi 2 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001000011...........................0000000000000000000000000
........0.....000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `S8.` |
| `11` | `S8.S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `4A.U8.` |
| `01` | `2A.LO.U16.` |
| `11` | `2A.HI.U16.` |

<a id="v4"></a>
## 4. `IDP_R_R_R_R`

Syntax: `IDP.4A R, R, R, R`  
Example: `@P0 IDP.4A.U8.U8 R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
| modi 1 | 73-74 |
| cNEG (op 3) | 75 |
| modi 2 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001000100............................000000000000000000000000
........0.....000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `S8.` |
| `11` | `S8.S8.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `4A.U8.` |
| `01` | `2A.LO.U16.` |
| `11` | `2A.HI.U16.` |

