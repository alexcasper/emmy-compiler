# ULDC (SM89 SASS)

**NVIDIA:** Load from Constant Memory into a Uniform Register (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Load constant into uniform register (category: Uniform datapath)

Typically emitted for: `ld.param` / constant bank reads of kernel args into uniform regs

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [uniform_loop](../verify/RESULTS.md#uniform_loop): `loop with trip count from kernel param (uniform datapath)`
- [prologue](../verify/RESULTS.md#prologue): `empty kernel body: param pointer + %tid.x load/store`

Encodings: <https://kuterdinel.com/nv_isa_sm89/ULDC.html> (machine-derived by fuzzing the assembler; no semantics).

7 encoding variant(s):

- [ULDC_UR_I](#v1)
- [ULDC_UR_URI_UP](#v2)
- [ULDC_UR_UR_UP](#v3)
- [ULDC_UR_c[I][I]](#v4)
- [ULDC_UR_cx[UR][I]](#v5)
- [ULDC_UR_c[I][URI]](#v6)
- [ULDC_UR_c[I][UR]](#v7)

<a id="v1"></a>
## 1. `ULDC_UR_I`

Syntax: `ULDC UR, [INT_IMM]`  
Example: `@UP0 ULDC.U8 UR0, [0x0];`

Register access: WRITE UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 37-69 |
| modi 1 | 73-75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000111010001...........01111110000000...........................
......000...00000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v2"></a>
## 2. `ULDC_UR_URI_UP`

Syntax: `ULDC UR, [UR+INT_IMM], UP`  
Example: `@UP0 ULDC.U8 UR0, [UR0+0x1], UP0;`

Register access: WRITE UR (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 38-69 |
| modi 1 | 73-75 |
| operand 3 | 86-89 |
| cNOT (op 3) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000111010001...........0.......0000000..........................
......000...0000000000.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v3"></a>
## 3. `ULDC_UR_UR_UP`

Syntax: `ULDC UR, [UR], UP`  
Example: `@UP0 ULDC.U8 UR0, [UR0], UP0;`

Register access: WRITE UR (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| modi 1 | 73-75 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000111010001...........0.......000000000000000000000000000000000
000000000...0000000000.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v4"></a>
## 4. `ULDC_UR_c[I][I]`

Syntax: `ULDC UR, c[INT_IMM][INT_IMM]`  
Example: `@UP0 ULDC.U8 UR0, c[0x0][0x0];`

Register access: WRITE UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 37-52 |
| operand 1 | 53-58 |
| modi 1 | 73-75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100111010101...........00000000000000......................00000
000000000...00000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v5"></a>
## 5. `ULDC_UR_cx[UR][I]`

Syntax: `ULDC UR, cx[UR][INT_IMM]`  
Example: `@UP0 ULDC.U8 UR0, cx[UR0][0x0];`

Register access: WRITE UR (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 24-30 |
| operand 2 | 37-53 |
| modi 1 | 73-75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100111010101...........0.......000000.................0000000000
000000000...00000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v6"></a>
## 6. `ULDC_UR_c[I][URI]`

Syntax: `ULDC UR, c[INT_IMM][UR+INT_IMM]`  
Example: `@UP0 ULDC.U8 UR0, c[0x0][UR0+0x1];`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 3 | 38-52 |
| operand 1 | 53-58 |
| modi 1 | 73-75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110111010101...........0.......0000000.....................00000
000000000...00000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

<a id="v7"></a>
## 7. `ULDC_UR_c[I][UR]`

Syntax: `ULDC UR, c[INT_IMM][UR]`  
Example: `@UP0 ULDC.U8 UR0, c[0x0][UR0];`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 24-30 |
| operand 1 | 54-58 |
| modi 1 | 73-75 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110111010101...........0.......00000000000000000000000.....00000
000000000...00000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `(default)` |
| `101` | `64.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

