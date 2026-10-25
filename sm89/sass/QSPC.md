# QSPC (SM89 SASS)

**NVIDIA:** Query Space (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Query address space of generic pointer (isspacep) (category: Load / store)

Typically emitted for: `isspacep.global/shared/local`

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [qspc](../verify/RESULTS.md#qspc): `isspacep.shared`

Encodings: <https://kuterdinel.com/nv_isa_sm89/QSPC.html> (machine-derived by fuzzing the assembler; no semantics).

7 encoding variant(s):

- [QSPC_P_R_RUR](#v1)
- [QSPC_P_R_RURI](#v2)
- [QSPC_P_R_UR](#v3)
- [QSPC_P_R_URI](#v4)
- [QSPC_P_R_I](#v5)
- [QSPC_P_R_R](#v6)
- [QSPC_P_R_RI](#v7)

<a id="v1"></a>
## 1. `QSPC_P_R_RUR`

Syntax: `QSPC P, R, [R+UR]`  
Example: `@P0 QSPC.G P0, R0, [R0.U32+UR0] ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| E | 72 |
| modi 1 | 73-74 |
| operand 0 | 80-83 |
| modi (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101011001...........................0000000000000000000000000
00000000...00000....000000.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `G.` |
| `01` | `L.` |
| `10` | `S.` |
| `11` | `INVALID3.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v2"></a>
## 2. `QSPC_P_R_RURI`

Syntax: `QSPC P, R, [R+UR+INT_IMM]`  
Example: `@P0 QSPC.G P0, R0, [R0.U32+UR0+0x1] ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 32-38 |
| operand 4 | 40-63 |
| E | 72 |
| modi 1 | 73-74 |
| operand 0 | 80-83 |
| modi (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101011001...........................0........................
00000000...00000....000000.10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `G.` |
| `01` | `L.` |
| `10` | `S.` |
| `11` | `INVALID3.` |

Operand 2 operand modifiers:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `64.` |

<a id="v3"></a>
## 3. `QSPC_P_R_UR`

Syntax: `QSPC P, R, [UR]`  
Example: `@P0 QSPC.G P0, R0, [UR0] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 32-38 |
| E | 72 |
| modi 1 | 73-74 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101011001............11111111.......0000000000000000000000000
00000000...00000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `G.` |
| `01` | `L.` |
| `10` | `S.` |
| `11` | `INVALID3.` |

<a id="v4"></a>
## 4. `QSPC_P_R_URI`

Syntax: `QSPC P, R, [UR+INT_IMM]`  
Example: `@P0 QSPC.G P0, R0, [UR0+0x20] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 32-38 |
| operand 3 | 40-63 |
| E | 72 |
| modi 1 | 73-74 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101011001............11111111.......0........................
00000000...00000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `G.` |
| `01` | `L.` |
| `10` | `S.` |
| `11` | `INVALID3.` |

<a id="v5"></a>
## 5. `QSPC_P_R_I`

Syntax: `QSPC P, R, [INT_IMM]`  
Example: `@P0 QSPC.G P0, R0, [0x2] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 40-63 |
| E | 72 |
| modi 1 | 73-74 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101011100............1111111100000000........................
00000000...00000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `G.` |
| `01` | `L.` |
| `10` | `S.` |
| `11` | `INVALID3.` |

<a id="v6"></a>
## 6. `QSPC_P_R_R`

Syntax: `QSPC P, R, [R]`  
Example: `@P0 QSPC.G P0, R0, [R0] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| E | 72 |
| modi 1 | 73-74 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101011100....................00000000000000000000000000000000
00000000...00000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `G.` |
| `01` | `L.` |
| `10` | `S.` |
| `11` | `INVALID3.` |

<a id="v7"></a>
## 7. `QSPC_P_R_RI`

Syntax: `QSPC P, R, [R+INT_IMM]`  
Example: `@P0 QSPC.G P0, R0, [R0+0x1] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 16-23 |
| operand 2 | 24-31 |
| operand 3 | 40-63 |
| E | 72 |
| modi 1 | 73-74 |
| operand 0 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010101011100....................00000000........................
00000000...00000....000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `G.` |
| `01` | `L.` |
| `10` | `S.` |
| `11` | `INVALID3.` |

