# LDS (SM89 SASS)

**NVIDIA:** Load within Shared Memory Window (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Load from shared memory (category: Load / store)

Typically emitted for: `ld.shared`

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [lds_sts](../verify/RESULTS.md#lds_sts): `ld.shared / st.shared`

Encodings: <https://kuterdinel.com/nv_isa_sm89/LDS.html> (machine-derived by fuzzing the assembler; no semantics).

7 encoding variant(s):

- [LDS_R_I](#v1)
- [LDS_R_R](#v2)
- [LDS_R_RI](#v3)
- [LDS_R_RUR](#v4)
- [LDS_R_RURI](#v5)
- [LDS_R_UR](#v6)
- [LDS_R_URI](#v7)

<a id="v1"></a>
## 1. `LDS_R_I`

Syntax: `LDS R, [INT_IMM]`  
Example: `@P0 LDS.U8 R0, [0x2] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 40-63 |
| modi 1 | 73-75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000011001............1111111100000000........................
000000000...00000000000000000000000000000.....................00
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
| `111` | `???7.` |

<a id="v2"></a>
## 2. `LDS_R_R`

Syntax: `LDS R, [R]`  
Example: `@P0 LDS.U8 R0, [R0] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 73-75 |
| modi (op 1) | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000011001....................00000000000000000000000000000000
000000000...00..0000000000000000000000000.....................00
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
| `111` | `???7.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

<a id="v3"></a>
## 3. `LDS_R_RI`

Syntax: `LDS R, [R+INT_IMM]`  
Example: `@P0 LDS.U8 R0, [R0+0x1] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 40-63 |
| modi 1 | 73-75 |
| modi (op 1) | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000011001....................00000000........................
000000000...00..0000000000000000000000000.....................00
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
| `111` | `???7.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

<a id="v4"></a>
## 4. `LDS_R_RUR`

Syntax: `LDS R, [R+UR]`  
Example: `@P0 LDS.U8 R0, [R0+UR0] ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| modi 1 | 73-75 |
| modi (op 1) | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000011001...........................0000000000000000000000000
000000000...00..0000000000010000000000000.....................00
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
| `111` | `???7.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

<a id="v5"></a>
## 5. `LDS_R_RURI`

Syntax: `LDS R, [R+UR+INT_IMM]`  
Example: `@P0 LDS.U8 R0, [R0+UR0+0x1] ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-63 |
| modi 1 | 73-75 |
| modi (op 1) | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000011001...........................0........................
000000000...00..0000000000010000000000000.....................00
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
| `111` | `???7.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

<a id="v6"></a>
## 6. `LDS_R_UR`

Syntax: `LDS R, [UR]`  
Example: `@P0 LDS.U8 R0, [UR0] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| modi 1 | 73-75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000011001............11111111.......0000000000000000000000000
000000000...00000000000000010000000000000.....................00
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
| `111` | `???7.` |

<a id="v7"></a>
## 7. `LDS_R_URI`

Syntax: `LDS R, [UR+INT_IMM]`  
Example: `@P0 LDS.U8 R0, [UR0+0x2] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-63 |
| modi 1 | 73-75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000011001............11111111.......0........................
000000000...00000000000000010000000000000.....................00
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
| `111` | `???7.` |

