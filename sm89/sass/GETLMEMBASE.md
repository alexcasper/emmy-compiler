# GETLMEMBASE (SM89 SASS)

**NVIDIA:** Get Local Memory Base Address (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Get local memory base address (category: Load / store)

Typically emitted for: local-memory window base (compiler-generated)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/GETLMEMBASE.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [GETLMEMBASE_R](#v1)

<a id="v1"></a>
## 1. `GETLMEMBASE_R`

Syntax: `GETLMEMBASE R`  
Example: `@P0 GETLMEMBASE R0 ;`

Register access: WRITE R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000000111100............0000000000000000000000000000000000000000
00000000000000000000000000000000000000000.....................00
```

