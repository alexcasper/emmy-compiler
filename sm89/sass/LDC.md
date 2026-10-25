# LDC (SM89 SASS)

**NVIDIA:** Load Constant (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Load from constant bank c[bank][offset] (category: Load / store)

Typically emitted for: `ld.const`, `ld.param` (kernel params live in constant bank 0), `__constant__`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x582, 0x7ac, 0xab9, 0xb82, 0xbac ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3505)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [ldc](../verify/RESULTS.md#ldc): `ld.const with dynamic index`

Encodings: <https://kuterdinel.com/nv_isa_sm89/LDC.html> (machine-derived by fuzzing the assembler; no semantics).

6 encoding variant(s):

- [LDC_R_cx[UR][I]](#v1)
- [LDC_R_cx[UR][RI]](#v2)
- [LDC_R_cx[UR][R]](#v3)
- [LDC_R_c[I][I]](#v4)
- [LDC_R_c[I][RI]](#v5)
- [LDC_R_c[I][R]](#v6)

<a id="v1"></a>
## 1. `LDC_R_cx[UR][I]`

Syntax: `LDC R, cx[UR][INT_IMM]`  
Example: `@P0 LDC.U8 R0, cx[UR0][0x0] ;`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 2 | 37-53 |
| modi 1 | 73-75 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000011010...................000000.................0000000000
111111110...00..0000000000010000000000000.....................00
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
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `IL.` |
| `10` | `IS.` |
| `11` | `ISL.` |

<a id="v2"></a>
## 2. `LDC_R_cx[UR][RI]`

Syntax: `LDC R, cx[UR][R+INT_IMM]`  
Example: `@P0 LDC.U8 R0, cx[UR0][R0+0x1] ;`

Register access: WRITE R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 3 | 38-53 |
| operand 2 | 64-71 |
| modi 1 | 73-75 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000011010...................0000000................0000000000
........0...00..0000000000010000000000000.....................00
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
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `IL.` |
| `10` | `IS.` |
| `11` | `ISL.` |

<a id="v3"></a>
## 3. `LDC_R_cx[UR][R]`

Syntax: `LDC R, cx[UR][R]`  
Example: `@P0 LDC.U8 R0, cx[UR0][R0] ;`

Register access: WRITE R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 2 | 64-71 |
| modi 1 | 73-75 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000011010...................000000000000000000000000000000000
........0...00..0000000000010000000000000.....................00
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
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `IL.` |
| `10` | `IS.` |
| `11` | `ISL.` |

<a id="v4"></a>
## 4. `LDC_R_c[I][I]`

Syntax: `LDC R, c[INT_IMM][INT_IMM]`  
Example: `@P0 LDC.U8 R0, c[0x0][0x8] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 37-52 |
| operand 1 | 53-58 |
| modi 1 | 73-75 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000011101............1111111100000......................00000
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
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `IL.` |
| `10` | `IS.` |
| `11` | `ISL.` |

<a id="v5"></a>
## 5. `LDC_R_c[I][RI]`

Syntax: `LDC R, c[INT_IMM][R+INT_IMM]`  
Example: `@P0 LDC.U8 R0, c[0x0][R0+0x1] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 38-52 |
| operand 1 | 53-58 |
| modi 1 | 73-75 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000011101....................000000.....................00000
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
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `IL.` |
| `10` | `IS.` |
| `11` | `ISL.` |

<a id="v6"></a>
## 6. `LDC_R_c[I][R]`

Syntax: `LDC R, c[INT_IMM][R]`  
Example: `@P0 LDC.U8 R0, c[0x0][R0] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 54-58 |
| modi 1 | 73-75 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000011101....................0000000000000000000000.....00000
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
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `IL.` |
| `10` | `IS.` |
| `11` | `ISL.` |

