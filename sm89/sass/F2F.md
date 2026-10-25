# F2F (SM89 SASS)

**NVIDIA:** Floating Point To Floating Point Conversion (Conversion Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Float to float conversion (precision change) (category: Conversion)

Typically emitted for: `cvt.f32.f64`, `cvt.f64.f32`, `cvt.rn.f16.f32` (single value)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x5b, 0x104, 0x110 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2189)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [f2f](../verify/RESULTS.md#f2f): `cvt.rn.f32.f64`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 75 | `F2F.F32.F64 R5, R4` |
| 84 | `F2F.F32.F64 R5, R4` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/F2F.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [F2F_R_FI](#v1)
- [F2F_R_c[I][I]](#v2)
- [F2F_R_cx[UR][I]](#v3)
- [F2F_R_UR](#v4)
- [F2F_R_R](#v5)

<a id="v1"></a>
## 1. `F2F_R_FI`

Syntax: `F2F.F64.F32 R, FIMM`  
Example: `@P0 F2F.F64.F32 R0, 0 ;`

Register access: WRITE R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| modi 1 | 78-79 |
| FTZ | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010001001............00000000................................
00000000000110...000010000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v2"></a>
## 2. `F2F_R_c[I][I]`

Syntax: `F2F.F64.F32 R, c[INT_IMM][INT_IMM]`  
Example: `@P0 F2F.F64.F32 R0, c[0x0][0x0] ;`

Register access: WRITE R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| modi 1 | 78-79 |
| FTZ | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010001101............0000000000000000...................00000
00000000000110...000010000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v3"></a>
## 3. `F2F_R_cx[UR][I]`

Syntax: `F2F.F64.F32 R, cx[UR][INT_IMM]`  
Example: `@P0 F2F.F64.F32 R0, cx[UR0][0x0] ;`

Register access: WRITE R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| modi 1 | 78-79 |
| FTZ | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010001101............00000000.......0...............000000000
00000000000110...000010000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v4"></a>
## 4. `F2F_R_UR`

Syntax: `F2F.F64.F32 R, UR`  
Example: `@P0 F2F.F32.F64 R0, UR0 ;`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| cABS (op 1) | 62 |
| cNEG (op 1) | 63 |
| modi 1 | 78-79 |
| FTZ | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010001011............00000000.......00000000000000000000000..
00000000000010...000110000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v5"></a>
## 5. `F2F_R_R`

Syntax: `F2F.F64.F32 R, R`  
Example: `@P0 F2F.F64.F32 R0, R0 ;`

Register access: WRITE R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| cABS (op 1) | 62 |
| cNEG (op 1) | 63 |
| modi 1 | 78-79 |
| FTZ | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010001100............00000000........0000000000000000000000..
00000000000110...000010000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

