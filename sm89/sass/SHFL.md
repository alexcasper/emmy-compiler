# SHFL (SM89 SASS)

**NVIDIA:** Warp Wide Register Shuffle (Movement Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Warp shuffle (IDX, UP, DOWN, BFLY) (category: Movement)

Typically emitted for: `shfl.sync.idx/up/down/bfly`; `__shfl_sync`, `__shfl_xor_sync`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x389, 0x589, 0x989, 0xf89 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2558)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [shfl](../verify/RESULTS.md#shfl): `shfl.sync.bfly.b32`
- [agg_atomic](../verify/RESULTS.md#agg_atomic): `atom.global.add.u32 to a warp-uniform address (ptxas warp-aggregates it)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/SHFL.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [SHFL_P_R_R_R_I](#v1)
- [SHFL_P_R_R_I_R](#v2)
- [SHFL_P_R_R_I_I](#v3)
- [SHFL_P_R_R_R_R](#v4)

<a id="v1"></a>
## 1. `SHFL_P_R_R_R_I`

Syntax: `SHFL P, R, R, R, INT_IMM`  
Example: `@P0 SHFL.IDX P0, R0, R0, R0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| operand 4 | 40-53 |
| modi 1 | 58-59 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100100011010..........................................0000..0000
0000000000000000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `IDX.` |
| `01` | `UP.` |
| `10` | `DOWN.` |
| `11` | `BFLY.` |

<a id="v2"></a>
## 2. `SHFL_P_R_R_I_R`

Syntax: `SHFL P, R, R, INT_IMM, R`  
Example: `@P0 SHFL.IDX P0, R0, R0, 0x0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 52-57 |
| modi 1 | 58-59 |
| operand 4 | 64-71 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100100011001....................00000000000000000000........0000
........00000000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `IDX.` |
| `01` | `UP.` |
| `10` | `DOWN.` |
| `11` | `BFLY.` |

<a id="v3"></a>
## 3. `SHFL_P_R_R_I_I`

Syntax: `SHFL P, R, R, INT_IMM, INT_IMM`  
Example: `@P0 SHFL.IDX P0, R0, R0, 0x0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 4 | 40-51, 53 |
| operand 3 | 52, 54-57 |
| modi 1 | 58-59 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100100011111....................00000000....................0000
0000000000000000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `IDX.` |
| `01` | `UP.` |
| `10` | `DOWN.` |
| `11` | `BFLY.` |

<a id="v4"></a>
## 4. `SHFL_P_R_R_R_R`

Syntax: `SHFL P, R, R, R, R`  
Example: `@P0 SHFL.IDX P0, R0, R0, R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-39 |
| modi 1 | 58-59 |
| operand 4 | 64-71 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100100011100............................000000000000000000..0000
........00000000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `IDX.` |
| `01` | `UP.` |
| `10` | `DOWN.` |
| `11` | `BFLY.` |

