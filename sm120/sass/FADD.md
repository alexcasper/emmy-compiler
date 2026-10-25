# FADD (SM120 SASS)

**NVIDIA:** FP32 Add (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: FP32 add (also the tail of emulated fp ops) (category: FP32)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x21, 0x54 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L849)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 15 instruction(s) across 14 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fadd`: `add.f32`
- `fsetp_selp`: `setp.lt.f32 + selp.f32 (both arms computed)`
- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `mufu_lg2`: `lg2.approx.f32`
- `ldg_v2`: `ld.global.v2.f32`
- `ldg_nc`: `ld.global.nc.v4.f32`
- `stg_v4`: `st.global.v4.f32`
- `atom_v2_f32`: `atom.global.v2.add.f32 (vector atomic, sm_90+)`
- `hmma_f16`: `mma.sync.aligned.m16n8k16.row.col.f32.f16.f16.f32`
- `hmma_bf16`: `mma.sync.aligned.m16n8k16.row.col.f32.bf16.bf16.f32`
- `hmma_tf32`: `mma.sync.aligned.m16n8k8.row.col.f32.tf32.tf32.f32`
- `qmma_e4m3`: `mma.sync.aligned.m16n8k32.row.col.f32.e4m3.e4m3.f32 (FP8)`
- `qmma_e5m2`: `mma.sync.aligned.m16n8k32.row.col.f32.e5m2.e5m2.f32 (FP8)`
- `uniform_i2fp`: `cvt.rn.f32.s32 on a warp-uniform constant (uniform FP conversion, UI2F)`

12-bit opcode field (bits 0-11) values observed: `0x842`, `0x844`.

## Encoding observations

**Constant bits across all 15 observed instance(s): 92 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
100001000..0....1...0000.0..0000........00000000000000...0.000..
00000000.0000000.000000000000000000000000...0.111111.0..00.00000
```

6 normalized operand form(s) observed:

### `FADD R, R, R` - 10 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FADD R5, R0, R5` | `0000000500057221 004fca0000000000` | fadd |
| `FADD R5, R4, R5` | `0000000504057221 004fca0000000000` | ldg_v2 |
| `FADD R5, R0, R5` | `0000000500057221 004fca0000000000` | ldg_nc |
| `FADD R7, R4, R8` | `0000000804077221 008fca0000000000` | stg_v4 |
| ... 6 more instance(s) in results.json | | |

### `FADD R, R.reuse, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FADD R5, R0.reuse, R5` | `0000000500057221 044fe20000000000` | fsetp_selp |

### `FADD.FTZ R, -R, -R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FADD.FTZ R11, -R9, -RZ` | `800000ff090b7221 000fe40000010100` | fdiv_rn |

### `FADD.FTZ R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FADD.FTZ R3, R0, R3` | `0000000300037221 000fce0000010000` | fdiv_rn |

### `FADD R, R, -IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `@!P0 FADD R5, R5, -24` | `c1c0000005058421 001fca0000000000` | mufu_lg2 |

### `FADD R, R, IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FADD R5, R0, 1024` | `4480000000057421 004fca0000000000` | uniform_i2fp |

