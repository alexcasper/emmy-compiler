# RED (SM89 SASS)

**NVIDIA:** Reduction Operation on Generic Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Reduction to global memory (atomic without return) (category: Atomics / reductions)

Typically emitted for: `red.global.*`; `atomicAdd` whose result is unused

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [red](../verify/RESULTS.md#red): `red.global.add.u32 (no result)`
- [agg_red](../verify/RESULTS.md#agg_red): `red.global.add.u32 to a warp-uniform address (warp-aggregated)`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 71 | `@P0 RED.E.ADD.STRONG.GPU [R2.64], R5`<br>`RED.E.ADD.STRONG.GPU [R2.64], R5` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/RED.html> (machine-derived by fuzzing the assembler; no semantics).

7 encoding variant(s):

- [RED_I_R](#v1)
- [RED_RI_R](#v2)
- [RED_RURI_R](#v3)
- [RED_RUR_R](#v4)
- [RED_R_R](#v5)
- [RED_URI_R](#v6)
- [RED_UR_R](#v7)

<a id="v1"></a>
## 1. `RED_I_R`

Syntax: `RED [INT_IMM], R`  
Example: `@P0 RED.ADD.EF [0x20], R0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| operand 0 | 40-63 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011100011001....0000000011111111................................
00000000.........000......000000000000000.....111.............00
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
| `000` | `ADD.` |
| `001` | `MIN.` |
| `010` | `MAX.` |
| `011` | `INC.` |
| `100` | `DEC.` |
| `101` | `AND.` |
| `110` | `OR.` |
| `111` | `XOR.` |

<a id="v2"></a>
## 2. `RED_RI_R`

Syntax: `RED [R+INT_IMM], R`  
Example: `@P0 RED.ADD.EF [R0+0x1], R0 ;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 2 | 32-39 |
| operand 1 | 40-63 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011100011001....00000000........................................
00000000.........000......000000000000000.....111.............00
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
| `000` | `ADD.` |
| `001` | `MIN.` |
| `010` | `MAX.` |
| `011` | `INC.` |
| `100` | `DEC.` |
| `101` | `AND.` |
| `110` | `OR.` |
| `111` | `XOR.` |

<a id="v3"></a>
## 3. `RED_RURI_R`

Syntax: `RED [R+UR+INT_IMM], R`  
Example: `@P0 RED.ADD.EF [R0.U32+UR0+0x4], R0 ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 3 | 32-39 |
| operand 2 | 40-63 |
| operand 1 | 64-70 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| modi 5 | 90 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011100011001....00000000........................................
.......0.........000.......10000000000000.....111.............00
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
| `000` | `ADD.` |
| `001` | `MIN.` |
| `010` | `MAX.` |
| `011` | `INC.` |
| `100` | `DEC.` |
| `101` | `AND.` |
| `110` | `OR.` |
| `111` | `XOR.` |

Modifier Group 5:

| value | modifier |
|---|---|
| `0` | `(default)` |
| `1` | `???0.` |

<a id="v4"></a>
## 4. `RED_RUR_R`

Syntax: `RED [R+UR], R`  
Example: `@P0 RED.ADD.EF [R0.U32+UR0], R0 ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 2 | 32-39 |
| operand 1 | 64-70 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| modi 5 | 90 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011100011001....00000000................000000000000000000000000
.......0.........000.......10000000000000.....111.............00
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
| `000` | `ADD.` |
| `001` | `MIN.` |
| `010` | `MAX.` |
| `011` | `INC.` |
| `100` | `DEC.` |
| `101` | `AND.` |
| `110` | `OR.` |
| `111` | `XOR.` |

Modifier Group 5:

| value | modifier |
|---|---|
| `0` | `(default)` |
| `1` | `???0.` |

<a id="v5"></a>
## 5. `RED_R_R`

Syntax: `RED [R], R`  
Example: `@P0 RED.ADD.EF [R0], R0 ;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 32-39 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011100011001....00000000................000000000000000000000000
00000000.........000......000000000000000.....111.............00
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
| `000` | `ADD.` |
| `001` | `MIN.` |
| `010` | `MAX.` |
| `011` | `INC.` |
| `100` | `DEC.` |
| `101` | `AND.` |
| `110` | `OR.` |
| `111` | `XOR.` |

<a id="v6"></a>
## 6. `RED_URI_R`

Syntax: `RED [UR+INT_IMM], R`  
Example: `@P0 RED.ADD.EF [UR0+0x20], R0 ;`

Register access: READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 32-39 |
| operand 1 | 40-63 |
| operand 0 | 64-70 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011100011001....0000000011111111................................
.......0.........000......010000000000000.....111.............00
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
| `000` | `ADD.` |
| `001` | `MIN.` |
| `010` | `MAX.` |
| `011` | `INC.` |
| `100` | `DEC.` |
| `101` | `AND.` |
| `110` | `OR.` |
| `111` | `XOR.` |

<a id="v7"></a>
## 7. `RED_UR_R`

Syntax: `RED [UR], R`  
Example: `@P0 RED.ADD.EF [UR0], R0 ;`

Register access: READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| operand 0 | 64-70 |
| E | 72 |
| modi 1 | 73-76 |
| modi 2 | 77-80 |
| modi 3 | 84-86 |
| modi 4 | 87-89 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011100011001....0000000011111111........000000000000000000000000
.......0.........000......010000000000000.....111.............00
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
| `000` | `ADD.` |
| `001` | `MIN.` |
| `010` | `MAX.` |
| `011` | `INC.` |
| `100` | `DEC.` |
| `101` | `AND.` |
| `110` | `OR.` |
| `111` | `XOR.` |

