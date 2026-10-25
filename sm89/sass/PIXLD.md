# PIXLD (SM89 SASS)

**NVIDIA:** not listed in the official Ampere/Ada opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)).

Notes: Pixel info load (category: Graphics-only)

Typically emitted for: graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x925 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4381)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/PIXLD.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [PIXLD_R](#v1)
- [PIXLD_R_P](#v2)

<a id="v1"></a>
## 1. `PIXLD_R`

Syntax: `PIXLD R`  
Example: `@P0 PIXLD R0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| modi 1 | 78-80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101001001001............0000000000000000000000000000000000000000
00000000000000...111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `COVMASK.` |
| `010` | `CENTROID_OFFSET.` |
| `011` | `MY_INDEX.` |
| `100` | `INNER_COVERAGE.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

<a id="v2"></a>
## 2. `PIXLD_R_P`

Syntax: `PIXLD R, P`  
Example: `@P0 PIXLD R0, P0 ;`

Register access: WRITE R (1 slots); WRITE P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| modi 1 | 78-80 |
| operand 1 | 81-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101001001001............0000000000000000000000000000000000000000
00000000000000......000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `COVMASK.` |
| `010` | `CENTROID_OFFSET.` |
| `011` | `MY_INDEX.` |
| `100` | `INNER_COVERAGE.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

