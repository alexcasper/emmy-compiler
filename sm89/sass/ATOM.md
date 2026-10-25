# ATOM (SM89 SASS)

**NVIDIA:** Atomic Operation on Generic Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Generic-address atomic (category: Atomics / reductions)

Typically emitted for: `atom` on generic pointers

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **NAK op maps to ATOMG/ATOMS/RED**. NAK encodes 0x38c, 0x38d, 0x3a8, 0x3a9, 0x98c, 0x98e, 0x9a3, 0x9a6, 0x9a8 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3777)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [atom_generic](../verify/RESULTS.md#atom_generic): `atom.add.u32 (generic)`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 66 | `ATOM.E.ADD.STRONG.GPU PT, R5, [R4.64], R7` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/ATOM.html> (machine-derived by fuzzing the assembler; no semantics).

14 encoding variant(s):

- [ATOM_P_R_RI_R](#v1)
- [ATOM_P_R_RURI_R](#v2)
- [ATOM_P_R_RUR_R](#v3)
- [ATOM_P_R_R_R](#v4)
- [ATOM_P_R_URI_R](#v5)
- [ATOM_P_R_UR_R](#v6)
- [ATOM_P_R_desc[UR][RI]_R](#v7)
- [ATOM_P_R_desc[UR][R]_R](#v8)
- [ATOM_P_R_I_R](#v9)
- [ATOM_P_R_RI_R](#v10)
- [ATOM_P_R_R_R](#v11)
- [ATOM_P_R_I_R_R](#v12)
- [ATOM_P_R_RI_R_R](#v13)
- [ATOM_P_R_R_R_R](#v14)

<a id="v1"></a>
## 1. `ATOM_P_R_RI_R`

Syntax: `ATOM P, R, [R+INT_IMM], R`  
Example: `@P0 ATOM.???0.ADD.EF P0, R0, [R0.64+-0x800000], R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-39 |
| operand 3 | 40-63 |
| modi 1 | 72 |
| modi 2 | 73-76 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| modi 5 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100011001....................................................
00000011...................10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `F32.FTZ.RN.` |
| `0100` | `F16x2.RN.` |
| `0101` | `S64.` |
| `0110` | `F64.RN.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Modifier Group 3:

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

Modifier Group 4:

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

Modifier Group 5:

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
## 2. `ATOM_P_R_RURI_R`

Syntax: `ATOM P, R, [R+UR+INT_IMM], R`  
Example: `@P0 ATOM.ADD.EF P0, R0, [R0.U32+UR0+0x1], R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 5 | 32-39 |
| operand 4 | 40-63 |
| operand 3 | 64-70 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100011001....................................................
.......0...................10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `F32.FTZ.RN.` |
| `0100` | `F16x2.RN.` |
| `0101` | `S64.` |
| `0110` | `F64.RN.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Modifier Group 2:

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

Modifier Group 3:

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

Modifier Group 4:

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
## 3. `ATOM_P_R_RUR_R`

Syntax: `ATOM P, R, [R+UR], R`  
Example: `@P0 ATOM.ADD.EF P0, R0, [R0.U32+UR0], R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-39 |
| operand 3 | 64-70 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100011001............................000000000000000000000000
.......0...................10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `F32.FTZ.RN.` |
| `0100` | `F16x2.RN.` |
| `0101` | `S64.` |
| `0110` | `F64.RN.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Modifier Group 2:

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

Modifier Group 3:

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

Modifier Group 4:

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

<a id="v4"></a>
## 4. `ATOM_P_R_R_R`

Syntax: `ATOM P, R, [R], R`  
Example: `@P0 ATOM.???0.ADD.EF P0, R0, [R0.64], R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 72 |
| modi 2 | 73-76 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| modi 5 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100011001............................000000000000000000000000
00000011...................10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `F32.FTZ.RN.` |
| `0100` | `F16x2.RN.` |
| `0101` | `S64.` |
| `0110` | `F64.RN.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Modifier Group 3:

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

Modifier Group 4:

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

Modifier Group 5:

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

<a id="v5"></a>
## 5. `ATOM_P_R_URI_R`

Syntax: `ATOM P, R, [UR+INT_IMM], R`  
Example: `@P0 ATOM.ADD.EF P0, R0, [UR0+0x20], R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 4 | 32-39 |
| operand 3 | 40-63 |
| operand 2 | 64-70 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100011001............11111111................................
.......0...................10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `F32.FTZ.RN.` |
| `0100` | `F16x2.RN.` |
| `0101` | `S64.` |
| `0110` | `F64.RN.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Modifier Group 2:

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

Modifier Group 3:

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

Modifier Group 4:

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
## 6. `ATOM_P_R_UR_R`

Syntax: `ATOM P, R, [UR], R`  
Example: `@P0 ATOM.ADD.EF P0, R0, [UR0], R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 2 | 64-70 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100011001............11111111........000000000000000000000000
.......0...................10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `F32.FTZ.RN.` |
| `0100` | `F16x2.RN.` |
| `0101` | `S64.` |
| `0110` | `F64.RN.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Modifier Group 2:

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

Modifier Group 3:

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

Modifier Group 4:

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
## 7. `ATOM_P_R_desc[UR][RI]_R`

Syntax: `ATOM P, R, desc[UR][R+INT_IMM], R`  
Example: `@P0 ATOM.???0.ADD.EF P0, R0, desc[UR0][R0.64+-0x800000], R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 24-31 |
| operand 5 | 32-39 |
| operand 4 | 40-63 |
| operand 2 | 64-69 |
| modi 1 | 72 |
| modi 2 | 73-76 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| modi 5 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100011001....................................................
......11...................10000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `F32.FTZ.RN.` |
| `0100` | `F16x2.RN.` |
| `0101` | `S64.` |
| `0110` | `F64.RN.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Modifier Group 3:

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

Modifier Group 4:

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

Modifier Group 5:

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

<a id="v8"></a>
## 8. `ATOM_P_R_desc[UR][R]_R`

Syntax: `ATOM P, R, desc[UR][R], R`  
Example: `@P0 ATOM.???0.ADD.EF P0, R0, desc[UR0][R0.64], R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-39 |
| operand 2 | 64-69 |
| modi 1 | 72 |
| modi 2 | 73-76 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| modi 5 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100011001............................000000000000000000000000
......11...................10000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `F32.FTZ.RN.` |
| `0100` | `F16x2.RN.` |
| `0101` | `S64.` |
| `0110` | `F64.RN.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Modifier Group 3:

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

Modifier Group 4:

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

Modifier Group 5:

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

<a id="v9"></a>
## 9. `ATOM_P_R_I_R`

Syntax: `ATOM P, R, [INT_IMM], R`  
Example: `@P0 ATOM.ADD.EF P0, R0, [0x2], R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 2 | 40-63 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100011100............11111111................................
00000000...................00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `F32.FTZ.RN.` |
| `0100` | `F16x2.RN.` |
| `0101` | `S64.` |
| `0110` | `F64.RN.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Modifier Group 2:

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

Modifier Group 3:

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

Modifier Group 4:

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
## 10. `ATOM_P_R_RI_R`

Syntax: `ATOM P, R, [R+INT_IMM], R`  
Example: `@P0 ATOM.ADD.EF P0, R0, [R0+0x1], R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-39 |
| operand 3 | 40-63 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100011100....................................................
00000000...................00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `F32.FTZ.RN.` |
| `0100` | `F16x2.RN.` |
| `0101` | `S64.` |
| `0110` | `F64.RN.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Modifier Group 2:

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

Modifier Group 3:

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

Modifier Group 4:

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
## 11. `ATOM_P_R_R_R`

Syntax: `ATOM P, R, [R], R`  
Example: `@P0 ATOM.ADD.EF P0, R0, [R0], R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010100011100............................000000000000000000000000
00000000...................00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `F32.FTZ.RN.` |
| `0100` | `F16x2.RN.` |
| `0101` | `S64.` |
| `0110` | `F64.RN.` |
| `0111` | `INVALID7.` |
| `1000` | `INVALID8.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Modifier Group 2:

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

Modifier Group 3:

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

Modifier Group 4:

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

<a id="v12"></a>
## 12. `ATOM_P_R_I_R_R`

Syntax: `ATOM P, R, [INT_IMM], R, R`  
Example: `@P0 ATOM.CAS.EF P0, R0, [0x2], R0, R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 32-39 |
| operand 2 | 40-63 |
| operand 4 | 64-71 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110100011100............11111111................................
........................00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `INVALID3.` |
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
| `1111` | `INVALID15.` |

Modifier Group 2:

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

Modifier Group 3:

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

Modifier Group 4:

| value | modifier |
|---|---|
| `0` | `CAS.` |
| `1` | `CAST.` |

<a id="v13"></a>
## 13. `ATOM_P_R_RI_R_R`

Syntax: `ATOM P, R, [R+INT_IMM], R, R`  
Example: `@P0 ATOM.CAS.EF P0, R0, [R0+0x1], R0, R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-39 |
| operand 3 | 40-63 |
| operand 5 | 64-71 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110100011100....................................................
........................00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `INVALID3.` |
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
| `1111` | `INVALID15.` |

Modifier Group 2:

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

Modifier Group 3:

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

Modifier Group 4:

| value | modifier |
|---|---|
| `0` | `CAS.` |
| `1` | `CAST.` |

<a id="v14"></a>
## 14. `ATOM_P_R_R_R_R`

Syntax: `ATOM P, R, [R], R, R`  
Example: `@P0 ATOM.CAS.EF P0, R0, [R0], R0, R0 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 64-71 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| operand 0 | 81-83 |
| modi 3 | 84-86 |
| modi 4 | 87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110100011100............................000000000000000000000000
........................00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `(default)` |
| `0001` | `S32.` |
| `0010` | `64.` |
| `0011` | `INVALID3.` |
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
| `1111` | `INVALID15.` |

Modifier Group 2:

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

Modifier Group 3:

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

Modifier Group 4:

| value | modifier |
|---|---|
| `0` | `CAS.` |
| `1` | `CAST.` |

