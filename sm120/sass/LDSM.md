# LDSM (SM120 SASS)

**NVIDIA:** Load Matrix from Shared Memory with Element Size Expansion (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: ldmatrix shared-load of matrix fragments (category: Load / store)

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `ldsm`: `ldmatrix.sync.aligned.m8n8.x4.shared.b16`
- `ldsm_trans`: `ldmatrix.sync.aligned.m8n8.x1.trans.shared.b16`

12-bit opcode field (bits 0-11) values observed: `0xdc1`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 120 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1101110000011110....00001010000000000000000000000000000000000000
000000000.0000.000000000000000000000000000..01000111000000000000
```

2 normalized operand form(s) observed:

### `LDSM.IMM.M88.IMM R, [R]` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDSM.16.M88.4 R8, [R5]` | `000000000508783b 000e240000000200` | ldsm |

### `LDSM.IMM.MT88 R, [R]` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDSM.16.MT88 R7, [R5]` | `000000000507783b 000e280000004000` | ldsm_trans |

