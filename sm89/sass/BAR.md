# BAR (SM89 SASS)

**NVIDIA:** Barrier Synchronization (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: CTA barrier (bar.sync / bar.arrive / bar.red) (category: Synchronization / barriers)

Typically emitted for: `bar.sync`/`barrier.sync` (`__syncthreads`), `bar.arrive`, `bar.red` (`__syncthreads_count/and/or`)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x31d, 0xb1d ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4245)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [bar](../verify/RESULTS.md#bar): `bar.sync 0`
- [bar_red](../verify/RESULTS.md#bar_red): `bar.red.popc.u32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/BAR.html> (machine-derived by fuzzing the assembler; no semantics).

8 encoding variant(s):

- [BAR_I_R](#v1)
- [BAR_I_R_P](#v2)
- [BAR_I](#v3)
- [BAR_I_I](#v4)
- [BAR_I_I_P](#v5)
- [BAR_I_P](#v6)
- [BAR_R_R](#v7)
- [BAR_R_R_P](#v8)

<a id="v1"></a>
## 1. `BAR_I_R`

Syntax: `BAR INT_IMM, R`  
Example: `@P0 BAR.SYNC 0x0, R0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| operand 0 | 53-57 |
| modi 1 | 77 |
| DEFER_BLOCKING | 80 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110001001....0000000000000000........0000000000000.....000000
0000000000000.00.000000000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `SYNC.` |
| `1` | `ARV.` |

<a id="v2"></a>
## 2. `BAR_I_R_P`

Syntax: `BAR.RED INT_IMM, R, P`  
Example: `@P0 BAR.RED.POPC 0x0, R0, P0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| operand 0 | 53-57 |
| modi 1 | 74-75 |
| modi 2 | 77 |
| DEFER_BLOCKING | 80 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110001001....0000000000000000........0000000000000.....000000
0000000000..0.10.00000.....00000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `POPC.` |
| `01` | `AND.` |
| `10` | `OR.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `RED.POPC.` |
| `1` | `SCAN.` |

<a id="v3"></a>
## 3. `BAR_I`

Syntax: `BAR.SYNC INT_IMM`  
Example: `@P0 BAR.SYNC 0x0 ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 54-57 |
| DEFER_BLOCKING | 80 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110001101....00000000000000000000000000000000000000....000000
0000000000000000.000000000000000000000000.....111.............00
```

<a id="v4"></a>
## 4. `BAR_I_I`

Syntax: `BAR.ARV INT_IMM, INT_IMM`  
Example: `@P0 BAR.ARV 0x0, 0x0 ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 41-52 |
| operand 0 | 53-57 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110001101....0000000000000000000000000.................000000
00000000000001000000000000000000000000000.....111.............00
```

<a id="v5"></a>
## 5. `BAR_I_I_P`

Syntax: `BAR.RED INT_IMM, INT_IMM, P`  
Example: `@P0 BAR.RED.POPC 0x0, 0x1, P0 ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 42-52 |
| operand 0 | 53-57 |
| modi 1 | 74-75 |
| modi 2 | 77 |
| DEFER_BLOCKING | 80 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110001101....00000000000000000000000000................000000
0000000000..0.10.00000.....00000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `POPC.` |
| `01` | `AND.` |
| `10` | `OR.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `RED.POPC.` |
| `1` | `SCAN.` |

<a id="v6"></a>
## 6. `BAR_I_P`

Syntax: `BAR.RED INT_IMM, P`  
Example: `@P0 BAR.RED.POPC 0x0, P0 ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 54-57 |
| modi 1 | 74-75 |
| DEFER_BLOCKING | 80 |
| operand 1 | 86-89 |
| cNOT (op 1) | 90 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110001101....00000000000000000000000000000000000000....000000
0000000000..0010.00000.....00000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `POPC.` |
| `01` | `AND.` |
| `10` | `OR.` |
| `11` | `INVALID3.` |

<a id="v7"></a>
## 7. `BAR_R_R`

Syntax: `BAR R, R`  
Example: `@P0 BAR.SYNC R0, R0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| modi 1 | 77 |
| DEFER_BLOCKING | 80 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110001100....0000000000000000........000000000000000000000000
0000000000000.00.000000000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `SYNC.` |
| `1` | `ARV.` |

<a id="v8"></a>
## 8. `BAR_R_R_P`

Syntax: `BAR.RED R, R, P`  
Example: `@P0 BAR.RED.POPC R0, R0, P0 ;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| modi 1 | 74-75 |
| modi 2 | 77 |
| DEFER_BLOCKING | 80 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110001100....0000000000000000........000000000000000000000000
0000000000..0.10.00000.....00000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `POPC.` |
| `01` | `AND.` |
| `10` | `OR.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `RED.POPC.` |
| `1` | `SCAN.` |

