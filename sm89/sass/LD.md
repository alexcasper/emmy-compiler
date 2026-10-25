# LD (SM89 SASS)

**NVIDIA:** Load from generic Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Generic-address load (category: Load / store)

Typically emitted for: `ld` on a generic pointer (space not provable)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **NAK op maps to LDG/LDL/LDS**. NAK encodes 0x381, 0x981, 0x983, 0x984 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3428)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [ld_generic](../verify/RESULTS.md#ld_generic): `ld (generic pointer)`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 76 | `LD.E R5, [R4.64]` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/LD.html> (machine-derived by fuzzing the assembler; no semantics).

18 encoding variant(s):

- [LD_R_I](#v1)
- [LD_R_I_P](#v2)
- [LD_R_R](#v3)
- [LD_R_RI](#v4)
- [LD_R_RI_P](#v5)
- [LD_R_RUR](#v6)
- [LD_R_RURI](#v7)
- [LD_R_RURI_P](#v8)
- [LD_R_RUR_P](#v9)
- [LD_R_R_P](#v10)
- [LD_R_UR](#v11)
- [LD_R_URI](#v12)
- [LD_R_URI_P](#v13)
- [LD_R_UR_P](#v14)
- [LD_R_desc[UR][RI]](#v15)
- [LD_R_desc[UR][RI]_P](#v16)
- [LD_R_desc[UR][R]](#v17)
- [LD_R_desc[UR][R]_P](#v18)

<a id="v1"></a>
## 1. `LD_R_I`

Syntax: `LD R, [INT_IMM]`  
Example: `@P0 LD.EF.U8 R0, [0x200] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
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
000000011001............11111111................................
0000..00....0....000...000000000000000000.....................00
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

<a id="v2"></a>
## 2. `LD_R_I_P`

Syntax: `LD R, [INT_IMM], P`  
Example: `@P0 LD.EF.U8 R0, [0x2000], P6 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
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
000000011001............11111111................................
......00....0....000...000000000000000000.....................00
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

<a id="v3"></a>
## 3. `LD_R_R`

Syntax: `LD R, [R]`  
Example: `@P0 LD.EF.U8 R0, [R0] ;`

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
000000011001....................00000000000000000000000000000000
0000..00....0....000...000000000000000000.....................00
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

<a id="v4"></a>
## 4. `LD_R_RI`

Syntax: `LD R, [R+INT_IMM]`  
Example: `@P0 LD.EF.U8 R0, [R0+0x1] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
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
000000011001....................................................
0000..00....0....000...000000000000000000.....................00
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

<a id="v5"></a>
## 5. `LD_R_RI_P`

Syntax: `LD R, [R+INT_IMM], P`  
Example: `@P0 LD.EF.U8 R0, [R0+0x1], P6 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
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
000000011001....................................................
......00....0....000...000000000000000000.....................00
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

<a id="v6"></a>
## 6. `LD_R_RUR`

Syntax: `LD R, [R+UR]`  
Example: `@P0 LD.EF.U8 R0, [R0.U32+UR0] ;`

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
000000011001...........................0000000000000000000000000
0000..00....0....000...000.10000000000000.....................00
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

<a id="v7"></a>
## 7. `LD_R_RURI`

Syntax: `LD R, [R+UR+INT_IMM]`  
Example: `@P0 LD.EF.U8 R0, [R0.U32+UR0+0x1] ;`

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
000000011001...........................0........................
0000..00....0....000...000.10000000000000.....................00
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

<a id="v8"></a>
## 8. `LD_R_RURI_P`

Syntax: `LD R, [R+UR+INT_IMM], P`  
Example: `@P0 LD.EF.U8 R0, [R0.U32+UR0+0x1], P6 ;`

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
000000011001...........................0........................
......00....0....000...000.10000000000000.....................00
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

<a id="v9"></a>
## 9. `LD_R_RUR_P`

Syntax: `LD R, [R+UR], P`  
Example: `@P0 LD.EF.U8 R0, [R0.U32+UR0], P6 ;`

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
000000011001...........................0000000000000000000000000
......00....0....000...000.10000000000000.....................00
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

<a id="v10"></a>
## 10. `LD_R_R_P`

Syntax: `LD R, [R], P`  
Example: `@P0 LD.EF.U8 R0, [R0], P6 ;`

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
000000011001....................00000000000000000000000000000000
......00....0....000...000000000000000000.....................00
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

<a id="v11"></a>
## 11. `LD_R_UR`

Syntax: `LD R, [UR]`  
Example: `@P0 LD.EF.U8 R0, [UR0] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
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
000000011001............11111111.......0000000000000000000000000
0000..00....0....000...000010000000000000.....................00
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

<a id="v12"></a>
## 12. `LD_R_URI`

Syntax: `LD R, [UR+INT_IMM]`  
Example: `@P0 LD.EF.U8 R0, [UR0+0x2] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
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
000000011001............11111111.......0........................
0000..00....0....000...000010000000000000.....................00
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

<a id="v13"></a>
## 13. `LD_R_URI_P`

Syntax: `LD R, [UR+INT_IMM], P`  
Example: `@P0 LD.EF.U8 R0, [UR0+0x20], P6 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
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
000000011001............11111111.......0........................
......00....0....000...000010000000000000.....................00
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

<a id="v14"></a>
## 14. `LD_R_UR_P`

Syntax: `LD R, [UR], P`  
Example: `@P0 LD.EF.U8 R0, [UR0], P6 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
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
000000011001............11111111.......0000000000000000000000000
......00....0....000...000010000000000000.....................00
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

<a id="v15"></a>
## 15. `LD_R_desc[UR][RI]`

Syntax: `LD R, desc[UR][R+INT_IMM]`  
Example: `@P0 LD.???0.EF.U8 R0, desc[UR0][R0.64+0x4] ;`

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
000000011001...........................0........................
0000..00....1....000...000110000000001000.....................00
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

<a id="v16"></a>
## 16. `LD_R_desc[UR][RI]_P`

Syntax: `LD R, desc[UR][R+INT_IMM], P`  
Example: `@P0 LD.???0.EF.U8 R0, desc[UR0][R0.64+0x1], P5 ;`

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
000000011001...........................0........................
......00....1....000...000110000000001000.....................00
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

<a id="v17"></a>
## 17. `LD_R_desc[UR][R]`

Syntax: `LD R, desc[UR][R]`  
Example: `@P0 LD.???0.EF.U8 R0, desc[UR0][R0.64] ;`

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
000000011001...........................0000000000000000000000000
0000..00....1....000...000110000000001000.....................00
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
## 18. `LD_R_desc[UR][R]_P`

Syntax: `LD R, desc[UR][R], P`  
Example: `@P0 LD.???0.EF.U8 R0, desc[UR0][R0.64], P6 ;`

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
000000011001...........................0000000000000000000000000
......00....1....000...000110000000001000.....................00
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

