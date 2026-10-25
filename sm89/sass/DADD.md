# DADD (SM89 SASS)

**NVIDIA:** FP64 Add (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: FP64 add (category: FP64)

Typically emitted for: `add.f64`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x29 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1215)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [dadd](../verify/RESULTS.md#dadd): `add.f64`

Encodings: <https://kuterdinel.com/nv_isa_sm89/DADD.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [DADD_R_R_FI](#v1)
- [DADD_R_R_c[I][I]](#v2)
- [DADD_R_R_cx[UR][I]](#v3)
- [DADD_R_R_UR](#v4)
- [DADD_R_R_R](#v5)

<a id="v1"></a>
## 1. `DADD_R_R_FI`

Syntax: `DADD R, R, FIMM`  
Example: `@P0 DADD R0, R0, 0 ;`

Register access: WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101000010....................................................
00000000..0000..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v2"></a>
## 2. `DADD_R_R_c[I][I]`

Syntax: `DADD R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 DADD R0, R0, c[0x0][0x0] ;`

Register access: WRITE R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101000110....................00000000...................00000
00000000..0000..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v3"></a>
## 3. `DADD_R_R_cx[UR][I]`

Syntax: `DADD R, R, cx[UR][INT_IMM]`  
Example: `@P0 DADD R0, R0, cx[UR0][0x0] ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101000110...........................0...............000000000
00000000..0000..0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v4"></a>
## 4. `DADD_R_R_UR`

Syntax: `DADD R, R, UR`  
Example: `@P0 DADD R0, R0, UR0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ UR (2 slots)

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
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101000111...........................00000000000000000000000..
00000000..0000..0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v5"></a>
## 5. `DADD_R_R_R`

Syntax: `DADD R, R, R`  
Example: `@P0 DADD R0, R0, R0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| cABS (op 2) | 74 |
| cNEG (op 2) | 75 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100101000100....................00000000000000000000000000000000
............00..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

