# PRMT (SM120 SASS)

**NVIDIA:** Permute Register Pair (Movement Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: byte permute (category: Integer)

Observed on sm_120: 15 instruction(s) across 6 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `prmt`: `prmt.b32`
- `sgxt`: `bfe.s32 (signed field extract)`
- `vabsdiff`: `vabsdiff.u32.u32.u32 (observe)`
- `vabsdiff2`: `vabsdiff2.u32.u32.u32 (observe)`
- `i2i`: `cvt.sat.s8.s32`
- `mapa`: `mapa.u64 (cluster address mapping, sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0x681`.

## Encoding observations

**Constant bits across all 15 observed instance(s): 87 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0110100000011110....0000.........0.0.0..........0000000000000000
..1.....000000000000000000000000000000000...0.11111100...0.0.000
```

3 normalized operand form(s) observed:

### `PRMT R, R, IMM, R` - 13 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `PRMT R5, R0, 0x5140, R5` | `0000514000057816 004fca0000000005` | prmt |
| `PRMT R4, R5, 0x7604, R4` | `0000760405047816 004fc80000000004` | sgxt |
| `PRMT R4, RZ, 0x5, R4` | `00000005ff047816 000fe40000000004` | sgxt |
| `PRMT R4, R4, 0x3210, RZ` | `0000321004047816 004fe400000000ff` | vabsdiff |
| `PRMT R7, R0, 0x7710, RZ` | `0000771000077816 004fe400000000ff` | vabsdiff2 |
| `PRMT R5, R0, 0x8880, RZ` | `0000888000057816 000fca00000000ff` | i2i |
| `PRMT R4, R7, 0x654, R4` | `0000065407047816 004fe20000000004` | mapa |

### `PRMT R, R, IMM, R.reuse` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `PRMT R5, RZ, 0x4, R4.reuse` | `00000004ff057816 100fe40000000004` | sgxt |

### `PRMT R, R.reuse, IMM, R.reuse` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `PRMT R6, R0.reuse, 0x7654, R5.reuse` | `0000765400067816 140fe40000000005` | vabsdiff2 |

