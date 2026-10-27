# STSM (SM120 SASS)

**NVIDIA:** Store Matrix to Shared Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: stmatrix - store matrix fragments to shared (legal on sm_120; rejected on sm_89) (category: Load / store)

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `stmatrix`: `stmatrix.sync.aligned.m8n8.x1.shared.b16 (sm_90+)`
- `stmatrix_x4`: `stmatrix.sync.aligned.m8n8.x4.shared.b16`

12-bit opcode field (bits 0-11) values observed: `0x221`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 124 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
001000100001111000000000.0.0000000.00000000000000000000000000000
000000000.000000000000000000000000000000010001111111001000000000
```

2 normalized operand form(s) observed:

### `STSM.IMM.M88 [R], R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `STSM.16.M88 [R5], R0` | `0000000005007844 004fe20000000000` | stmatrix |

### `STSM.IMM.M88.IMM [R], R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `STSM.16.M88.4 [R0], R4` | `0000000400007844 004fe20000000200` | stmatrix_x4 |

