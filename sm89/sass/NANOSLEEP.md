# NANOSLEEP (SM89 SASS)

**NVIDIA:** Suspend Execution (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Suspend thread for approx. duration (category: Control flow)

Typically emitted for: `nanosleep.u32`; `__nanosleep`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x15d ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4679)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [nanosleep](../verify/RESULTS.md#nanosleep): `nanosleep.u32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/NANOSLEEP.html> (machine-derived by fuzzing the assembler; no semantics).

10 encoding variant(s):

- [NANOSLEEP](#v1)
- [NANOSLEEP_I](#v2)
- [NANOSLEEP_P](#v3)
- [NANOSLEEP_P_I](#v4)
- [NANOSLEEP_P_c[I][I]](#v5)
- [NANOSLEEP_P_cx[UR][I]](#v6)
- [NANOSLEEP_c[I][I]](#v7)
- [NANOSLEEP_cx[UR][I]](#v8)
- [NANOSLEEP_P_R](#v9)
- [NANOSLEEP_R](#v10)

<a id="v1"></a>
## 1. `NANOSLEEP`

Syntax: `NANOSLEEP.CLEAR`  
Example: `@P0 NANOSLEEP.CLEAR;`

| field | bits |
|---|---|
| predicate | 12-15 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110101001....000000000000000000000000000000000000000000000000
00000000000000000001000111000000000000000.....111111..........00
```

<a id="v2"></a>
## 2. `NANOSLEEP_I`

Syntax: `NANOSLEEP INT_IMM`  
Example: `@P0 NANOSLEEP 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 32-63 |
| WARP | 85 |
| RAND | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110101001....0000000000000000................................
000000000000000000000..111000000000000000.....111111..........00
```

<a id="v3"></a>
## 3. `NANOSLEEP_P`

Syntax: `NANOSLEEP.CLEAR P`  
Example: `@P0 NANOSLEEP.CLEAR P0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 86-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110101001....000000000000000000000000000000000000000000000000
0000000000000000000100.....00000000000000.....111111..........00
```

<a id="v4"></a>
## 4. `NANOSLEEP_P_I`

Syntax: `NANOSLEEP P, INT_IMM`  
Example: `@P0 NANOSLEEP P0, 0x0;`

Register access: READ P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-63 |
| WARP | 85 |
| RAND | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110101001....0000000000000000................................
000000000000000000000......00000000000000.....111111..........00
```

<a id="v5"></a>
## 5. `NANOSLEEP_P_c[I][I]`

Syntax: `NANOSLEEP P, c[INT_IMM][INT_IMM]`  
Example: `@P0 NANOSLEEP P0, c[0x0][0x0];`

Register access: READ P (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| WARP | 85 |
| RAND | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110101101....000000000000000000000000...................00000
000000000000000000000......00000000000000.....111111..........00
```

<a id="v6"></a>
## 6. `NANOSLEEP_P_cx[UR][I]`

Syntax: `NANOSLEEP P, cx[UR][INT_IMM]`  
Example: `@P0 NANOSLEEP P0, cx[UR0][0x0];`

Register access: READ P (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| WARP | 85 |
| RAND | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110101101....0000000000000000.......0...............000000000
000000000000000000000......10000000000000.....111111..........00
```

<a id="v7"></a>
## 7. `NANOSLEEP_c[I][I]`

Syntax: `NANOSLEEP c[INT_IMM][INT_IMM]`  
Example: `@P0 NANOSLEEP c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 40-52, 54 |
| operand 0 | 53, 55-58 |
| WARP | 85 |
| RAND | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110101101....000000000000000000000000...................00000
000000000000000000000..111000000000000000.....111111..........00
```

<a id="v8"></a>
## 8. `NANOSLEEP_cx[UR][I]`

Syntax: `NANOSLEEP cx[UR][INT_IMM]`  
Example: `@P0 NANOSLEEP cx[UR0][0x0];`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 32-38 |
| operand 1 | 40-54 |
| WARP | 85 |
| RAND | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110101101....0000000000000000.......0...............000000000
000000000000000000000..111010000000000000.....111111..........00
```

<a id="v9"></a>
## 9. `NANOSLEEP_P_R`

Syntax: `NANOSLEEP P, R`  
Example: `@P0 NANOSLEEP P0, R0;`

Register access: READ P (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| WARP | 85 |
| RAND | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110101100....0000000000000000........000000000000000000000000
000000000000000000000......00000000000000.....111111..........00
```

<a id="v10"></a>
## 10. `NANOSLEEP_R`

Syntax: `NANOSLEEP R`  
Example: `@P0 NANOSLEEP R0;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 32-39 |
| WARP | 85 |
| RAND | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101110101100....0000000000000000........000000000000000000000000
000000000000000000000..111000000000000000.....111111..........00
```

