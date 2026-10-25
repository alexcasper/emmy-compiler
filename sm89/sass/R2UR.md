# R2UR (SM89 SASS)

**NVIDIA:** Move from Vector Register to a Uniform Register (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Register to uniform register (category: Movement)

Typically emitted for: compiler moving warp-uniform values into uniform datapath

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x2ca, 0x3c2 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2688)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/R2UR.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [R2UR_P_UR_R](#v1)
- [R2UR_UR_R](#v2)

<a id="v1"></a>
## 1. `R2UR_P_UR_R`

Syntax: `R2UR P, UR, R`  
Example: `@P0 R2UR P0, UR0, R0 ;`

Register access: WRITE UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-22 |
| operand 2 | 24-31 |
| operand 0 | 80-83 |
| OR | 84 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000111100...........0........00000000000000000000000000000000
0000000000000000.....00000000000000000000.....................00
```

<a id="v2"></a>
## 2. `R2UR_UR_R`

Syntax: `R2UR UR, R`  
Example: `@P0 R2UR UR0, R0 ;`

Register access: WRITE UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-31 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000111100...........0........00000000000000000000000000000000
00000000000000000111000000000000000000000.....................00
```

