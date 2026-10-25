# S2R (SM89 SASS)

**NVIDIA:** Move Special Register to Register (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Move special register (tid, ctaid, laneid, clock...) to register (category: Movement)

Typically emitted for: `mov.u32 %tid.x`, `%ctaid`, `%laneid`, `%lanemask_*`, `%smid` ...

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x919, 0x9c3 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4404)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [s2r](../verify/RESULTS.md#s2r): `mov.u32 %laneid`
- [s2r_ctaid](../verify/RESULTS.md#s2r_ctaid): `mov.u32 %ctaid.x stored directly`
- [prologue](../verify/RESULTS.md#prologue): `empty kernel body: param pointer + %tid.x load/store`

Encodings: <https://kuterdinel.com/nv_isa_sm89/S2R.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [S2R_R_SR](#v1)

<a id="v1"></a>
## 1. `S2R_R_SR`

Syntax: `S2R R, SR`  
Example: `@P0 S2R R0, SR_LANEID ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 72-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110001001............0000000000000000000000000000000000000000
00000000........0000000000000000000000000.....................00
```

