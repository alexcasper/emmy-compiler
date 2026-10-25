# SUATOM (SM89 SASS)

**NVIDIA:** Atomic Op on Surface Memory (Surface Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Surface atomic (category: Texture / surface)

Typically emitted for: surface atomics with return; PTX `sured` (no return) lowers to SURED instead (probe `sured`)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x394, 0x396, 0x3a0 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3391)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/SUATOM.html> (machine-derived by fuzzing the assembler; no semantics).

20 encoding variant(s):

- [SUATOM_P_R_R_R_I_I](#v1)
- [SUATOM_R_R_R_I_I](#v2)
- [SUATOM_P_R_R_R_I_I](#v3)
- [SUATOM_R_R_R_I_I](#v4)
- [SUATOM_P_R_R_R_I_I_I](#v5)
- [SUATOM_R_R_R_I_I_I](#v6)
- [SUATOM_P_R_R_R_I_I_I](#v7)
- [SUATOM_R_R_R_I_I_I](#v8)
- [SUATOM_P_R_R_R_UR_I](#v9)
- [SUATOM_R_R_R_UR_I](#v10)
- [SUATOM_P_R_R_R_UR_I](#v11)
- [SUATOM_R_R_R_UR_I](#v12)
- [SUATOM_P_R_R_R_R](#v13)
- [SUATOM_P_R_R_R_SNOWFLAKE](#v14)
- [SUATOM_R_R_R_R](#v15)
- [SUATOM_R_R_R_SNOWFLAKE](#v16)
- [SUATOM_P_R_R_R_R](#v17)
- [SUATOM_P_R_R_R_SNOWFLAKE](#v18)
- [SUATOM_R_R_R_R](#v19)
- [SUATOM_R_R_R_SNOWFLAKE](#v20)

<a id="v1"></a>
## 1. `SUATOM_P_R_R_R_I_I`

Syntax: `SUATOM.D P, R, [R], R, INT_IMM, INT_IMM`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN P0, R0, [R0], R0, 0x0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010011010....................................................
00000000....0..............00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v2"></a>
## 2. `SUATOM_R_R_R_I_I`

Syntax: `SUATOM.D R, [R], R, INT_IMM, INT_IMM`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN R0, [R0], R0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010011010....................................................
00000000....0....111.......00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v3"></a>
## 3. `SUATOM_P_R_R_R_I_I`

Syntax: `SUATOM.D.CAS P, R, [R], R, INT_IMM, INT_IMM`  
Example: `@P0 SUATOM.D.1D.CAS.EF.IGN P0, R0, [R0], R0, 0x0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-52, 54 |
| operand 4 | 53, 55-58 |
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
101010011010....................................................
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `INVALID3.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
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

<a id="v4"></a>
## 4. `SUATOM_R_R_R_I_I`

Syntax: `SUATOM.D.CAS R, [R], R, INT_IMM, INT_IMM`  
Example: `@P0 SUATOM.D.1D.CAS.EF.IGN R0, [R0], R0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
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
101010011010....................................................
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `INVALID3.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
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

<a id="v5"></a>
## 5. `SUATOM_P_R_R_R_I_I_I`

Syntax: `SUATOM.D P, R, [R], R, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN P0, R0, [R0], R0, 0x0, 0x0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010011110....................................................
00000000....0..............00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v6"></a>
## 6. `SUATOM_R_R_R_I_I_I`

Syntax: `SUATOM.D R, [R], R, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN R0, [R0], R0, 0x0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-52 |
| operand 3 | 53-58 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010011110....................................................
00000000....0....111.......00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v7"></a>
## 7. `SUATOM_P_R_R_R_I_I_I`

Syntax: `SUATOM.D.CAS P, R, [R], R, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 SUATOM.D.1D.CAS.EF.IGN P0, R0, [R0], R0, 0x0, 0x0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 5 | 40-44, 46 |
| operand 6 | 45, 47-52 |
| operand 4 | 53-58 |
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
101010011110....................................................
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `INVALID3.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
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

<a id="v8"></a>
## 8. `SUATOM_R_R_R_I_I_I`

Syntax: `SUATOM.D.CAS R, [R], R, INT_IMM, INT_IMM, INT_IMM`  
Example: `@P0 SUATOM.D.1D.CAS.EF.IGN R0, [R0], R0, 0x0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-52 |
| operand 3 | 53-58 |
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
101010011110....................................................
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `INVALID3.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
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

<a id="v9"></a>
## 9. `SUATOM_P_R_R_R_UR_I`

Syntax: `SUATOM.D P, R, [R], R, UR, INT_IMM`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN P0, R0, [R0], R0, UR0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010011111..........................................00000.....
00000000....0..............10000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v10"></a>
## 10. `SUATOM_R_R_R_UR_I`

Syntax: `SUATOM.D R, [R], R, UR, INT_IMM`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN R0, [R0], R0, UR0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010011111..........................................00000.....
00000000....0....111.......10000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v11"></a>
## 11. `SUATOM_P_R_R_R_UR_I`

Syntax: `SUATOM.D.CAS P, R, [R], R, UR, INT_IMM`  
Example: `@P0 SUATOM.D.1D.CAS.EF.IGN P0, R0, [R0], R0, UR0, 0x0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (2 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-44, 46 |
| operand 5 | 45, 47-53 |
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
101010011111..........................................00000.....
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `INVALID3.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
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

<a id="v12"></a>
## 12. `SUATOM_R_R_R_UR_I`

Syntax: `SUATOM.D.CAS R, [R], R, UR, INT_IMM`  
Example: `@P0 SUATOM.D.1D.CAS.EF.IGN R0, [R0], R0, UR0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (2 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 40-44, 46 |
| operand 4 | 45, 47-53 |
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
101010011111..........................................00000.....
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `INVALID3.` |
| `100` | `INVALID4.` |
| `101` | `INVALID5.` |
| `110` | `INVALID6.` |
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

<a id="v13"></a>
## 13. `SUATOM_P_R_R_R_R`

Syntax: `SUATOM.D P, R, [R], R, R`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN P0, R0, [R0], R0, R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| operand 4 | 64-71 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010011100............................0000000000000000000.....
............0..............00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v14"></a>
## 14. `SUATOM_P_R_R_R_SNOWFLAKE`

Syntax: `SUATOM.D P, R, [R], R, SNOWFLAKE`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN P0, R0, [R0], R0,     ???255 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010011100............................0000000000000000000.....
11111111....0..............00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v15"></a>
## 15. `SUATOM_R_R_R_R`

Syntax: `SUATOM.D R, [R], R, R`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN R0, [R0], R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| operand 3 | 64-71 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010011100............................0000000000000000000.....
............0....111.......00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v16"></a>
## 16. `SUATOM_R_R_R_SNOWFLAKE`

Syntax: `SUATOM.D R, [R], R, SNOWFLAKE`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN R0, [R0], R0,     ???255 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010011100............................0000000000000000000.....
11111111....0....111.......00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v17"></a>
## 17. `SUATOM_P_R_R_R_R`

Syntax: `SUATOM.D P, R, [R], R, R`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN P0, R0, [R0], R0, R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| operand 4 | 64-71 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010011100............................0000000000000000000.....
............0..............00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v18"></a>
## 18. `SUATOM_P_R_R_R_SNOWFLAKE`

Syntax: `SUATOM.D P, R, [R], R, SNOWFLAKE`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN P0, R0, [R0], R0,     ???255 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| operand 0 | 81-83 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010011100............................0000000000000000000.....
11111111....0..............00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v19"></a>
## 19. `SUATOM_R_R_R_R`

Syntax: `SUATOM.D R, [R], R, R`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN R0, [R0], R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| operand 3 | 64-71 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010011100............................0000000000000000000.....
............0....111.......00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v20"></a>
## 20. `SUATOM_R_R_R_SNOWFLAKE`

Syntax: `SUATOM.D R, [R], R, SNOWFLAKE`  
Example: `@P0 SUATOM.D.1D.ADD.EF.IGN R0, [R0], R0,     ???255 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi 1 | 59-60 |
| modi 2 | 61-63 |
| BA | 72 |
| modi 3 | 73-75 |
| modi 4 | 77-80 |
| modi 5 | 84-86 |
| modi 6 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001010011100............................0000000000000000000.....
11111111....0....111.......00000000000000.....................00
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
| `000` | `(default)` |
| `001` | `S32.` |
| `010` | `U64.` |
| `011` | `F32.FTZ.RN.` |
| `100` | `F16x2.RN.` |
| `101` | `S64.` |
| `110` | `SD32.` |
| `111` | `SD64.` |

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

Modifier Group 6:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

