# LDG (SM89 SASS)

**NVIDIA:** Load from Global Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Load from global memory (category: Load / store)

Typically emitted for: `ld.global[.nc/.ca/.cg/.cs/.lu]` (`__ldg`, plain global loads; vectorized .v2/.v4 -> LDG.E.64/.128)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [ldg_nc](../verify/RESULTS.md#ldg_nc): `ld.global.nc.v4.f32`
- [prologue](../verify/RESULTS.md#prologue): `empty kernel body: param pointer + %tid.x load/store`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 34 | `@P0 LDG.E R5, [R2.64+0x14]`<br>`LDG.E R0, [R2.64+0x10]`<br>`LDG.E R0, [R2.64+0x8]` |
| 76 | `LDG.E R0, [R2.64]` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/LDG.html> (machine-derived by fuzzing the assembler; no semantics).

56 encoding variant(s):

- [LDG_R_R_RI_I](#v1)
- [LDG_R_R_RI_I_P](#v2)
- [LDG_R_R_RURI_I](#v3)
- [LDG_R_R_RURI_I_P](#v4)
- [LDG_R_R_RUR_I](#v5)
- [LDG_R_R_RUR_I_P](#v6)
- [LDG_R_R_R_I](#v7)
- [LDG_R_R_R_I_P](#v8)
- [LDG_R_R_URI_I](#v9)
- [LDG_R_R_URI_I_P](#v10)
- [LDG_R_R_UR_I](#v11)
- [LDG_R_R_UR_I_P](#v12)
- [LDG_R_R_desc[UR][RI]_I](#v13)
- [LDG_R_R_desc[UR][RI]_I_P](#v14)
- [LDG_R_R_desc[UR][R]_I](#v15)
- [LDG_R_R_desc[UR][R]_I_P](#v16)
- [LDG_P_R_R](#v17)
- [LDG_P_R_RI](#v18)
- [LDG_P_R_RI_P](#v19)
- [LDG_P_R_RUR](#v20)
- [LDG_P_R_RURI](#v21)
- [LDG_P_R_RURI_P](#v22)
- [LDG_P_R_RUR_P](#v23)
- [LDG_P_R_R_P](#v24)
- [LDG_P_R_UR](#v25)
- [LDG_P_R_URI](#v26)
- [LDG_P_R_URI_P](#v27)
- [LDG_P_R_UR_P](#v28)
- [LDG_P_R_desc[UR][RI]](#v29)
- [LDG_P_R_desc[UR][RI]_P](#v30)
- [LDG_P_R_desc[UR][R]](#v31)
- [LDG_P_R_desc[UR][R]_P](#v32)
- [LDG_R_R](#v33)
- [LDG_R_RI](#v34)
- [LDG_R_RI_P](#v35)
- [LDG_R_RUR](#v36)
- [LDG_R_RURI](#v37)
- [LDG_R_RURI_P](#v38)
- [LDG_R_RUR_P](#v39)
- [LDG_R_R_P](#v40)
- [LDG_R_desc[UR][RI]](#v41)
- [LDG_R_desc[UR][RI]_P](#v42)
- [LDG_R_desc[UR][R]](#v43)
- [LDG_R_desc[UR][R]_P](#v44)
- [LDG_P_R_I](#v45)
- [LDG_P_R_I_P](#v46)
- [LDG_P_R_R](#v47)
- [LDG_P_R_RI](#v48)
- [LDG_P_R_RI_P](#v49)
- [LDG_P_R_R_P](#v50)
- [LDG_R_I](#v51)
- [LDG_R_I_P](#v52)
- [LDG_R_R](#v53)
- [LDG_R_RI](#v54)
- [LDG_R_RI_P](#v55)
- [LDG_R_R_P](#v56)

<a id="v1"></a>
## 1. `LDG_R_R_RI_I`

Syntax: `LDG.E.256.EFL2 R, R, [R+INT_IMM], INT_IMM`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [R0.64+0x100000], 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 37-39, 58, 60-63, 72 |
| operand 3 | 40-57, 59 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001....................00000...........................
...........11......0...000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

<a id="v2"></a>
## 2. `LDG_R_R_RI_I_P`

Syntax: `LDG.E.256.EFL2 R, R, [R+INT_IMM], INT_IMM, P`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [R0.64+0x80], 0x0, !PT ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 37-39, 58-63, 72 |
| operand 3 | 40-57 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| operand 5 | 87-89 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001....................00000...........................
...........11......0......110000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

<a id="v3"></a>
## 3. `LDG_R_R_RURI_I`

Syntax: `LDG.E.256.EFL2 R, R, [R+UR+INT_IMM], INT_IMM`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [R0.U32+UR0+0x20], 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-36, 38 |
| operand 5 | 37, 39, 58-63, 72 |
| operand 4 | 40-57 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi (op 2) | 75 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001....................................................
............0......0...000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v4"></a>
## 4. `LDG_R_R_RURI_I_P`

Syntax: `LDG.E.256.EFL2 R, R, [R+UR+INT_IMM], INT_IMM, P`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [R0.U32+UR0+0x20], 0x0, P6 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-36, 38 |
| operand 5 | 37, 39, 58-63, 72 |
| operand 4 | 40-57 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi (op 2) | 75 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| operand 6 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001....................................................
............0......0...1...10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v5"></a>
## 5. `LDG_R_R_RUR_I`

Syntax: `LDG.E.256.EFL2 R, R, [R+UR], INT_IMM`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [R0.U32+UR0], 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-36, 38 |
| operand 4 | 37, 39, 59-63, 72 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi (op 2) | 75 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001............................0000000000000000000.....
............0......0...000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v6"></a>
## 6. `LDG_R_R_RUR_I_P`

Syntax: `LDG.E.256.EFL2 R, R, [R+UR], INT_IMM, P`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [R0.U32+UR0], 0x0, P6 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-36, 38 |
| operand 4 | 37, 39, 59-63, 72 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi (op 2) | 75 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| operand 5 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001............................0000000000000000000.....
............0......0...1...10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v7"></a>
## 7. `LDG_R_R_R_I`

Syntax: `LDG.E.256.EFL2 R, R, [R], INT_IMM`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [R0.64], 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 37-39, 59-63, 72 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001....................00000...0000000000000000000.....
...........11......0...000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

<a id="v8"></a>
## 8. `LDG_R_R_R_I_P`

Syntax: `LDG.E.256.EFL2 R, R, [R], INT_IMM, P`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [R0.64], 0x0, P6 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 37-39, 59-63, 72 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| operand 4 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001....................00000...0000000000000000000.....
...........11......0...1...10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

<a id="v9"></a>
## 9. `LDG_R_R_URI_I`

Syntax: `LDG.E.256.EFL2 R, R, [UR+INT_IMM], INT_IMM`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [UR0+0x400], 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 32-36, 38 |
| operand 4 | 37, 39, 58-63, 72 |
| operand 3 | 40-57 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001............11111111................................
...........00......0...000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

<a id="v10"></a>
## 10. `LDG_R_R_URI_I_P`

Syntax: `LDG.E.256.EFL2 R, R, [UR+INT_IMM], INT_IMM, P`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [UR0+0x400], 0x0, P6 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ UR (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 32-36, 38 |
| operand 4 | 37, 39, 58-63, 72 |
| operand 3 | 40-57 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| operand 5 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001............11111111................................
...........00......0...1...10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

<a id="v11"></a>
## 11. `LDG_R_R_UR_I`

Syntax: `LDG.E.256.EFL2 R, R, [UR], INT_IMM`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [UR0], 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 32-36, 38 |
| operand 3 | 37, 39, 59-63, 72 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001............11111111........0000000000000000000.....
...........00......0...000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

<a id="v12"></a>
## 12. `LDG_R_R_UR_I_P`

Syntax: `LDG.E.256.EFL2 R, R, [UR], INT_IMM, P`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, [UR0], 0x0, P6 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ UR (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 32-36, 38 |
| operand 3 | 37, 39, 59-63, 72 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| operand 4 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001............11111111........0000000000000000000.....
...........00......0...1...10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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
## 13. `LDG_R_R_desc[UR][RI]_I`

Syntax: `LDG.E.256.EFL2 R, R, desc[UR][R+INT_IMM], INT_IMM`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, desc[UR0][R0.64+0x100000], 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 24-31 |
| operand 2 | 32-36, 38 |
| operand 5 | 37, 39, 58, 60-63, 72 |
| operand 4 | 40-57, 59 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001....................................................
...........11......0...000010000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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
## 14. `LDG_R_R_desc[UR][RI]_I_P`

Syntax: `LDG.E.256.EFL2 R, R, desc[UR][R+INT_IMM], INT_IMM, P`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, desc[UR0][R0.64+0x80], 0x0, !PT ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 24-31 |
| operand 2 | 32-36, 38 |
| operand 5 | 37, 39, 58-63, 72 |
| operand 4 | 40-57 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| operand 6 | 87-89 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001....................................................
...........11......0......110000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

<a id="v15"></a>
## 15. `LDG_R_R_desc[UR][R]_I`

Syntax: `LDG.E.256.EFL2 R, R, desc[UR][R], INT_IMM`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, desc[UR0][R0.64], 0x0 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 24-31 |
| operand 2 | 32-36, 38 |
| operand 4 | 37, 39, 59-63, 72 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001............................0000000000000000000.....
...........11......0...000010000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

<a id="v16"></a>
## 16. `LDG_R_R_desc[UR][R]_I_P`

Syntax: `LDG.E.256.EFL2 R, R, desc[UR][R], INT_IMM, P`  
Example: `@P0 LDG.E.EF.EFL2.256 R0, R0, desc[UR0][R0.64], 0x0, P6 ;`

Register access: WRITE R (1 slots); WRITE R (1 slots); READ UR (2 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 24-31 |
| operand 2 | 32-36, 38 |
| operand 4 | 37, 39, 59-63, 72 |
| operand 0 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 77-82 |
| modi 3 | 84-86 |
| operand 5 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111101001............................0000000000000000000.....
...........11......0...1...10000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000000` | `(default)` |
| `000001` | `CONSTANT.PRIVATE.` |
| `000010` | `CONSTANT.CTA.` |
| `000011` | `CONSTANT.CTA.PRIVATE.` |
| `000100` | `CONSTANT.` |
| `000101` | `STRONG.SM.` |
| `000110` | `STRONG.GPU.PRIVATE.` |
| `000111` | `STRONG.GPU.` |
| `001000` | `MMIO.GPU.` |
| `001001` | `CONSTANT.SM.` |
| `001010` | `STRONG.SYS.` |
| `001011` | `CONSTANT.SM.PRIVATE.` |
| `001100` | `MMIO.SYS.` |
| `001101` | `CONSTANT.VC.` |
| `001110` | `CONSTANT.VC.PRIVATE.` |
| `001111` | `CONSTANT.GPU.` |
| `010000` | `ENL2.` |
| `010001` | `ENL2.CONSTANT.PRIVATE.` |
| `010010` | `ENL2.CONSTANT.CTA.` |
| `010011` | `ENL2.CONSTANT.CTA.PRIVATE.` |
| `010100` | `ENL2.CONSTANT.` |
| `010101` | `ENL2.STRONG.SM.` |
| `010110` | `ENL2.STRONG.GPU.PRIVATE.` |
| `010111` | `ENL2.STRONG.GPU.` |
| `011000` | `ENL2.MMIO.GPU.` |
| `011001` | `ENL2.CONSTANT.SM.` |
| `011010` | `ENL2.STRONG.SYS.` |
| `011011` | `ENL2.CONSTANT.SM.PRIVATE.` |
| `011100` | `ENL2.MMIO.SYS.` |
| `011101` | `ENL2.CONSTANT.VC.` |
| `011110` | `ENL2.CONSTANT.VC.PRIVATE.` |
| `011111` | `ENL2.CONSTANT.GPU.` |
| `100000` | `ELL2.` |
| `100001` | `ELL2.CONSTANT.PRIVATE.` |
| `100010` | `ELL2.CONSTANT.CTA.` |
| `100011` | `ELL2.CONSTANT.CTA.PRIVATE.` |
| `100100` | `ELL2.CONSTANT.` |
| `100101` | `ELL2.STRONG.SM.` |
| `100110` | `ELL2.STRONG.GPU.PRIVATE.` |
| `100111` | `ELL2.STRONG.GPU.` |
| `101000` | `ELL2.MMIO.GPU.` |
| `101001` | `ELL2.CONSTANT.SM.` |
| `101010` | `ELL2.STRONG.SYS.` |
| `101011` | `ELL2.CONSTANT.SM.PRIVATE.` |
| `101100` | `ELL2.MMIO.SYS.` |
| `101101` | `ELL2.CONSTANT.VC.` |
| `101110` | `ELL2.CONSTANT.VC.PRIVATE.` |
| `101111` | `ELL2.CONSTANT.GPU.` |
| `110000` | `INVALID3.` |
| `110001` | `INVALID3.CONSTANT.PRIVATE.` |
| `110010` | `INVALID3.CONSTANT.CTA.` |
| `110011` | `INVALID3.CONSTANT.CTA.PRIVATE.` |
| `110100` | `INVALID3.CONSTANT.` |
| `110101` | `INVALID3.STRONG.SM.` |
| `110110` | `INVALID3.STRONG.GPU.PRIVATE.` |
| `110111` | `INVALID3.STRONG.GPU.` |
| `111000` | `INVALID3.MMIO.GPU.` |
| `111001` | `INVALID3.CONSTANT.SM.` |
| `111010` | `INVALID3.STRONG.SYS.` |
| `111011` | `INVALID3.CONSTANT.SM.PRIVATE.` |
| `111100` | `INVALID3.MMIO.SYS.` |
| `111101` | `INVALID3.CONSTANT.VC.` |
| `111110` | `INVALID3.CONSTANT.VC.PRIVATE.` |
| `111111` | `INVALID3.CONSTANT.GPU.` |

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

<a id="v17"></a>
## 17. `LDG_P_R_R`

Syntax: `LDG P, R, [R]`  
Example: `@P0 LDG.???0.EF.U8 P0, R0, [R0.64] ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001....................00000000000000000000000000000000
0000..00....1..........000110000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v18"></a>
## 18. `LDG_P_R_RI`

Syntax: `LDG P, R, [R+INT_IMM]`  
Example: `@P0 LDG.???0.EF.U8 P0, R0, [R0.64+0x4] ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-63 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001....................00000000........................
0000..00....1..........000110000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v19"></a>
## 19. `LDG_P_R_RI_P`

Syntax: `LDG P, R, [R+INT_IMM], P`  
Example: `@P0 LDG.???0.EF.U8 P0, R0, [R0.64+0x1], P5 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-63 |
| operand 4 | 64-66 |
| cNOT (op 4) | 67 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001....................00000000........................
......00....1..........000110000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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
## 20. `LDG_P_R_RUR`

Syntax: `LDG P, R, [R+UR]`  
Example: `@P0 LDG.EF.U8 P0, R0, [R0.U32+UR0] ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| modi (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001...........................0000000000000000000000000
0000..00....0..........000.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v21"></a>
## 21. `LDG_P_R_RURI`

Syntax: `LDG P, R, [R+UR+INT_IMM]`  
Example: `@P0 LDG.EF.U8 P0, R0, [R0.U32+UR0+0x1] ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-63 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| modi (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001...........................0........................
0000..00....0..........000.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v22"></a>
## 22. `LDG_P_R_RURI_P`

Syntax: `LDG P, R, [R+UR+INT_IMM], P`  
Example: `@P0 LDG.EF.U8 P0, R0, [R0.U32+UR0+0x1], P6 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-63 |
| operand 5 | 64-66 |
| cNOT (op 5) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| modi (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001...........................0........................
......00....0..........000.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v23"></a>
## 23. `LDG_P_R_RUR_P`

Syntax: `LDG P, R, [R+UR], P`  
Example: `@P0 LDG.EF.U8 P0, R0, [R0.U32+UR0], P6 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 64-66 |
| cNOT (op 4) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| modi (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001...........................0000000000000000000000000
......00....0..........000.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v24"></a>
## 24. `LDG_P_R_R_P`

Syntax: `LDG P, R, [R], P`  
Example: `@P0 LDG.???0.EF.U8 P0, R0, [R0.64], P5 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 64-66 |
| cNOT (op 3) | 67 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001....................00000000000000000000000000000000
......00....1..........000110000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v25"></a>
## 25. `LDG_P_R_UR`

Syntax: `LDG P, R, [UR]`  
Example: `@P0 LDG.EF.U8 P0, R0, [UR0] ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 32-38 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001............11111111.......0000000000000000000000000
0000..00....0..........000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v26"></a>
## 26. `LDG_P_R_URI`

Syntax: `LDG P, R, [UR+INT_IMM]`  
Example: `@P0 LDG.EF.U8 P0, R0, [UR0+0x2] ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 32-38 |
| operand 3 | 40-63 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001............11111111.......0........................
0000..00....0..........000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v27"></a>
## 27. `LDG_P_R_URI_P`

Syntax: `LDG P, R, [UR+INT_IMM], P`  
Example: `@P0 LDG.EF.U8 P0, R0, [UR0+0x20], P6 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 32-38 |
| operand 3 | 40-63 |
| operand 4 | 64-66 |
| cNOT (op 4) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001............11111111.......0........................
......00....0..........000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v28"></a>
## 28. `LDG_P_R_UR_P`

Syntax: `LDG P, R, [UR], P`  
Example: `@P0 LDG.EF.U8 P0, R0, [UR0], P6 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 32-38 |
| operand 3 | 64-66 |
| cNOT (op 3) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001............11111111.......0000000000000000000000000
......00....0..........000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v29"></a>
## 29. `LDG_P_R_desc[UR][RI]`

Syntax: `LDG P, R, desc[UR][R+INT_IMM]`  
Example: `@P0 LDG.???0.EF.U8 P0, R0, desc[UR0][R0.64+0x4] ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 24-31 |
| operand 2 | 32-38 |
| operand 4 | 40-63 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001...........................0........................
0000..00....1..........000110000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v30"></a>
## 30. `LDG_P_R_desc[UR][RI]_P`

Syntax: `LDG P, R, desc[UR][R+INT_IMM], P`  
Example: `@P0 LDG.???0.EF.U8 P0, R0, desc[UR0][R0.64+0x1], P5 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 24-31 |
| operand 2 | 32-38 |
| operand 4 | 40-63 |
| operand 5 | 64-66 |
| cNOT (op 5) | 67 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001...........................0........................
......00....1..........000110000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v31"></a>
## 31. `LDG_P_R_desc[UR][R]`

Syntax: `LDG P, R, desc[UR][R]`  
Example: `@P0 LDG.???0.EF.U8 P0, R0, desc[UR0][R0.64] ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 24-31 |
| operand 2 | 32-38 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001...........................0000000000000000000000000
0000..00....1..........000110000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v32"></a>
## 32. `LDG_P_R_desc[UR][R]_P`

Syntax: `LDG P, R, desc[UR][R], P`  
Example: `@P0 LDG.???0.EF.U8 P0, R0, desc[UR0][R0.64], P5 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 3 | 24-31 |
| operand 2 | 32-38 |
| operand 4 | 64-66 |
| cNOT (op 4) | 67 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001...........................0000000000000000000000000
......00....1..........000110000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v33"></a>
## 33. `LDG_R_R`

Syntax: `LDG R, [R]`  
Example: `@P0 LDG.???0.EF.U8 R0, [R0.64] ;`

Register access: WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001....................00000000000000000000000000000000
0000..00....1....111...000110000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v34"></a>
## 34. `LDG_R_RI`

Syntax: `LDG R, [R+INT_IMM]`  
Example: `@P0 LDG.???0.EF.U8 R0, [R0.64+0x4] ;`

Register access: WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 40-63 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001....................00000000........................
0000..00....1....111...000110000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v35"></a>
## 35. `LDG_R_RI_P`

Syntax: `LDG R, [R+INT_IMM], P`  
Example: `@P0 LDG.???0.EF.U8 R0, [R0.64+0x4], P6 ;`

Register access: WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 40-63 |
| operand 3 | 64-66 |
| cNOT (op 3) | 67 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001....................00000000........................
......00....1....111...000110000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v36"></a>
## 36. `LDG_R_RUR`

Syntax: `LDG R, [R+UR]`  
Example: `@P0 LDG.EF.U8 R0, [R0.U32+UR0] ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| modi (op 1) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001...........................0000000000000000000000000
0000..00....0....111...000.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v37"></a>
## 37. `LDG_R_RURI`

Syntax: `LDG R, [R+UR+INT_IMM]`  
Example: `@P0 LDG.EF.U8 R0, [R0.U32+UR0+0x4] ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-63 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| modi (op 1) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001...........................0........................
0000..00....0....111...000.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v38"></a>
## 38. `LDG_R_RURI_P`

Syntax: `LDG R, [R+UR+INT_IMM], P`  
Example: `@P0 LDG.EF.U8 R0, [R0.U32+UR0+-0x800000], P6 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-63 |
| operand 4 | 64-66 |
| cNOT (op 4) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| modi (op 1) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001...........................0........................
......00....0....111...000.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v39"></a>
## 39. `LDG_R_RUR_P`

Syntax: `LDG R, [R+UR], P`  
Example: `@P0 LDG.EF.U8 R0, [R0.U32+UR0], P6 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-66 |
| cNOT (op 3) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| modi (op 1) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011001...........................0000000000000000000000000
......00....0....111...000.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v40"></a>
## 40. `LDG_R_R_P`

Syntax: `LDG R, [R], P`  
Example: `@P0 LDG.???0.EF.U8 R0, [R0.64], P6 ;`

Register access: WRITE R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 64-66 |
| cNOT (op 2) | 67 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001....................00000000000000000000000000000000
......00....1....111...000110000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v41"></a>
## 41. `LDG_R_desc[UR][RI]`

Syntax: `LDG R, desc[UR][R+INT_IMM]`  
Example: `@P0 LDG.???0.EF.U8 R0, desc[UR0][R0.64+0x4] ;`

Register access: WRITE R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 32-38 |
| operand 3 | 40-63 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001...........................0........................
0000..00....1....111...000110000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v42"></a>
## 42. `LDG_R_desc[UR][RI]_P`

Syntax: `LDG R, desc[UR][R+INT_IMM], P`  
Example: `@P0 LDG.???0.EF.U8 R0, desc[UR0][R0.64+0x4], P6 ;`

Register access: WRITE R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 32-38 |
| operand 3 | 40-63 |
| operand 4 | 64-66 |
| cNOT (op 4) | 67 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001...........................0........................
......00....1....111...000110000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v43"></a>
## 43. `LDG_R_desc[UR][R]`

Syntax: `LDG R, desc[UR][R]`  
Example: `@P0 LDG.???0.EF.U8 R0, desc[UR0][R0.64] ;`

Register access: WRITE R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 32-38 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001...........................0000000000000000000000000
0000..00....1....111...000110000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v44"></a>
## 44. `LDG_R_desc[UR][R]_P`

Syntax: `LDG R, desc[UR][R], P`  
Example: `@P0 LDG.???0.EF.U8 R0, desc[UR0][R0.64], P6 ;`

Register access: WRITE R (1 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 32-38 |
| operand 3 | 64-66 |
| cNOT (op 3) | 67 |
| modi 1 | 68-69 |
| modi 2 | 72 |
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
100000011001...........................0000000000000000000000000
......00....1....111...000110000000001000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `E.` |

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

<a id="v45"></a>
## 45. `LDG_P_R_I`

Syntax: `LDG P, R, [INT_IMM]`  
Example: `@P0 LDG.EF.U8 P0, R0, [0x2] ;`

Register access: WRITE P (1 slots); WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 40-63 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100............1111111100000000........................
0000..00....0..........000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v46"></a>
## 46. `LDG_P_R_I_P`

Syntax: `LDG P, R, [INT_IMM], P`  
Example: `@P0 LDG.EF.U8 P0, R0, [0x20], P6 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 40-63 |
| operand 3 | 64-66 |
| cNOT (op 3) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100............1111111100000000........................
......00....0..........000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v47"></a>
## 47. `LDG_P_R_R`

Syntax: `LDG P, R, [R]`  
Example: `@P0 LDG.EF.U8 P0, R0, [R0] ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100....................00000000000000000000000000000000
0000..00....0..........000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v48"></a>
## 48. `LDG_P_R_RI`

Syntax: `LDG P, R, [R+INT_IMM]`  
Example: `@P0 LDG.EF.U8 P0, R0, [R0+0x1] ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-63 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100....................00000000........................
0000..00....0..........000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v49"></a>
## 49. `LDG_P_R_RI_P`

Syntax: `LDG P, R, [R+INT_IMM], P`  
Example: `@P0 LDG.EF.U8 P0, R0, [R0+0x1], P6 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-63 |
| operand 4 | 64-66 |
| cNOT (op 4) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100....................00000000........................
......00....0..........000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v50"></a>
## 50. `LDG_P_R_R_P`

Syntax: `LDG P, R, [R], P`  
Example: `@P0 LDG.EF.U8 P0, R0, [R0], P6 ;`

Register access: WRITE P (1 slots); WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 64-66 |
| cNOT (op 3) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| operand 0 | 81-83 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100....................00000000000000000000000000000000
......00....0..........000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v51"></a>
## 51. `LDG_R_I`

Syntax: `LDG R, [INT_IMM]`  
Example: `@P0 LDG.EF.U8 R0, [0x20] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 40-63 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100............1111111100000000........................
0000..00....0....111...000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v52"></a>
## 52. `LDG_R_I_P`

Syntax: `LDG R, [INT_IMM], P`  
Example: `@P0 LDG.EF.U8 R0, [0x20], P6 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 40-63 |
| operand 2 | 64-66 |
| cNOT (op 2) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100............1111111100000000........................
......00....0....111...000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v53"></a>
## 53. `LDG_R_R`

Syntax: `LDG R, [R]`  
Example: `@P0 LDG.EF.U8 R0, [R0] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100....................00000000000000000000000000000000
0000..00....0....111...000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v54"></a>
## 54. `LDG_R_RI`

Syntax: `LDG R, [R+INT_IMM]`  
Example: `@P0 LDG.EF.U8 R0, [R0+0x1] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 40-63 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100....................00000000........................
0000..00....0....111...000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v55"></a>
## 55. `LDG_R_RI_P`

Syntax: `LDG R, [R+INT_IMM], P`  
Example: `@P0 LDG.EF.U8 R0, [R0+0x1], P6 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 40-63 |
| operand 3 | 64-66 |
| cNOT (op 3) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100....................00000000........................
......00....0....111...000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

<a id="v56"></a>
## 56. `LDG_R_R_P`

Syntax: `LDG R, [R], P`  
Example: `@P0 LDG.EF.U8 R0, [R0], P5 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 64-66 |
| cNOT (op 2) | 67 |
| modi 1 | 68-69 |
| E | 72 |
| modi 2 | 73-75 |
| modi 3 | 77-80 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000011100....................00000000000000000000000000000000
......00....0....111...000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `LTC64B.` |
| `10` | `LTC128B.` |
| `11` | `LTC256B.` |

Modifier Group 2:

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

Modifier Group 3:

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

