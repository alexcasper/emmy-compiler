# FMNMX (SM120 SASS)

**NVIDIA:** FP32 Minimum/Maximum (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: FP32 min/max, incl. .NaN propagation forms (min.NaN/max.NaN) (category: FP32)

Observed on sm_120: 5 instruction(s) across 3 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fminmax`: `min.f32 / max.f32`
- `fminmax_nan`: `min.NaN.f32 / max.NaN.f32 (sm_80+ NaN propagation)`
- `fminmax_xorsign`: `min.xorsign.abs.f32 (sm_80+ modifier combo)`

12-bit opcode field (bits 0-11) values observed: `0x904`.

## Encoding observations

**Constant bits across all 5 observed instance(s): 120 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
10010000010011101010000000.00000101000000000000000000000000000.0
000000000.0000000..0000111.000000000000001010011111100..00000000
```

5 normalized operand form(s) observed:

### `FMNMX R, R, R, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FMNMX R5, R0, R5, PT` | `0000000500057209 004fca0003800000` | fminmax |

### `FMNMX R, R, R, !P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FMNMX R5, R4, R5, !PT` | `0000000504057209 008fca0007800000` | fminmax |

### `FMNMX.NAN R, R, R, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FMNMX.NAN R5, R0, R5, PT` | `0000000500057209 004fca0003820000` | fminmax_nan |

### `FMNMX.NAN R, R, R, !P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FMNMX.NAN R5, R4, R5, !PT` | `0000000504057209 008fca0007820000` | fminmax_nan |

### `FMNMX.XORSIGN R, |R|, |R|, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FMNMX.XORSIGN R5, |R0|, |R5|, PT` | `4000000500057209 004fca0003840200` | fminmax_xorsign |

