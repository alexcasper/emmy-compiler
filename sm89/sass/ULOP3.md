# ULOP3 (SM89 SASS)

**NVIDIA:** Logic Operation (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform 3-input logic (category: Uniform datapath)

Typically emitted for: warp-uniform bitwise logic

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [uniform_alu](../verify/RESULTS.md#uniform_alu): `integer ops on a kernel parameter (warp-uniform)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/ULOP3.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [ULOP3_UP_UR_UR_I_UR_I_UP](#v1)
- [ULOP3_UR_UR_I_UR_I_UP](#v2)
- [ULOP3_UP_UR_UR_UR_UR_I_UP](#v3)
- [ULOP3_UR_UR_UR_UR_I_UP](#v4)

<a id="v1"></a>
## 1. `ULOP3_UP_UR_UR_I_UR_I_UP`

Syntax: `ULOP3.LUT UP, UR, UR, INT_IMM, UR, INT_IMM, UP`  
Example: `@UP0 ULOP3.LUT UP0, UR0, UR0, 0x0, UR0, 0x0, UP0;`

Register access: READ_WRITE UP (1 slots); WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| operand 4 | 64-70 |
| operand 5 | 72-79 |
| PAND | 80 |
| operand 0 | 81-83 |
| operand 6 | 86-89 |
| cNOT (op 6) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010010001...........0.......0................................
.......0............00.....10000000000000.....................00
```

<a id="v2"></a>
## 2. `ULOP3_UR_UR_I_UR_I_UP`

Syntax: `ULOP3.LUT UR, UR, INT_IMM, UR, INT_IMM, UP`  
Example: `@UP0 ULOP3.LUT UR0, UR0, 0x0, UR0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| operand 4 | 72-79 |
| PAND | 80 |
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
010010010001...........0.......0................................
.......0.........11100.....10000000000000.....................00
```

<a id="v3"></a>
## 3. `ULOP3_UP_UR_UR_UR_UR_I_UP`

Syntax: `ULOP3.LUT UP, UR, UR, UR, UR, INT_IMM, UP`  
Example: `@UP0 ULOP3.LUT UP0, UR0, UR0, UR0, UR0, 0x0, UP0;`

Register access: READ_WRITE UP (1 slots); WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| operand 4 | 64-70 |
| operand 5 | 72-79 |
| PAND | 80 |
| operand 0 | 81-83 |
| operand 6 | 86-89 |
| cNOT (op 6) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010010100...........0.......0.......0000000000000000000000000
.......0............00.....10000000000000.....................00
```

<a id="v4"></a>
## 4. `ULOP3_UR_UR_UR_UR_I_UP`

Syntax: `ULOP3.LUT UR, UR, UR, UR, INT_IMM, UP`  
Example: `@UP0 ULOP3.LUT UR0, UR0, UR0, UR0, 0x0, UP0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| operand 3 | 64-70 |
| operand 4 | 72-79 |
| PAND | 80 |
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
010010010100...........0.......0.......0000000000000000000000000
.......0.........11100.....10000000000000.....................00
```

