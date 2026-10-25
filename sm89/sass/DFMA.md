# DFMA (SM89 SASS)

**NVIDIA:** FP64 Fused Mutiply Add (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: FP64 fused multiply-add (category: FP64)

Typically emitted for: `fma.rn.f64`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x2b ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1235)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [dfma](../verify/RESULTS.md#dfma): `fma.rn.f64`

Encodings: <https://kuterdinel.com/nv_isa_sm89/DFMA.html> (machine-derived by fuzzing the assembler; no semantics).

9 encoding variant(s):

- [DFMA_R_R_R_FI](#v1)
- [DFMA_R_R_R_c[I][I]](#v2)
- [DFMA_R_R_R_cx[UR][I]](#v3)
- [DFMA_R_R_FI_R](#v4)
- [DFMA_R_R_c[I][I]_R](#v5)
- [DFMA_R_R_cx[UR][I]_R](#v6)
- [DFMA_R_R_UR_R](#v7)
- [DFMA_R_R_R_UR](#v8)
- [DFMA_R_R_R_R](#v9)

<a id="v1"></a>
## 1. `DFMA_R_R_R_FI`

Syntax: `DFMA R, R, R, FIMM`  
Example: `@P0 DFMA R0, R0, R0, 0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-63 |
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
110101000010....................................................
............00..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v2"></a>
## 2. `DFMA_R_R_R_c[I][I]`

Syntax: `DFMA R, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 DFMA R0, R0, R0, c[0x0][0x0] ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
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
110101000110....................00000000...................00000
............00..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v3"></a>
## 3. `DFMA_R_R_R_cx[UR][I]`

Syntax: `DFMA R, R, R, cx[UR][INT_IMM]`  
Example: `@P0 DFMA R0, R0, R0, cx[UR0][0x0] ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
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
110101000110...........................0...............000000000
............00..0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v4"></a>
## 4. `DFMA_R_R_FI_R`

Syntax: `DFMA R, R, FIMM, R`  
Example: `@P0 DFMA R0, R0, 0, R0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| cABS (op 3) | 74 |
| cNEG (op 3) | 75 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101000001....................................................
............00..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v5"></a>
## 5. `DFMA_R_R_c[I][I]_R`

Syntax: `DFMA R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 DFMA R0, R0, c[0x0][0x0], R0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| cABS (op 4) | 74 |
| cNEG (op 4) | 75 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101000101....................00000000...................00000
............00..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v6"></a>
## 6. `DFMA_R_R_cx[UR][I]_R`

Syntax: `DFMA R, R, cx[UR][INT_IMM], R`  
Example: `@P0 DFMA R0, R0, cx[UR0][0x0], R0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| cABS (op 4) | 74 |
| cNEG (op 4) | 75 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101000101...........................0...............000000000
............00..0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v7"></a>
## 7. `DFMA_R_R_UR_R`

Syntax: `DFMA R, R, UR, R`  
Example: `@P0 DFMA R0, R0, UR0, R0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ UR (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| cABS (op 3) | 74 |
| cNEG (op 3) | 75 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101000011...........................00000000000000000000000..
............00..0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v8"></a>
## 8. `DFMA_R_R_R_UR`

Syntax: `DFMA R, R, R, UR`  
Example: `@P0 DFMA R0, R0, R0, UR0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| cABS (op 3) | 62 |
| cNEG (op 3) | 63 |
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
110101000111...........................00000000000000000000000..
............00..0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

<a id="v9"></a>
## 9. `DFMA_R_R_R_R`

Syntax: `DFMA R, R, R, R`  
Example: `@P0 DFMA R0, R0, R0, R0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| cABS (op 3) | 74 |
| cNEG (op 3) | 75 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110101000100............................0000000000000000000000..
............00..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

