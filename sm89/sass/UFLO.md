# UFLO (SM89 SASS)

**NVIDIA:** Uniform Find Leading One (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Uniform find leading one (category: Uniform datapath)

Typically emitted for: uniform `bfind`; leader election when ptxas warp-aggregates `red` to a uniform address

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [agg_red](../verify/RESULTS.md#agg_red): `red.global.add.u32 to a warp-uniform address (warp-aggregated)`

Encodings: <https://kuterdinel.com/nv_isa_sm89/UFLO.html> (machine-derived by fuzzing the assembler; no semantics).

4 encoding variant(s):

- [UFLO_UR_I](#v1)
- [UFLO_UR_UP_I](#v2)
- [UFLO_UR_UP_UR](#v3)
- [UFLO_UR_UR](#v4)

<a id="v1"></a>
## 1. `UFLO_UR_I`

Syntax: `UFLO UR, INT_IMM`  
Example: `@UP0 UFLO.U32 UR0, 0x0;`

Register access: WRITE UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 32-63 |
| modi 1 | 73 |
| SH | 74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101111010001...........000000000................................
000000000..000000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v2"></a>
## 2. `UFLO_UR_UP_I`

Syntax: `UFLO UR, UP, INT_IMM`  
Example: `@UP0 UFLO.U32 UR0, UP0, 0x0;`

Register access: WRITE UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 32-63 |
| modi 1 | 73 |
| SH | 74 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101111010001...........000000000................................
000000000..00000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v3"></a>
## 3. `UFLO_UR_UP_UR`

Syntax: `UFLO UR, UP, UR`  
Example: `@UP0 UFLO.U32 UR0, UP0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 2 | 32-38 |
| cINV (op 2) | 63 |
| modi 1 | 73 |
| SH | 74 |
| operand 1 | 80-83 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101111010100...........000000000.......000000000000000000000000.
000000000..00000....000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

<a id="v4"></a>
## 4. `UFLO_UR_UR`

Syntax: `UFLO UR, UR`  
Example: `@UP0 UFLO.U32 UR0, UR0;`

Register access: WRITE UR (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| operand 1 | 32-38 |
| cINV (op 1) | 63 |
| modi 1 | 73 |
| SH | 74 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
101111010100...........000000000.......000000000000000000000000.
000000000..000000111000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `0` | `U32.` |
| `1` | `(default)` |

