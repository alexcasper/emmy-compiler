# S2UR (SM120 SASS)

**NVIDIA:** Move Special Register to Uniform Register (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: special register to uniform register (warp-uniform values, e.g. SR_CgaCtaId) (category: Movement)

Observed on sm_120: 10 instruction(s) across 10 probe(s).

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
- `s2ur_loop`: `%ctaid.x as a loop bound (warp-uniform)`

12-bit opcode field (bits 0-11) values observed: `0xc39`.

## Encoding observations

**Constant bits across all 10 observed instance(s): 117 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1100001110011110....00000000000000000000000000000000000000000000
00000000.0..0.0.000000000000000000000000010001..0111000000000000
```

1 normalized operand form(s) observed:

### `S2UR UR, SR` - 10 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `S2UR UR5, SR_CgaCtaId` | `00000000000579c3 000e220000008800` | lds_sts |
| `S2UR UR5, SR_CgaCtaId` | `00000000000579c3 000ea20000008800` | cp_async |
| `S2UR UR5, SR_CgaCtaId` | `00000000000579c3 000e220000008800` | ldsm |
| `S2UR UR5, SR_CgaCtaId` | `00000000000579c3 000e220000008800` | ldsm_trans |
| ... 6 more instance(s) in results.json | | |

