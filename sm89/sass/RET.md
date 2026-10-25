# RET (SM89 SASS)

**NVIDIA:** Return From Subroutine (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Return from subroutine (category: Control flow)

Typically emitted for: `ret` from a device function

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [call](../verify/RESULTS.md#call): `.func .noinline call`

Encodings: <https://kuterdinel.com/nv_isa_sm89/RET.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [RET_P_R_I](#v1)
- [RET_P_UR_I](#v2)
- [RET_R_I](#v3)
- [RET_UR_I](#v4)

<a id="v1"></a>
## 1. `RET_P_R_I`

Syntax: `RET.REL P, R, INT_IMM`  
Example: `@P0 RET.REL P0, R0 0x10;`

Register access: READ P (1 slots); READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-31 |
| operand 2 | 33-81, 84-85 |
| NODEC | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010101001....00000000........0...............................
..................00.......00000000000000.....111111..........00
```

<a id="v2"></a>
## 2. `RET_P_UR_I`

Syntax: `RET.REL P, UR, INT_IMM`  
Example: `@P0 RET.REL P0, UR0 0x10;`

Register access: READ P (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 24-30 |
| operand 2 | 33-81, 84-85 |
| NODEC | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010101001....00000000.......00...............................
..................00.......10000000000000.....111111..........00
```

<a id="v3"></a>
## 3. `RET_R_I`

Syntax: `RET.REL R, INT_IMM`  
Example: `@P0 RET.REL R0 0x10;`

Register access: READ R (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-31 |
| operand 1 | 33-81, 84-85 |
| NODEC | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010101001....00000000........0...............................
..................00...111000000000000000.....111111..........00
```

<a id="v4"></a>
## 4. `RET_UR_I`

Syntax: `RET.REL UR, INT_IMM`  
Example: `@P0 RET.REL UR0 0x10;`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 24-30 |
| operand 1 | 33-81, 84-85 |
| NODEC | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000010101001....00000000.......00...............................
..................00...111010000000000000.....111111..........00
```

