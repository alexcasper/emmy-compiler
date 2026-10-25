# SUST (SM89 SASS)

**NVIDIA:** Surface Store (Surface Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Surface store (category: Texture / surface)

Typically emitted for: `sust.b` (`surf2Dwrite`)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x99c, 0x99e ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3359)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [sust](../verify/RESULTS.md#sust): `sust.b.2d.b32.trap`

Encodings: <https://kuterdinel.com/nv_isa_sm89/SUST.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [SUST_R_R_R](#v1)
- [SUST_R_R_SNOWFLAKE](#v2)
- [SUST_R_R_R](#v3)
- [SUST_R_R_SNOWFLAKE](#v4)
- [SUST_R_R_I_I](#v5)

<a id="v1"></a>
## 1. `SUST_R_R_R`

Syntax: `SUST.P [R], R, R`  
Example: `@P0 SUST.P.1D.EF.INVALID0.IGN [R0], R0, R0 ;`

Register access: READ R (1 slots); READ R (4 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| operand 2 | 64-71 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001110011001....00000000................0000000000000000000.....
............0....000...000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `IGN.` |
| `01` | `(default)` |
| `10` | `TRAP.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0000` | `INVALID0.` |
| `0001` | `R.` |
| `0010` | `INVALID2.` |
| `0011` | `RG.` |
| `0100` | `INVALID4.` |
| `0101` | `INVALID5.` |
| `0110` | `INVALID6.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `(default)` |

Modifier Group 4:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 5:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v2"></a>
## 2. `SUST_R_R_SNOWFLAKE`

Syntax: `SUST.P [R], R, SNOWFLAKE`  
Example: `@P0 SUST.P.1D.EF.INVALID0.IGN [R0], R0,     ???255 ;`

Register access: READ R (1 slots); READ R (4 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001110011001....00000000................0000000000000000000.....
11111111....0....000...000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `IGN.` |
| `01` | `(default)` |
| `10` | `TRAP.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0000` | `INVALID0.` |
| `0001` | `R.` |
| `0010` | `INVALID2.` |
| `0011` | `RG.` |
| `0100` | `INVALID4.` |
| `0101` | `INVALID5.` |
| `0110` | `INVALID6.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `(default)` |

Modifier Group 4:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 5:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v3"></a>
## 3. `SUST_R_R_R`

Syntax: `SUST.P [R], R, R`  
Example: `@P0 SUST.P.1D.EF.INVALID0.IGN [R0], R0, R0 ;`

Register access: READ R (1 slots); READ R (4 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| operand 2 | 64-71 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001110011001....00000000................0000000000000000000.....
............0....000...000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `IGN.` |
| `01` | `(default)` |
| `10` | `TRAP.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0000` | `INVALID0.` |
| `0001` | `R.` |
| `0010` | `INVALID2.` |
| `0011` | `RG.` |
| `0100` | `INVALID4.` |
| `0101` | `INVALID5.` |
| `0110` | `INVALID6.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `(default)` |

Modifier Group 4:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 5:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v4"></a>
## 4. `SUST_R_R_SNOWFLAKE`

Syntax: `SUST.P [R], R, SNOWFLAKE`  
Example: `@P0 SUST.P.1D.EF.INVALID0.IGN [R0], R0,     ???255 ;`

Register access: READ R (1 slots); READ R (4 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001110011001....00000000................0000000000000000000.....
11111111....0....000...000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `IGN.` |
| `01` | `(default)` |
| `10` | `TRAP.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0000` | `INVALID0.` |
| `0001` | `R.` |
| `0010` | `INVALID2.` |
| `0011` | `RG.` |
| `0100` | `INVALID4.` |
| `0101` | `INVALID5.` |
| `0110` | `INVALID6.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `(default)` |

Modifier Group 4:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 5:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v5"></a>
## 5. `SUST_R_R_I_I`

Syntax: `SUST.D [R], R, INT_IMM, INT_IMM`  
Example: `@P0 SUST.D.1D.EF.U8.IGN [R0], R0, 0x0, 0x0 ;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 32-39 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110011101....00000000........................................
00000000....0....000...000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `IGN.` |
| `01` | `(default)` |
| `10` | `TRAP.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `1D.` |
| `001` | `1D_BUFFER.` |
| `010` | `1D_ARRAY.` |
| `011` | `2D.` |
| `100` | `2D_ARRAY.` |
| `101` | `3D.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 3:

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

Modifier Group 4:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `CONSTANT.PRIVATE.` |
| `0010` | `CONSTANT.CTA.` |
| `0011` | `CONSTANT.CTA.PRIVATE.` |
| `0100` | `STRONG.SM.PRIVATE.` |
| `0101` | `STRONG.SM.` |
| `0110` | `STRONG.GPU.PRIVATE.` |
| `0111` | `STRONG.GPU.` |
| `1000` | `MMIO.GPU.` |
| `1001` | `CONSTANT.SM.` |
| `1010` | `STRONG.SYS.` |
| `1011` | `CONSTANT.SM.PRIVATE.` |
| `1100` | `MMIO.SYS.` |
| `1101` | `CONSTANT.VC.` |
| `1110` | `CONSTANT.VC.PRIVATE.` |
| `1111` | `CONSTANT.GPU.` |

Modifier Group 5:

| value | modifier |
|---|---|
| `000` | `EF.` |
| `001` | `(default)` |
| `010` | `EL.` |
| `011` | `LU.` |
| `100` | `EU.` |
| `101` | `NA.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

