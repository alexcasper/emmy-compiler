# UIMAD (SM120 SASS)

**NVIDIA:** Uniform Integer Multiplication (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: uniform multiply-add (category: Uniform datapath)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `uniform_txq`: `txq.num_mipmap_levels (handle arithmetic on uniform datapath)`

12-bit opcode field (bits 0-11) values observed: `0x252`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0010010100101110001000000010000000110100000000000000000000000000
1010000001000000011100011111000000000000011000111111100000000000
```

1 normalized operand form(s) observed:

### `UIMAD UR, UR, UR, IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UIMAD UR4, UR4, UR5, 0x2c` | `0000002c040474a4 001fc6000f8e0205` | uniform_txq |

