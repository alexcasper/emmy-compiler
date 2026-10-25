# CS2R (SM89 SASS)

**NVIDIA:** Move Special Register to Register (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Move special register to register pair (fast: SR_CLOCKLO, zero idiom RZ) (category: Movement)

Typically emitted for: `mov.u32 %clock` / `%clock64`; also `CS2R R, SRZ` = zero a 64-bit pair

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x805 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4273)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [cs2r](../verify/RESULTS.md#cs2r): `mov.u64 %clock64`

Encodings: <https://kuterdinel.com/nv_isa_sm89/CS2R.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [CS2R_R_SR](#v1)

<a id="v1"></a>
## 1. `CS2R_R_SR`

Syntax: `CS2R R, SR`  
Example: `@P0 CS2R.32 R0, SR_LANEID;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 72-79 |
| modi 1 | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000000001............0000000000000000000000000000000000000000
00000000.........000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `32.` |
| `1` | `(default)` |

