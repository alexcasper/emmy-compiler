# MOVM (SM89 SASS)

**NVIDIA:** Move Matrix with Transposition or Expansion (Movement Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Matrix move/transpose within warp (movmatrix) (category: Movement)

Typically emitted for: `movmatrix.sync.aligned.m8n8.trans.b16`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x23a ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4663)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [movm](../verify/RESULTS.md#movm): `movmatrix.sync.aligned.m8n8.trans.b16`

Encodings: <https://kuterdinel.com/nv_isa_sm89/MOVM.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [MOVM_R_R](#v1)

<a id="v1"></a>
## 1. `MOVM_R_R`

Syntax: `MOVM.16 R, R`  
Example: `@P0 MOVM.16.MT88 R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010111000100....................00000000000000000000000000000000
00000000000000..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `MT88.` |
| `01` | `M832.` |
| `10` | `M864.` |
| `11` | `INVALID3.` |

