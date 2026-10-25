# FSET (SM89 SASS)

**NVIDIA:** FP32 Compare And Set (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: FP32 compare, write boolean/mask to register (category: FP32)

Typically emitted for: `set.<cmp>.f32` in principle, but on sm_89 ptxas lowers `set.lt.u32.f32` to FSETP + SEL (probe `fset`); FSET itself was not reproduced

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0xa, 0x52 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1052)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/FSET.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [FSET_R_R_FI_P](#v1)
- [FSET_R_R_c[I][I]_P](#v2)
- [FSET_R_R_cx[UR][I]_P](#v3)
- [FSET_R_R_UR_P](#v4)
- [FSET_R_R_R_P](#v5)

<a id="v1"></a>
## 1. `FSET_R_R_FI_P`

Syntax: `FSET.BF R, R, FIMM, P`  
Example: `@P0 FSET.BF.F.AND R0, R0, 0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi 1 | 74-75 |
| modi 2 | 76-79 |
| FTZ | 80 |
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
010100000001....................................................
00000000.........00000.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `AND.` |
| `01` | `OR.` |
| `10` | `XOR.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `F.` |
| `0001` | `LT.` |
| `0010` | `EQ.` |
| `0011` | `LE.` |
| `0100` | `GT.` |
| `0101` | `NE.` |
| `0110` | `GE.` |
| `0111` | `NUM.` |
| `1000` | `NAN.` |
| `1001` | `LTU.` |
| `1010` | `EQU.` |
| `1011` | `LEU.` |
| `1100` | `GTU.` |
| `1101` | `NEU.` |
| `1110` | `GEU.` |
| `1111` | `T.` |

<a id="v2"></a>
## 2. `FSET_R_R_c[I][I]_P`

Syntax: `FSET.BF R, R, c[INT_IMM][INT_IMM], P`  
Example: `@P0 FSET.BF.F.AND R0, R0, c[0x0][0x0], P0;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 3 | 40-52, 54 |
| operand 2 | 53, 55-58 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi 1 | 74-75 |
| modi 2 | 76-79 |
| FTZ | 80 |
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
010100000101....................00000000...................00000
00000000.........00000.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `AND.` |
| `01` | `OR.` |
| `10` | `XOR.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `F.` |
| `0001` | `LT.` |
| `0010` | `EQ.` |
| `0011` | `LE.` |
| `0100` | `GT.` |
| `0101` | `NE.` |
| `0110` | `GE.` |
| `0111` | `NUM.` |
| `1000` | `NAN.` |
| `1001` | `LTU.` |
| `1010` | `EQU.` |
| `1011` | `LEU.` |
| `1100` | `GTU.` |
| `1101` | `NEU.` |
| `1110` | `GEU.` |
| `1111` | `T.` |

<a id="v3"></a>
## 3. `FSET_R_R_cx[UR][I]_P`

Syntax: `FSET.BF R, R, cx[UR][INT_IMM], P`  
Example: `@P0 FSET.BF.F.AND R0, R0, cx[UR0][0x0], P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-54 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi 1 | 74-75 |
| modi 2 | 76-79 |
| FTZ | 80 |
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
010100000101...........................0...............000000000
00000000.........00000.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `AND.` |
| `01` | `OR.` |
| `10` | `XOR.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `F.` |
| `0001` | `LT.` |
| `0010` | `EQ.` |
| `0011` | `LE.` |
| `0100` | `GT.` |
| `0101` | `NE.` |
| `0110` | `GE.` |
| `0111` | `NUM.` |
| `1000` | `NAN.` |
| `1001` | `LTU.` |
| `1010` | `EQU.` |
| `1011` | `LEU.` |
| `1100` | `GTU.` |
| `1101` | `NEU.` |
| `1110` | `GEU.` |
| `1111` | `T.` |

<a id="v4"></a>
## 4. `FSET_R_R_UR_P`

Syntax: `FSET.BF R, R, UR, P`  
Example: `@P0 FSET.BF.F.AND R0, R0, UR0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi 1 | 74-75 |
| modi 2 | 76-79 |
| FTZ | 80 |
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
010100000011...........................00000000000000000000000..
00000000.........00000.....10000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `AND.` |
| `01` | `OR.` |
| `10` | `XOR.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `F.` |
| `0001` | `LT.` |
| `0010` | `EQ.` |
| `0011` | `LE.` |
| `0100` | `GT.` |
| `0101` | `NE.` |
| `0110` | `GE.` |
| `0111` | `NUM.` |
| `1000` | `NAN.` |
| `1001` | `LTU.` |
| `1010` | `EQU.` |
| `1011` | `LEU.` |
| `1100` | `GTU.` |
| `1101` | `NEU.` |
| `1110` | `GEU.` |
| `1111` | `T.` |

<a id="v5"></a>
## 5. `FSET_R_R_R_P`

Syntax: `FSET.BF R, R, R, P`  
Example: `@P0 FSET.BF.F.AND R0, R0, R0, P0;`

Register access: WRITE R (1 slots); READ R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-39 |
| cABS (op 2) | 62 |
| cNEG (op 2) | 63 |
| cNEG (op 1) | 72 |
| cABS (op 1) | 73 |
| modi 1 | 74-75 |
| modi 2 | 76-79 |
| FTZ | 80 |
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
010100000100............................0000000000000000000000..
00000000.........00000.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `AND.` |
| `01` | `OR.` |
| `10` | `XOR.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `0000` | `F.` |
| `0001` | `LT.` |
| `0010` | `EQ.` |
| `0011` | `LE.` |
| `0100` | `GT.` |
| `0101` | `NE.` |
| `0110` | `GE.` |
| `0111` | `NUM.` |
| `1000` | `NAN.` |
| `1001` | `LTU.` |
| `1010` | `EQU.` |
| `1011` | `LEU.` |
| `1100` | `GTU.` |
| `1101` | `NEU.` |
| `1110` | `GEU.` |
| `1111` | `T.` |

