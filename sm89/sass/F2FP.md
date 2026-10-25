# F2FP (SM89 SASS)

**NVIDIA:** not listed in the official Ampere/Ada opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)).

Notes: Pack two FP32 into FP16x2 / BF16x2 (and FP8 pairs on sm_89) (category: Conversion)

Typically emitted for: `cvt.rn.f16x2.f32`, `cvt.rn.bf16x2.f32`, `cvt.rn.satfinite.e4m3x2/e5m2x2.f32` (FP8, sm_89); `__floats2half2_rn`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x3e, 0xba ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2237)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [f2fp_f16](../verify/RESULTS.md#f2fp_f16): `cvt.rn.f16x2.f32`
- [f2fp_bf16](../verify/RESULTS.md#f2fp_bf16): `cvt.rn.bf16x2.f32`
- [f2fp_e4m3](../verify/RESULTS.md#f2fp_e4m3): `cvt.rn.satfinite.e4m3x2.f32 (FP8)`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 76 | `F2FP.BF16.F32.PACK_AB R5, R0, R5`<br>`F2FP.SATFINITE.E4M3.F32.PACK_AB_MERGE_C R0, R0, R5, RZ` |
| 81 | `F2FP.BF16.F32.PACK_AB R5, R0, R5`<br>`F2FP.F16.F32.PACK_AB R5, R0, R5`<br>`F2FP.SATFINITE.E4M3.F32.PACK_AB_MERGE_C R0, R0, R5, RZ` |
| 87 | `F2FP.SATFINITE.E4M3.F32.PACK_AB_MERGE_C R0, R0, R5, RZ` |
| 90 | `F2FP.SATFINITE.E4M3.F32.PACK_AB_MERGE_C R0, R0, R5, RZ` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/F2FP.html> (machine-derived by fuzzing the assembler; no semantics).

22 encoding variant(s):

- [F2FP_R_R_FI](#v1)
- [F2FP_R_R_R_FI](#v2)
- [F2FP_R_R_R_c[I][I]](#v3)
- [F2FP_R_R_R_cx[UR][I]](#v4)
- [F2FP_R_R_c[I][I]](#v5)
- [F2FP_R_R_cx[UR][I]](#v6)
- [F2FP_R_FI_R](#v7)
- [F2FP_R_R_FI](#v8)
- [F2FP_R_R_FI_R](#v9)
- [F2FP_R_R_c[I][I]](#v10)
- [F2FP_R_R_c[I][I]_R](#v11)
- [F2FP_R_R_cx[UR][I]](#v12)
- [F2FP_R_R_cx[UR][I]_R](#v13)
- [F2FP_R_c[I][I]_R](#v14)
- [F2FP_R_cx[UR][I]_R](#v15)
- [F2FP_R_R_UR](#v16)
- [F2FP_R_R_UR_R](#v17)
- [F2FP_R_UR_R](#v18)
- [F2FP_R_R_R_UR](#v19)
- [F2FP_R_R_UR](#v20)
- [F2FP_R_R_R](#v21)
- [F2FP_R_R_R_R](#v22)

<a id="v1"></a>
## 1. `F2FP_R_R_FI`

Syntax: `F2FP.F32.MERGE_C R, R, FIMM`  
Example: `@P0 F2FP.F16.F32.MERGE_C R0, R0, 0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-63, 72 |
| operand 1 | 64-71 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000010............00000000................................
.........00...10000000..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v2"></a>
## 2. `F2FP_R_R_R_FI`

Syntax: `F2FP.RS R, R, R, FIMM`  
Example: `@P0 F2FP.PACK_AB.RS.7b R0, R0, R0, 0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-63, 72 |
| operand 2 | 64-71 |
| RELU | 75 |
| ???1 | 76 |
| SATFINITE | 77 |
| modi 1 | 78 |
| REG_RS | 82 |
| modi 2 | 83-84, 86-87 |
| LTN25 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000010....................................................
.........00....001......00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `PACK_AB.` |
| `1` | `MERGE_C.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `7b.` |
| `01` | `(default)` |
| `10` | `9b.` |
| `11` | `10b.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `???2.` |
| `10` | `???4.` |
| `11` | `???6.` |

<a id="v3"></a>
## 3. `F2FP_R_R_R_c[I][I]`

Syntax: `F2FP.RS R, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 F2FP.PACK_AB.RS.7b R0, R0, R0, c[0x0] [0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 2 | 64-71 |
| RELU | 75 |
| ???1 | 76 |
| SATFINITE | 77 |
| modi 1 | 78 |
| REG_RS | 82 |
| modi 2 | 83-84, 86-87 |
| LTN25 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000110....................00000000...................00000
........000....001......00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `PACK_AB.` |
| `1` | `MERGE_C.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `7b.` |
| `01` | `(default)` |
| `10` | `9b.` |
| `11` | `10b.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `???2.` |
| `10` | `???4.` |
| `11` | `???6.` |

<a id="v4"></a>
## 4. `F2FP_R_R_R_cx[UR][I]`

Syntax: `F2FP.RS R, R, R, cx[UR][INT_IMM]`  
Example: `@P0 F2FP.PACK_AB.RS.7b R0, R0, R0, cx[UR0] [0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 2 | 64-71 |
| RELU | 75 |
| ???1 | 76 |
| SATFINITE | 77 |
| modi 1 | 78 |
| REG_RS | 82 |
| modi 2 | 83-84, 86-87 |
| LTN25 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000110...........................0...............000000000
........000....001......00010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `PACK_AB.` |
| `1` | `MERGE_C.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `7b.` |
| `01` | `(default)` |
| `10` | `9b.` |
| `11` | `10b.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `???2.` |
| `10` | `???4.` |
| `11` | `???6.` |

<a id="v5"></a>
## 5. `F2FP_R_R_c[I][I]`

Syntax: `F2FP.F32.MERGE_C R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 F2FP.F16.F32.MERGE_C R0, R0, c[0x0] [0x0];`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 1 | 64-71 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000110............0000000000000000...................00000
........000...10000000..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v6"></a>
## 6. `F2FP_R_R_cx[UR][I]`

Syntax: `F2FP.F32.MERGE_C R, R, cx[UR][INT_IMM]`  
Example: `@P0 F2FP.F16.F32.MERGE_C R0, R0, cx[UR0] [0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 1 | 64-71 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000110............00000000.......0...............000000000
........000...10000000..00010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v7"></a>
## 7. `F2FP_R_FI_R`

Syntax: `F2FP.F32.MERGE_C R, FIMM, R`  
Example: `@P0 F2FP.F16.F32.MERGE_C R0, 0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| operand 2 | 64-71 |
| H1 (op 2) | 72 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000001............00000000................................
.........00...10000000..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v8"></a>
## 8. `F2FP_R_R_FI`

Syntax: `F2FP.F32.PACK_AB R, R, FIMM`  
Example: `@P0 F2FP.F16.F32.PACK_AB R0, R0, 0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000001....................................................
00000000000...00000000..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v9"></a>
## 9. `F2FP_R_R_FI_R`

Syntax: `F2FP.RS R, R, FIMM, R`  
Example: `@P0 F2FP.PACK_AB.RS.7b R0, R0, 0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
| H1 (op 3) | 72 |
| RELU | 75 |
| SATFINITE | 77 |
| modi 2 | 78 |
| REG_RS | 82 |
| modi 3 | 83-84 |
| LTN25 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000001....................................................
.........00.0..001....0000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `PACK_AB.` |
| `1` | `MERGE_C.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `7b.` |
| `01` | `(default)` |
| `10` | `9b.` |
| `11` | `10b.` |

<a id="v10"></a>
## 10. `F2FP_R_R_c[I][I]`

Syntax: `F2FP.F32.PACK_AB R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 F2FP.F16.F32.PACK_AB R0, R0, c[0x0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000101....................00000000...................00000
00000000000...00000000..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v11"></a>
## 11. `F2FP_R_R_c[I][I]_R`

Syntax: `F2FP.RS R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 F2FP.PACK_AB.RS.7b R0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| H1 (op 4) | 72 |
| RELU | 75 |
| SATFINITE | 77 |
| modi 2 | 78 |
| REG_RS | 82 |
| modi 3 | 83-84 |
| LTN25 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000101....................00000000...................00000
.........00.0..001....0000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `PACK_AB.` |
| `1` | `MERGE_C.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `7b.` |
| `01` | `(default)` |
| `10` | `9b.` |
| `11` | `10b.` |

<a id="v12"></a>
## 12. `F2FP_R_R_cx[UR][I]`

Syntax: `F2FP.F32.PACK_AB R, R, cx[UR][INT_IMM]`  
Example: `@P0 F2FP.F16.F32.PACK_AB R0, R0, cx[UR0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000101...........................0...............000000000
00000000000...00000000..00010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v13"></a>
## 13. `F2FP_R_R_cx[UR][I]_R`

Syntax: `F2FP.RS R, R, cx[UR][INT_IMM], R`  
Example: `@P0 F2FP.PACK_AB.RS.7b R0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| H1 (op 4) | 72 |
| RELU | 75 |
| SATFINITE | 77 |
| modi 2 | 78 |
| REG_RS | 82 |
| modi 3 | 83-84 |
| LTN25 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000101...........................0...............000000000
.........00.0..001....0000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `PACK_AB.` |
| `1` | `MERGE_C.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `7b.` |
| `01` | `(default)` |
| `10` | `9b.` |
| `11` | `10b.` |

<a id="v14"></a>
## 14. `F2FP_R_c[I][I]_R`

Syntax: `F2FP.F32.MERGE_C R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 F2FP.F16.F32.MERGE_C R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| operand 3 | 64-71 |
| H1 (op 3) | 72 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000101............0000000000000000...................00000
.........00...10000000..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v15"></a>
## 15. `F2FP_R_cx[UR][I]_R`

Syntax: `F2FP.F32.MERGE_C R, cx[UR][INT_IMM], R`  
Example: `@P0 F2FP.F16.F32.MERGE_C R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| operand 3 | 64-71 |
| H1 (op 3) | 72 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000101............00000000.......0...............000000000
.........00...10000000..00010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v16"></a>
## 16. `F2FP_R_R_UR`

Syntax: `F2FP.F32.PACK_AB R, R, UR`  
Example: `@P0 F2FP.F16.F32.PACK_AB R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000011...........................0000000000000000000000000
00000000000...00000000..00010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v17"></a>
## 17. `F2FP_R_R_UR_R`

Syntax: `F2FP.RS R, R, UR, R`  
Example: `@P0 F2FP.PACK_AB.RS.7b R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
| H1 (op 3) | 72 |
| RELU | 75 |
| SATFINITE | 77 |
| modi 2 | 78 |
| REG_RS | 82 |
| modi 3 | 83-84 |
| LTN25 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000011...........................0000000000000000000000000
.........00.0..001....0000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `PACK_AB.` |
| `1` | `MERGE_C.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `7b.` |
| `01` | `(default)` |
| `10` | `9b.` |
| `11` | `10b.` |

<a id="v18"></a>
## 18. `F2FP_R_UR_R`

Syntax: `F2FP.F32.MERGE_C R, UR, R`  
Example: `@P0 F2FP.F16.F32.MERGE_C R0, UR0, R0;`

Register access: WRITE R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 64-71 |
| H1 (op 2) | 72 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000011............00000000.......0000000000000000000000000
.........00...10000000..00010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v19"></a>
## 19. `F2FP_R_R_R_UR`

Syntax: `F2FP.RS R, R, R, UR`  
Example: `@P0 F2FP.PACK_AB.RS.7b R0, R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| operand 2 | 64-71 |
| H1 (op 3) | 72 |
| RELU | 75 |
| ???1 | 76 |
| SATFINITE | 77 |
| modi 1 | 78 |
| REG_RS | 82 |
| modi 2 | 83-84, 86-87 |
| LTN25 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000111...........................0000000000000000000000000
.........00....001......00010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `PACK_AB.` |
| `1` | `MERGE_C.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `7b.` |
| `01` | `(default)` |
| `10` | `9b.` |
| `11` | `10b.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `???2.` |
| `10` | `???4.` |
| `11` | `???6.` |

<a id="v20"></a>
## 20. `F2FP_R_R_UR`

Syntax: `F2FP.F32.MERGE_C R, R, UR`  
Example: `@P0 F2FP.F16.F32.MERGE_C R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-38 |
| operand 1 | 64-71 |
| H1 (op 2) | 72 |
| RELU | 75 |
| modi 1 | 76 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000111............00000000.......0000000000000000000000000
.........00...10000000..00010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

<a id="v21"></a>
## 21. `F2FP_R_R_R`

Syntax: `F2FP.F32 R, R, R`  
Example: `@P0 F2FP.F16.F32.PACK_AB R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| RELU | 75 |
| modi 1 | 76, 78 |
| SATFINITE | 77 |
| modi 2 | 86-87 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000100............................000000000000000000000000
00000000000....0000000..00000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `BF16.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `PACK_AB.` |
| `1` | `MERGE_C.` |

<a id="v22"></a>
## 22. `F2FP_R_R_R_R`

Syntax: `F2FP.RS R, R, R, R`  
Example: `@P0 F2FP.PACK_AB.RS.7b R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
| H1 (op 3) | 72 |
| RELU | 75 |
| SATFINITE | 77 |
| modi 2 | 78 |
| REG_RS | 82 |
| modi 3 | 83-84 |
| LTN25 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011111000100............................000000000000000000000000
.........00.0..001....0000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `PACK_AB.` |
| `1` | `MERGE_C.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `7b.` |
| `01` | `(default)` |
| `10` | `9b.` |
| `11` | `10b.` |

