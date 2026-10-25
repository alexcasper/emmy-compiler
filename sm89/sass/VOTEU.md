# VOTEU (SM89 SASS)

**NVIDIA:** Voting across SIMD Thread Group with Results in Uniform Destination (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Warp vote with uniform destination (category: Uniform datapath)

Typically emitted for: `activemask.b32`; ptxas-generated warp aggregation of atomics/reductions to a uniform address

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [agg_atomic](../verify/RESULTS.md#agg_atomic): `atom.global.add.u32 to a warp-uniform address (ptxas warp-aggregates it)`
- [agg_red](../verify/RESULTS.md#agg_red): `red.global.add.u32 to a warp-uniform address (warp-aggregated)`
- [activemask](../verify/RESULTS.md#activemask): `activemask.b32`

Encodings: <https://kuterdinel.com/nv_isa_sm89/VOTEU.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [VOTEU_UP_P](#v1)
- [VOTEU_UR_UP_P](#v2)

<a id="v1"></a>
## 1. `VOTEU_UP_P`

Syntax: `VOTEU UP, P`  
Example: `@P0 VOTEU.ALL UP0, P0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| modi 1 | 72-73 |
| operand 0 | 80-83 |
| operand 1 | 86-89 |
| cNOT (op 1) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000010001....111111000000000000000000000000000000000000000000
00000000..000000....00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `ALL.` |
| `01` | `ANY.` |
| `10` | `EQ.` |
| `11` | `INVALID3.` |

<a id="v2"></a>
## 2. `VOTEU_UR_UP_P`

Syntax: `VOTEU UR, UP, P`  
Example: `@P0 VOTEU.ALL UR0, UP0, P0;`

Register access: WRITE UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-22 |
| modi 1 | 72-73 |
| operand 1 | 80-83 |
| operand 2 | 86-89 |
| cNOT (op 2) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
011000010001...........00000000000000000000000000000000000000000
00000000..000000....00.....00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `ALL.` |
| `01` | `ANY.` |
| `10` | `EQ.` |
| `11` | `INVALID3.` |

