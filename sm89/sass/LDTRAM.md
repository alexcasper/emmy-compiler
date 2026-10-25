# LDTRAM (SM89 SASS)

**NVIDIA:** not listed in the official Ampere/Ada opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)).

Notes: Unknown; not in NVIDIA's table (name suggests attribute-RAM load) (category: Graphics-only)

Typically emitted for: graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x3ad ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4015)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/LDTRAM.html> (machine-derived by fuzzing the assembler; no semantics).

3 encoding variant(s):

- [LDTRAM_R_a[I]](#v1)
- [LDTRAM_R_a[URI]](#v2)
- [LDTRAM_R_a[UR]](#v3)

<a id="v1"></a>
## 1. `LDTRAM_R_a[I]`

Syntax: `LDTRAM R, a[INT_IMM]`  
Example: `@P0 LDTRAM.AB R0, a[0x4] ;`

Register access: WRITE R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 64-71 |
| modi 1 | 72 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101011100............1111110000000000000000000000000000000000
.........00000000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `AB.` |
| `1` | `C.` |

<a id="v2"></a>
## 2. `LDTRAM_R_a[URI]`

Syntax: `LDTRAM R, a[UR+INT_IMM]`  
Example: `@P0 LDTRAM.AB R0, a[UR0+0x4] ;`

Register access: WRITE R (2 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 2 | 64-71 |
| modi 1 | 72 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101011100...................000000000000000000000000000000000
.........00000000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `AB.` |
| `1` | `C.` |

<a id="v3"></a>
## 3. `LDTRAM_R_a[UR]`

Syntax: `LDTRAM R, a[UR]`  
Example: `@P0 LDTRAM.AB R0, a[UR0] ;`

Register access: WRITE R (2 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| modi 1 | 72 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101101011100...................000000000000000000000000000000000
00000000.00000000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `AB.` |
| `1` | `C.` |

