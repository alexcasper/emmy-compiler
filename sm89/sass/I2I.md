# I2I (SM89 SASS)

**NVIDIA:** Integer To Integer Conversion (Conversion Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Integer to integer conversion (saturating narrow) (category: Conversion)

Typically emitted for: `cvt.sat.s8.s32` etc. (saturating narrow)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [i2i](../verify/RESULTS.md#i2i): `cvt.sat.s8.s32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/I2I.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [I2I_R_I](#v1)
- [I2I_R_c[I][I]](#v2)
- [I2I_R_cx[UR][I]](#v3)
- [I2I_R_UR](#v4)
- [I2I_R_R](#v5)

<a id="v1"></a>
## 1. `I2I_R_I`

Syntax: `I2I.SAT.S32 R, INT_IMM`  
Example: `@P0 I2I.U8.S32.SAT R0, 0x0;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| modi 1 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000111000001............00000000................................
000000000000..000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `U16.` |
| `11` | `S16.` |

<a id="v2"></a>
## 2. `I2I_R_c[I][I]`

Syntax: `I2I.SAT.S32 R, c[INT_IMM][INT_IMM]`  
Example: `@P0 I2I.U8.S32.SAT R0, c[0x0][0x0];`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| modi 1 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000111000101............0000000000000000...................00000
000000000000..000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `U16.` |
| `11` | `S16.` |

<a id="v3"></a>
## 3. `I2I_R_cx[UR][I]`

Syntax: `I2I.SAT.S32 R, cx[UR][INT_IMM]`  
Example: `@P0 I2I.U8.S32.SAT R0, cx[UR0][0x0];`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| modi 1 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000111000101............00000000.......0...............000000000
000000000000..000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `U16.` |
| `11` | `S16.` |

<a id="v4"></a>
## 4. `I2I_R_UR`

Syntax: `I2I.SAT.S32 R, UR`  
Example: `@P0 I2I.U8.S32.SAT R0, UR0;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| modi 1 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000111000011............00000000.......0000000000000000000000000
000000000000..000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `U16.` |
| `11` | `S16.` |

<a id="v5"></a>
## 5. `I2I_R_R`

Syntax: `I2I.SAT.S32 R, R`  
Example: `@P0 I2I.U8.S32.SAT R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| modi 1 | 76-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000111000100............00000000........000000000000000000000000
000000000000..000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `U8.` |
| `01` | `S8.` |
| `10` | `U16.` |
| `11` | `S16.` |

