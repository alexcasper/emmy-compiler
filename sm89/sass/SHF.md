# SHF (SM89 SASS)

**NVIDIA:** Funnel Shift (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Funnel shift (64-bit shifts, rotates) (category: Integer)

Typically emitted for: `shl/shr` on 32/64-bit, `shf.l/r`; `__funnelshift_l/r`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x19, 0x99 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2141)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [shf](../verify/RESULTS.md#shf): `shf.l.wrap.b32`
- [shl64](../verify/RESULTS.md#shl64): `shl.b64 by register`

Encodings: <https://kuterdinel.com/nv_isa_sm89/SHF.html> (machine-derived by fuzzing the assembler; no semantics).

9 encoding variant(s):

- [SHF_R_R_R_I](#v1)
- [SHF_R_R_R_c[I][I]](#v2)
- [SHF_R_R_R_cx[UR][I]](#v3)
- [SHF_R_R_I_R](#v4)
- [SHF_R_R_c[I][I]_R](#v5)
- [SHF_R_R_cx[UR][I]_R](#v6)
- [SHF_R_R_UR_R](#v7)
- [SHF_R_R_R_UR](#v8)
- [SHF_R_R_R_R](#v9)

<a id="v1"></a>
## 1. `SHF_R_R_R_I`

Syntax: `SHF R, R, R, INT_IMM`  
Example: `@P0 SHF.L.S64 R0, R0, R0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-63 |
| operand 2 | 64-71 |
| modi 1 | 73-74, 76 |
| W | 75 |
| HI | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110000010....................................................
........0....000.000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `S64.` |
| `01` | `U64.` |
| `10` | `S32.` |
| `11` | `U32.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `L.` |
| `1` | `R.` |

<a id="v2"></a>
## 2. `SHF_R_R_R_c[I][I]`

Syntax: `SHF R, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 SHF.L.S64 R0, R0, R0, c[0x0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 2 | 64-71 |
| modi 1 | 73-74, 76 |
| W | 75 |
| HI | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110000110....................00000000...................00000
........0....000.000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `S64.` |
| `01` | `U64.` |
| `10` | `S32.` |
| `11` | `U32.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `L.` |
| `1` | `R.` |

<a id="v3"></a>
## 3. `SHF_R_R_R_cx[UR][I]`

Syntax: `SHF R, R, R, cx[UR][INT_IMM]`  
Example: `@P0 SHF.L.S64 R0, R0, R0, cx[UR0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 2 | 64-71 |
| modi 1 | 73-74, 76 |
| W | 75 |
| HI | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110000110...........................0...............000000000
........0....000.000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `S64.` |
| `01` | `U64.` |
| `10` | `S32.` |
| `11` | `U32.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `L.` |
| `1` | `R.` |

<a id="v4"></a>
## 4. `SHF_R_R_I_R`

Syntax: `SHF R, R, INT_IMM, R`  
Example: `@P0 SHF.L.S64 R0, R0, 0x0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
| modi 1 | 73-74, 76 |
| W | 75 |
| HI | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110000001....................................................
........0....000.000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `S64.` |
| `01` | `U64.` |
| `10` | `S32.` |
| `11` | `U32.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `L.` |
| `1` | `R.` |

<a id="v5"></a>
## 5. `SHF_R_R_c[I][I]_R`

Syntax: `SHF R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 SHF.L.S64 R0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| modi 1 | 73-74, 76 |
| W | 75 |
| HI | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110000101....................00000000...................00000
........0....000.000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `S64.` |
| `01` | `U64.` |
| `10` | `S32.` |
| `11` | `U32.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `L.` |
| `1` | `R.` |

<a id="v6"></a>
## 6. `SHF_R_R_cx[UR][I]_R`

Syntax: `SHF R, R, cx[UR][INT_IMM], R`  
Example: `@P0 SHF.L.S64 R0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| modi 1 | 73-74, 76 |
| W | 75 |
| HI | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110000101...........................0...............000000000
........0....000.000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `S64.` |
| `01` | `U64.` |
| `10` | `S32.` |
| `11` | `U32.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `L.` |
| `1` | `R.` |

<a id="v7"></a>
## 7. `SHF_R_R_UR_R`

Syntax: `SHF R, R, UR, R`  
Example: `@P0 SHF.L.S64 R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
| modi 1 | 73-74, 76 |
| W | 75 |
| HI | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110000011...........................0000000000000000000000000
........0....000.000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `S64.` |
| `01` | `U64.` |
| `10` | `S32.` |
| `11` | `U32.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `L.` |
| `1` | `R.` |

<a id="v8"></a>
## 8. `SHF_R_R_R_UR`

Syntax: `SHF R, R, R, UR`  
Example: `@P0 SHF.L.S64 R0, R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| operand 2 | 64-71 |
| modi 1 | 73-74, 76 |
| W | 75 |
| HI | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110000111...........................0000000000000000000000000
........0....000.000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `S64.` |
| `01` | `U64.` |
| `10` | `S32.` |
| `11` | `U32.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `L.` |
| `1` | `R.` |

<a id="v9"></a>
## 9. `SHF_R_R_R_R`

Syntax: `SHF R, R, R, R`  
Example: `@P0 SHF.L.S64 R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
| modi 1 | 73-74, 76 |
| W | 75 |
| HI | 80 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100110000100............................000000000000000000000000
........0....000.000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `S64.` |
| `01` | `U64.` |
| `10` | `S32.` |
| `11` | `U32.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `L.` |
| `1` | `R.` |

