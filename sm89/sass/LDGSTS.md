# LDGSTS (SM89 SASS)

**NVIDIA:** Asynchronous Global to Shared Memcopy (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Async global->shared copy (cp.async) (category: Load / store)

Typically emitted for: `cp.async.ca/cg.shared.global` (`__pipeline_memcpy_async`, `cuda::memcpy_async`)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [cp_async](../verify/RESULTS.md#cp_async): `cp.async.cg.shared.global + commit_group + wait_group`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 76 | `LDGSTS.E.BYPASS.128 [R5], [R2.64]` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/LDGSTS.html> (machine-derived by fuzzing the assembler; no semantics).

32 encoding variant(s):

- [LDGSTS_RURI_R](#v1)
- [LDGSTS_RURI_RI](#v2)
- [LDGSTS_RURI_RI_P](#v3)
- [LDGSTS_RURI_R_P](#v4)
- [LDGSTS_RURI_desc[UR][RI]_P](#v5)
- [LDGSTS_RURI_desc[UR][R]_P](#v6)
- [LDGSTS_RUR_R](#v7)
- [LDGSTS_RUR_RI](#v8)
- [LDGSTS_RUR_RI_P](#v9)
- [LDGSTS_RUR_R_P](#v10)
- [LDGSTS_RUR_desc[UR][RI]_P](#v11)
- [LDGSTS_RUR_desc[UR][R]_P](#v12)
- [LDGSTS_RI_R](#v13)
- [LDGSTS_RI_RI](#v14)
- [LDGSTS_RI_RI_P](#v15)
- [LDGSTS_RI_RUR](#v16)
- [LDGSTS_RI_RURI](#v17)
- [LDGSTS_RI_RURI_P](#v18)
- [LDGSTS_RI_RUR_P](#v19)
- [LDGSTS_RI_R_P](#v20)
- [LDGSTS_RI_desc[UR][RI]_P](#v21)
- [LDGSTS_RI_desc[UR][R]_P](#v22)
- [LDGSTS_R_R](#v23)
- [LDGSTS_R_RI](#v24)
- [LDGSTS_R_RI_P](#v25)
- [LDGSTS_R_RUR](#v26)
- [LDGSTS_R_RURI](#v27)
- [LDGSTS_R_RURI_P](#v28)
- [LDGSTS_R_RUR_P](#v29)
- [LDGSTS_R_R_P](#v30)
- [LDGSTS_R_desc[UR][RI]_P](#v31)
- [LDGSTS_R_desc[UR][R]_P](#v32)

<a id="v1"></a>
## 1. `LDGSTS_RURI_R`

Syntax: `LDGSTS.E.BYPASS [R+UR+INT_IMM], [R]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0+0x1], [R0.64] ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 2 | 44-63 |
| operand 1 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011....................000000000000....................
......1.....0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v2"></a>
## 2. `LDGSTS_RURI_RI`

Syntax: `LDGSTS.E.BYPASS [R+UR+INT_IMM], [R+INT_IMM]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0+0x1], [R0.64+0x8] ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-43 |
| operand 2 | 44-63 |
| operand 1 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011....................................................
......1.....0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v3"></a>
## 3. `LDGSTS_RURI_RI_P`

Syntax: `LDGSTS.E.BYPASS [R+UR+INT_IMM], [R+INT_IMM], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0+-0x80000], [R0.64+0x1], P0 ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-42 |
| operand 2 | 43-62 |
| operand 1 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 5 | 87-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011...................................................1
......1.....0......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v4"></a>
## 4. `LDGSTS_RURI_R_P`

Syntax: `LDGSTS.E.BYPASS [R+UR+INT_IMM], [R], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0+0x800], [R0.64], P0 ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 2 | 44-54, 56-63 |
| operand 1 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 4 | 87-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011....................000000000000...........1........
......1.....0......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v5"></a>
## 5. `LDGSTS_RURI_desc[UR][RI]_P`

Syntax: `LDGSTS.E.BYPASS [R+UR+INT_IMM], desc[UR][R+INT_IMM], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0+0x800], desc[UR1][R0.64+0x1], P0 ;`

Register access: READ R (1 slots); READ UR (2 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 4 | 24-31 |
| operand 5 | 32-42 |
| operand 2 | 43-54, 56-63 |
| operand 3 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 6 | 87-89 |
| cNOT (op 6) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011...........................................1........
......1.....1......0.......10000000001000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v6"></a>
## 6. `LDGSTS_RURI_desc[UR][R]_P`

Syntax: `LDGSTS.E.BYPASS [R+UR+INT_IMM], desc[UR][R], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0+0x800], desc[UR1][R0.64], P0 ;`

Register access: READ R (1 slots); READ UR (2 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 4 | 24-31 |
| operand 2 | 44-54, 56-63 |
| operand 3 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 5 | 87-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011....................000000000000...........1........
......1.....1......0.......10000000001000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v7"></a>
## 7. `LDGSTS_RUR_R`

Syntax: `LDGSTS.E.BYPASS [R+UR], [R]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0], [R0.64] ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011....................00000000000000000000000000000000
......1.....0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v8"></a>
## 8. `LDGSTS_RUR_RI`

Syntax: `LDGSTS.E.BYPASS [R+UR], [R+INT_IMM]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0], [R0.64+0x8] ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-43 |
| operand 1 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011................................00000000000000000000
......1.....0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v9"></a>
## 9. `LDGSTS_RUR_RI_P`

Syntax: `LDGSTS.E.BYPASS [R+UR], [R+INT_IMM], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0], [R0.64+0x8], !P0 ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-43 |
| operand 1 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 4 | 87-89 |
| modi (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011................................00000000000000000000
......1.....0......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v10"></a>
## 10. `LDGSTS_RUR_R_P`

Syntax: `LDGSTS.E.BYPASS [R+UR], [R], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0], [R0.64], P0 ;`

Register access: READ R (1 slots); READ UR (1 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 3 | 87-89 |
| cNOT (op 3) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011....................00000000000000000000000000000000
......1.....0......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v11"></a>
## 11. `LDGSTS_RUR_desc[UR][RI]_P`

Syntax: `LDGSTS.E.BYPASS [R+UR], desc[UR][R+INT_IMM], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0], desc[UR1][R0.64+0x1], P0 ;`

Register access: READ R (1 slots); READ UR (2 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-43 |
| operand 2 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 5 | 87-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011................................00000000000000000000
......1.....1......0.......10000000001000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v12"></a>
## 12. `LDGSTS_RUR_desc[UR][R]_P`

Syntax: `LDGSTS.E.BYPASS [R+UR], desc[UR][R], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+UR0], desc[UR1][R0.64], P0 ;`

Register access: READ R (1 slots); READ UR (2 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 2 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 4 | 87-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011011....................00000000000000000000000000000000
......1.....1......0.......10000000001000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v13"></a>
## 13. `LDGSTS_RI_R`

Syntax: `LDGSTS.E.BYPASS [R+INT_IMM], [R]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+0x1], [R0.U32] ;`

Register access: READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 44-63 |
| modi (op 2) | 70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................000000000000....................
111111......0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v14"></a>
## 14. `LDGSTS_RI_RI`

Syntax: `LDGSTS.E.BYPASS [R+INT_IMM], [R+INT_IMM]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+0x1], [R0.U32+0x8] ;`

Register access: READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-43 |
| operand 1 | 44-63 |
| modi (op 2) | 70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................................................
111111......0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v15"></a>
## 15. `LDGSTS_RI_RI_P`

Syntax: `LDGSTS.E.BYPASS [R+INT_IMM], [R+INT_IMM], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+-0x80000], [R0.U32+0x1], P0 ;`

Register access: READ R (1 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-42 |
| operand 1 | 43-62 |
| modi (op 2) | 70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 4 | 87-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111...................................................1
111111......0......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v16"></a>
## 16. `LDGSTS_RI_RUR`

Syntax: `LDGSTS.E.BYPASS [R+INT_IMM], [R+UR]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+0x1], [R0.U32+UR0] ;`

Register access: READ R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 44-63 |
| operand 3 | 64-70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................000000000000....................
............0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v17"></a>
## 17. `LDGSTS_RI_RURI`

Syntax: `LDGSTS.E.BYPASS [R+INT_IMM], [R+UR+INT_IMM]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+0x1], [R0.U32+UR0+0x1] ;`

Register access: READ R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-43 |
| operand 1 | 44-63 |
| operand 3 | 64-70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................................................
............0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v18"></a>
## 18. `LDGSTS_RI_RURI_P`

Syntax: `LDGSTS.E.BYPASS [R+INT_IMM], [R+UR+INT_IMM], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+0x1], [R0.U32+UR0+0x1], P0 ;`

Register access: READ R (1 slots); READ R (2 slots); READ UR (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 32-43 |
| operand 1 | 44-63 |
| operand 3 | 64-70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 5 | 87-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................................................
............0......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v19"></a>
## 19. `LDGSTS_RI_RUR_P`

Syntax: `LDGSTS.E.BYPASS [R+INT_IMM], [R+UR], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+0x1], [R0.U32+UR0], P0 ;`

Register access: READ R (1 slots); READ R (2 slots); READ UR (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 44-63 |
| operand 3 | 64-70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 4 | 87-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................000000000000....................
............0......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v20"></a>
## 20. `LDGSTS_RI_R_P`

Syntax: `LDGSTS.E.BYPASS [R+INT_IMM], [R], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+0x800], [R0.64], P0 ;`

Register access: READ R (1 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 44-54, 56-63 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 3 | 87-89 |
| cNOT (op 3) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................000000000000...........1........
0000001.....1......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v21"></a>
## 21. `LDGSTS_RI_desc[UR][RI]_P`

Syntax: `LDGSTS.E.BYPASS [R+INT_IMM], desc[UR][R+INT_IMM], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+0x800], desc[UR0][R0.64+0x1], P0 ;`

Register access: READ R (1 slots); READ UR (2 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 4 | 32-42 |
| operand 1 | 43-54, 56-63 |
| operand 2 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 5 | 87-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111...........................................1........
......1.....1......0.......10000000001000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v22"></a>
## 22. `LDGSTS_RI_desc[UR][R]_P`

Syntax: `LDGSTS.E.BYPASS [R+INT_IMM], desc[UR][R], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0+0x800], desc[UR0][R0.64], P0 ;`

Register access: READ R (1 slots); READ UR (2 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 24-31 |
| operand 1 | 44-54, 56-63 |
| operand 2 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 4 | 87-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................000000000000...........1........
......1.....1......0.......10000000001000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v23"></a>
## 23. `LDGSTS_R_R`

Syntax: `LDGSTS.E.BYPASS [R], [R]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0], [R0.U32] ;`

Register access: READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi (op 1) | 70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................00000000000000000000000000000000
111111......0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v24"></a>
## 24. `LDGSTS_R_RI`

Syntax: `LDGSTS.E.BYPASS [R], [R+INT_IMM]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0], [R0.U32+0x8] ;`

Register access: READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-43 |
| modi (op 1) | 70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111................................00000000000000000000
111111......0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v25"></a>
## 25. `LDGSTS_R_RI_P`

Syntax: `LDGSTS.E.BYPASS [R], [R+INT_IMM], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0], [R0.U32+0x1], P0 ;`

Register access: READ R (1 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-43 |
| modi (op 1) | 70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 3 | 87-89 |
| cNOT (op 3) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111................................00000000000000000000
111111......0......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v26"></a>
## 26. `LDGSTS_R_RUR`

Syntax: `LDGSTS.E.BYPASS [R], [R+UR]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0], [R0.U32+UR0] ;`

Register access: READ R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 64-70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................00000000000000000000000000000000
............0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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
## 27. `LDGSTS_R_RURI`

Syntax: `LDGSTS.E.BYPASS [R], [R+UR+INT_IMM]`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0], [R0.U32+UR0+0x1] ;`

Register access: READ R (1 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-43 |
| operand 2 | 64-70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111................................00000000000000000000
............0......0...111010000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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
## 28. `LDGSTS_R_RURI_P`

Syntax: `LDGSTS.E.BYPASS [R], [R+UR+INT_IMM], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0], [R0.U32+UR0+0x1], P0 ;`

Register access: READ R (1 slots); READ R (2 slots); READ UR (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-43 |
| operand 2 | 64-70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 4 | 87-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111................................00000000000000000000
............0......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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
## 29. `LDGSTS_R_RUR_P`

Syntax: `LDGSTS.E.BYPASS [R], [R+UR], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0], [R0.U32+UR0], P0 ;`

Register access: READ R (1 slots); READ R (2 slots); READ UR (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 64-70 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 3 | 87-89 |
| cNOT (op 3) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................00000000000000000000000000000000
............0......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v30"></a>
## 30. `LDGSTS_R_R_P`

Syntax: `LDGSTS.E.BYPASS [R], [R], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0], [R0.64], P0 ;`

Register access: READ R (1 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 2 | 87-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................00000000000000000000000000000000
0000001.....1......0.......10000000000000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v31"></a>
## 31. `LDGSTS_R_desc[UR][RI]_P`

Syntax: `LDGSTS.E.BYPASS [R], desc[UR][R+INT_IMM], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0], desc[UR0][R0.64+0x1], P0 ;`

Register access: READ R (1 slots); READ UR (2 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-43 |
| operand 1 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 4 | 87-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111................................00000000000000000000
......1.....1......0.......10000000001000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

<a id="v32"></a>
## 32. `LDGSTS_R_desc[UR][R]_P`

Syntax: `LDGSTS.E.BYPASS [R], desc[UR][R], P`  
Example: `@P0 LDGSTS.E.BYPASS.EF.INVALID0 [R0], desc[UR0][R0.64], P0 ;`

Register access: READ R (1 slots); READ UR (2 slots); READ R (2 slots); READ_WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-31 |
| operand 1 | 64-69 |
| modi 1 | 71-72 |
| modi 2 | 73-75 |
| modi 3 | 77-81 |
| ZFILL | 82 |
| modi 4 | 84-86 |
| operand 3 | 87-89 |
| cNOT (op 3) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011101011111....................00000000000000000000000000000000
......1.....1......0.......10000000001000.....................00
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
| `000` | `INVALID0.` |
| `001` | `INVALID1.` |
| `010` | `INVALID2.` |
| `011` | `INVALID3.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `128.` |
| `111` | `INVALID7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00000` | `(default)` |
| `00001` | `CONSTANT.PRIVATE.` |
| `00010` | `CONSTANT.CTA.` |
| `00011` | `CONSTANT.CTA.PRIVATE.` |
| `00100` | `CONSTANT.` |
| `00101` | `MMIO.CTA.` |
| `00110` | `GPU.PRIVATE.` |
| `00111` | `MMIO.CTA.PRIVATE.` |
| `01000` | `MMIO.SM.` |
| `01001` | `CONSTANT.SM.` |
| `01010` | `MMIO.VC.` |
| `01011` | `CONSTANT.SM.PRIVATE.` |
| `01100` | `MMIO.GPU.` |
| `01101` | `CONSTANT.VC.` |
| `01110` | `CONSTANT.VC.PRIVATE.` |
| `01111` | `CONSTANT.GPU.` |
| `10000` | `(default)` |
| `10001` | `CONSTANT.PRIVATE.` |
| `10010` | `CONSTANT.CTA.` |
| `10011` | `CONSTANT.CTA.PRIVATE.` |
| `10100` | `CONSTANT.` |
| `10101` | `MMIO.CTA.` |
| `10110` | `GPU.PRIVATE.` |
| `10111` | `MMIO.CTA.PRIVATE.` |
| `11000` | `MMIO.SM.` |
| `11001` | `CONSTANT.SM.` |
| `11010` | `MMIO.VC.` |
| `11011` | `CONSTANT.SM.PRIVATE.` |
| `11100` | `MMIO.GPU.` |
| `11101` | `CONSTANT.VC.` |
| `11110` | `CONSTANT.VC.PRIVATE.` |
| `11111` | `CONSTANT.GPU.` |

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

