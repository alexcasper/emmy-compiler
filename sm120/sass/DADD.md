# DADD (SM120 SASS)

**NVIDIA:** FP64 Add (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: FP64 add (category: FP64)

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `dadd`: `add.f64`
- `dmma`: `mma.sync.aligned.m8n8k4.row.col.f64.f64.f64.f64 (FP64 MMA)`

12-bit opcode field (bits 0-11) values observed: `0x944`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 126 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1001010001001110001000000010000000000000000000000000000000000000
0110000000000000000000000000000000000000001001000111.0.000000000
```

1 normalized operand form(s) observed:

### `DADD R, R, R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `DADD R4, R4, R6` | `0000000004047229 004e240000000006` | dadd |
| `DADD R4, R4, R6` | `0000000004047229 001e240000000006` | dmma |

