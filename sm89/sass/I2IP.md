# I2IP (SM89 SASS)

**NVIDIA:** Integer To Integer Conversion and Packing (Conversion Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Pack integers to narrower integers (category: Conversion)

Typically emitted for: `cvt.pack.sat.s8.s32.b32`

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [i2ip](../verify/RESULTS.md#i2ip): `cvt.pack.sat.s8.s32.b32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/I2IP.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [I2IP_R_R_I_R](#v1)
- [I2IP_R_R_c[I][I]_R](#v2)
- [I2IP_R_R_cx[UR][I]_R](#v3)
- [I2IP_R_R_UR_R](#v4)
- [I2IP_R_R_R_R](#v5)

<a id="v1"></a>
## 1. `I2IP_R_R_I_R`

Syntax: `I2IP.S32 R, R, INT_IMM, R`  
Example: `@P0 I2IP.U8.S32.SAT R0, R0, 0x0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| operand 3 | 64-71 |
| modi (op 3) | 72-73 |
| modi 1 | 74-75 |
| modi 2 | 76-78 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100111000001....................................................
...............00000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `SAT.` |
| `01` | `(default)` |
| `10` | `SATRELU.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `U2.` |
| `101` | `S2.` |
| `110` | `U4.` |
| `111` | `S4.` |

Operand 3 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `H1.` |
| `10` | `???2.` |
| `11` | `???3.` |

<a id="v2"></a>
## 2. `I2IP_R_R_c[I][I]_R`

Syntax: `I2IP.S32 R, R, c[INT_IMM][INT_IMM], R`  
Example: `@P0 I2IP.U8.S32.SAT R0, R0, c[0x0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 64-71 |
| modi (op 4) | 72-73 |
| modi 1 | 74-75 |
| modi 2 | 76-78 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100111000101....................00000000...................00000
...............00000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `SAT.` |
| `01` | `(default)` |
| `10` | `SATRELU.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `U2.` |
| `101` | `S2.` |
| `110` | `U4.` |
| `111` | `S4.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `H1.` |
| `10` | `???2.` |
| `11` | `???3.` |

<a id="v3"></a>
## 3. `I2IP_R_R_cx[UR][I]_R`

Syntax: `I2IP.S32 R, R, cx[UR][INT_IMM], R`  
Example: `@P0 I2IP.U8.S32.SAT R0, R0, cx[UR0][0x0], R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 64-71 |
| modi (op 4) | 72-73 |
| modi 1 | 74-75 |
| modi 2 | 76-78 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100111000101...........................0...............000000000
...............00000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `SAT.` |
| `01` | `(default)` |
| `10` | `SATRELU.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `U2.` |
| `101` | `S2.` |
| `110` | `U4.` |
| `111` | `S4.` |

Operand 4 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `H1.` |
| `10` | `???2.` |
| `11` | `???3.` |

<a id="v4"></a>
## 4. `I2IP_R_R_UR_R`

Syntax: `I2IP.S32 R, R, UR, R`  
Example: `@P0 I2IP.U8.S32.SAT R0, R0, UR0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 64-71 |
| modi (op 3) | 72-73 |
| modi 1 | 74-75 |
| modi 2 | 76-78 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100111000011...........................0000000000000000000000000
...............00000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `SAT.` |
| `01` | `(default)` |
| `10` | `SATRELU.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `U2.` |
| `101` | `S2.` |
| `110` | `U4.` |
| `111` | `S4.` |

Operand 3 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `H1.` |
| `10` | `???2.` |
| `11` | `???3.` |

<a id="v5"></a>
## 5. `I2IP_R_R_R_R`

Syntax: `I2IP.S32 R, R, R, R`  
Example: `@P0 I2IP.U8.S32.SAT R0, R0, R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
| modi (op 3) | 72-73 |
| modi 1 | 74-75 |
| modi 2 | 76-78 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100111000100............................000000000000000000000000
...............00000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `SAT.` |
| `01` | `(default)` |
| `10` | `SATRELU.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `U8.` |
| `001` | `S8.` |
| `010` | `U16.` |
| `011` | `S16.` |
| `100` | `U2.` |
| `101` | `S2.` |
| `110` | `U4.` |
| `111` | `S4.` |

Operand 3 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `H1.` |
| `10` | `???2.` |
| `11` | `???3.` |

