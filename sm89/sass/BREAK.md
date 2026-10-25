# BREAK (SM89 SASS)

**NVIDIA:** Break out of the Specified Convergence Barrier (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Break out of convergence barrier (category: Control flow)

Typically emitted for: divergent `break` out of loop

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x942 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4152)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/BREAK.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [BREAK_B](#v1)
- [BREAK_P_B](#v2)

<a id="v1"></a>
## 1. `BREAK_B`

Syntax: `BREAK B`  
Example: `@P0 BREAK B0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-20 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000101001.........0000000000000000000000000000000000000000000
00000000000000000000000111000000000000000.....111111..........00
```

<a id="v2"></a>
## 2. `BREAK_P_B`

Syntax: `BREAK P, B`  
Example: `@P0 BREAK P0, B0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-20 |
| operand 0 | 86-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000101001.........0000000000000000000000000000000000000000000
0000000000000000000000.....00000000000000.....111111..........00
```

