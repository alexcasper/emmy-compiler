# B2R (SM89 SASS)

**NVIDIA:** Move Barrier To Register (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Barrier state to register (category: Movement)

Typically emitted for: barrier result read (e.g. `bar.red.popc` result)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [bar_red](../verify/RESULTS.md#bar_red): `bar.red.popc.u32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/B2R.html> (machine-derived by fuzzing the assembler; no semantics).

3 encoding variant(s):

- [B2R_R](#v1)
- [B2R_R_I](#v2)
- [B2R_R_P](#v3)

<a id="v1"></a>
## 1. `B2R_R`

Syntax: `B2R.WARP R`  
Example: `@P0 B2R.WARP R0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001110001100............0000000000000000000000000000000000000000
00000000000000010000000000000000000000000.....................00
```

<a id="v2"></a>
## 2. `B2R_R_I`

Syntax: `B2R R, INT_IMM`  
Example: `@P0 B2R R0, 0x0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 53-57 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001110001100............00000000000000000000000000000.....000000
00000000000000000000000000000000000000000.....................00
```

<a id="v3"></a>
## 3. `B2R_R_P`

Syntax: `B2R.RESULT R, P`  
Example: `@P0 B2R.RESULT R0, P0 ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
001110001100............0000000000000000000000000000000000000000
0000000000000010....000000000000000000000.....................00
```

