# UPLOP3 (SM89 SASS)

**NVIDIA:** Uniform Predicate Logic Operation (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform predicate logic (category: Uniform datapath)

Typically emitted for: uniform predicate logic

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/UPLOP3.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [UPLOP3_UP_UP_UP_UP_UP_I_I](#v1)
- [UPLOP3_UP_UP_UP_UR_UP_I_I](#v2)
- [UPLOP3_UP_UP_UP_UR_UR_I_I](#v3)
- [UPLOP3_UP_UP_UR_UR_UR_I_I](#v4)

<a id="v1"></a>
## 1. `UPLOP3_UP_UP_UP_UP_UP_I_I`

Syntax: `UPLOP3.LUT UP, UP, UP, UP, UP, INT_IMM, INT_IMM`  
Example: `@UP0 UPLOP3.LUT UP0, UP0, UP0, UP0, UP0, 0x0, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 5 | 64-66, 72-75, 77 |
| operand 4 | 67-70 |
| cNOT (op 4) | 71 |
| operand 3 | 76, 78-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001110010001............0000000000000000000000000000000000000000
...........................00000000000000.....................00
```

<a id="v2"></a>
## 2. `UPLOP3_UP_UP_UP_UR_UP_I_I`

Syntax: `UPLOP3.LUT UP, UP, UP, UR, UP, INT_IMM, INT_IMM`  
Example: `@UP0 UPLOP3.LUT UP0, UP0, UP0, UR0.SIGN, UP0, 0x0, 0x0;`

Register access: READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 3 | 32-38 |
| operand 4 | 67-70 |
| cNOT (op 4) | 71 |
| operand 5 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110010100............00000000.......0000000000000000000000000
000........................10000000000000.....................00
```

<a id="v3"></a>
## 3. `UPLOP3_UP_UP_UP_UR_UR_I_I`

Syntax: `UPLOP3.LUT UP, UP, UP, UR, UR, INT_IMM, INT_IMM`  
Example: `@UP0 UPLOP3.LUT UP0, UP0, UP0, UR0.SIGN, UR0.SIGN, 0x0, 0x0;`

Register access: READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 3 | 32-38 |
| operand 4 | 64-70 |
| operand 5 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011110010100............00000000.......0000000000000000000000000
.......0...................10000000000000.....................00
```

<a id="v4"></a>
## 4. `UPLOP3_UP_UP_UR_UR_UR_I_I`

Syntax: `UPLOP3.LUT UP, UP, UR, UR, UR, INT_IMM, INT_IMM`  
Example: `@UP0 UPLOP3.LUT UP0, UP0, UR0.SIGN, UR0.SIGN, UR0.SIGN, 0x0, 0x0;`

Register access: READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 6 | 16-23 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| operand 4 | 64-70 |
| operand 5 | 72-79 |
| operand 0 | 80-82 |
| operand 1 | 83-86 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111110010100...................0.......0000000000000000000000000
.......0...............000010000000000000.....................00
```

