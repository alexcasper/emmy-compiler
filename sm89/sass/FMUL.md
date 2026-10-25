# FMUL (SM89 SASS)

**NVIDIA:** FP32 Multiply (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: FP32 multiply (category: FP32)

Typically emitted for: `mul.f32`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x20, 0x56 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L963)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [fmul](../verify/RESULTS.md#fmul): `mul.f32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/FMUL.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [FMUL_R_R_FI](#v1)
- [FMUL_R_R_c[I][I]](#v2)
- [FMUL_R_R_cx[UR][I]](#v3)
- [FMUL_R_R_UR](#v4)
- [FMUL_R_R_R](#v5)

<a id="v1"></a>
## 1. `FMUL_R_R_FI`

Syntax: `FMUL R, R, FIMM`  
Example: `@P0 FMUL.INVALID0 R0, R0, 0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| FMZ | 76 |
| SAT | 77 |
| modi 1 | 78-79 |
| FTZ | 80 |
| modi 2 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001000001....................................................
00000000..00.....000...000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `INVALID0.` |
| `001` | `D8.` |
| `010` | `D4.` |
| `011` | `D2.` |
| `100` | `(default)` |
| `101` | `M2.` |
| `110` | `M4.` |
| `111` | `M8.` |

<a id="v2"></a>
## 2. `FMUL_R_R_c[I][I]`

Syntax: `FMUL R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 FMUL.INVALID0 R0, R0, c[0x0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| FMZ | 76 |
| SAT | 77 |
| modi 1 | 78-79 |
| FTZ | 80 |
| modi 2 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001000101....................00000000...................00000
00000000..00.....000...000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `INVALID0.` |
| `001` | `D8.` |
| `010` | `D4.` |
| `011` | `D2.` |
| `100` | `(default)` |
| `101` | `M2.` |
| `110` | `M4.` |
| `111` | `M8.` |

<a id="v3"></a>
## 3. `FMUL_R_R_cx[UR][I]`

Syntax: `FMUL R, R, cx[UR][INT_IMM]`  
Example: `@P0 FMUL.INVALID0 R0, R0, cx[UR0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| FMZ | 76 |
| SAT | 77 |
| modi 1 | 78-79 |
| FTZ | 80 |
| modi 2 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001000101...........................0...............000000000
00000000..00.....000...000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `INVALID0.` |
| `001` | `D8.` |
| `010` | `D4.` |
| `011` | `D2.` |
| `100` | `(default)` |
| `101` | `M2.` |
| `110` | `M4.` |
| `111` | `M8.` |

<a id="v4"></a>
## 4. `FMUL_R_R_UR`

Syntax: `FMUL R, R, UR`  
Example: `@P0 FMUL.INVALID0 R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| FMZ | 76 |
| SAT | 77 |
| modi 1 | 78-79 |
| FTZ | 80 |
| modi 2 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001000011...........................00000000000000000000000..
00000000..00.....000...000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `INVALID0.` |
| `001` | `D8.` |
| `010` | `D4.` |
| `011` | `D2.` |
| `100` | `(default)` |
| `101` | `M2.` |
| `110` | `M4.` |
| `111` | `M8.` |

<a id="v5"></a>
## 5. `FMUL_R_R_R`

Syntax: `FMUL R, R, R`  
Example: `@P0 FMUL.INVALID0 R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| FMZ | 76 |
| SAT | 77 |
| modi 1 | 78-79 |
| FTZ | 80 |
| modi 2 | 84-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000001000100............................0000000000000000000000..
00000000..00.....000...000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `INVALID0.` |
| `001` | `D8.` |
| `010` | `D4.` |
| `011` | `D2.` |
| `100` | `(default)` |
| `101` | `M2.` |
| `110` | `M4.` |
| `111` | `M8.` |

