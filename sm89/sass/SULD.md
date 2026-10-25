# SULD (SM89 SASS)

**NVIDIA:** Surface Load (Surface Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Surface load (category: Texture / surface)

Typically emitted for: `suld.b` (`surf2Dread`)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x998, 0x99a ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3321)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [suld](../verify/RESULTS.md#suld): `suld.b.2d.b32.trap`

Encodings: <https://kuterdinel.com/nv_isa_sm89/SULD.html> (machine-derived by fuzzing the assembler; no semantics).

20 encoding variant(s):

- [SULD_P_R_R_I_I_I](#v1)
- [SULD_R_R_I_I_I](#v2)
- [SULD_P_R_R_I_I_I](#v3)
- [SULD_R_R_I_I_I](#v4)
- [SULD_P_R_R_R](#v5)
- [SULD_P_R_R_SNOWFLAKE](#v6)
- [SULD_R_R_R](#v7)
- [SULD_R_R_SNOWFLAKE](#v8)
- [SULD_P_R_R_R](#v9)
- [SULD_P_R_R_SNOWFLAKE](#v10)
- [SULD_R_R_R](#v11)
- [SULD_R_R_SNOWFLAKE](#v12)
- [SULD_P_R_R_I_I](#v13)
- [SULD_R_R_I_I](#v14)
- [SULD_P_R_R_I_I](#v15)
- [SULD_R_R_I_I](#v16)
- [SULD_P_R_R_UR_I](#v17)
- [SULD_R_R_UR_I](#v18)
- [SULD_P_R_R_UR_I](#v19)
- [SULD_R_R_UR_I](#v20)

<a id="v1"></a>
## 1. `SULD_P_R_R_I_I_I`

Syntax: `SULD.P P, R, [R], INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN P0, R0, [R0], 0x0, 0x0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (4 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-52 |
| operand 3 | 53-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010011110....................00000000........................
00000000....0..........000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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
## 2. `SULD_R_R_I_I_I`

Syntax: `SULD.P R, [R], INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN R0, [R0], 0x0, 0x0, 0x0 ;`

Register access: WRITE R (4 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-52 |
| operand 2 | 53-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010011110....................00000000........................
00000000....0....111...000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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
## 3. `SULD_P_R_R_I_I_I`

Syntax: `SULD.D P, R, [R], INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 SULD.D.1D.EF.U8.IGN P0, R0, [R0], 0x0, 0x0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-52 |
| operand 3 | 53-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110011110....................00000000........................
00000000....0..........000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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
## 4. `SULD_R_R_I_I_I`

Syntax: `SULD.D R, [R], INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 SULD.D.1D.EF.U8.IGN R0, [R0], 0x0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-52 |
| operand 2 | 53-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110011110....................00000000........................
00000000....0....111...000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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
## 5. `SULD_P_R_R_R`

Syntax: `SULD.P P, R, [R], R`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN P0, R0, [R0], R0 ;`

Register access: WRITE P (1 slots); WRITE R (4 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| operand 3 | 64-71 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000110011001....................000000000000000000000000000.....
............0..........000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v6"></a>
## 6. `SULD_P_R_R_SNOWFLAKE`

Syntax: `SULD.P P, R, [R], SNOWFLAKE`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN P0, R0, [R0],     ???255 ;`

Register access: WRITE P (1 slots); WRITE R (4 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000110011001....................000000000000000000000000000.....
11111111....0..........000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v7"></a>
## 7. `SULD_R_R_R`

Syntax: `SULD.P R, [R], R`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN R0, [R0], R0 ;`

Register access: WRITE R (4 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| operand 2 | 64-71 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000110011001....................000000000000000000000000000.....
............0....111...000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v8"></a>
## 8. `SULD_R_R_SNOWFLAKE`

Syntax: `SULD.P R, [R], SNOWFLAKE`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN R0, [R0],     ???255 ;`

Register access: WRITE R (4 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000110011001....................000000000000000000000000000.....
11111111....0....111...000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v9"></a>
## 9. `SULD_P_R_R_R`

Syntax: `SULD.P P, R, [R], R`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN P0, R0, [R0], R0 ;`

Register access: WRITE P (1 slots); WRITE R (4 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| operand 3 | 64-71 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000110011001....................000000000000000000000000000.....
............0..........000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v10"></a>
## 10. `SULD_P_R_R_SNOWFLAKE`

Syntax: `SULD.P P, R, [R], SNOWFLAKE`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN P0, R0, [R0],     ???255 ;`

Register access: WRITE P (1 slots); WRITE R (4 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000110011001....................000000000000000000000000000.....
11111111....0..........000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v11"></a>
## 11. `SULD_R_R_R`

Syntax: `SULD.P R, [R], R`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN R0, [R0], R0 ;`

Register access: WRITE R (4 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| operand 2 | 64-71 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000110011001....................000000000000000000000000000.....
............0....111...000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v12"></a>
## 12. `SULD_R_R_SNOWFLAKE`

Syntax: `SULD.P R, [R], SNOWFLAKE`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN R0, [R0],     ???255 ;`

Register access: WRITE R (4 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000110011001....................000000000000000000000000000.....
11111111....0....111...000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v13"></a>
## 13. `SULD_P_R_R_I_I`

Syntax: `SULD.P P, R, [R], INT_IMM, INT_IMM`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN P0, R0, [R0], 0x0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (4 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010011101....................00000000........................
00000000....0..........000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v14"></a>
## 14. `SULD_R_R_I_I`

Syntax: `SULD.P R, [R], INT_IMM, INT_IMM`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN R0, [R0], 0x0, 0x0 ;`

Register access: WRITE R (4 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010011101....................00000000........................
00000000....0....111...000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v15"></a>
## 15. `SULD_P_R_R_I_I`

Syntax: `SULD.D P, R, [R], INT_IMM, INT_IMM`  
Example: `@P0 SULD.D.1D.EF.U8.IGN P0, R0, [R0], 0x0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110011101....................00000000........................
00000000....0..........000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v16"></a>
## 16. `SULD_R_R_I_I`

Syntax: `SULD.D R, [R], INT_IMM, INT_IMM`  
Example: `@P0 SULD.D.1D.EF.U8.IGN R0, [R0], 0x0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
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
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110011101....................00000000........................
00000000....0....111...000000000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v17"></a>
## 17. `SULD_P_R_R_UR_I`

Syntax: `SULD.P P, R, [R], UR, INT_IMM`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN P0, R0, [R0], UR0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (4 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010011111....................00000000..............00000.....
00000000....0..........000010000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v18"></a>
## 18. `SULD_R_R_UR_I`

Syntax: `SULD.P R, [R], UR, INT_IMM`  
Example: `@P0 SULD.P.1D.EF.INVALID0.IGN R0, [R0], UR0, 0x0 ;`

Register access: WRITE R (4 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 40-44, 46 |
| operand 3 | 45, 47-53 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| modi 3 | 72-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111010011111....................00000000..............00000.....
00000000....0....111...000010000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v19"></a>
## 19. `SULD_P_R_R_UR_I`

Syntax: `SULD.D P, R, [R], UR, INT_IMM`  
Example: `@P0 SULD.D.1D.EF.U8.IGN P0, R0, [R0], UR0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110011111....................00000000..............00000.....
00000000....0..........000010000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

<a id="v20"></a>
## 20. `SULD_R_R_UR_I`

Syntax: `SULD.D R, [R], UR, INT_IMM`  
Example: `@P0 SULD.D.1D.EF.U8.IGN R0, [R0], UR0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 40-44, 46 |
| operand 3 | 45, 47-53 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110011111....................00000000..............00000.....
00000000....0....111...000010000000000000.....................00
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
| `0100` | `CONSTANT.` |
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

