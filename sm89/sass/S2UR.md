# S2UR (SM89 SASS)

**NVIDIA:** Move Special Register to Uniform Register (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Special register to uniform register (category: Movement)

Typically emitted for: special register read whose value is warp-uniform and used on the uniform datapath (e.g. `%ctaid.x` as a loop bound); a plain `%ctaid.x` store still uses S2R

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [s2ur_loop](../verify/RESULTS.md#s2ur_loop): `%ctaid.x as a loop bound (warp-uniform)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/S2UR.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [S2UR_UR_SR](#v1)

<a id="v1"></a>
## 1. `S2UR_UR_SR`

Syntax: `S2UR UR, SR`  
Example: `@UP0 S2UR UR0, SR_LANEID ;`

Register access: WRITE UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 72-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110000111001...........00000000000000000000000000000000000000000
00000000........0000000000000000000000000.....................00
```

