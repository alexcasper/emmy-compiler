# PMTRIG (SM89 SASS)

**NVIDIA:** Performance Monitor Trigger (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Performance monitor trigger (category: Miscellaneous)

Typically emitted for: `pmevent` (profiler trigger)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [pmtrig](../verify/RESULTS.md#pmtrig): `pmevent`

Encodings: <https://kuterdinel.com/nv_isa_sm89/PMTRIG.html> (machine-derived by fuzzing the assembler; no semantics).

2 encoding variant(s):

- [PMTRIG_I](#v1)
- [PMTRIG_P_I](#v2)

<a id="v1"></a>
## 1. `PMTRIG_I`

Syntax: `PMTRIG INT_IMM`  
Example: `@P0 PMTRIG 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 32-47 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000000001....0000000000000000................0000000000000000
00000000000000000000000111000000000000000.....................00
```

<a id="v2"></a>
## 2. `PMTRIG_P_I`

Syntax: `PMTRIG P, INT_IMM`  
Example: `@P0 PMTRIG P0, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 32-47 |
| operand 0 | 86-89 |
| cNOT (op 0) | 90 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
100000000001....0000000000000000................0000000000000000
0000000000000000000000.....00000000000000.....................00
```

