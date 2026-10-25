# IPA (SM89 SASS)

**NVIDIA:** not listed in the official Ampere/Ada opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)).

Notes: Interpolate attribute (category: Graphics-only)

Typically emitted for: graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x326 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3974)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/IPA.html> (machine-derived by fuzzing the assembler; no semantics).

20 encoding variant(s):

- [IPA_R_P_a[URI]](#v1)
- [IPA_R_P_a[URI]_R](#v2)
- [IPA_R_P_a[UR]](#v3)
- [IPA_R_P_a[UR]_R](#v4)
- [IPA_R_a[URI]](#v5)
- [IPA_R_a[URI]_R](#v6)
- [IPA_R_a[UR]](#v7)
- [IPA_R_a[UR]_R](#v8)
- [IPA_R_P_a[I]_I](#v9)
- [IPA_R_P_a[URI]_I](#v10)
- [IPA_R_P_a[UR]_I](#v11)
- [IPA_R_a[I]_I](#v12)
- [IPA_R_a[URI]_I](#v13)
- [IPA_R_a[UR]_I](#v14)
- [IPA_R_P_a[I]_c[I][I]](#v15)
- [IPA_R_a[I]_c[I][I]](#v16)
- [IPA_R_P_a[I]](#v17)
- [IPA_R_P_a[I]_R](#v18)
- [IPA_R_a[I]](#v19)
- [IPA_R_a[I]_R](#v20)

<a id="v1"></a>
## 1. `IPA_R_P_a[URI]`

Syntax: `IPA R, P, a[UR+INT_IMM]`  
Example: `@P0 IPA.PASS R0, P0, a[UR0+0x4] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-30 |
| operand 3 | 64-71 |
| CENTROID | 76 |
| modi 2 | 78-79 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001010...................000000000000000000000000000000000
........0000.0......000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v2"></a>
## 2. `IPA_R_P_a[URI]_R`

Syntax: `IPA.OFFSET R, P, a[UR+INT_IMM], R`  
Example: `@P0 IPA.PASS.OFFSET R0, P0, a[UR0+0x4], R0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-30 |
| operand 4 | 32-39 |
| operand 3 | 64-71 |
| modi 1 | 78-79 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001010...................0........000000000000000000000000
........000001......000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v3"></a>
## 3. `IPA_R_P_a[UR]`

Syntax: `IPA R, P, a[UR]`  
Example: `@P0 IPA.PASS R0, P0, a[UR0] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-30 |
| CENTROID | 76 |
| modi 2 | 78-79 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001010...................000000000000000000000000000000000
000000000000.0......000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v4"></a>
## 4. `IPA_R_P_a[UR]_R`

Syntax: `IPA.OFFSET R, P, a[UR], R`  
Example: `@P0 IPA.PASS.OFFSET R0, P0, a[UR0], R0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-30 |
| operand 3 | 32-39 |
| modi 1 | 78-79 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001010...................0........000000000000000000000000
00000000000001......000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v5"></a>
## 5. `IPA_R_a[URI]`

Syntax: `IPA R, a[UR+INT_IMM]`  
Example: `@P0 IPA.PASS R0, a[UR0+0x4] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 2 | 64-71 |
| CENTROID | 76 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001010...................000000000000000000000000000000000
........0000.0..0111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v6"></a>
## 6. `IPA_R_a[URI]_R`

Syntax: `IPA.OFFSET R, a[UR+INT_IMM], R`  
Example: `@P0 IPA.PASS.OFFSET R0, a[UR0+0x4], R0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 3 | 32-39 |
| operand 2 | 64-71 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001010...................0........000000000000000000000000
........000001..0111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v7"></a>
## 7. `IPA_R_a[UR]`

Syntax: `IPA R, a[UR]`  
Example: `@P0 IPA.PASS R0, a[UR0] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| CENTROID | 76 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001010...................000000000000000000000000000000000
000000000000.0..0111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v8"></a>
## 8. `IPA_R_a[UR]_R`

Syntax: `IPA.OFFSET R, a[UR], R`  
Example: `@P0 IPA.PASS.OFFSET R0, a[UR0], R0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 2 | 32-39 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001010...................0........000000000000000000000000
00000000000001..0111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v9"></a>
## 9. `IPA_R_P_a[I]_I`

Syntax: `IPA R, P, a[INT_IMM], INT_IMM`  
Example: `@P0 IPA.PASS.???0 R0, P0, a[0x0], 0x0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 32-63 |
| operand 2 | 64-71 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001001............00000000................................
........0000........000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `OFFSET.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v10"></a>
## 10. `IPA_R_P_a[URI]_I`

Syntax: `IPA R, P, a[UR+INT_IMM], INT_IMM`  
Example: `@P0 IPA.PASS.???0 R0, P0, a[UR0+0x4], 0x0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-30 |
| operand 4 | 32-63 |
| operand 3 | 64-71 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001001...................0................................
........0000........000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `OFFSET.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v11"></a>
## 11. `IPA_R_P_a[UR]_I`

Syntax: `IPA R, P, a[UR], INT_IMM`  
Example: `@P0 IPA.PASS.???0 R0, P0, a[UR0], 0x0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 24-30 |
| operand 3 | 32-63 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001001...................0................................
000000000000........000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `OFFSET.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v12"></a>
## 12. `IPA_R_a[I]_I`

Syntax: `IPA R, a[INT_IMM], INT_IMM`  
Example: `@P0 IPA.PASS.???0 R0, a[0x0], 0x0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-63 |
| operand 1 | 64-71 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001001............00000000................................
........0000....0111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `OFFSET.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v13"></a>
## 13. `IPA_R_a[URI]_I`

Syntax: `IPA R, a[UR+INT_IMM], INT_IMM`  
Example: `@P0 IPA.PASS.???0 R0, a[UR0+0x4], 0x0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 3 | 32-63 |
| operand 2 | 64-71 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001001...................0................................
........0000....0111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `OFFSET.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v14"></a>
## 14. `IPA_R_a[UR]_I`

Syntax: `IPA R, a[UR], INT_IMM`  
Example: `@P0 IPA.PASS.???0 R0, a[UR0], 0x0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 2 | 32-63 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001001...................0................................
000000000000....0111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `OFFSET.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v15"></a>
## 15. `IPA_R_P_a[I]_c[I][I]`

Syntax: `IPA R, P, a[INT_IMM], c[INT_IMM][INT_IMM]`  
Example: `@P0 IPA.PASS.???0 R0, P0, a[0x0], c[0x0][0x0] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 2 | 64-71 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001101............0000000000000000...................00000
........0000........000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `OFFSET.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v16"></a>
## 16. `IPA_R_a[I]_c[I][I]`

Syntax: `IPA R, a[INT_IMM], c[INT_IMM][INT_IMM]`  
Example: `@P0 IPA.PASS.???0 R0, a[0x0], c[0x0][0x0] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 1 | 64-71 |
| modi 1 | 76-77 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001101............0000000000000000...................00000
........0000....0111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `OFFSET.` |
| `11` | `???3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v17"></a>
## 17. `IPA_R_P_a[I]`

Syntax: `IPA R, P, a[INT_IMM]`  
Example: `@P0 IPA.PASS R0, P0, a[0x0] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 64-71 |
| CENTROID | 76 |
| modi 2 | 78-79 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001100............0000000000000000000000000000000000000000
........0000.0......000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v18"></a>
## 18. `IPA_R_P_a[I]_R`

Syntax: `IPA.OFFSET R, P, a[INT_IMM], R`  
Example: `@P0 IPA.PASS.OFFSET R0, P0, a[0x0], R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 32-39 |
| operand 2 | 64-71 |
| modi 1 | 78-79 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001100............00000000........000000000000000000000000
........000001......000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v19"></a>
## 19. `IPA_R_a[I]`

Syntax: `IPA R, a[INT_IMM]`  
Example: `@P0 IPA.PASS R0, a[0x0] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 64-71 |
| CENTROID | 76 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001100............0000000000000000000000000000000000000000
........0000.0..0111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

<a id="v20"></a>
## 20. `IPA_R_a[I]_R`

Syntax: `IPA.OFFSET R, a[INT_IMM], R`  
Example: `@P0 IPA.PASS.OFFSET R0, a[0x0], R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-39 |
| operand 1 | 64-71 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011001001100............00000000........000000000000000000000000
........000001..0111000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `PASS.` |
| `01` | `CONSTANT.` |
| `10` | `STATE.` |
| `11` | `INVALID3.` |

