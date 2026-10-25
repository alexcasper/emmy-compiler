# LDGDEPBAR (SM89 SASS)

**NVIDIA:** Global Load Dependency Barrier (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Commit group of LDGSTS (cp.async.commit_group) (category: Load / store)

Typically emitted for: `cp.async.commit_group`

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [cp_async](../verify/RESULTS.md#cp_async): `cp.async.cg.shared.global + commit_group + wait_group`

Encodings: <https://kuterdinel.com/nv_isa_sm89/LDGDEPBAR.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [LDGDEPBAR](#v1)

<a id="v1"></a>
## 1. `LDGDEPBAR`

Syntax: `LDGDEPBAR`  
Example: `@P0 LDGDEPBAR ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
111101011001....000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000.....................00
```

