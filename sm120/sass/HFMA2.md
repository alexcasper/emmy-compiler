# HFMA2 (SM120 SASS)

**NVIDIA:** FP16 Fused Mutiply Add (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: packed FP16x2/BF16x2 FMA; on sm_120 also absorbs add.f16x2/mul.f16x2 (no HADD2/HMUL2 seen) (category: FP16 (packed half2))

Observed on sm_120: 19 instruction(s) across 16 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `mufu_rcp`: `rcp.approx.f32`
- `hadd2`: `add.f16x2`
- `hfma2`: `fma.rn.f16x2`
- `hfma2_bf16`: `fma.rn.bf16x2`
- `hmul2`: `mul.f16x2`
- `vabsdiff`: `vabsdiff.u32.u32.u32 (observe)`
- `mapa`: `mapa.u64 (cluster address mapping, sm_90+)`
- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `diverge`: `data-dependent loop`
- `call`: `.func .noinline call`
- `brx`: `brx.idx (jump table)`
- `uniform_loop`: `loop with trip count from kernel param (uniform datapath)`
- `s2ur_loop`: `%ctaid.x as a loop bound (warp-uniform)`
- `txq`: `txq.width.b32`
- `suq`: `suq.width.b32`

12-bit opcode field (bits 0-11) values observed: `0x8c1`, `0x8c2`, `0x8c4`.

## Encoding observations

**Constant bits across all 19 observed instance(s): 81 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
100011000...1110....0000.............00000....000000000........0
..1......00000000000..0000000000000000000...0.11111100.000000000
```

8 normalized operand form(s) observed:

### `HFMA2 R, -R, R, IMM, IMM` - 10 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `HFMA2 R3, -RZ, RZ, 0, 0` | `00000000ff037431 000fc800000001ff` | fdiv_rn |
| `HFMA2 R4, -RZ, RZ, 15, 0` | `4b800000ff047431 000fe200000001ff` | mufu_rcp |
| `HFMA2 R5, -RZ, RZ, 0, 0` | `00000000ff057431 000fe200000001ff` | vabsdiff |
| `HFMA2 R5, -RZ, RZ, 0, 0` | `00000000ff057431 000fe200000001ff` | cp_async_bulk_tma |
| `HFMA2 R5, -RZ, RZ, 0, 0` | `00000000ff057431 000fe200000001ff` | diverge |
| `HFMA2 R5, -RZ, RZ, 0, 0` | `00000000ff057431 000fe400000001ff` | call |
| `HFMA2 R5, -RZ, RZ, 0, 0` | `00000000ff057431 000fc800000001ff` | uniform_loop |
| `HFMA2 R5, -RZ, RZ, 0, 0` | `00000000ff057431 000fc800000001ff` | s2ur_loop |
| `HFMA2 R5, -RZ, RZ, 0, 0` | `00000000ff057431 000fe200000001ff` | txq |
| `HFMA2 R5, -RZ, RZ, 0, 0` | `00000000ff057431 000fe200000001ff` | suq |

### `HFMA2 R, -R, R, IMM, IMM.9604644775390625e-IMM` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `HFMA2 R7, -RZ, RZ, 0, 5.9604644775390625e-08` | `00000001ff077431 000fca00000001ff` | mapa |
| `HFMA2 R5, -RZ, RZ, 0, 5.9604644775390625e-07` | `0000000aff057431 000fe200000001ff` | brx |

### `HFMA2 R, -R, R, IMM, IMM.5367431640625e-IMM` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `HFMA2 R8, -RZ, RZ, 0, 9.5367431640625e-07` | `00000010ff087431 000fe200000001ff` | cp_async_bulk_tma |
| `HFMA2 R0, -RZ, RZ, 0, 9.5367431640625e-07` | `00000010ff007431 000fc800000001ff` | cp_async_bulk_tma |

### `HFMA2 R, R, IMM, IMM, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `HFMA2 R5, R0, 1, 1, R5` | `3c003c0000057831 004fca0000000005` | hadd2 |

### `HFMA2 R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `HFMA2 R5, R0, R5, R4` | `0000000500057231 004fca0000000004` | hfma2 |

### `HFMA2.BF16_V2 R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `HFMA2.BF16_V2 R5, R0, R5, R4` | `0000000500057231 004fca0000200004` | hfma2_bf16 |

### `HFMA2 R, R, R, -R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `HFMA2 R5, R0, R5, -RZ` | `0000000500057231 004fca00001000ff` | hmul2 |

### `HFMA2 R, -R, R, IMM, IMM.78813934326171875e-IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `HFMA2 R5, -RZ, RZ, 0, 1.78813934326171875e-06` | `0000001eff057431 000fe200000001ff` | brx |

