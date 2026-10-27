# F2FP (SM120 SASS)

**NVIDIA:** not listed in NVIDIA's Blackwell/Rubin opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html)).

Notes: pack two FP32 into FP16x2/BF16x2/FP8 pairs (category: Conversion)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x3e, 0xba ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2237)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 5 instruction(s) across 4 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `f2fp_f16`: `cvt.rn.f16x2.f32`
- `f2fp_bf16`: `cvt.rn.bf16x2.f32`
- `f2fp_e4m3`: `cvt.rn.satfinite.e4m3x2.f32 (FP8)`
- `cvt_e4m3_to_f16x2`: `cvt.rn.f16x2.e4m3x2 (FP8 -> half2)`

12-bit opcode field (bits 0-11) values observed: `0x7c4`.

## Encoding observations

**Constant bits across all 5 observed instance(s): 106 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0111110001001110.0.00000.........0.00000000000000000000000000000
111111110..0...00000000.0..00000000000000.010011111100.000000000
```

4 normalized operand form(s) observed:

### `F2FP.SATFINITE.E4M3.F32.PACK_AB_MERGE_C R, R, R, R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `F2FP.SATFINITE.E4M3.F32.PACK_AB_MERGE_C R0, R0, R5, RZ` | `000000050000723e 004fc800048070ff` | f2fp_e4m3 |
| `F2FP.SATFINITE.E4M3.F32.PACK_AB_MERGE_C R0, R0, R5, RZ` | `000000050000723e 004fc800048070ff` | cvt_e4m3_to_f16x2 |

### `F2FP.F16.F32.PACK_AB R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `F2FP.F16.F32.PACK_AB R5, R0, R5` | `000000050005723e 004fca00000000ff` | f2fp_f16 |

### `F2FP.BF16.F32.PACK_AB R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `F2FP.BF16.F32.PACK_AB R5, R0, R5` | `000000050005723e 004fca00000010ff` | f2fp_bf16 |

### `F2FP.F16.E4M3.UNPACK_B R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `F2FP.F16.E4M3.UNPACK_B R5, R0` | `00000000ff05723e 000fca00020006ff` | cvt_e4m3_to_f16x2 |

