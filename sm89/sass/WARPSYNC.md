# WARPSYNC (SM89 SASS)

**NVIDIA:** Synchronize Threads in Warp (Control Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Synchronize threads in warp mask (__syncwarp) (category: Control flow)

Typically emitted for: `bar.warp.sync`; `__syncwarp`; implicit in `*.sync` ops with non-full masks

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x148 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4234)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [warpsync](../verify/RESULTS.md#warpsync): `bar.warp.sync with partial mask`

Encodings: <https://kuterdinel.com/nv_isa_sm89/WARPSYNC.html> (machine-derived by fuzzing the assembler; no semantics).

8 encoding variant(s):

- [WARPSYNC_I](#v1)
- [WARPSYNC_P_I](#v2)
- [WARPSYNC_P_c[I][I]](#v3)
- [WARPSYNC_P_cx[UR][I]](#v4)
- [WARPSYNC_c[I][I]](#v5)
- [WARPSYNC_cx[UR][I]](#v6)
- [WARPSYNC_P_R](#v7)
- [WARPSYNC_R](#v8)

<a id="v1"></a>
## 1. `WARPSYNC_I`

Syntax: `WARPSYNC INT_IMM`  
Example: `@P0 WARPSYNC 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 32-63 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100101001....0000000000000000................................
00000000000000000000000111000000000000000.....111111..........00
```

<a id="v2"></a>
## 2. `WARPSYNC_P_I`

Syntax: `WARPSYNC P, INT_IMM`  
Example: `@P0 WARPSYNC P0, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-63 |
| operand 0 | 86-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100101001....0000000000000000................................
0000000000000000000000.....00000000000000.....111111..........00
```

<a id="v3"></a>
## 3. `WARPSYNC_P_c[I][I]`

Syntax: `WARPSYNC P, c[INT_IMM][INT_IMM]`  
Example: `@P0 WARPSYNC P0, c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| operand 0 | 86-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100101101....000000000000000000000000...................00000
0000000000000000000000.....00000000000000.....111111..........00
```

<a id="v4"></a>
## 4. `WARPSYNC_P_cx[UR][I]`

Syntax: `WARPSYNC P, cx[UR][INT_IMM]`  
Example: `@P0 WARPSYNC P0, cx[UR0][0x0];`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| operand 0 | 86-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100101101....0000000000000000.......0...............000000000
0000000000000000000000.....10000000000000.....111111..........00
```

<a id="v5"></a>
## 5. `WARPSYNC_c[I][I]`

Syntax: `WARPSYNC c[INT_IMM][INT_IMM]`  
Example: `@P0 WARPSYNC c[0x0][0x0];`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 40-52, 54 |
| operand 0 | 53, 55-58 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100101101....000000000000000000000000...................00000
00000000000000000000000111000000000000000.....111111..........00
```

<a id="v6"></a>
## 6. `WARPSYNC_cx[UR][I]`

Syntax: `WARPSYNC cx[UR][INT_IMM]`  
Example: `@P0 WARPSYNC cx[UR0][0x0];`

Register access: READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 32-38 |
| operand 1 | 40-54 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100101101....0000000000000000.......0...............000000000
00000000000000000000000111010000000000000.....111111..........00
```

<a id="v7"></a>
## 7. `WARPSYNC_P_R`

Syntax: `WARPSYNC P, R`  
Example: `@P0 WARPSYNC P0, R0;`

Register access: READ P (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-39 |
| EXCLUSIVE | 86 |
| operand 0 | 87-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100101100....0000000000000000........000000000000000000000000
0000000000000000000000.....00000000000000.....111111..........00
```

<a id="v8"></a>
## 8. `WARPSYNC_R`

Syntax: `WARPSYNC R`  
Example: `@P0 WARPSYNC R0;`

Register access: READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 32-39 |
| EXCLUSIVE | 86 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100101100....0000000000000000........000000000000000000000000
0000000000000000000000.111000000000000000.....111111..........00
```

