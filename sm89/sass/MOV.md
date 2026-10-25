# MOV (SM89 SASS)

**NVIDIA:** Move (Movement Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Move register / immediate / constant (category: Movement)

Typically emitted for: `mov`; register copies, immediates, `ld.param` of kernel args in some cases

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x2, 0xc82 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2417)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [prologue](../verify/RESULTS.md#prologue): `empty kernel body: param pointer + %tid.x load/store`

Encodings: <https://kuterdinel.com/nv_isa_sm89/MOV.html> (machine-derived by fuzzing the assembler; no semantics).

10 encoding variant(s):

- [MOV_R_I](#v1)
- [MOV_R_I_I](#v2)
- [MOV_R_c[I][I]](#v3)
- [MOV_R_c[I][I]_I](#v4)
- [MOV_R_cx[UR][I]](#v5)
- [MOV_R_cx[UR][I]_I](#v6)
- [MOV_R_UR](#v7)
- [MOV_R_UR_I](#v8)
- [MOV_R_R](#v9)
- [MOV_R_R_I](#v10)

<a id="v1"></a>
## 1. `MOV_R_I`

Syntax: `MOV R, INT_IMM`  
Example: `@P0 MOV R0, 0x0;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000000001............00000000................................
00000000111100000000000000000000000000000.....................00
```

<a id="v2"></a>
## 2. `MOV_R_I_I`

Syntax: `MOV R, INT_IMM, INT_IMM`  
Example: `@P0 MOV R0, 0x0, 0x0;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| operand 2 | 72-76 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000000001............00000000................................
00000000.....0000000000000000000000000000.....................00
```

<a id="v3"></a>
## 3. `MOV_R_c[I][I]`

Syntax: `MOV R, c[INT_IMM][INT_IMM]`  
Example: `@P0 MOV R0, c[0x0][0x0];`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000000101............0000000000000000...................00000
00000000111100000000000000000000000000000.....................00
```

<a id="v4"></a>
## 4. `MOV_R_c[I][I]_I`

Syntax: `MOV R, c[INT_IMM][INT_IMM], INT_IMM`  
Example: `@P0 MOV R0, c[0x0][0x0], 0x0;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| operand 3 | 72-76 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000000101............0000000000000000...................00000
00000000.....0000000000000000000000000000.....................00
```

<a id="v5"></a>
## 5. `MOV_R_cx[UR][I]`

Syntax: `MOV R, cx[UR][INT_IMM]`  
Example: `@P0 MOV R0, cx[UR0][0x0];`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000000101............00000000.......0...............000000000
00000000111100000000000000010000000000000.....................00
```

<a id="v6"></a>
## 6. `MOV_R_cx[UR][I]_I`

Syntax: `MOV R, cx[UR][INT_IMM], INT_IMM`  
Example: `@P0 MOV R0, cx[UR0][0x0], 0x0;`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| operand 3 | 72-76 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000000101............00000000.......0...............000000000
00000000.....0000000000000010000000000000.....................00
```

<a id="v7"></a>
## 7. `MOV_R_UR`

Syntax: `MOV R, UR`  
Example: `@P0 MOV R0, UR0;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000000011............00000000.......0000000000000000000000000
00000000111100000000000000010000000000000.....................00
```

<a id="v8"></a>
## 8. `MOV_R_UR_I`

Syntax: `MOV R, UR, INT_IMM`  
Example: `@P0 MOV R0, UR0, 0x0;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 72-76 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000000011............00000000.......0000000000000000000000000
00000000.....0000000000000010000000000000.....................00
```

<a id="v9"></a>
## 9. `MOV_R_R`

Syntax: `MOV R, R`  
Example: `@P0 MOV R0, R0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000000100............00000000........000000000000000000000000
00000000111100000000000000000000000000000.....................00
```

<a id="v10"></a>
## 10. `MOV_R_R_I`

Syntax: `MOV R, R, INT_IMM`  
Example: `@P0 MOV R0, R0, 0x0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| operand 2 | 72-76 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010000000100............00000000........000000000000000000000000
00000000.....0000000000000000000000000000.....................00
```

