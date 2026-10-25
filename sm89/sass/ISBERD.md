# ISBERD (SM89 SASS)

**NVIDIA:** not listed in the official Ampere/Ada opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)).

Notes: Internal stage buffer entry read (category: Graphics-only)

Typically emitted for: graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x923 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4286)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/ISBERD.html> (machine-derived by fuzzing the assembler; no semantics).

3 encoding variant(s):

- [ISBERD_R_I](#v1)
- [ISBERD_R_R](#v2)
- [ISBERD_R_RI](#v3)

<a id="v1"></a>
## 1. `ISBERD_R_I`

Syntax: `ISBERD R, [INT_IMM]`  
Example: `@P0 ISBERD R0, [0x2] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 40-55 |
| modi 1 | 74-75 |
| modi 2 | 76-77 |
| SKEW | 78 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110001001001............1111111100000000................00000000
0000000000......0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `U16.` |
| `10` | `32.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `PATCH.` |
| `10` | `PRIM.` |
| `11` | `ATTR.` |

<a id="v2"></a>
## 2. `ISBERD_R_R`

Syntax: `ISBERD R, [R]`  
Example: `@P0 ISBERD R0, [R0] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 74-75 |
| modi 2 | 76-77 |
| SKEW | 78 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110001001001....................00000000000000000000000000000000
0000000000......0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `U16.` |
| `10` | `32.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `PATCH.` |
| `10` | `PRIM.` |
| `11` | `ATTR.` |

<a id="v3"></a>
## 3. `ISBERD_R_RI`

Syntax: `ISBERD R, [R+INT_IMM]`  
Example: `@P0 ISBERD R0, [R0+0x1] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 40-55 |
| modi 1 | 74-75 |
| modi 2 | 76-77 |
| SKEW | 78 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110001001001....................00000000................00000000
0000000000......0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `U16.` |
| `10` | `32.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `PATCH.` |
| `10` | `PRIM.` |
| `11` | `ATTR.` |

