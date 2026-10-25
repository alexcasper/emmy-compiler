# HMMA (SM89 SASS)

**NVIDIA:** Matrix Multiply and Accumulate (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: FP16 / BF16 / TF32 tensor-core MMA (mma.sync m16n8k8/m16n8k16) (category: Tensor core (MMA))

Typically emitted for: `mma.sync.aligned.m16n8k8/k16.*.f16/bf16`, `.tf32` m16n8k4/k8; `wmma.mma` half/bf16/tf32

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x23c ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4577)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [hmma_f16](../verify/RESULTS.md#hmma_f16): `mma.sync.aligned.m16n8k16.row.col.f32.f16.f16.f32`
- [hmma_tf32](../verify/RESULTS.md#hmma_tf32): `mma.sync.aligned.m16n8k8.row.col.f32.tf32.tf32.f32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/HMMA.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [HMMA_R_R_R_R](#v1)
- [HMMA_R_R_R_R_R_I](#v2)
- [HMMA_R_R_R_R_UP](#v3)
- [HMMA_R_R_R_R_UP_R_I](#v4)

<a id="v1"></a>
## 1. `HMMA_R_R_R_R`

Syntax: `HMMA R, R, R, R`  
Example: `@P0 HMMA.1688.F16 R0, R0, R0, R0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| modi 1 | 75 |
| modi 2 | 76 |
| modi 3 | 78 |
| BF16 | 82 |
| TF32 | 83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001111000100............................00000000000000000000000.
.........00..0.000..000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `1688.` |
| `1` | `16816.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `F32.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0` | `1688.` |
| `1` | `1684.` |

<a id="v2"></a>
## 2. `HMMA_R_R_R_R_R_I`

Syntax: `HMMA.SP R, R, R, R, R, INT_IMM`  
Example: `@P0 HMMA.SP.1688.F16 R0, R0, R0, R0, R0, 0x0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots); READ R (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 4 | 40-47 |
| operand 5 | 48-50 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| modi 1 | 75 |
| modi 2 | 76 |
| modi 3 | 78 |
| BF16 | 82 |
| TF32 | 83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001111000100.......................................000000000000.
.........10..0.000..000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `1688.` |
| `1` | `16816.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `F32.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0` | `1688.` |
| `1` | `INVALID2.` |

<a id="v3"></a>
## 3. `HMMA_R_R_R_R_UP`

Syntax: `HMMA R, R, R, R, UP`  
Example: `@P0 HMMA.1688.F16 R0, R0, R0, R0, UP6 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (1 slots); READ R (2 slots); READ UP (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| modi 1 | 75 |
| modi 2 | 76 |
| modi 3 | 78 |
| BF16 | 82 |
| TF32 | 83 |
| operand 4 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001111000100............................00000000000000000000000.
.........00..0.000..0001...00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `1688.` |
| `1` | `16816.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `F32.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0` | `1688.` |
| `1` | `1684.` |

<a id="v4"></a>
## 4. `HMMA_R_R_R_R_UP_R_I`

Syntax: `HMMA.SP R, R, R, R, UP, R, INT_IMM`  
Example: `@P0 HMMA.SP.1688.F16 R0, R0, R0, R0, UP6, R0, 0x0 ;`

Register access: WRITE R (2 slots); READ R (2 slots); READ R (2 slots); READ R (2 slots); READ UP (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 5 | 40-47 |
| operand 6 | 48-50 |
| cNEG (op 2) | 63 |
| operand 3 | 64-71 |
| cNEG (op 1) | 72 |
| modi 1 | 75 |
| modi 2 | 76 |
| modi 3 | 78 |
| BF16 | 82 |
| TF32 | 83 |
| operand 4 | 88-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001111000100.......................................000000000000.
.........10..0.000..0001...00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `1688.` |
| `1` | `16816.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `F16.` |
| `1` | `F32.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0` | `1688.` |
| `1` | `INVALID2.` |

