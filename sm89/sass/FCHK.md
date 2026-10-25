# FCHK (SM89 SASS)

**NVIDIA:** Floating-point Range Check (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Range check for FP32 division (sets predicate when slow path needed) (category: FP32)

Typically emitted for: `div.rn.f32` full-precision division (guards the slow path)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [fdiv_rn](../verify/RESULTS.md#fdiv_rn): `div.rn.f32 (IEEE division)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/FCHK.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [FCHK_P_R_FI](#v1)
- [FCHK_P_R_c[I][I]](#v2)
- [FCHK_P_R_cx[UR][I]](#v3)
- [FCHK_P_R_UR](#v4)
- [FCHK_P_R_R](#v5)

<a id="v1"></a>
## 1. `FCHK_P_R_FI`

Syntax: `FCHK P, R, FIMM`  
Example: `@P0 FCHK P0, R0, 0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000001001....00000000........................................
00000000..000000....000000000000000000000.....................00
```

<a id="v2"></a>
## 2. `FCHK_P_R_c[I][I]`

Syntax: `FCHK P, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 FCHK P0, R0, c[0x0][0x0] ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000001101....00000000........00000000...................00000
00000000..000000....000000000000000000000.....................00
```

<a id="v3"></a>
## 3. `FCHK_P_R_cx[UR][I]`

Syntax: `FCHK P, R, cx[UR][INT_IMM]`  
Example: `@P0 FCHK P0, R0, cx[UR0][0x0] ;`

Register access: READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000001101....00000000...............0...............000000000
00000000..000000....000000010000000000000.....................00
```

<a id="v4"></a>
## 4. `FCHK_P_R_UR`

Syntax: `FCHK P, R, UR`  
Example: `@P0 FCHK P0, R0, UR0 ;`

Register access: READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000001011....00000000...............00000000000000000000000..
00000000..000000....000000010000000000000.....................00
```

<a id="v5"></a>
## 5. `FCHK_P_R_R`

Syntax: `FCHK P, R, R`  
Example: `@P0 FCHK P0, R0, R0 ;`

Register access: READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000001100....00000000................0000000000000000000000..
00000000..000000....000000000000000000000.....................00
```

