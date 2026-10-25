# DEPBAR (SM120 SASS)

**NVIDIA:** Dependency Barrier (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: dependency-barrier wait (cp.async.wait_group) (category: Synchronization / barriers)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cp_async`: `cp.async.cg.shared.global + commit_group + wait_group`

12-bit opcode field (bits 0-11) values observed: `0x589`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0101100010011110000000000000000000000000000000010000000000000000
0000000000000000000000000000000000000000000100111111000000000000
```

1 normalized operand form(s) observed:

### `DEPBAR.LE SB0, IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `DEPBAR.LE SB0, 0x0` | `000080000000791a 000fc80000000000` | cp_async |

