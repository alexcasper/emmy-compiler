# MUFU (SM89 SASS)

**NVIDIA:** FP32 Multi Function Operation (Floating Point Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Multi-function unit: RCP, RSQ, SQRT, LG2, EX2, SIN, COS, TANH, RCP64H, ... (category: FP32)

Typically emitted for: `rcp.approx`, `rsqrt.approx`, `sqrt.approx`, `lg2.approx`, `ex2.approx`, `sin/cos.approx`, `tanh.approx`; `__expf`, `__logf`, `__fdividef`; also inside full-precision div/sqrt sequences

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x108 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1168)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [fdiv_rn](../verify/RESULTS.md#fdiv_rn): `div.rn.f32 (IEEE division)`
- [mufu_rcp](../verify/RESULTS.md#mufu_rcp): `rcp.approx.f32`
- [mufu_rsqrt](../verify/RESULTS.md#mufu_rsqrt): `rsqrt.approx.f32`
- [mufu_sqrt](../verify/RESULTS.md#mufu_sqrt): `sqrt.approx.f32`
- [mufu_lg2](../verify/RESULTS.md#mufu_lg2): `lg2.approx.f32`
- [mufu_ex2](../verify/RESULTS.md#mufu_ex2): `ex2.approx.f32`
- [mufu_sin](../verify/RESULTS.md#mufu_sin): `sin.approx.f32`
- [mufu_cos](../verify/RESULTS.md#mufu_cos): `cos.approx.f32`
- [mufu_tanh](../verify/RESULTS.md#mufu_tanh): `tanh.approx.f32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/MUFU.html> (machine-derived by fuzzing the assembler; no semantics).

5 encoding variant(s):

- [MUFU_R_FI](#v1)
- [MUFU_R_c[I][I]](#v2)
- [MUFU_R_cx[UR][I]](#v3)
- [MUFU_R_UR](#v4)
- [MUFU_R_R](#v5)

<a id="v1"></a>
## 1. `MUFU_R_FI`

Syntax: `MUFU R, FIMM`  
Example: `@P0 MUFU.COS R0, 0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-63 |
| F16 | 73 |
| modi 1 | 74-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100001001............00000000................................
000000000.....000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `COS.` |
| `0001` | `SIN.` |
| `0010` | `EX2.` |
| `0011` | `LG2.` |
| `0100` | `RCP.` |
| `0101` | `RSQ.` |
| `0110` | `RCP64H.` |
| `0111` | `RSQ64H.` |
| `1000` | `SQRT.` |
| `1001` | `TANH.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v2"></a>
## 2. `MUFU_R_c[I][I]`

Syntax: `MUFU R, c[INT_IMM][INT_IMM]`  
Example: `@P0 MUFU.COS R0, c[0x0][0x0] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 2 | 40-52, 54 |
| operand 1 | 53, 55-58 |
| F16 | 73 |
| modi 1 | 74-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100001101............0000000000000000...................00000
000000000.....000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `COS.` |
| `0001` | `SIN.` |
| `0010` | `EX2.` |
| `0011` | `LG2.` |
| `0100` | `RCP.` |
| `0101` | `RSQ.` |
| `0110` | `RCP64H.` |
| `0111` | `RSQ64H.` |
| `1000` | `SQRT.` |
| `1001` | `TANH.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v3"></a>
## 3. `MUFU_R_cx[UR][I]`

Syntax: `MUFU R, cx[UR][INT_IMM]`  
Example: `@P0 MUFU.COS R0, cx[UR0][0x0] ;`

Register access: WRITE R (1 slots); READ UR (2 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-54 |
| F16 | 73 |
| modi 1 | 74-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100001101............00000000.......0...............000000000
000000000.....000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `COS.` |
| `0001` | `SIN.` |
| `0010` | `EX2.` |
| `0011` | `LG2.` |
| `0100` | `RCP.` |
| `0101` | `RSQ.` |
| `0110` | `RCP64H.` |
| `0111` | `RSQ64H.` |
| `1000` | `SQRT.` |
| `1001` | `TANH.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v4"></a>
## 4. `MUFU_R_UR`

Syntax: `MUFU R, UR`  
Example: `@P0 MUFU.COS R0, UR0 ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| cABS (op 1) | 62 |
| cNEG (op 1) | 63 |
| F16 | 73 |
| modi 1 | 74-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100001011............00000000.......00000000000000000000000..
000000000.....000000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `COS.` |
| `0001` | `SIN.` |
| `0010` | `EX2.` |
| `0011` | `LG2.` |
| `0100` | `RCP.` |
| `0101` | `RSQ.` |
| `0110` | `RCP64H.` |
| `0111` | `RSQ64H.` |
| `1000` | `SQRT.` |
| `1001` | `TANH.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

<a id="v5"></a>
## 5. `MUFU_R_R`

Syntax: `MUFU R, R`  
Example: `@P0 MUFU.COS R0, R0 ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-39 |
| cABS (op 1) | 62 |
| cNEG (op 1) | 63 |
| F16 | 73 |
| modi 1 | 74-77 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
000100001100............00000000........0000000000000000000000..
000000000.....000000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0000` | `COS.` |
| `0001` | `SIN.` |
| `0010` | `EX2.` |
| `0011` | `LG2.` |
| `0100` | `RCP.` |
| `0101` | `RSQ.` |
| `0110` | `RCP64H.` |
| `0111` | `RSQ64H.` |
| `1000` | `SQRT.` |
| `1001` | `TANH.` |
| `1010` | `INVALID10.` |
| `1011` | `INVALID11.` |
| `1100` | `INVALID12.` |
| `1101` | `INVALID13.` |
| `1110` | `INVALID14.` |
| `1111` | `INVALID15.` |

