# UMOV (SM89 SASS)

**NVIDIA:** Uniform Move (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform register move (category: Uniform datapath)

Typically emitted for: uniform constants/moves (compiler-generated)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [uniform_txq](../verify/RESULTS.md#uniform_txq): `txq.num_mipmap_levels (handle arithmetic runs on uniform datapath)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/UMOV.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [UMOV_UR_I](#v1)
- [UMOV_UR_UR](#v2)

<a id="v1"></a>
## 1. `UMOV_UR_I`

Syntax: `UMOV UR, INT_IMM`  
Example: `@UP0 UMOV UR0, 0x0;`

Register access: WRITE UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 32-63 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000010001...........000000000................................
00000000000000000000000000000000000000000.....................00
```

<a id="v2"></a>
## 2. `UMOV_UR_UR`

Syntax: `UMOV UR, UR`  
Example: `@UP0 UMOV UR0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 32-38 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000010011...........000000000.......0000000000000000000000000
00000000000000000000000000010000000000000.....................00
```

