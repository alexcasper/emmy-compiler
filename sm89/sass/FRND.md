# FRND (SM89 SASS)

**NVIDIA:** Round To Integer (Conversion Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Round FP to integral value (in FP format) (category: FP32)

Typically emitted for: `cvt.rni/rzi/rmi/rpi.f32.f32`; `rintf`, `truncf`, `floorf`, `ceilf`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x5d, 0x107, 0x113 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2371)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [frnd](../verify/RESULTS.md#frnd): `cvt.rmi.f32.f32 (floor)`

Real encodings whose 12-bit opcode field matches **no** variant on the source page (form missing from the site): `FRND.FLOOR R5, R0`

Encodings: <https://kuterdinel.com/nv_isa_sm89/FRND.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [FRND_R_FI](#v1)
- [FRND_R_c[I][I]](#v2)
- [FRND_R_cx[UR][I]](#v3)
- [FRND_R_UR](#v4)
- [FRND_R_R](#v5)

<a id="v1"></a>
## 1. `FRND_R_FI`

Syntax: `FRND R, FIMM`  
Example: `@P0 FRND.???0 R0, 0 ;`

Register access: WRITE R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| modi 1 | 75-76 |
| modi 2 | 78-79 |
| FTZ | 80 |
| modi 3 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010001001............00000000................................
00000000000..0...000..0000000000000000000.....................00
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
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???4.` |
| `10` | `???8.` |
| `11` | `???12.` |

<a id="v2"></a>
## 2. `FRND_R_c[I][I]`

Syntax: `FRND R, c[INT_IMM][INT_IMM]`  
Example: `@P0 FRND.???0 R0, c[0x0][0x0] ;`

Register access: WRITE R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| modi 1 | 75-76 |
| modi 2 | 78-79 |
| FTZ | 80 |
| modi 3 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010001101............0000000000000000...................00000
00000000000..0...000..0000000000000000000.....................00
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
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???4.` |
| `10` | `???8.` |
| `11` | `???12.` |

<a id="v3"></a>
## 3. `FRND_R_cx[UR][I]`

Syntax: `FRND R, cx[UR][INT_IMM]`  
Example: `@P0 FRND.???0 R0, cx[UR0][0x0] ;`

Register access: WRITE R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| modi 1 | 75-76 |
| modi 2 | 78-79 |
| FTZ | 80 |
| modi 3 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010001101............00000000.......0...............000000000
00000000000..0...000..0000010000000000000.....................00
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
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???4.` |
| `10` | `???8.` |
| `11` | `???12.` |

<a id="v4"></a>
## 4. `FRND_R_UR`

Syntax: `FRND R, UR`  
Example: `@P0 FRND.???0 R0, UR0 ;`

Register access: WRITE R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| cABS (op 1) | 62 |
| cNEG (op 1) | 63 |
| modi 1 | 75-76 |
| modi 2 | 78-79 |
| FTZ | 80 |
| modi 3 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010001011............00000000.......00000000000000000000000..
00000000000..0...000..0000010000000000000.....................00
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
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???4.` |
| `10` | `???8.` |
| `11` | `???12.` |

<a id="v5"></a>
## 5. `FRND_R_R`

Syntax: `FRND R, R`  
Example: `@P0 FRND.???0 R0, R0 ;`

Register access: WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| cABS (op 1) | 62 |
| cNEG (op 1) | 63 |
| modi 1 | 75-76 |
| modi 2 | 78-79 |
| FTZ | 80 |
| modi 3 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110010001100............00000000........0000000000000000000000..
00000000000..0...000..0000000000000000000.....................00
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
| `00` | `(default)` |
| `01` | `FLOOR.` |
| `10` | `CEIL.` |
| `11` | `TRUNC.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???4.` |
| `10` | `???8.` |
| `11` | `???12.` |

