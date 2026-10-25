# EXIT (SM89 SASS)

**NVIDIA:** Exit Program (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Exit thread (category: Control flow)

Typically emitted for: `exit` / `ret` from the kernel; early `return`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x94d ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4218)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [prologue](../verify/RESULTS.md#prologue): `empty kernel body: param pointer + %tid.x load/store`

Encodings: <https://kuterdinel.com/nv_isa_sm89/EXIT.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [EXIT](#v1)
- [EXIT_P](#v2)

<a id="v1"></a>
## 1. `EXIT`

Syntax: `EXIT`  
Example: `@P0 EXIT;`

| field | bits |
|---|---|
| predicate | 12-15 |
| modi 1 | 84-85 |
| NO_ATEXIT | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101100101001....000000000000000000000000000000000000000000000000
00000000000000000000...111000000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `KEEPREFCOUNT.` |
| `10` | `PREEMPTED.` |
| `11` | `INVALID3.` |

<a id="v2"></a>
## 2. `EXIT_P`

Syntax: `EXIT P`  
Example: `@P0 EXIT P0;`

Register access: READ P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| modi 1 | 84-85 |
| NO_ATEXIT | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101100101001....000000000000000000000000000000000000000000000000
00000000000000000000.......00000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `KEEPREFCOUNT.` |
| `10` | `PREEMPTED.` |
| `11` | `INVALID3.` |

