# MATCH (SM89 SASS)

**NVIDIA:** Match Register Values Across Thread Group (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Warp match (match.any / match.all) (category: Predicate / compare)

Typically emitted for: `match.any/all.sync`; `__match_any_sync`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x3a1 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4493)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [match](../verify/RESULTS.md#match): `match.any.sync.b32`

Bits marked fixed on the source page that real ptxas output sets (typically modifiers or implicit operands the page did not label):

| bit | seen in |
|---|---|
| 79 | `MATCH.ANY R5, R0` |

Encodings: <https://kuterdinel.com/nv_isa_sm89/MATCH.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [MATCH_P_R_R](#v1)
- [MATCH_R_R](#v2)

<a id="v1"></a>
## 1. `MATCH_P_R_R`

Syntax: `MATCH.ALL P, R, R`  
Example: `@P0 MATCH.ALL P0, R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| U64 | 73 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001011100....................00000000000000000000000000000000
000000000.000000....000000000000000000000.....................00
```

<a id="v2"></a>
## 2. `MATCH_R_R`

Syntax: `MATCH.ANY R, R`  
Example: `@P0 MATCH.ANY R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| U64 | 73 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001011100....................00000000000000000000000000000000
000000000.0000010000000000000000000000000.....................00
```

