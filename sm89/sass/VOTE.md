# VOTE (SM89 SASS)

**NVIDIA:** Vote Across SIMD Thread Group (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Warp vote (ALL, ANY, EQ, ballot) (category: Predicate / compare)

Typically emitted for: `vote.sync.all/any/uni/ballot`; `__all_sync`, `__ballot_sync`; `activemask`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x806, 0x886 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4465)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [vote](../verify/RESULTS.md#vote): `vote.sync.ballot.b32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/VOTE.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [VOTE_R_P_P](#v1)

<a id="v1"></a>
## 1. `VOTE_R_P_P`

Syntax: `VOTE R, P, P`  
Example: `@P0 VOTE.ALL R0, P0, P0;`

Register access: WRITE R (1 slots); READ P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| modi 1 | 72-73 |
| operand 1 | 80-83 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000000001............0000000000000000000000000000000000000000
00000000..000000....00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `ALL.` |
| `01` | `ANY.` |
| `10` | `EQ.` |
| `11` | `INVALID3.` |

