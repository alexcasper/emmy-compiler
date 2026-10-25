# ALD (SM89 SASS)

**NVIDIA:** not listed in the official Ampere/Ada opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)).

Notes: Attribute load (category: Graphics-only)

Typically emitted for: graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x321 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3932)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/ALD.html> (machine-derived by fuzzing the assembler; no semantics).

12 encoding variant(s):

- [ALD_R_a[URI]](#v1)
- [ALD_R_a[URI]_R](#v2)
- [ALD_R_a[URI]_SNOWFLAKE](#v3)
- [ALD_R_a[UR]](#v4)
- [ALD_R_a[UR]_R](#v5)
- [ALD_R_a[UR]_SNOWFLAKE](#v6)
- [ALD_R_a[I]_R](#v7)
- [ALD_R_a[I]_SNOWFLAKE](#v8)
- [ALD_R_a[RI]_SNOWFLAKE](#v9)
- [ALD_R_a[R]](#v10)
- [ALD_R_a[R]_R](#v11)
- [ALD_R_a[R]_SNOWFLAKE](#v12)

<a id="v1"></a>
## 1. `ALD_R_a[URI]`

Syntax: `ALD R, a[UR+INT_IMM]`  
Example: `@P0 ALD R0, a[UR0+0x1] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 2 | 40-50 |
| modi 1 | 74-75 |
| P | 76 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001010...................011111111...........0000000000000
0000000000...00.0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `64.` |
| `10` | `96.` |
| `11` | `128.` |

<a id="v2"></a>
## 2. `ALD_R_a[URI]_R`

Syntax: `ALD R, a[UR+INT_IMM], R`  
Example: `@P0 ALD R0, a[UR0+0x1], R0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 3 | 32-39 |
| operand 2 | 40-50 |
| modi 1 | 74-75 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001010...................0...................0000000000000
0000000000..000.0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `64.` |
| `10` | `96.` |
| `11` | `128.` |

<a id="v3"></a>
## 3. `ALD_R_a[URI]_SNOWFLAKE`

Syntax: `ALD.P R, a[UR+INT_IMM], SNOWFLAKE`  
Example: `@P0 ALD.P R0, a[UR0+0x1],     ???0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 3 | 32-39 |
| operand 2 | 40-50 |
| modi 1 | 74-75 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001010...................0...................0000000000000
0000000000..100.0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `64.` |
| `10` | `96.` |
| `11` | `128.` |

<a id="v4"></a>
## 4. `ALD_R_a[UR]`

Syntax: `ALD R, a[UR]`  
Example: `@P0 ALD R0, a[UR0] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| modi 1 | 74-75 |
| P | 76 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001010...................011111111000000000000000000000000
0000000000...00.0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `64.` |
| `10` | `96.` |
| `11` | `128.` |

<a id="v5"></a>
## 5. `ALD_R_a[UR]_R`

Syntax: `ALD R, a[UR], R`  
Example: `@P0 ALD R0, a[UR0], R0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 2 | 32-39 |
| modi 1 | 74-75 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001010...................0........000000000000000000000000
0000000000..000.0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `64.` |
| `10` | `96.` |
| `11` | `128.` |

<a id="v6"></a>
## 6. `ALD_R_a[UR]_SNOWFLAKE`

Syntax: `ALD.P R, a[UR], SNOWFLAKE`  
Example: `@P0 ALD.P R0, a[UR0],     ???0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-30 |
| operand 2 | 32-39 |
| modi 1 | 74-75 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001010...................0........000000000000000000000000
0000000000..100.0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `64.` |
| `10` | `96.` |
| `11` | `128.` |

<a id="v7"></a>
## 7. `ALD_R_a[I]_R`

Syntax: `ALD R, a[INT_IMM], R`  
Example: `@P0 ALD R0, a[0x0], R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-39 |
| operand 1 | 40-50 |
| modi 1 | 74-75 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001100............11111111...................0000000000000
0000000000..000.0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `64.` |
| `10` | `96.` |
| `11` | `128.` |

<a id="v8"></a>
## 8. `ALD_R_a[I]_SNOWFLAKE`

Syntax: `ALD.P R, a[INT_IMM], SNOWFLAKE`  
Example: `@P0 ALD.P R0, a[0x0],     ???0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-39 |
| operand 1 | 40-50 |
| modi 1 | 74-75 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001100............11111111...................0000000000000
0000000000..100.0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `64.` |
| `10` | `96.` |
| `11` | `128.` |

<a id="v9"></a>
## 9. `ALD_R_a[RI]_SNOWFLAKE`

Syntax: `ALD.P R, a[R+INT_IMM], SNOWFLAKE`  
Example: `@P0 ALD.P R0, a[R0+0x1],     ???0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-39 |
| operand 2 | 40-50 |
| modi 1 | 74-75 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001100.......................................0000000000000
0000000000..100.0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `64.` |
| `10` | `96.` |
| `11` | `128.` |

<a id="v10"></a>
## 10. `ALD_R_a[R]`

Syntax: `ALD.PHYS R, a[R]`  
Example: `@P0 ALD.PHYS R0, a[R0] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 74-75 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001100....................11111111000000000000000000000000
0000000000..010.0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `???1.` |
| `10` | `???2.` |
| `11` | `???3.` |

<a id="v11"></a>
## 11. `ALD_R_a[R]_R`

Syntax: `ALD.PHYS R, a[R], R`  
Example: `@P0 ALD.PHYS R0, a[R0], R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi 1 | 74-75 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001100............................000000000000000000000000
0000000000..010.0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `???1.` |
| `10` | `???2.` |
| `11` | `???3.` |

<a id="v12"></a>
## 12. `ALD_R_a[R]_SNOWFLAKE`

Syntax: `ALD.P R, a[R], SNOWFLAKE`  
Example: `@P0 ALD.P R0, a[R0],     ???0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi 1 | 74-75 |
| O | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100001001100............................000000000000000000000000
0000000000..100.0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `64.` |
| `10` | `96.` |
| `11` | `128.` |

