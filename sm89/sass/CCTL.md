# CCTL (SM89 SASS)

**NVIDIA:** Cache Control (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Cache control (prefetch/invalidate) (category: Load / store)

Typically emitted for: `prefetch.global.L1/L2`, `discard`, `applypriority`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x98f ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4033)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [cctl](../verify/RESULTS.md#cctl): `prefetch.global.L1`

Encodings: <https://kuterdinel.com/nv_isa_sm89/CCTL.html> (machine-derived by fuzzing the assembler; no semantics).

6 encoding variant(s):

- [CCTL](#v1)
- [CCTL_I](#v2)
- [CCTL_P_R](#v3)
- [CCTL_P_RI](#v4)
- [CCTL_R](#v5)
- [CCTL_RI](#v6)

<a id="v1"></a>
## 1. `CCTL`

Syntax: `CCTL`  
Example: `@P0 CCTL.IVALL;`

| field | bits |
|---|---|
| predicate | 12-15 |
| modi 1 | 78-79 |
| modi 2 | 87-89 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111100011001....000000001111111100000000000000000000000000000000
00000000000000..0000000...000000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `U.` |
| `10` | `C.` |
| `11` | `I.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `PF1.` |
| `001` | `PF2.` |
| `010` | `WB.` |
| `011` | `IV.` |
| `100` | `IVALL.` |
| `101` | `RS.` |
| `110` | `IVALLP.` |
| `111` | `WBALL.` |

<a id="v2"></a>
## 2. `CCTL_I`

Syntax: `CCTL [INT_IMM]`  
Example: `@P0 CCTL.PF1 [0x2000] ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 32-63 |
| E | 72 |
| modi 2 | 78-80 |
| modi 3 | 87-90 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111100011001....0000000011111111................................
00000000.00000...000000....00000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `U.` |
| `010` | `C.` |
| `011` | `I.` |
| `100` | `???4.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `PF1.` |
| `0001` | `PF2.` |
| `0010` | `WB.` |
| `0011` | `IV.` |
| `0101` | `RS.` |
| `1001` | `PML2.` |
| `1010` | `DML2.` |
| `1011` | `RML2.` |

<a id="v3"></a>
## 3. `CCTL_P_R`

Syntax: `CCTL.PF2.QFAULT P, [R]`  
Example: `@P0 CCTL.PF2.QFAULT P0, [R0] ;`

Register access: WRITE P (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| E | 72 |
| modi 2 | 78-80 |
| operand 0 | 81-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111100011001....00000000........00000000000000000000000000000000
00000000.00010......000100000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `U.` |
| `010` | `C.` |
| `011` | `I.` |
| `100` | `???4.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

<a id="v4"></a>
## 4. `CCTL_P_RI`

Syntax: `CCTL.PF2.QFAULT P, [R+INT_IMM]`  
Example: `@P0 CCTL.PF2.QFAULT P0, [R0+0x10] ;`

Register access: WRITE P (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| E | 72 |
| modi 2 | 78-80 |
| operand 0 | 81-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111100011001....00000000........................................
00000000.00010......000100000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `U.` |
| `010` | `C.` |
| `011` | `I.` |
| `100` | `???4.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

<a id="v5"></a>
## 5. `CCTL_R`

Syntax: `CCTL [R]`  
Example: `@P0 CCTL.PF1 [R0] ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| E | 72 |
| modi 2 | 78-80 |
| modi 3 | 87-90 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111100011001....00000000........00000000000000000000000000000000
00000000.00000...000000....00000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `U.` |
| `010` | `C.` |
| `011` | `I.` |
| `100` | `???4.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `PF1.` |
| `0001` | `PF2.` |
| `0010` | `WB.` |
| `0011` | `IV.` |
| `0101` | `RS.` |
| `1001` | `PML2.` |
| `1010` | `DML2.` |
| `1011` | `RML2.` |

<a id="v6"></a>
## 6. `CCTL_RI`

Syntax: `CCTL [R+INT_IMM]`  
Example: `@P0 CCTL.WB [R0+0x10] ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 32-63 |
| E | 72 |
| modi 2 | 78-80 |
| modi 3 | 87-88 |
| modi 4 | 90 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111100011001....00000000........................................
00000000.00000...000000..0.00000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `U.` |
| `010` | `C.` |
| `011` | `I.` |
| `100` | `???4.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `PF1.` |
| `01` | `PF2.` |
| `10` | `WB.` |
| `11` | `IV.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0` | `WB.` |
| `1` | `DML2.` |

