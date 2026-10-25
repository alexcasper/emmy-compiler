# BSSY (SM89 SASS)

**NVIDIA:** Barrier Set Convergence Synchronization Point (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Set convergence barrier (start of divergent region) (category: Control flow)

Typically emitted for: start of a divergent region (compiler-inserted for if/else, loops with divergent exits)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x945 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4165)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [bssy_bsync](../verify/RESULTS.md#bssy_bsync): `divergent loop exit followed by a warp-synchronous op`

Encodings: <https://kuterdinel.com/nv_isa_sm89/BSSY.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [BSSY_B_I](#v1)
- [BSSY_P_B_I](#v2)

<a id="v1"></a>
## 1. `BSSY_B_I`

Syntax: `BSSY B, INT_IMM`  
Example: `@P0 BSSY B0, 0x10;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-20 |
| operand 1 | 33-63 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000101001.........000000000000...............................
00000000000000000000000111000000000000000.....111111..........00
```

<a id="v2"></a>
## 2. `BSSY_P_B_I`

Syntax: `BSSY P, B, INT_IMM`  
Example: `@P0 BSSY P0, B0, 0x10;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-20 |
| operand 2 | 33-63 |
| operand 0 | 86-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000101001.........000000000000...............................
0000000000000000000000.....00000000000000.....111111..........00
```

