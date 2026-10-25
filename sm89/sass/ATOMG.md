# ATOMG (SM89 SASS)

**NVIDIA:** Atomic Operation on Global Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Global atomic (category: Atomics / reductions)

Typically emitted for: `atom.global.*` (`atomicAdd`, `atomicCAS`, ... with return)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [atomg](../verify/RESULTS.md#atomg): `atom.global.add.u32 (result used)`
- [agg_atomic](../verify/RESULTS.md#agg_atomic): `atom.global.add.u32 to a warp-uniform address (ptxas warp-aggregates it)`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 66 | `@P0 ATOMG.E.ADD.STRONG.GPU PT, R5, [R4.64], R9`<br>`ATOMG.E.ADD.STRONG.GPU PT, R5, [R2.64], R5` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/ATOMG.html> (machine-derived by fuzzing the assembler; no semantics).

14 encoding variant(s):

- [ATOMG_P_R_RI_R](#v1)
- [ATOMG_P_R_RURI_R](#v2)
- [ATOMG_P_R_RUR_R](#v3)
- [ATOMG_P_R_R_R](#v4)
- [ATOMG_P_R_URI_R](#v5)
- [ATOMG_P_R_UR_R](#v6)
- [ATOMG_P_R_desc[UR][RI]_R](#v7)
- [ATOMG_P_R_desc[UR][R]_R](#v8)
- [ATOMG_P_R_I_R](#v9)
- [ATOMG_P_R_RI_R](#v10)
- [ATOMG_P_R_R_R](#v11)
- [ATOMG_P_R_I_R_R](#v12)
- [ATOMG_P_R_RI_R_R](#v13)
- [ATOMG_P_R_R_R_R](#v14)

<a id="v1"></a>
## 1. `ATOMG_P_R_RI_R`

Syntax: `ATOMG P, R, [R+INT_IMM], R`  
Example: `@P0 ATOMG.???0.ADD.EF P0, R0, [R0.64+-0x800000], R0 ;`

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
000101011001....................................................
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
| `1001` | `SAFEADD.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v2"></a>
## 2. `ATOMG_P_R_RURI_R`

Syntax: `ATOMG P, R, [R+UR+INT_IMM], R`  
Example: `@P0 ATOMG.ADD.EF P0, R0, [R0.U32+UR0+0x1], R0 ;`

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
000101011001....................................................
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
| `1001` | `SAFEADD.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v3"></a>
## 3. `ATOMG_P_R_RUR_R`

Syntax: `ATOMG P, R, [R+UR], R`  
Example: `@P0 ATOMG.ADD.EF P0, R0, [R0.U32+UR0], R0 ;`

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
000101011001............................000000000000000000000000
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
| `1001` | `SAFEADD.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v4"></a>
## 4. `ATOMG_P_R_R_R`

Syntax: `ATOMG P, R, [R], R`  
Example: `@P0 ATOMG.???0.ADD.EF P0, R0, [R0.64], R0 ;`

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
000101011001............................000000000000000000000000
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
| `1001` | `SAFEADD.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v5"></a>
## 5. `ATOMG_P_R_URI_R`

Syntax: `ATOMG P, R, [UR+INT_IMM], R`  
Example: `@P0 ATOMG.ADD.EF P0, R0, [UR0+0x20], R0 ;`

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
000101011001............11111111................................
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
| `1001` | `SAFEADD.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v6"></a>
## 6. `ATOMG_P_R_UR_R`

Syntax: `ATOMG P, R, [UR], R`  
Example: `@P0 ATOMG.ADD.EF P0, R0, [UR0], R0 ;`

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
000101011001............11111111........000000000000000000000000
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
| `1001` | `SAFEADD.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v7"></a>
## 7. `ATOMG_P_R_desc[UR][RI]_R`

Syntax: `ATOMG P, R, desc[UR][R+INT_IMM], R`  
Example: `@P0 ATOMG.???0.ADD.EF P0, R0, desc[UR0][R0.64+-0x800000], R0 ;`

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
000101011001....................................................
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
| `1001` | `SAFEADD.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v8"></a>
## 8. `ATOMG_P_R_desc[UR][R]_R`

Syntax: `ATOMG P, R, desc[UR][R], R`  
Example: `@P0 ATOMG.???0.ADD.EF P0, R0, desc[UR0][R0.64], R0 ;`

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
000101011001............................000000000000000000000000
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
| `1001` | `SAFEADD.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v9"></a>
## 9. `ATOMG_P_R_I_R`

Syntax: `ATOMG P, R, [INT_IMM], R`  
Example: `@P0 ATOMG.ADD.EF P0, R0, [0x2], R0 ;`

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
000101011100............11111111................................
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
| `1001` | `SAFEADD.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v10"></a>
## 10. `ATOMG_P_R_RI_R`

Syntax: `ATOMG P, R, [R+INT_IMM], R`  
Example: `@P0 ATOMG.ADD.EF P0, R0, [R0+0x1], R0 ;`

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
000101011100....................................................
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
| `1001` | `SAFEADD.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v11"></a>
## 11. `ATOMG_P_R_R_R`

Syntax: `ATOMG P, R, [R], R`  
Example: `@P0 ATOMG.ADD.EF P0, R0, [R0], R0 ;`

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
000101011100............................000000000000000000000000
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
| `1001` | `SAFEADD.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v12"></a>
## 12. `ATOMG_P_R_I_R_R`

Syntax: `ATOMG.CAS P, R, [INT_IMM], R, R`  
Example: `@P0 ATOMG.CAS.EF P0, R0, [0x2], R0, R0 ;`

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
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101011100............11111111................................
.......................000000000000000000.....................00
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

<a id="v13"></a>
## 13. `ATOMG_P_R_RI_R_R`

Syntax: `ATOMG.CAS P, R, [R+INT_IMM], R, R`  
Example: `@P0 ATOMG.CAS.EF P0, R0, [R0+0x1], R0, R0 ;`

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
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101011100....................................................
.......................000000000000000000.....................00
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

<a id="v14"></a>
## 14. `ATOMG_P_R_R_R_R`

Syntax: `ATOMG.CAS P, R, [R], R, R`  
Example: `@P0 ATOMG.CAS.EF P0, R0, [R0], R0, R0 ;`

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
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101011100............................000000000000000000000000
.......................000000000000000000.....................00
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

