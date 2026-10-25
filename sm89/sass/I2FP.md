# I2FP (SM89 SASS)

**NVIDIA:** Integer to FP32 Convert and Pack (Conversion Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Integer to FP32 conversion on the FMA pipe (sm_86+ fast path) (category: Conversion)

Typically emitted for: `cvt.rn.f32.s32/u32` (fast 32-bit form)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [i2fp](../verify/RESULTS.md#i2fp): `cvt.rn.f32.s32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/I2FP.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [I2FP_R_I](#v1)
- [I2FP_R_c[I][I]](#v2)
- [I2FP_R_cx[UR][I]](#v3)
- [I2FP_R_UR](#v4)
- [I2FP_R_R](#v5)

<a id="v1"></a>
## 1. `I2FP_R_I`

Syntax: `I2FP R, INT_IMM`  
Example: `@P0 I2FP.???0.U32 R0, 0x0;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| modi 1 | 74 |
| modi 2 | 75-77 |
| modi 3 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000100001............00000000................................
0000000000......0000010000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `S32.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `000` | `???0.` |
| `001` | `???1.` |
| `010` | `F32.` |
| `011` | `???3.` |
| `100` | `???4.` |
| `101` | `???5.` |
| `110` | `???6.` |
| `111` | `???7.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `RZ.` |

<a id="v2"></a>
## 2. `I2FP_R_c[I][I]`

Syntax: `I2FP R, c[INT_IMM][INT_IMM]`  
Example: `@P0 I2FP.???0.???0 R0, c[0x0][0x0];`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| modi 1 | 74-75 |
| modi 2 | 76-77 |
| modi 3 | 78-79 |
| modi 4 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000100101............0000000000000000...................00000
0000000000......0000..0000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `???1.` |
| `11` | `???1.???1.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `F32.` |
| `10` | `???4.` |
| `11` | `???6.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `RZ.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???2.` |
| `10` | `U32.` |
| `11` | `???6.` |

<a id="v3"></a>
## 3. `I2FP_R_cx[UR][I]`

Syntax: `I2FP R, cx[UR][INT_IMM]`  
Example: `@P0 I2FP.???0.???0 R0, cx[UR0][0x0];`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| modi 1 | 74-75 |
| modi 2 | 76-77 |
| modi 3 | 78-79 |
| modi 4 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000100101............00000000.......0...............000000000
0000000000......0000..0000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `???1.` |
| `11` | `???1.???1.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `F32.` |
| `10` | `???4.` |
| `11` | `???6.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `RZ.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???2.` |
| `10` | `U32.` |
| `11` | `???6.` |

<a id="v4"></a>
## 4. `I2FP_R_UR`

Syntax: `I2FP R, UR`  
Example: `@P0 I2FP.???0.???0 R0, UR0;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| modi 1 | 74-75 |
| modi 2 | 76-77 |
| modi 3 | 78-79 |
| modi 4 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000100011............00000000.......0000000000000000000000000
0000000000......0000..0000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `???1.` |
| `11` | `???1.???1.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `F32.` |
| `10` | `???4.` |
| `11` | `???6.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `RZ.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???2.` |
| `10` | `U32.` |
| `11` | `???6.` |

<a id="v5"></a>
## 5. `I2FP_R_R`

Syntax: `I2FP R, R`  
Example: `@P0 I2FP.???0.???0 R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| modi 1 | 74-75 |
| modi 2 | 76-77 |
| modi 3 | 78-79 |
| modi 4 | 84-85 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101000100100............00000000........000000000000000000000000
0000000000......0000..0000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???1.` |
| `10` | `???1.` |
| `11` | `???1.???1.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `F32.` |
| `10` | `???4.` |
| `11` | `???6.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INVALID1.` |
| `10` | `INVALID2.` |
| `11` | `RZ.` |

Modifier Group 4:

| value | modifier |
|---|---|
| `00` | `???0.` |
| `01` | `???2.` |
| `10` | `U32.` |
| `11` | `???6.` |

