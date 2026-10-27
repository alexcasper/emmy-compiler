# IADD (SM120 SASS)

**NVIDIA:** Integer Addition (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: 2-input 32-bit integer add - distinct opcode from IADD3 on sm_120; emitted for PTX add/sub.b32 in some patterns (category: Integer)

Observed on sm_120: 3 instruction(s) across 3 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `iadd64`: `add.s64`
- `vabsdiff`: `vabsdiff.u32.u32.u32 (observe)`
- `uniform_txq`: `txq.num_mipmap_levels (handle arithmetic on uniform datapath)`

12-bit opcode field (bits 0-11) values observed: `0xac3`, `0xac4`.

## Encoding observations

**Constant bits across all 3 observed instance(s): 119 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
101011000...111000100000001000000.10000000000000000000000000000.
000000000100000001110001111.0000000000000.11001111110..000000000
```

3 normalized operand form(s) observed:

### `IADD.IMM R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IADD.64 R4, R4, R4` | `0000000404047235 004fcc00078e0200` | iadd64 |

### `IADD.IMM R, R, -R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IADD.64 R4, R4, -R6` | `8000000604047235 000fcc00078e0200` | vabsdiff |

### `IADD.IMM R, R, UR` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IADD.64 R4, R4, UR4` | `0000000404047c35 002fce000f8e0200` | uniform_txq |

