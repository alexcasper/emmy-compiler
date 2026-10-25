# SEL (SM89 SASS)

**NVIDIA:** Select Source with Predicate (Movement Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Select by predicate (category: Movement)

Typically emitted for: `selp.b32`; integer ternary

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x7, 0x87 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2491)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [fset](../verify/RESULTS.md#fset): `set.lt.u32.f32 (lowered as FSETP + SEL)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/SEL.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [SEL_R_R_I_P](#v1)
- [SEL_R_R_c[I][I]_P](#v2)
- [SEL_R_R_cx[UR][I]_P](#v3)
- [SEL_R_R_UR_P](#v4)
- [SEL_R_R_R_P](#v5)

<a id="v1"></a>
## 1. `SEL_R_R_I_P`

Syntax: `SEL R, R, INT_IMM, P`  
Example: `@P0 SEL R0, R0, 0x0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
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
111000000001....................................................
0000000000000000000000.....00000000000000.....................00
```

<a id="v2"></a>
## 2. `SEL_R_R_c[I][I]_P`

Syntax: `SEL R, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 SEL R0, R0, c[0x0][0x0], P0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111000000101....................00000000...................00000
0000000000000000000000.....00000000000000.....................00
```

<a id="v3"></a>
## 3. `SEL_R_R_cx[UR][I]_P`

Syntax: `SEL R, R, cx[UR][INT_IMM], P`  
Example: `@P0 SEL R0, R0, cx[UR0][0x0], P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| operand 4 | 86-89 |
| cNOT (op 4) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111000000101...........................0...............000000000
0000000000000000000000.....10000000000000.....................00
```

<a id="v4"></a>
## 4. `SEL_R_R_UR_P`

Syntax: `SEL R, R, UR, P`  
Example: `@P0 SEL R0, R0, UR0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
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
111000000011...........................0000000000000000000000000
0000000000000000000000.....10000000000000.....................00
```

<a id="v5"></a>
## 5. `SEL_R_R_R_P`

Syntax: `SEL R, R, R, P`  
Example: `@P0 SEL R0, R0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
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
111000000100............................000000000000000000000000
0000000000000000000000.....00000000000000.....................00
```

