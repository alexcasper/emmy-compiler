# LDS (SM120 SASS)

**NVIDIA:** Load within Shared Memory Window (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: shared load (category: Load / store)

Observed on sm_120: 9 instruction(s) across 6 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `lds_sts`: `ld.shared / st.shared`
- `cp_async`: `cp.async.cg.shared.global + commit_group + wait_group`
- `stmatrix`: `stmatrix.sync.aligned.m8n8.x1.shared.b16 (sm_90+)`
- `stmatrix_x4`: `stmatrix.sync.aligned.m8n8.x4.shared.b16`
- `st_bulk`: `st.bulk (shared-memory init, sm_90+)`
- `st_async`: `st.async.shared::cta.mbarrier::complete_tx::bytes (sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0x219`.

## Encoding observations

**Constant bits across all 9 observed instance(s): 103 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
001000011001111.1...............0..0000000.000000000000000000000
000000000001000000000000000.0000000000000.0.01...111000000000000
```

3 normalized operand form(s) observed:

### `LDS R, [R]` - 6 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `@!PT LDS RZ, [RZ]` | `00000000fffff984 000fe20000000800` | cp_async |
| `@!PT LDS RZ, [RZ]` | `00000000fffff984 000fe20000000800` | cp_async |
| `@!PT LDS RZ, [RZ]` | `00000000fffff984 000fe20000000800` | cp_async |
| `LDS R7, [R5]` | `0000000005077984 000e280000000800` | stmatrix |
| `LDS R9, [R0]` | `0000000000097984 000e280000000800` | stmatrix_x4 |

### `LDS R, [UR]` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDS R5, [UR4]` | `00000004ff057984 000e620008000800` | st_bulk |
| `LDS R5, [UR6]` | `00000006ff057984 000e680008000800` | st_async |

### `LDS R, [R+IMM]` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDS R7, [R5+0x4]` | `0000040005077984 000e280000000800` | lds_sts |

