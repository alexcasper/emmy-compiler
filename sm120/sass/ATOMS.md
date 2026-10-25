# ATOMS (SM120 SASS)

**NVIDIA:** Atomic Operation on Shared Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: shared-memory atomic (category: Atomics / reductions)

Observed on sm_120: 2 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `atoms`: `atom.shared.add.u32`

12-bit opcode field (bits 0-11) values observed: `0x319`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 117 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
001100011001.00..0.000001111111100.00000000000000000000000000000
00100000000000000000000000010000000000000.0.010.01..00.000000000
```

1 normalized operand form(s) observed:

### `ATOMS.ADD R, [UR], R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `@!P0 ATOMS.ADD R5, [UR4], R0` | `00000000ff05898c 0042a20008000004` | atoms |
| `@P1 ATOMS.ADD R0, [UR4], R4` | `00000004ff00198c 000e280008000004` | atoms |

