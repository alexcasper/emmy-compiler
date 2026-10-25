# CCTLL (SM89 SASS)

**NVIDIA:** Cache Control (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Cache control on local memory (category: Load / store)

Typically emitted for: `prefetch.local`

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [cctll](../verify/RESULTS.md#cctll): `prefetch.local.L1`

Encodings: <https://kuterdinel.com/nv_isa_sm89/CCTLL.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [CCTLL](#v1)
- [CCTLL_I](#v2)
- [CCTLL_R](#v3)
- [CCTLL_RI](#v4)

<a id="v1"></a>
## 1. `CCTLL`

Syntax: `CCTLL.IVALL`  
Example: `@P0 CCTLL.IVALL;`

| field | bits |
|---|---|
| predicate | 12-15 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010011001....000000001111111100000000000000000000000000000000
00000000000000000000000001000000000000000.....111111..........00
```

<a id="v2"></a>
## 2. `CCTLL_I`

Syntax: `CCTLL [INT_IMM]`  
Example: `@P0 CCTLL.PF1 [0x20] ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 40-63 |
| modi 1 | 87-89 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010011001....000000001111111100000000........................
00000000000000000000000...000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `PF1.` |
| `001` | `PF2.` |
| `010` | `WB.` |
| `011` | `IV.` |
| `101` | `RS.` |

<a id="v3"></a>
## 3. `CCTLL_R`

Syntax: `CCTLL [R]`  
Example: `@P0 CCTLL.PF1 [R0] ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| modi 1 | 87-89 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010011001....00000000........00000000000000000000000000000000
00000000000000000000000...000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `PF1.` |
| `001` | `PF2.` |
| `010` | `WB.` |
| `011` | `IV.` |
| `101` | `RS.` |

<a id="v4"></a>
## 4. `CCTLL_RI`

Syntax: `CCTLL [R+INT_IMM]`  
Example: `@P0 CCTLL.PF1 [R0+0x1] ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 40-63 |
| modi 1 | 87-89 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010011001....00000000........00000000........................
00000000000000000000000...000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `PF1.` |
| `001` | `PF2.` |
| `010` | `WB.` |
| `011` | `IV.` |
| `101` | `RS.` |

