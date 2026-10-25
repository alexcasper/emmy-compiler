# YIELD (SM89 SASS)

**NVIDIA:** Yield Control (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Yield warp scheduling (category: Control flow)

Typically emitted for: compiler-inserted in spin loops for forward progress

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/YIELD.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [YIELD](#v1)
- [YIELD_P](#v2)

<a id="v1"></a>
## 1. `YIELD`

Syntax: `YIELD`  
Example: `@P0 YIELD;`

| field | bits |
|---|---|
| predicate | 12-15 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000101001....000000000000000000000000000000000000000000000000
00000000000000000000000111000000000000000.....111111..........00
```

<a id="v2"></a>
## 2. `YIELD_P`

Syntax: `YIELD P`  
Example: `@P0 YIELD P0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 86-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000101001....000000000000000000000000000000000000000000000000
0000000000000000000000.....00000000000000.....111111..........00
```

