# UMEMSETS (SM120 SASS)

**NVIDIA:** Initialize Shared Memory (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: st.bulk shared-memory bulk init, run with uniform setup (S2UR/ULEA/UMOV) (category: Load / store)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `st_bulk`: `st.bulk (shared-memory init, sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0xd3c`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1101001111001110000000001010000011111111000000000000000000000000
0110000000000000000000000001000000000000010001111000000000000000
```

1 normalized operand form(s) observed:

### `UMEMSETS.IMM [UR], UR, UR` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UMEMSETS.64 [UR5], URZ, UR6` | `000000ff050073cb 0001e20008000006` | st_bulk |

