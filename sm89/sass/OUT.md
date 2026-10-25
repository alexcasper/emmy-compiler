# OUT (SM89 SASS)

**NVIDIA:** not listed in the official Ampere/Ada opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)).

Notes: Geometry shader output (category: Graphics-only)

Typically emitted for: graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x124 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4421)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/OUT.html> (machine-derived by fuzzing the assembler; no semantics).

6 encoding variant(s):

- [OUT_R_R_I](#v1)
- [OUT_R_R_UR](#v2)
- [OUT_R_R_R](#v3)
- [OUT_R_R_SNOWFLAKE](#v4)
- [OUT_SNOWFLAKE_R](#v5)
- [OUT_SNOWFLAKE_R_SNOWFLAKE](#v6)

<a id="v1"></a>
## 1. `OUT_R_R_I`

Syntax: `OUT R, R, INT_IMM`  
Example: `@P0 OUT.???0 R0, R0, 0x0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001001001....................................................
00000000000000..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `EMIT.` |
| `10` | `???2.` |
| `11` | `EMIT_THEN_CUT.` |

<a id="v2"></a>
## 2. `OUT_R_R_UR`

Syntax: `OUT R, R, UR`  
Example: `@P0 OUT.???0 R0, R0, UR0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| modi 1 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001001011...........................0000000000000000000000000
00000000000000..0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `EMIT.` |
| `10` | `???2.` |
| `11` | `EMIT_THEN_CUT.` |

<a id="v3"></a>
## 3. `OUT_R_R_R`

Syntax: `OUT R, R, R`  
Example: `@P0 OUT.EMIT R0, R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi 1 | 79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001001100............................000000000000000000000000
000000000000001.0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `EMIT.` |
| `1` | `EMIT_THEN_CUT.` |

<a id="v4"></a>
## 4. `OUT_R_R_SNOWFLAKE`

Syntax: `OUT.CUT R, R, SNOWFLAKE`  
Example: `@P0 OUT.CUT R0, R0,     ???0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001001100............................000000000000000000000000
00000000000000010000000000000000000000000.....................00
```

<a id="v5"></a>
## 5. `OUT_SNOWFLAKE_R`

Syntax: `OUT.FINAL SNOWFLAKE, R`  
Example: `@P0 OUT.FINAL     ???0, R0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001001100....................11111111000000000000000000000000
00000000000000000000000000000000000000000.....111.............00
```

<a id="v6"></a>
## 6. `OUT_SNOWFLAKE_R_SNOWFLAKE`

Syntax: `OUT.FINAL SNOWFLAKE, R, SNOWFLAKE`  
Example: `@P0 OUT.FINAL     ???0, R0, ???0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001001001100............................000000000000000000000000
00000000000000000000000000000000000000000.....111.............00
```

