# UMOV (SM120 SASS)

**NVIDIA:** Uniform Move (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: uniform move/immediate (category: Uniform datapath)

Observed on sm_120: 28 instruction(s) across 18 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `vabsdiff4`: `vabsdiff4.u32.u32.u32.add`
- `lds_sts`: `ld.shared / st.shared`
- `cp_async`: `cp.async.cg.shared.global + commit_group + wait_group`
- `ldsm`: `ldmatrix.sync.aligned.m8n8.x4.shared.b16`
- `ldsm_trans`: `ldmatrix.sync.aligned.m8n8.x1.trans.shared.b16`
- `atoms`: `atom.shared.add.u32`
- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `mbarrier_red`: `mbarrier.arrive.release.cluster.shared::cta.b64 (sm_90+)`
- `st_bulk`: `st.bulk (shared-memory init, sm_90+)`
- `cp_async_bulk_prefetch`: `cp.async.bulk.prefetch.L2.global (sm_90+)`
- `st_async`: `st.async.shared::cta.mbarrier::complete_tx::bytes (sm_90+)`
- `uniform_txq`: `txq.num_mipmap_levels (handle arithmetic on uniform datapath)`
- `tex`: `tex.2d.v4.f32.f32`
- `tld4`: `tld4.r.2d.v4.f32.f32`
- `txq`: `txq.width.b32`
- `tld`: `tex.1d.v4.s32.s32 (integer coords)`
- `txd`: `tex.grad.2d.v4.f32.f32`
- `suq`: `suq.width.b32`

12-bit opcode field (bits 0-11) values observed: `0x411`, `0x413`.

## Encoding observations

**Constant bits across all 28 observed instance(s): 106 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0100000100.11110..10000000000000.........0.00000.0000000.0000000
000000000000000000000000000.0000000000000.....1111110.0000000000
```

3 normalized operand form(s) observed:

### `UMOV UR, IMM` - 16 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UMOV UR6, 0x1010101` | `0101010100067882 000fe20000000000` | vabsdiff4 |
| `UMOV UR4, 0x400` | `0000040000047882 000fe40000000000` | lds_sts |
| `UMOV UR4, 0x400` | `0000040000047882 000fcc0000000000` | cp_async |
| `UMOV UR4, 0x400` | `0000040000047882 000fe40000000000` | ldsm |
| `UMOV UR4, 0x400` | `0000040000047882 000fe40000000000` | ldsm_trans |
| `UMOV UR4, 0x400` | `0000040000047882 000fc80000000000` | atoms |
| `UMOV UR6, 0x400` | `0000040000067882 000fe20000000000` | cp_async_bulk_tma |
| `UMOV UR4, 0x400` | `0000040000047882 000fe20000000000` | mbarrier_red |
| `UMOV UR4, 0x400` | `0000040000047882 000fe20000000000` | st_bulk |
| `UMOV UR4, 0x4` | `0000000400047882 000fe20000000000` | cp_async_bulk_prefetch |
| `UMOV UR6, 0x400` | `0000040000067882 000fe20000000000` | st_async |

### `UMOV UR, UR` - 11 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UMOV UR4, UR38` | `0000002600047c82 002fe20008000000` | cp_async_bulk_tma |
| `UMOV UR5, URZ` | `000000ff00057c82 000fe40008000000` | cp_async_bulk_tma |
| `UMOV UR5, URZ` | `000000ff00057c82 000fc80008000000` | st_bulk |
| `UMOV UR5, URZ` | `000000ff00057c82 000fc60008000000` | uniform_txq |
| `UMOV UR5, URZ` | `000000ff00057c82 000fe40008000000` | tex |
| `UMOV UR5, URZ` | `000000ff00057c82 000fe40008000000` | tld4 |
| `UMOV UR5, URZ` | `000000ff00057c82 000fca0008000000` | txq |
| `UMOV UR5, URZ` | `000000ff00057c82 000fe40008000000` | tld |
| `UMOV UR5, URZ` | `000000ff00057c82 000fe20008000000` | txd |
| `UMOV UR5, URZ` | `000000ff00057c82 000fca0008000000` | suq |

### `UMOV UR, (.nv.unified.texrefDescSize)` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UMOV UR4, (.nv.unified.texrefDescSize)` | `0000000000047882 000fe20000000000` | uniform_txq |

