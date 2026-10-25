# HMNMX2 (SM89 SASS)

**NVIDIA:** FP16 Minimum / Maximum (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Packed FP16x2 / BF16x2 min/max (category: FP16 (packed half2))

Typically emitted for: `min/max.f16x2`/`bf16x2`; `__hmin2`/`__hmax2`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x40 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1488)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [hmnmx2](../verify/RESULTS.md#hmnmx2): `min.f16x2`

Encodings: <https://kuterdinel.com/nv_isa_sm89/HMNMX2.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [HMNMX2_R_R_FI_FI_P](#v1)
- [HMNMX2_R_R_c[I][I]_P](#v2)
- [HMNMX2_R_R_cx[UR][I]_P](#v3)
- [HMNMX2_R_R_UR_P](#v4)
- [HMNMX2_R_R_R_P](#v5)

<a id="v1"></a>
## 1. `HMNMX2_R_R_FI_FI_P`

Syntax: `HMNMX2 R, R, FIMM, FIMM, P`  
Example: `@P0 HMNMX2 R0, R0, 0, 0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-47 |
| operand 2 | 48-63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| F32 | 78 |
| FTZ | 80 |
| NAN | 81 |
| XORSIGN | 82 |
| BF16_V2 | 85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000100001....................................................
00000000....00.0...00......00000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v2"></a>
## 2. `HMNMX2_R_R_c[I][I]_P`

Syntax: `HMNMX2 R, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 HMNMX2 R0, R0, c[0x0] [0x0], P0;`

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
| modi (op 1) | 74-75 |
| F32 | 78 |
| FTZ | 80 |
| NAN | 81 |
| XORSIGN | 82 |
| BF16_V2 | 85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000100101....................00000000...................00000
00000000....00.0...00......00000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v3"></a>
## 3. `HMNMX2_R_R_cx[UR][I]_P`

Syntax: `HMNMX2 R, R, cx[UR][INT_IMM], P`  
Example: `@P0 HMNMX2 R0, R0, cx[UR0] [0x0], P0;`

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
| modi (op 1) | 74-75 |
| F32 | 78 |
| FTZ | 80 |
| NAN | 81 |
| XORSIGN | 82 |
| BF16_V2 | 85 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000100101...........................0...............000000000
00000000....00.0...00......10000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v4"></a>
## 4. `HMNMX2_R_R_UR_P`

Syntax: `HMNMX2 R, R, UR, P`  
Example: `@P0 HMNMX2 R0, R0, UR0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| modi (op 2) | 60-61 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| F32 | 78 |
| FTZ | 80 |
| NAN | 81 |
| XORSIGN | 82 |
| BF16_V2 | 85 |
| operand 3 | 86-89 |
| cNOT (op 3) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000100011...........................000000000000000000000....
00000000....00.0...00......10000000000000.....................00
```

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v5"></a>
## 5. `HMNMX2_R_R_R_P`

Syntax: `HMNMX2 R, R, R, P`  
Example: `@P0 HMNMX2 R0, R0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi (op 2) | 60-61 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| F32 | 78 |
| FTZ | 80 |
| NAN | 81 |
| XORSIGN | 82 |
| BF16_V2 | 85 |
| operand 3 | 86-89 |
| cNOT (op 3) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000100100............................00000000000000000000....
00000000....00.0...00......00000000000000.....................00
```

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

