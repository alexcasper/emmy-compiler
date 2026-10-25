# FSEL (SM89 SASS)

**NVIDIA:** Floating Point Select (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: FP32 select by predicate (category: FP32)

Typically emitted for: `selp.f32` / float ternary `c ? a : b`

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [fsetp_selp](../verify/RESULTS.md#fsetp_selp): `setp.lt.f32 + selp.f32 (both arms computed)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/FSEL.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [FSEL_R_R_FI_P](#v1)
- [FSEL_R_R_c[I][I]_P](#v2)
- [FSEL_R_R_cx[UR][I]_P](#v3)
- [FSEL_R_R_UR_P](#v4)
- [FSEL_R_R_R_P](#v5)

<a id="v1"></a>
## 1. `FSEL_R_R_FI_P`

Syntax: `FSEL R, R, FIMM, P`  
Example: `@P0 FSEL R0, R0, 0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| FTZ | 80 |
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
000100000001....................................................
00000000..000000.00000.....00000000000000.....................00
```

<a id="v2"></a>
## 2. `FSEL_R_R_c[I][I]_P`

Syntax: `FSEL R, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 FSEL R0, R0, c[0x0][0x0], P0;`

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
| FTZ | 80 |
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
000100000101....................00000000...................00000
00000000..000000.00000.....00000000000000.....................00
```

<a id="v3"></a>
## 3. `FSEL_R_R_cx[UR][I]_P`

Syntax: `FSEL R, R, cx[UR][INT_IMM], P`  
Example: `@P0 FSEL R0, R0, cx[UR0][0x0], P0;`

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
| FTZ | 80 |
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
000100000101...........................0...............000000000
00000000..000000.00000.....10000000000000.....................00
```

<a id="v4"></a>
## 4. `FSEL_R_R_UR_P`

Syntax: `FSEL R, R, UR, P`  
Example: `@P0 FSEL R0, R0, UR0, P0;`

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
| FTZ | 80 |
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
000100000011...........................00000000000000000000000..
00000000..000000.00000.....10000000000000.....................00
```

<a id="v5"></a>
## 5. `FSEL_R_R_R_P`

Syntax: `FSEL R, R, R, P`  
Example: `@P0 FSEL R0, R0, R0, P0;`

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
| FTZ | 80 |
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
000100000100............................0000000000000000000000..
00000000..000000.00000.....00000000000000.....................00
```

