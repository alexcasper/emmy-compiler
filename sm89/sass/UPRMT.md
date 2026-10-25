# UPRMT (SM89 SASS)

**NVIDIA:** Uniform Byte Permute (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform byte permute (category: Uniform datapath)

Typically emitted for: warp-uniform byte permute

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [uniform_alu](../verify/RESULTS.md#uniform_alu): `integer ops on a kernel parameter (warp-uniform)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/UPRMT.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [UPRMT_UR_UR_I_UR](#v1)
- [UPRMT_UR_UR_UR_UR](#v2)

<a id="v1"></a>
## 1. `UPRMT_UR_UR_I_UR`

Syntax: `UPRMT UR, UR, INT_IMM, UR`  
Example: `@UP0 UPRMT UR0, UR0, 0x0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| operand 3 | 64-70 |
| ???1 | 72 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010010001...........0.......0................................
.......0.00000000000000000010000000000000.....................00
```

<a id="v2"></a>
## 2. `UPRMT_UR_UR_UR_UR`

Syntax: `UPRMT UR, UR, UR, UR`  
Example: `@UP0 UPRMT UR0, UR0, UR0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots); READ UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 32-38 |
| operand 3 | 64-70 |
| ???1 | 72 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010010100...........0.......0.......0000000000000000000000000
.......0.00000000000000000010000000000000.....................00
```

