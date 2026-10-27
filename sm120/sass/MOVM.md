# MOVM (SM120 SASS)

**NVIDIA:** Move Matrix with Transposition or Expansion (Movement Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: movmatrix transpose (also appears in b1-mma emulation) (category: Movement)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x23a ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4663)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 13 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `movm`: `movmatrix.sync.aligned.m8n8.trans.b16`
- `bmma`: `mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc`

12-bit opcode field (bits 0-11) values observed: `0x5c4`.

## Encoding observations

**Constant bits across all 13 observed instance(s): 108 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0101110001001110.....000.....00000000000000000000000000000000000
00000000000.00.00000000000000000000000000.......011100.000000000
```

2 normalized operand form(s) observed:

### `MOVM.U4TO8.M832 R, R` - 12 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MOVM.U4TO8.M832 R22, R2` | `000000000216723a 000e220000004800` | bmma |
| `MOVM.U4TO8.M832 R4, R3` | `000000000304723a 000e620000004800` | bmma |
| `MOVM.U4TO8.M832 R18, R6` | `000000000612723a 000ea80000004800` | bmma |
| `MOVM.U4TO8.M832 R2, R24` | `000000001802723a 000ee20000004800` | bmma |
| ... 8 more instance(s) in results.json | | |

### `MOVM.IMM.MT88 R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MOVM.16.MT88 R5, R0` | `000000000005723a 004e280000000000` | movm |

