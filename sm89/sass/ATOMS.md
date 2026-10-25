# ATOMS (SM89 SASS)

**NVIDIA:** Atomic Operation on Shared Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Shared-memory atomic (category: Atomics / reductions)

Typically emitted for: `atom.shared.*`

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [atoms](../verify/RESULTS.md#atoms): `atom.shared.add.u32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/ATOMS.html> (machine-derived by fuzzing the assembler; no semantics).

10 encoding variant(s):

- [ATOMS_R_RURI_R](#v1)
- [ATOMS_R_RUR_R](#v2)
- [ATOMS_R_URI_R](#v3)
- [ATOMS_R_UR_R](#v4)
- [ATOMS_R_I_R](#v5)
- [ATOMS_R_RI_R](#v6)
- [ATOMS_R_R_R](#v7)
- [ATOMS_R_I_R_R](#v8)
- [ATOMS_R_RI_R_R](#v9)
- [ATOMS_R_R_R_R](#v10)

<a id="v1"></a>
## 1. `ATOMS_R_RURI_R`

Syntax: `ATOMS R, [R+UR+INT_IMM], R`  
Example: `@P0 ATOMS.ADD R0, [R0+UR0+0x1], R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 4 | 32-39 |
| operand 3 | 40-63 |
| operand 2 | 64-70 |
| modi 1 | 73-74 |
| modi (op 1) | 78-79 |
| modi 2 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100011001....................................................
.......00..000..0000000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `S32.` |
| `10` | `64.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

<a id="v2"></a>
## 2. `ATOMS_R_RUR_R`

Syntax: `ATOMS R, [R+UR], R`  
Example: `@P0 ATOMS.ADD R0, [R0+UR0], R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-39 |
| operand 2 | 64-70 |
| modi 1 | 73-74 |
| modi (op 1) | 78-79 |
| modi 2 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100011001............................000000000000000000000000
.......00..000..0000000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `S32.` |
| `10` | `64.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

<a id="v3"></a>
## 3. `ATOMS_R_URI_R`

Syntax: `ATOMS R, [UR+INT_IMM], R`  
Example: `@P0 ATOMS.ADD R0, [UR0+0x2], R0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 3 | 32-39 |
| operand 2 | 40-63 |
| operand 1 | 64-70 |
| modi 1 | 73-74 |
| modi 2 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100011001............11111111................................
.......00..000000000000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `S32.` |
| `10` | `64.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v4"></a>
## 4. `ATOMS_R_UR_R`

Syntax: `ATOMS R, [UR], R`  
Example: `@P0 ATOMS.ADD R0, [UR0], R0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-39 |
| operand 1 | 64-70 |
| modi 1 | 73-74 |
| modi 2 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100011001............11111111........000000000000000000000000
.......00..000000000000....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `S32.` |
| `10` | `64.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v5"></a>
## 5. `ATOMS_R_I_R`

Syntax: `ATOMS R, [INT_IMM], R`  
Example: `@P0 ATOMS.ADD R0, [0x2], R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-39 |
| operand 1 | 40-63 |
| modi 1 | 73-74 |
| modi 2 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100011100............11111111................................
000000000..000000000000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `S32.` |
| `10` | `64.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v6"></a>
## 6. `ATOMS_R_RI_R`

Syntax: `ATOMS R, [R+INT_IMM], R`  
Example: `@P0 ATOMS.ADD R0, [R0+0x1], R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-39 |
| operand 2 | 40-63 |
| modi 1 | 73-74 |
| modi (op 1) | 78-79 |
| modi 2 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100011100....................................................
000000000..000..0000000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `S32.` |
| `10` | `64.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

<a id="v7"></a>
## 7. `ATOMS_R_R_R`

Syntax: `ATOMS R, [R], R`  
Example: `@P0 ATOMS.ADD R0, [R0], R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| modi 1 | 73-74 |
| modi (op 1) | 78-79 |
| modi 2 | 87-90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001100011100............................000000000000000000000000
000000000..000..0000000....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `S32.` |
| `10` | `64.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `ADD.` |
| `0001` | `MIN.` |
| `0010` | `MAX.` |
| `0011` | `INC.` |
| `0100` | `DEC.` |
| `0101` | `AND.` |
| `0110` | `OR.` |
| `0111` | `XOR.` |
| `1000` | `EXCH.` |
| `1001` | `INVALID9.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

<a id="v8"></a>
## 8. `ATOMS_R_I_R_R`

Syntax: `ATOMS R, [INT_IMM], R, R`  
Example: `@P0 ATOMS.CAS R0, [0x2], R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 32-39 |
| operand 1 | 40-63 |
| operand 3 | 64-71 |
| modi 1 | 73-74 |
| modi 2 | 87 |
| modi 3 | 88 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101100011100............11111111................................
........0..000000000000..0000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `S32.` |
| `10` | `64.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `CAS.` |
| `1` | `CAST.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0` | `(default)` |
| `1` | `(default)` |

<a id="v9"></a>
## 9. `ATOMS_R_RI_R_R`

Syntax: `ATOMS R, [R+INT_IMM], R, R`  
Example: `@P0 ATOMS.CAS R0, [R0+0x1], R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 32-39 |
| operand 2 | 40-63 |
| operand 4 | 64-71 |
| modi 1 | 73-74 |
| modi (op 1) | 78-79 |
| modi 2 | 87 |
| modi 3 | 88 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101100011100....................................................
........0..000..0000000..0000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `S32.` |
| `10` | `64.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `CAS.` |
| `1` | `CAST.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0` | `(default)` |
| `1` | `(default)` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

<a id="v10"></a>
## 10. `ATOMS_R_R_R_R`

Syntax: `ATOMS R, [R], R, R`  
Example: `@P0 ATOMS.CAS R0, [R0], R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| operand 3 | 64-71 |
| modi 1 | 73-74 |
| modi (op 1) | 78-79 |
| modi 2 | 87 |
| modi 3 | 88 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101100011100............................000000000000000000000000
........0..000..0000000..0000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `S32.` |
| `10` | `64.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0` | `CAS.` |
| `1` | `CAST.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `0` | `(default)` |
| `1` | `(default)` |

Operand 1 operand modifiers:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `X4.` |
| `10` | `X8.` |
| `11` | `X16.` |

