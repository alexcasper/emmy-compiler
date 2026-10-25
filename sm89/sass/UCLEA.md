# UCLEA (SM89 SASS)

**NVIDIA:** Load Effective Address for a Constant (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform address of a constant (category: Uniform datapath)

Typically emitted for: per NVIDIA: load effective address for a constant; no PTX source found

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/UCLEA.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [UCLEA_UR_UP_UR_I_I](#v1)
- [UCLEA_UR_UP_UR_UR_I](#v2)

<a id="v1"></a>
## 1. `UCLEA_UR_UP_UR_I_I`

Syntax: `UCLEA UR, UP, UR, INT_IMM, INT_IMM`  
Example: `@UP0 UCLEA UR0, UP0, UR0, 0x0, 0x0;`

Register access: WRITE UR (2 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-47 |
| operand 4 | 72-76 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001111010001...........0.......0................0000000000000000
00000000.....000....000000010000000000000.....................00
```

<a id="v2"></a>
## 2. `UCLEA_UR_UP_UR_UR_I`

Syntax: `UCLEA UR, UP, UR, UR, INT_IMM`  
Example: `@UP0 UCLEA UR0, UP0, UR0, UR0, 0x0;`

Register access: WRITE UR (2 slots); READ UR (2 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 32-38 |
| operand 4 | 72-76 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001111010011...........0.......0.......0000000000000000000000000
00000000.....000....000000010000000000000.....................00
```

