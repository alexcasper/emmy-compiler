# RPCMOV (SM89 SASS)

**NVIDIA:** PC Register Move (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Move to/from return PC register (category: Movement)

Typically emitted for: return-address save/restore (compiler-generated)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/RPCMOV.html> (machine-derived by fuzzing the assembler; no semantics).

10 encoding variant(s):

- [RPCMOV_PC_I](#v1)
- [RPCMOV_PC_I](#v2)
- [RPCMOV_PC_c[I][I]](#v3)
- [RPCMOV_PC_cx[UR][I]](#v4)
- [RPCMOV_PC_c[I][I]](#v5)
- [RPCMOV_PC_cx[UR][I]](#v6)
- [RPCMOV_PC_UR](#v7)
- [RPCMOV_PC_UR](#v8)
- [RPCMOV_PC_R](#v9)
- [RPCMOV_R_PC](#v10)

<a id="v1"></a>
## 1. `RPCMOV_PC_I`

Syntax: `RPCMOV.32 PC, INT_IMM`  
Example: `@P0 RPCMOV.32 Rpc.LO, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| modi | 31 |
| operand 1 | 32-63 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010101001....000000000000000.................................
00000000000000000000000000000000000000000.....................00
```

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `0` | `LO.` |
| `1` | `HI.` |

<a id="v2"></a>
## 2. `RPCMOV_PC_I`

Syntax: `RPCMOV.64 PC, INT_IMM`  
Example: `@P0 RPCMOV.64 Rpc, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 33-80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010101001....00000000000000000...............................
.................000000000000000000000000.....................00
```

<a id="v3"></a>
## 3. `RPCMOV_PC_c[I][I]`

Syntax: `RPCMOV.32 PC, c[INT_IMM][INT_IMM]`  
Example: `@P0 RPCMOV.32 Rpc.LO, c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| modi | 31 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010101101....000000000000000.00000000...................00000
00000000000000000000000000000000000000000.....................00
```

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `0` | `LO.` |
| `1` | `HI.` |

<a id="v4"></a>
## 4. `RPCMOV_PC_cx[UR][I]`

Syntax: `RPCMOV.32 PC, cx[UR][INT_IMM]`  
Example: `@P0 RPCMOV.32 Rpc.LO, cx[UR0][0x0];`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| modi | 31 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010101101....000000000000000........0...............000000000
00000000000000000000000000010000000000000.....................00
```

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `0` | `LO.` |
| `1` | `HI.` |

<a id="v5"></a>
## 5. `RPCMOV_PC_c[I][I]`

Syntax: `RPCMOV.64 PC, c[INT_IMM][INT_IMM]`  
Example: `@P0 RPCMOV.64 Rpc, c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010101101....000000000000000000000000...................00000
00000000000000000000000000000000000000000.....................00
```

<a id="v6"></a>
## 6. `RPCMOV_PC_cx[UR][I]`

Syntax: `RPCMOV.64 PC, cx[UR][INT_IMM]`  
Example: `@P0 RPCMOV.64 Rpc, cx[UR0][0x0];`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010101101....0000000000000000.......0...............000000000
00000000000000000000000000010000000000000.....................00
```

<a id="v7"></a>
## 7. `RPCMOV_PC_UR`

Syntax: `RPCMOV.32 PC, UR`  
Example: `@P0 RPCMOV.32 Rpc.LO, UR0;`

Register access: READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| modi | 31 |
| operand 1 | 32-38 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010101011....000000000000000........0000000000000000000000000
00000000000000000000000000010000000000000.....................00
```

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `0` | `LO.` |
| `1` | `HI.` |

<a id="v8"></a>
## 8. `RPCMOV_PC_UR`

Syntax: `RPCMOV.64 PC, UR`  
Example: `@P0 RPCMOV.64 Rpc, UR0;`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-38 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010101011....0000000000000000.......0000000000000000000000000
00000000000000000000000000010000000000000.....................00
```

<a id="v9"></a>
## 9. `RPCMOV_PC_R`

Syntax: `RPCMOV.32 PC, R`  
Example: `@P0 RPCMOV.32 Rpc.LO, R0;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| modi | 31 |
| operand 1 | 32-39 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010101100....000000000000000.........000000000000000000000000
00000000000000000000000000000000000000000.....................00
```

Operand 0 operand modifiers:

| value | modifier |
|---|---|
| `0` | `LO.` |
| `1` | `HI.` |

<a id="v10"></a>
## 10. `RPCMOV_R_PC`

Syntax: `RPCMOV.32 R, PC`  
Example: `@P0 RPCMOV.32 R0, Rpc.LO;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| modi | 31 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010101100............0000000.00000000000000000000000000000000
00000000000000000000000000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `0` | `LO.` |
| `1` | `HI.` |

