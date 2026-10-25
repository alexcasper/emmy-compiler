# MOV (SM120 SASS)

**NVIDIA:** Move (Movement Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: move register/immediate (category: Movement)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x2, 0xc82 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2417)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 106 instruction(s) across 25 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `vabsdiff`: `vabsdiff.u32.u32.u32 (observe)`
- `vabsdiff2`: `vabsdiff2.u32.u32.u32 (observe)`
- `redux`: `redux.sync.add.u32`
- `stg_v4`: `st.global.v4.f32`
- `atoms`: `atom.shared.add.u32`
- `elect_sync`: `elect.sync (sm_90+)`
- `stmatrix`: `stmatrix.sync.aligned.m8n8.x1.shared.b16 (sm_90+)`
- `stmatrix_x4`: `stmatrix.sync.aligned.m8n8.x4.shared.b16`
- `mapa`: `mapa.u64 (cluster address mapping, sm_90+)`
- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `st_async`: `st.async.shared::cta.mbarrier::complete_tx::bytes (sm_90+)`
- `hmma_f16`: `mma.sync.aligned.m16n8k16.row.col.f32.f16.f16.f32`
- `hmma_bf16`: `mma.sync.aligned.m16n8k16.row.col.f32.bf16.bf16.f32`
- `hmma_tf32`: `mma.sync.aligned.m16n8k8.row.col.f32.tf32.tf32.f32`
- `imma`: `mma.sync.aligned.m16n8k32.row.col.s32.s8.s8.s32`
- `bmma`: `mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc`
- `qmma_e4m3`: `mma.sync.aligned.m16n8k32.row.col.f32.e4m3.e4m3.f32 (FP8)`
- `qmma_e5m2`: `mma.sync.aligned.m16n8k32.row.col.f32.e5m2.e5m2.f32 (FP8)`
- `diverge`: `data-dependent loop`
- `call`: `.func .noinline call`
- `brx`: `brx.idx (jump table)`
- `uniform_loop`: `loop with trip count from kernel param (uniform datapath)`
- `s2ur_loop`: `%ctaid.x as a loop bound (warp-uniform)`
- `txd`: `tex.grad.2d.v4.f32.f32`

12-bit opcode field (bits 0-11) values observed: `0x401`, `0x403`, `0x404`.

## Encoding observations

**Constant bits across all 106 observed instance(s): 72 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
010000000...........000000000000................................
000000001111000000000000000.0000000000000.....111111......0.0000
```

4 normalized operand form(s) observed:

### `MOV R, R` - 85 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MOV R8, R0` | `0000000000087202 000fe20000000f00` | fdiv_rn |
| `MOV R7, RZ` | `000000ff00077202 000fe20000000f00` | vabsdiff |
| `MOV R0, R7` | `0000000700007202 000fca0000000f00` | vabsdiff2 |
| `MOV R6, R9` | `0000000900067202 004fe20000000f00` | stg_v4 |
| ... 81 more instance(s) in results.json | | |

### `MOV R, IMM` - 11 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MOV R2, 0x120` | `0000012000027802 000fce0000000f00` | fdiv_rn |
| `MOV R4, 0x400` | `0000040000047802 000fe20000000f00` | stmatrix |
| `MOV R0, 0x400` | `0000040000007802 000fe20000000f00` | stmatrix_x4 |
| `MOV R2, 0x0` | `0000000000027802 000fe20000000f00` | cp_async_bulk_tma |
| ... 7 more instance(s) in results.json | | |

### `MOV R, UR` - 6 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MOV R5, UR6` | `0000000600057c02 001fca0008000f00` | redux |
| `MOV R5, UR6` | `0000000600057c02 000fca0008000f00` | elect_sync |
| `MOV R4, UR38` | `0000002600047c02 000fe20008000f00` | cp_async_bulk_tma |
| `MOV R7, UR7` | `0000000700077c02 000fe20008000f00` | st_async |
| ... 2 more instance(s) in results.json | | |

### `MOV R, R.reuse` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MOV R8, R5.reuse` | `0000000500087202 084fe20000000f00` | imma |
| `MOV R9, R6.reuse` | `0000000600097202 088fe20000000f00` | imma |
| `MOV R7, R4.reuse` | `0000000400077202 090fe20000000f00` | imma |
| `MOV R12, R4.reuse` | `00000004000c7202 080fe20000000f00` | imma |

