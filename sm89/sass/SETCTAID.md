# SETCTAID (SM89 SASS)

**NVIDIA:** Set CTA ID (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Set CTA id (category: Synchronization / barriers)

Typically emitted for: (unknown; not produced by normal compute code)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/SETCTAID.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [SETCTAID_R](#v1)

<a id="v1"></a>
## 1. `SETCTAID_R`

Syntax: `SETCTAID R`  
Example: `@P0 SETCTAID.X R0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111110001100....00000000........00000000000000000000000000000000
00000000000000..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `X.` |
| `01` | `Y.` |
| `10` | `Z.` |
| `11` | `(default)` |

