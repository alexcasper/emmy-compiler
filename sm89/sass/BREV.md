# BREV (SM89 SASS)

**NVIDIA:** Bit Reverse (Integer Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Bit reverse (category: Integer)

Typically emitted for: `brev.b32` (`__brev`)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0xbe, 0x101 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1547)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [brev](../verify/RESULTS.md#brev): `brev.b32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/BREV.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [BREV_R_I](#v1)
- [BREV_R_c[I][I]](#v2)
- [BREV_R_cx[UR][I]](#v3)
- [BREV_R_UR](#v4)
- [BREV_R_R](#v5)

<a id="v1"></a>
## 1. `BREV_R_I`

Syntax: `BREV R, INT_IMM`  
Example: `@P0 BREV R0, 0x0 ;`

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
100000001001............00000000................................
00000000000000000000000000000000000000000.....................00
```

<a id="v2"></a>
## 2. `BREV_R_c[I][I]`

Syntax: `BREV R, c[INT_IMM][INT_IMM]`  
Example: `@P0 BREV R0, c[0x0][0x0] ;`

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
100000001101............0000000000000000...................00000
00000000000000000000000000000000000000000.....................00
```

<a id="v3"></a>
## 3. `BREV_R_cx[UR][I]`

Syntax: `BREV R, cx[UR][INT_IMM]`  
Example: `@P0 BREV R0, cx[UR0][0x0] ;`

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
100000001101............00000000.......0...............000000000
00000000000000000000000000010000000000000.....................00
```

<a id="v4"></a>
## 4. `BREV_R_UR`

Syntax: `BREV R, UR`  
Example: `@P0 BREV R0, UR0 ;`

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
100000001011............00000000.......0000000000000000000000000
00000000000000000000000000010000000000000.....................00
```

<a id="v5"></a>
## 5. `BREV_R_R`

Syntax: `BREV R, R`  
Example: `@P0 BREV R0, R0 ;`

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
100000001100............00000000........000000000000000000000000
00000000000000000000000000000000000000000.....................00
```

