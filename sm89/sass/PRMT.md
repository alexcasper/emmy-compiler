# PRMT (SM89 SASS)

**NVIDIA:** Permute Register Pair (Movement Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Byte permute (category: Integer)

Typically emitted for: `prmt.b32`; `__byte_perm`; byte extraction / packing (e.g. `cvt.u8`, `mov.b32 {a,b}`)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x16, 0x96 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2448)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [prmt](../verify/RESULTS.md#prmt): `prmt.b32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/PRMT.html> (machine-derived by fuzzing the assembler; no semantics).

9 encoding variant(s):

- [PRMT_R_R_R_I](#v1)
- [PRMT_R_R_R_c[I][I]](#v2)
- [PRMT_R_R_R_cx[UR][I]](#v3)
- [PRMT_R_R_I_R](#v4)
- [PRMT_R_R_c[I][I]_R](#v5)
- [PRMT_R_R_cx[UR][I]_R](#v6)
- [PRMT_R_R_UR_R](#v7)
- [PRMT_R_R_R_UR](#v8)
- [PRMT_R_R_R_R](#v9)

<a id="v1"></a>
## 1. `PRMT_R_R_R_I`

Syntax: `PRMT R, R, R, INT_IMM`  
Example: `@P0 PRMT R0, R0, R0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-63 |
| operand 2 | 64-71 |
| modi 1 | 72-74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010000010....................................................
...........000000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `F4E.` |
| `010` | `B4E.` |
| `011` | `RC8.` |
| `100` | `ECL.` |
| `101` | `ECR.` |
| `110` | `RC16.` |
| `111` | `INVALID7.` |

<a id="v2"></a>
## 2. `PRMT_R_R_R_c[I][I]`

Syntax: `PRMT R, R, R, c[INT_IMM][INT_IMM]`  
Example: `@P0 PRMT R0, R0, R0, c[0x0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 40-52, 54 |
| operand 3 | 53, 55-58 |
| operand 2 | 64-71 |
| modi 1 | 72-74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010000110....................00000000...................00000
...........000000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `F4E.` |
| `010` | `B4E.` |
| `011` | `RC8.` |
| `100` | `ECL.` |
| `101` | `ECR.` |
| `110` | `RC16.` |
| `111` | `INVALID7.` |

<a id="v3"></a>
## 3. `PRMT_R_R_R_cx[UR][I]`

Syntax: `PRMT R, R, R, cx[UR][INT_IMM]`  
Example: `@P0 PRMT R0, R0, R0, cx[UR0][0x0];`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-54 |
| operand 2 | 64-71 |
| modi 1 | 72-74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010000110...........................0...............000000000
...........000000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `F4E.` |
| `010` | `B4E.` |
| `011` | `RC8.` |
| `100` | `ECL.` |
| `101` | `ECR.` |
| `110` | `RC16.` |
| `111` | `INVALID7.` |

<a id="v4"></a>
## 4. `PRMT_R_R_I_R`

Syntax: `PRMT R, R, INT_IMM, R`  
Example: `@P0 PRMT R0, R0, 0x0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
| modi 1 | 72-74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010000001....................................................
...........000000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `F4E.` |
| `010` | `B4E.` |
| `011` | `RC8.` |
| `100` | `ECL.` |
| `101` | `ECR.` |
| `110` | `RC16.` |
| `111` | `INVALID7.` |

<a id="v5"></a>
## 5. `PRMT_R_R_c[I][I]_R`

Syntax: `PRMT R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 PRMT R0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| modi 1 | 72-74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010000101....................00000000...................00000
...........000000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `F4E.` |
| `010` | `B4E.` |
| `011` | `RC8.` |
| `100` | `ECL.` |
| `101` | `ECR.` |
| `110` | `RC16.` |
| `111` | `INVALID7.` |

<a id="v6"></a>
## 6. `PRMT_R_R_cx[UR][I]_R`

Syntax: `PRMT R, R, cx[UR][INT_IMM], R`  
Example: `@P0 PRMT R0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| modi 1 | 72-74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010000101...........................0...............000000000
...........000000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `F4E.` |
| `010` | `B4E.` |
| `011` | `RC8.` |
| `100` | `ECL.` |
| `101` | `ECR.` |
| `110` | `RC16.` |
| `111` | `INVALID7.` |

<a id="v7"></a>
## 7. `PRMT_R_R_UR_R`

Syntax: `PRMT R, R, UR, R`  
Example: `@P0 PRMT R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
| modi 1 | 72-74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010000011...........................0000000000000000000000000
...........000000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `F4E.` |
| `010` | `B4E.` |
| `011` | `RC8.` |
| `100` | `ECL.` |
| `101` | `ECR.` |
| `110` | `RC16.` |
| `111` | `INVALID7.` |

<a id="v8"></a>
## 8. `PRMT_R_R_R_UR`

Syntax: `PRMT R, R, R, UR`  
Example: `@P0 PRMT R0, R0, R0, UR0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-38 |
| operand 2 | 64-71 |
| modi 1 | 72-74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010000111...........................0000000000000000000000000
...........000000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `F4E.` |
| `010` | `B4E.` |
| `011` | `RC8.` |
| `100` | `ECL.` |
| `101` | `ECR.` |
| `110` | `RC16.` |
| `111` | `INVALID7.` |

<a id="v9"></a>
## 9. `PRMT_R_R_R_R`

Syntax: `PRMT R, R, R, R`  
Example: `@P0 PRMT R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
| modi 1 | 72-74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011010000100............................000000000000000000000000
...........000000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `(default)` |
| `001` | `F4E.` |
| `010` | `B4E.` |
| `011` | `RC8.` |
| `100` | `ECL.` |
| `101` | `ECR.` |
| `110` | `RC16.` |
| `111` | `INVALID7.` |

