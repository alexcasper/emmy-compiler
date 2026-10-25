# FSWZADD (SM89 SASS)

**NVIDIA:** FP32 Swizzle Add (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: FP32 swizzled add across quad lanes (derivatives) (category: FP32)

Typically emitted for: fragment-shader derivatives (ddx/ddy); no PTX equivalent; Mesa NAK emits it (see Evidence)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x822 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1132)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/FSWZADD.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [FSWZADD_R_R_R_SwzAdd](#v1)

<a id="v1"></a>
## 1. `FSWZADD_R_R_R_SwzAdd`

Syntax: `FSWZADD R, R, R, SwzAdd`  
Example: `@P0 FSWZADD R0, R0, R0, PPPPPPPP;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-39 |
| operand 2 | 64-71 |
| NDV | 77 |
| modi 1 | 78-79 |
| FTZ | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010001000001............................000000000000000000000000
........00000....000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `RM.` |
| `10` | `RP.` |
| `11` | `RZ.` |

