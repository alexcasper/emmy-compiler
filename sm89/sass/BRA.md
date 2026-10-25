# BRA (SM89 SASS)

**NVIDIA:** Relative Branch (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Relative branch (category: Control flow)

Typically emitted for: `bra`; loops, if/else

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x547, 0x947 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4191)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [diverge](../verify/RESULTS.md#diverge): `data-dependent loop`

Encodings: <https://kuterdinel.com/nv_isa_sm89/BRA.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [BRA_I](#v1)
- [BRA_P_I](#v2)
- [BRA_P_UR_I](#v3)
- [BRA_UR_I](#v4)

<a id="v1"></a>
## 1. `BRA_I`

Syntax: `BRA INT_IMM`  
Example: `@P0 BRA 0x10;`

| field | bits |
|---|---|
| predicate | 12-15 |
| modi 1 | 32-33 |
| operand 0 | 34-81 |
| modi 2 | 85-86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111000101001....0000000000000000................................
..................000..111000000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `U.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v2"></a>
## 2. `BRA_P_I`

Syntax: `BRA P, INT_IMM`  
Example: `@P0 BRA P0, 0x10;`

Register access: READ P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| modi 1 | 32-33 |
| operand 1 | 34-81 |
| modi 2 | 85-86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111000101001....0000000000000000................................
..................000......00000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `U.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v3"></a>
## 3. `BRA_P_UR_I`

Syntax: `BRA P, UR, INT_IMM`  
Example: `@P0 BRA.INVALID0 P0, UR0, 0x10;`

Register access: READ P (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
| modi 1 | 32-33 |
| operand 2 | 34-81 |
| modi 2 | 85-86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111000101001....00000000.......0................................
..................000......10000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `INVALID0.` |
| `01` | `INVALID1.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

<a id="v4"></a>
## 4. `BRA_UR_I`

Syntax: `BRA UR, INT_IMM`  
Example: `@P0 BRA.INVALID0 UR0, 0x10;`

Register access: READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-30 |
| modi 1 | 32-33 |
| operand 1 | 34-81 |
| modi 2 | 85-86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111000101001....00000000.......0................................
..................000..111010000000000000.....111111..........00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `INVALID0.` |
| `01` | `INVALID1.` |
| `10` | `DIV.` |
| `11` | `CONV.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `INC.` |
| `10` | `DEC.` |
| `11` | `INVALID3.` |

