# REDUX (SM89 SASS)

**NVIDIA:** Reduction of a Vector Register into a Uniform Register (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Warp-wide integer reduction to uniform register (redux.sync) (category: Atomics / reductions)

Typically emitted for: `redux.sync.add/min/max/and/or/xor.u32/s32`; `__reduce_add_sync`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x3c4 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2705)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [redux](../verify/RESULTS.md#redux): `redux.sync.add.u32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/REDUX.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [REDUX_UR_R](#v1)

<a id="v1"></a>
## 1. `REDUX_UR_R`

Syntax: `REDUX UR, R`  
Example: `@P0 REDUX UR0, R0 ;`

Register access: WRITE UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-31 |
| S32 | 73 |
| modi 2 | 78-80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001000111100...........0........00000000000000000000000000000000
000000000.0000...000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `OR.` |
| `010` | `XOR.` |
| `011` | `SUM.` |
| `100` | `MIN.` |
| `101` | `MAX.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

