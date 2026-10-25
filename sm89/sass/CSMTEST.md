# CSMTEST (SM89 SASS)

**NVIDIA:** not listed in the official Ampere/Ada opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)).

Notes: Unknown; not in NVIDIA's table (name suggests a CSM/state test) (category: Predicate / compare)

Typically emitted for: (unknown; not produced by normal compute code)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Not produced by any ptxas probe, so the "typically emitted for" line above is unverified.

Encodings: <https://kuterdinel.com/nv_isa_sm89/CSMTEST.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [CSMTEST_P_P_I_P](#v1)

<a id="v1"></a>
## 1. `CSMTEST_P_P_I_P`

Syntax: `CSMTEST P, P, INT_IMM, P`  
Example: `@P0 CSMTEST.INVALID0.F.AND P0, P0, 0x0, P0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 2 | 32-60 |
| modi 1 | 62-63 |
| modi 2 | 74-75 |
| modi 3 | 76-78 |
| operand 0 | 80-82 |
| operand 1 | 83-85 |
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
101100000001....0000000000000000.............................0..
0000000000.....0...........00000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `INVALID0.` |
| `01` | `R.` |
| `10` | `A.` |
| `11` | `RA.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `AND.` |
| `01` | `OR.` |
| `10` | `XOR.` |
| `11` | `INVALID3.` |

Modifier Group 3:

| value | modifier |
|---|---|
| `000` | `F.` |
| `001` | `CSM_TA.` |
| `010` | `CSM_TR.` |
| `011` | `CSM_MX.` |
| `100` | `T.` |
| `101` | `FCSM_TA.` |
| `110` | `FCSM_TR.` |
| `111` | `FCSM_MX.` |

