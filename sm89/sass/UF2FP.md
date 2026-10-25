# UF2FP (SM89 SASS)

**NVIDIA:** Uniform FP32 Down-convert and Pack (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform FP32 pack to FP16x2/BF16x2 (category: Uniform datapath)

Typically emitted for: uniform FP32->FP16x2 pack

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/UF2FP.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [UF2FP_UR_UR_FI](#v1)
- [UF2FP_UR_FI_UR](#v2)
- [UF2FP_UR_UR_FI](#v3)
- [UF2FP_UR_UR_UR](#v4)

<a id="v1"></a>
## 1. `UF2FP_UR_UR_FI`

Syntax: `UF2FP UR, UR, FIMM`  
Example: `@UP0 UF2FP.???0.???0 UR0, UR0, 0;`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 32-63 |
| operand 1 | 64-70 |
| modi 1 | 75-76 |
| modi 2 | 78 |
| modi 3 | 79-81 |
| modi 4 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010111010010...........000000000................................
.......0000..0....00..0000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `???2.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `???0.` |
| `1` | `MERGE_C.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `???1.` |
| `010` | `???2.` |
| `011` | `RZ.` |
| `100` | `???4.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???4.` |
| `10` | `???8.` |
| `11` | `???12.` |

<a id="v2"></a>
## 2. `UF2FP_UR_FI_UR`

Syntax: `UF2FP.MERGE_C UR, FIMM, UR`  
Example: `@UP0 UF2FP.???0.MERGE_C UR0, 0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 32-63 |
| operand 2 | 64-70 |
| H1 (op 2) | 72 |
| modi 1 | 75-76 |
| modi 2 | 79-81 |
| modi 3 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010111010001...........000000000................................
.......0.00..01...00..0000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `???2.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `???1.` |
| `010` | `???2.` |
| `011` | `RZ.` |
| `100` | `???4.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???4.` |
| `10` | `???8.` |
| `11` | `???12.` |

<a id="v3"></a>
## 3. `UF2FP_UR_UR_FI`

Syntax: `UF2FP.PACK_AB UR, UR, FIMM`  
Example: `@UP0 UF2FP.???0.PACK_AB UR0, UR0, 0;`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| modi 1 | 75-76 |
| modi 2 | 79-81 |
| modi 3 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010111010001...........0.......0................................
00000000000..00...00..0000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `???2.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `???1.` |
| `010` | `???2.` |
| `011` | `RZ.` |
| `100` | `???4.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???4.` |
| `10` | `???8.` |
| `11` | `???12.` |

<a id="v4"></a>
## 4. `UF2FP_UR_UR_UR`

Syntax: `UF2FP UR, UR, UR`  
Example: `@UP0 UF2FP.???0.PACK_AB UR0, UR0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| modi 1 | 75-76 |
| modi 2 | 78 |
| modi 3 | 79-81 |
| modi 4 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010111010100...........0.......0.......0000000000000000000000000
00000000000..0....00..0000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `???2.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `PACK_AB.` |
| `1` | `MERGE_C.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `???1.` |
| `010` | `???2.` |
| `011` | `RZ.` |
| `100` | `???4.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???4.` |
| `10` | `???8.` |
| `11` | `???12.` |

