# FSEL (SM120 SASS)

**NVIDIA:** Floating Point Select (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: FP32 select by predicate (category: FP32)

Observed on sm_120: 5 instruction(s) across 3 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fsetp_selp`: `setp.lt.f32 + selp.f32 (both arms computed)`
- `mufu_rcp`: `rcp.approx.f32`
- `dsetp`: `setp.lt.f64`

12-bit opcode field (bits 0-11) values observed: `0x101`, `0x104`.

## Encoding observations

**Constant bits across all 5 observed instance(s): 110 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
000100000.0.1110.0100000.0100000...00000000000000000000.......00
00000000000000000000000.0010000000000000010.0.111111.00000000000
```

3 normalized operand form(s) observed:

### `FSEL R, R, R, !P` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FSEL R5, R5, R0, !P0` | `0000000005057208 000fca0004000000` | fsetp_selp |
| `FSEL R4, R4, R6, !P0` | `0000000604047208 001fe20004000000` | dsetp |
| `FSEL R5, R5, R7, !P0` | `0000000705057208 000fca0004000000` | dsetp |

### `FSEL R, R, IMM, !P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FSEL R4, R4, 1, !P1` | `3f80000004047808 000fca0004800000` | mufu_rcp |

### `FSEL R, R, IMM.IMM, !P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FSEL R5, R4, 0.25, !P0` | `3e80000004057808 000fca0004000000` | mufu_rcp |

