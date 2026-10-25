# DEPBAR (SM89 SASS)

**NVIDIA:** Dependency Barrier (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Wait on dependency scoreboard count (cp.async.wait_group, etc.) (category: Synchronization / barriers)

Typically emitted for: `cp.async.wait_group N` / `wait_all` (DEPBAR.LE SB0, N)

## Evidence

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [cp_async](../verify/RESULTS.md#cp_async): `cp.async.cg.shared.global + commit_group + wait_group`

Encodings: <https://kuterdinel.com/nv_isa_sm89/DEPBAR.html> (machine-derived by fuzzing the assembler; no semantics).

3 encoding variant(s):

- [DEPBAR](#v1)
- [DEPBAR_SB_I](#v2)
- [DEPBAR_SNOWFLAKE_I](#v3)

<a id="v1"></a>
## 1. `DEPBAR`

Syntax: `DEPBAR`  
Example: `@P0 DEPBAR;`

| field | bits |
|---|---|
| predicate | 12-15 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010110001001....000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000.....111111..........00
```

<a id="v2"></a>
## 2. `DEPBAR_SB_I`

Syntax: `DEPBAR.LE SB, INT_IMM`  
Example: `@P0 DEPBAR.LE SB0, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 38-42 |
| operand 0 | 43-46 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010110001001....0000000000000000000000.........10000000000000000
00000000000000000000000000000000000000000.....111111..........00
```

<a id="v3"></a>
## 3. `DEPBAR_SNOWFLAKE_I`

Syntax: `DEPBAR.LE SNOWFLAKE, INT_IMM`  
Example: `@P0 DEPBAR.LE INVALID6, 0x0;`

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 1 | 38-42 |
| operand 0 | 43-44 |
| stall | 105-108 |
| y | 109 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010110001001....0000000000000000000000.......1110000000000000000
00000000000000000000000000000000000000000.....111111..........00
```

