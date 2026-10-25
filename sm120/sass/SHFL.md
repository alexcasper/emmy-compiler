# SHFL (SM120 SASS)

**NVIDIA:** Warp Wide Register Shuffle (Movement Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: warp shuffle (category: Movement)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x389, 0x589, 0x989, 0xf89 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2558)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 10 instruction(s) across 4 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `shfl`: `shfl.sync.bfly.b32`
- `atoms`: `atom.shared.add.u32`
- `bssy_bsync`: `divergent loop exit followed by a warp-synchronous op`
- `agg_atomic`: `atom.global.add.u32 to a warp-uniform address (warp-aggregation)`

12-bit opcode field (bits 0-11) values observed: `0x919`, `0x91a`, `0x91f`.

## Encoding observations

**Constant bits across all 10 observed instance(s): 86 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
100100011...1110.0.00000....000000000000.....00000000.......0000
........000000000...000000000000000000000...01...111....00000000
```

4 normalized operand form(s) observed:

### `SHFL.UP P, R, R, IMM, R` - 6 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHFL.UP P0, R5, R0, 0x1, RZ` | `0420000000057989 004e2200000000ff` | atoms |
| `SHFL.UP P0, R5, R6, 0x2, RZ` | `0440000006057989 000e6400000000ff` | atoms |
| `SHFL.UP P0, R5, R7, 0x4, RZ` | `0480000007057989 000e2400000000ff` | atoms |
| `SHFL.UP P0, R5, R8, 0x8, RZ` | `0500000008057989 000e2400000000ff` | atoms |
| ... 2 more instance(s) in results.json | | |

### `SHFL.BFLY P, R, R, IMM, IMM` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHFL.BFLY PT, R5, R0, 0x1, 0x1f` | `0c201f0000057f89 004e2800000e0000` | shfl |
| `SHFL.BFLY PT, R5, R6, 0x1, 0x1f` | `0c201f0006057f89 002e2800000e0000` | bssy_bsync |

### `SHFL.IDX P, R, R, IMM, IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHFL.IDX PT, R5, R0, 0x1f, 0x1f` | `03e01f0000057f89 001e2400000e0000` | atoms |

### `SHFL.IDX P, R, R, R, IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHFL.IDX PT, R0, R5, R0, 0x1f` | `00001f0005007589 008e2400000e0000` | agg_atomic |

