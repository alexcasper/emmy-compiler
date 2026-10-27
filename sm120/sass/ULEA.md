# ULEA (SM120 SASS)

**NVIDIA:** Uniform Load Effective Address (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: uniform effective address (category: Uniform datapath)

Observed on sm_120: 11 instruction(s) across 9 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `lds_sts`: `ld.shared / st.shared`
- `cp_async`: `cp.async.cg.shared.global + commit_group + wait_group`
- `ldsm`: `ldmatrix.sync.aligned.m8n8.x4.shared.b16`
- `ldsm_trans`: `ldmatrix.sync.aligned.m8n8.x1.trans.shared.b16`
- `atoms`: `atom.shared.add.u32`
- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `mbarrier_red`: `mbarrier.arrive.release.cluster.shared::cta.b64 (sm_90+)`
- `st_bulk`: `st.bulk (shared-memory init, sm_90+)`
- `st_async`: `st.async.shared::cta.mbarrier::complete_tx::bytes (sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0x894`.

## Encoding observations

**Constant bits across all 11 observed instance(s): 110 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1000100101001110..100.00....0000..100.00000000000000000000000000
11111111000000110111000111110000000000000.....111111...000000000
```

1 normalized operand form(s) observed:

### `ULEA UR, UR, UR, IMM` - 11 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ULEA UR4, UR5, UR4, 0x18` | `0000000405047291 001fcc000f8ec0ff` | lds_sts |
| `ULEA UR4, UR5, UR4, 0x18` | `0000000405047291 004fe2000f8ec0ff` | cp_async |
| `ULEA UR4, UR5, UR4, 0x18` | `0000000405047291 001fcc000f8ec0ff` | ldsm |
| `ULEA UR4, UR5, UR4, 0x18` | `0000000405047291 001fcc000f8ec0ff` | ldsm_trans |
| ... 7 more instance(s) in results.json | | |

