# NOP (SM89 SASS)

**NVIDIA:** No Operation (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: No operation (category: Control flow)

Typically emitted for: padding/alignment (compiler-generated)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x918 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4371)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/NOP.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [NOP](#v1)
- [NOP](#v2)

<a id="v1"></a>
## 1. `NOP`

Syntax: `NOP`  
Example: `NOP;`

| field | bits |
|---|---|
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
0000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000.....................00
```

<a id="v2"></a>
## 2. `NOP`

Syntax: `NOP`  
Example: `@P0 NOP;`

| field | bits |
|---|---|
| predicate | 12-15 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000110001001....000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000.....................00
```

