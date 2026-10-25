# HFMA2 (SM89 SASS)

**NVIDIA:** FP16 Fused Mutiply Add (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Packed FP16x2 / BF16x2 FMA (HFMA2.MMA variant runs on the FMA-heavy pipe) (category: FP16 (packed half2))

Typically emitted for: `fma.rn.f16x2`/`bf16x2`; `__hfma2`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x31 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1350)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [hfma2](../verify/RESULTS.md#hfma2): `fma.rn.f16x2`
- [hfma2_bf16](../verify/RESULTS.md#hfma2_bf16): `fma.rn.bf16x2`

Encodings: <https://kuterdinel.com/nv_isa_sm89/HFMA2.html> (machine-derived by fuzzing the assembler; no semantics).

36 encoding variant(s):

- [HFMA2_R_R_R_FI_FI](#v1)
- [HFMA2_R_R_R_FI_FI_P](#v2)
- [HFMA2_R_R_R_FI_FI](#v3)
- [HFMA2_R_R_R_FI_FI_P](#v4)
- [HFMA2_R_R_R_c[I][I]](#v5)
- [HFMA2_R_R_R_c[I][I]_P](#v6)
- [HFMA2_R_R_R_cx[UR][I]](#v7)
- [HFMA2_R_R_R_cx[UR][I]_P](#v8)
- [HFMA2_R_R_R_c[I][I]](#v9)
- [HFMA2_R_R_R_c[I][I]_P](#v10)
- [HFMA2_R_R_R_cx[UR][I]](#v11)
- [HFMA2_R_R_R_cx[UR][I]_P](#v12)
- [HFMA2_R_R_FI_FI_R](#v13)
- [HFMA2_R_R_FI_FI_R_P](#v14)
- [HFMA2_R_R_FI_FI_R](#v15)
- [HFMA2_R_R_FI_FI_R_P](#v16)
- [HFMA2_R_R_c[I][I]_R](#v17)
- [HFMA2_R_R_c[I][I]_R_P](#v18)
- [HFMA2_R_R_cx[UR][I]_R](#v19)
- [HFMA2_R_R_cx[UR][I]_R_P](#v20)
- [HFMA2_R_R_c[I][I]_R](#v21)
- [HFMA2_R_R_c[I][I]_R_P](#v22)
- [HFMA2_R_R_cx[UR][I]_R](#v23)
- [HFMA2_R_R_cx[UR][I]_R_P](#v24)
- [HFMA2_R_R_UR_R](#v25)
- [HFMA2_R_R_UR_R_P](#v26)
- [HFMA2_R_R_UR_R](#v27)
- [HFMA2_R_R_UR_R_P](#v28)
- [HFMA2_R_R_R_UR](#v29)
- [HFMA2_R_R_R_UR_P](#v30)
- [HFMA2_R_R_R_UR](#v31)
- [HFMA2_R_R_R_UR_P](#v32)
- [HFMA2_R_R_R_R](#v33)
- [HFMA2_R_R_R_R_P](#v34)
- [HFMA2_R_R_R_R](#v35)
- [HFMA2_R_R_R_R_P](#v36)

<a id="v1"></a>
## 1. `HFMA2_R_R_R_FI_FI`

Syntax: `HFMA2 R, R, R, FIMM, FIMM`  
Example: `@P0 HFMA2 R0, R0, R0, 0, 0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 32-47 |
| operand 3 | 48-63 |
| operand 2 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000010....................................................
...............0.......000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v2"></a>
## 2. `HFMA2_R_R_R_FI_FI_P`

Syntax: `HFMA2.RELU R, R, R, FIMM, FIMM, P`  
Example: `@P0 HFMA2.RELU R0, R0, R0, 0, 0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 32-47 |
| operand 3 | 48-63 |
| operand 2 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000010....................................................
.............0.1...........00000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v3"></a>
## 3. `HFMA2_R_R_R_FI_FI`

Syntax: `HFMA2 R, R, R, FIMM, FIMM`  
Example: `@P0 HFMA2 R0, R0, R0, 0, 0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 32-47 |
| operand 3 | 48-63 |
| operand 2 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000010....................................................
...............0.......000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v4"></a>
## 4. `HFMA2_R_R_R_FI_FI_P`

Syntax: `HFMA2.RELU R, R, R, FIMM, FIMM, P`  
Example: `@P0 HFMA2.RELU R0, R0, R0, 0, 0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 32-47 |
| operand 3 | 48-63 |
| operand 2 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000010....................................................
.............0.1...........00000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v5"></a>
## 5. `HFMA2_R_R_R_c[I][I]`

Syntax: `HFMA2 R, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 HFMA2 R0, R0, R0, c[0x0] [0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000110....................00000000...................00000
...............0.......000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v6"></a>
## 6. `HFMA2_R_R_R_c[I][I]_P`

Syntax: `HFMA2.RELU R, R, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 HFMA2.RELU R0, R0, R0, c[0x0] [0x0], P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000110....................00000000...................00000
.............0.1...........00000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v7"></a>
## 7. `HFMA2_R_R_R_cx[UR][I]`

Syntax: `HFMA2 R, R, R, cx[UR][INT_IMM]`  
Example: `@P0 HFMA2 R0, R0, R0, cx[UR0] [0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000110...........................0...............000000000
...............0.......000010000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v8"></a>
## 8. `HFMA2_R_R_R_cx[UR][I]_P`

Syntax: `HFMA2.RELU R, R, R, cx[UR][INT_IMM], P`  
Example: `@P0 HFMA2.RELU R0, R0, R0, cx[UR0] [0x0], P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000110...........................0...............000000000
.............0.1...........10000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v9"></a>
## 9. `HFMA2_R_R_R_c[I][I]`

Syntax: `HFMA2 R, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 HFMA2 R0, R0, R0, c[0x0] [0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000110....................00000000...................00000
...............0.......000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v10"></a>
## 10. `HFMA2_R_R_R_c[I][I]_P`

Syntax: `HFMA2.RELU R, R, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 HFMA2.RELU R0, R0, R0, c[0x0] [0x0], P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000110....................00000000...................00000
.............0.1...........00000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v11"></a>
## 11. `HFMA2_R_R_R_cx[UR][I]`

Syntax: `HFMA2 R, R, R, cx[UR][INT_IMM]`  
Example: `@P0 HFMA2 R0, R0, R0, cx[UR0] [0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000110...........................0...............000000000
...............0.......000010000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v12"></a>
## 12. `HFMA2_R_R_R_cx[UR][I]_P`

Syntax: `HFMA2.RELU R, R, R, cx[UR][INT_IMM], P`  
Example: `@P0 HFMA2.RELU R0, R0, R0, cx[UR0] [0x0], P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000110...........................0...............000000000
.............0.1...........10000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v13"></a>
## 13. `HFMA2_R_R_FI_FI_R`

Syntax: `HFMA2 R, R, FIMM, FIMM, R`  
Example: `@P0 HFMA2 R0, R0, 0, 0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-47 |
| operand 2 | 48-63 |
| operand 4 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000001....................................................
...............0......0000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v14"></a>
## 14. `HFMA2_R_R_FI_FI_R_P`

Syntax: `HFMA2.RELU R, R, FIMM, FIMM, R, P`  
Example: `@P0 HFMA2.RELU R0, R0, 0, 0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-47 |
| operand 2 | 48-63 |
| operand 4 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000001....................................................
.............0.1...........00000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v15"></a>
## 15. `HFMA2_R_R_FI_FI_R`

Syntax: `HFMA2 R, R, FIMM, FIMM, R`  
Example: `@P0 HFMA2 R0, R0, 0, 0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-47 |
| operand 2 | 48-63 |
| operand 4 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000001....................................................
...............0......0000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v16"></a>
## 16. `HFMA2_R_R_FI_FI_R_P`

Syntax: `HFMA2.RELU R, R, FIMM, FIMM, R, P`  
Example: `@P0 HFMA2.RELU R0, R0, 0, 0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-47 |
| operand 2 | 48-63 |
| operand 4 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000001....................................................
.............0.1...........00000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v17"></a>
## 17. `HFMA2_R_R_c[I][I]_R`

Syntax: `HFMA2 R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 HFMA2 R0, R0, c[0x0] [0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000101....................00000000...................00000
...............0......0000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v18"></a>
## 18. `HFMA2_R_R_c[I][I]_R_P`

Syntax: `HFMA2.RELU R, R, c[INT_IMM][INT_IMM], R, P`  
Example: `@P0 HFMA2.RELU R0, R0, c[0x0] [0x0], R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000101....................00000000...................00000
.............0.1...........00000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v19"></a>
## 19. `HFMA2_R_R_cx[UR][I]_R`

Syntax: `HFMA2 R, R, cx[UR][INT_IMM], R`  
Example: `@P0 HFMA2 R0, R0, cx[UR0] [0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000101...........................0...............000000000
...............0......0000010000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v20"></a>
## 20. `HFMA2_R_R_cx[UR][I]_R_P`

Syntax: `HFMA2.RELU R, R, cx[UR][INT_IMM], R, P`  
Example: `@P0 HFMA2.RELU R0, R0, cx[UR0] [0x0], R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000101...........................0...............000000000
.............0.1...........10000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v21"></a>
## 21. `HFMA2_R_R_c[I][I]_R`

Syntax: `HFMA2 R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 HFMA2 R0, R0, c[0x0] [0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000101....................00000000...................00000
...............0......0000000000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v22"></a>
## 22. `HFMA2_R_R_c[I][I]_R_P`

Syntax: `HFMA2.RELU R, R, c[INT_IMM][INT_IMM], R, P`  
Example: `@P0 HFMA2.RELU R0, R0, c[0x0] [0x0], R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000101....................00000000...................00000
.............0.1...........00000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v23"></a>
## 23. `HFMA2_R_R_cx[UR][I]_R`

Syntax: `HFMA2 R, R, cx[UR][INT_IMM], R`  
Example: `@P0 HFMA2 R0, R0, cx[UR0] [0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000101...........................0...............000000000
...............0......0000010000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v24"></a>
## 24. `HFMA2_R_R_cx[UR][I]_R_P`

Syntax: `HFMA2.RELU R, R, cx[UR][INT_IMM], R, P`  
Example: `@P0 HFMA2.RELU R0, R0, cx[UR0] [0x0], R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

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
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 4) | 81-82 |
| cABS (op 4) | 83 |
| cNEG (op 4) | 84 |
| BF16_V2 | 85 |
| operand 5 | 86-89 |
| cNOT (op 5) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000101...........................0...............000000000
.............0.1...........10000000000000.....................00
```

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v25"></a>
## 25. `HFMA2_R_R_UR_R`

Syntax: `HFMA2 R, R, UR, R`  
Example: `@P0 HFMA2 R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| modi (op 2) | 60-61 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 3) | 81-82 |
| cABS (op 3) | 83 |
| cNEG (op 3) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000011...........................000000000000000000000....
...............0.......000010000000000000.....................00
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

Operand 3 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v26"></a>
## 26. `HFMA2_R_R_UR_R_P`

Syntax: `HFMA2.RELU R, R, UR, R, P`  
Example: `@P0 HFMA2.RELU R0, R0, UR0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| modi (op 2) | 60-61 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 3) | 81-82 |
| cABS (op 3) | 83 |
| cNEG (op 3) | 84 |
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
100011000011...........................000000000000000000000....
.............0.1...........10000000000000.....................00
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

Operand 3 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v27"></a>
## 27. `HFMA2_R_R_UR_R`

Syntax: `HFMA2 R, R, UR, R`  
Example: `@P0 HFMA2 R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| modi (op 2) | 60-61 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 3) | 81-82 |
| cABS (op 3) | 83 |
| cNEG (op 3) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000011...........................000000000000000000000....
...............0.......000010000000000000.....................00
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

Operand 3 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v28"></a>
## 28. `HFMA2_R_R_UR_R_P`

Syntax: `HFMA2.RELU R, R, UR, R, P`  
Example: `@P0 HFMA2.RELU R0, R0, UR0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| modi (op 2) | 60-61 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 3) | 81-82 |
| cABS (op 3) | 83 |
| cNEG (op 3) | 84 |
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
100011000011...........................000000000000000000000....
.............0.1...........10000000000000.....................00
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

Operand 3 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v29"></a>
## 29. `HFMA2_R_R_R_UR`

Syntax: `HFMA2 R, R, R, UR`  
Example: `@P0 HFMA2 R0, R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| modi (op 3) | 60-61 |
| cABS (op 3) | 62 |
| cNEG (op 3) | 63 |
| operand 2 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000111...........................000000000000000000000....
...............0.......000010000000000000.....................00
```

Operand 3 operand modifiers:

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v30"></a>
## 30. `HFMA2_R_R_R_UR_P`

Syntax: `HFMA2.RELU R, R, R, UR, P`  
Example: `@P0 HFMA2.RELU R0, R0, R0, UR0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| modi (op 3) | 60-61 |
| cABS (op 3) | 62 |
| cNEG (op 3) | 63 |
| operand 2 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
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
100011000111...........................000000000000000000000....
.............0.1...........10000000000000.....................00
```

Operand 3 operand modifiers:

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v31"></a>
## 31. `HFMA2_R_R_R_UR`

Syntax: `HFMA2 R, R, R, UR`  
Example: `@P0 HFMA2 R0, R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| modi (op 3) | 60-61 |
| cABS (op 3) | 62 |
| cNEG (op 3) | 63 |
| operand 2 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000111...........................000000000000000000000....
...............0.......000010000000000000.....................00
```

Operand 3 operand modifiers:

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v32"></a>
## 32. `HFMA2_R_R_R_UR_P`

Syntax: `HFMA2.RELU R, R, R, UR, P`  
Example: `@P0 HFMA2.RELU R0, R0, R0, UR0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| modi (op 3) | 60-61 |
| cABS (op 3) | 62 |
| cNEG (op 3) | 63 |
| operand 2 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 2) | 81-82 |
| cABS (op 2) | 83 |
| cNEG (op 2) | 84 |
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
100011000111...........................000000000000000000000....
.............0.1...........10000000000000.....................00
```

Operand 3 operand modifiers:

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

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v33"></a>
## 33. `HFMA2_R_R_R_R`

Syntax: `HFMA2 R, R, R, R`  
Example: `@P0 HFMA2 R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi (op 2) | 60-61 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 3) | 81-82 |
| cABS (op 3) | 83 |
| cNEG (op 3) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000100............................00000000000000000000....
...............0.......000000000000000000.....................00
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

Operand 3 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v34"></a>
## 34. `HFMA2_R_R_R_R_P`

Syntax: `HFMA2.RELU R, R, R, R, P`  
Example: `@P0 HFMA2.RELU R0, R0, R0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi (op 2) | 60-61 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 3) | 81-82 |
| cABS (op 3) | 83 |
| cNEG (op 3) | 84 |
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
100011000100............................00000000000000000000....
.............0.1...........00000000000000.....................00
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

Operand 3 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v35"></a>
## 35. `HFMA2_R_R_R_R`

Syntax: `HFMA2 R, R, R, R`  
Example: `@P0 HFMA2 R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi (op 2) | 60-61 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| SAT | 77 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 3) | 81-82 |
| cABS (op 3) | 83 |
| cNEG (op 3) | 84 |
| BF16_V2 | 85 |
| H0_NH1 (op 2) | 86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100011000100............................00000000000000000000....
...............0.......000000000000000000.....................00
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

Operand 3 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

<a id="v36"></a>
## 36. `HFMA2_R_R_R_R_P`

Syntax: `HFMA2.RELU R, R, R, R, P`  
Example: `@P0 HFMA2.RELU R0, R0, R0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi (op 2) | 60-61 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi (op 1) | 74-75 |
| FMZ | 76 |
| F32 | 78 |
| FTZ | 80 |
| modi (op 3) | 81-82 |
| cABS (op 3) | 83 |
| cNEG (op 3) | 84 |
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
100011000100............................00000000000000000000....
.............0.1...........00000000000000.....................00
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

Operand 3 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `F32.` |
| `10` | `H0_H0.` |
| `11` | `H1_H1.` |

