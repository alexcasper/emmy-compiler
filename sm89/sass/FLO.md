# FLO (SM89 SASS)

**NVIDIA:** Find Leading One (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Find leading one (category: Integer)

Typically emitted for: `bfind`, `clz` (`__clz`)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0xbd, 0x100 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1561)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [flo](../verify/RESULTS.md#flo): `bfind.u32 / clz.b32`
- [agg_atomic](../verify/RESULTS.md#agg_atomic): `atom.global.add.u32 to a warp-uniform address (ptxas warp-aggregates it)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/FLO.html> (machine-derived by fuzzing the assembler; no semantics).

10 encoding variant(s):

- [FLO_R_I](#v1)
- [FLO_R_P_I](#v2)
- [FLO_R_P_c[I][I]](#v3)
- [FLO_R_P_cx[UR][I]](#v4)
- [FLO_R_c[I][I]](#v5)
- [FLO_R_cx[UR][I]](#v6)
- [FLO_R_P_UR](#v7)
- [FLO_R_UR](#v8)
- [FLO_R_P_R](#v9)
- [FLO_R_R](#v10)

<a id="v1"></a>
## 1. `FLO_R_I`

Syntax: `FLO R, INT_IMM`  
Example: `@P0 FLO.U32 R0, 0x0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| modi 1 | 73 |
| SH | 74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000001001............00000000................................
000000000..000000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v2"></a>
## 2. `FLO_R_P_I`

Syntax: `FLO R, P, INT_IMM`  
Example: `@P0 FLO.U32 R0, P0, 0x0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-63 |
| modi 1 | 73 |
| SH | 74 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000001001............00000000................................
000000000..00000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v3"></a>
## 3. `FLO_R_P_c[I][I]`

Syntax: `FLO R, P, c[INT_IMM][INT_IMM]`  
Example: `@P0 FLO.U32 R0, P0, c[0x0][0x0] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| modi 1 | 73 |
| SH | 74 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000001101............0000000000000000...................00000
000000000..00000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v4"></a>
## 4. `FLO_R_P_cx[UR][I]`

Syntax: `FLO R, P, cx[UR][INT_IMM]`  
Example: `@P0 FLO.U32 R0, P0, cx[UR0][0x0] ;`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| modi 1 | 73 |
| SH | 74 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000001101............00000000.......0...............000000000
000000000..00000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v5"></a>
## 5. `FLO_R_c[I][I]`

Syntax: `FLO R, c[INT_IMM][INT_IMM]`  
Example: `@P0 FLO.U32 R0, c[0x0][0x0] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| modi 1 | 73 |
| SH | 74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000001101............0000000000000000...................00000
000000000..000000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v6"></a>
## 6. `FLO_R_cx[UR][I]`

Syntax: `FLO R, cx[UR][INT_IMM]`  
Example: `@P0 FLO.U32 R0, cx[UR0][0x0] ;`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| modi 1 | 73 |
| SH | 74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000001101............00000000.......0...............000000000
000000000..000000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v7"></a>
## 7. `FLO_R_P_UR`

Syntax: `FLO R, P, UR`  
Example: `@P0 FLO.U32 R0, P0, UR0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-38 |
| cINV (op 2) | 63 |
| modi 1 | 73 |
| SH | 74 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000001011............00000000.......000000000000000000000000.
000000000..00000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v8"></a>
## 8. `FLO_R_UR`

Syntax: `FLO R, UR`  
Example: `@P0 FLO.U32 R0, UR0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| cINV (op 1) | 63 |
| modi 1 | 73 |
| SH | 74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000001011............00000000.......000000000000000000000000.
000000000..000000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v9"></a>
## 9. `FLO_R_P_R`

Syntax: `FLO R, P, R`  
Example: `@P0 FLO.U32 R0, P0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-39 |
| cINV (op 2) | 63 |
| modi 1 | 73 |
| SH | 74 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000001100............00000000........00000000000000000000000.
000000000..00000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v10"></a>
## 10. `FLO_R_R`

Syntax: `FLO R, R`  
Example: `@P0 FLO.U32 R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| cINV (op 1) | 63 |
| modi 1 | 73 |
| SH | 74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000001100............00000000........00000000000000000000000.
000000000..000000111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

