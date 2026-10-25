# BSSY (SM120 SASS)

**NVIDIA:** Barrier Set Convergence Synchronization Point (Control Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: convergence-barrier set (start of divergent region) (category: Control flow)

Observed on sm_120: 7 instruction(s) across 4 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `diverge`: `data-dependent loop`
- `brx`: `brx.idx (jump table)`
- `bssy_bsync`: `divergent loop exit followed by a warp-synchronous op`

12-bit opcode field (bits 0-11) values observed: `0xa29`.

## Encoding observations

**Constant bits across all 7 observed instance(s): 118 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1010001010011110..000000000000000000.......000000000000000000000
000000000100000000000001110000000000000001.001111111000000000000
```

3 normalized operand form(s) observed:

### `BSSY.RECONVERGENT B0, (L)` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `BSSY.RECONVERGENT B0, (.L_x_0)` | `000000b000007945 000fe20003800200` | fdiv_rn |
| `BSSY.RECONVERGENT B0, (.L_x_0)` | `000001c000007945 000fe20003800200` | diverge |
| `BSSY.RECONVERGENT B0, (.L_x_0)` | `000000d000007945 000fe20003800200` | brx |
| `BSSY.RECONVERGENT B0, (.L_x_0)` | `0000009000007945 000fe60003800200` | bssy_bsync |

### `BSSY.RECONVERGENT B1, (L)` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `BSSY.RECONVERGENT B1, (.L_x_2)` | `0000064000017945 000fe20003800200` | fdiv_rn |
| `BSSY.RECONVERGENT B1, (.L_x_2)` | `000000e000017945 000fe20003800200` | diverge |

### `BSSY.RECONVERGENT B2, (L)` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `BSSY.RECONVERGENT B2, (.L_x_8)` | `0000036000027945 000fe20003800200` | fdiv_rn |

