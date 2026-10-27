# BSYNC (SM120 SASS)

**NVIDIA:** Synchronize Threads on a Convergence Barrier (Control Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: convergence-barrier sync (reconverge) (category: Control flow)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x941 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4179)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 7 instruction(s) across 4 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `diverge`: `data-dependent loop`
- `brx`: `brx.idx (jump table)`
- `bssy_bsync`: `divergent loop exit followed by a warp-synchronous op`

12-bit opcode field (bits 0-11) values observed: `0x829`.

## Encoding observations

**Constant bits across all 7 observed instance(s): 126 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1000001010011110..0000000000000000000000000000000000000000000000
0000000001000000000000011100000000000000010101111111000000000000
```

3 normalized operand form(s) observed:

### `BSYNC.RECONVERGENT B0` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `BSYNC.RECONVERGENT B0` | `0000000000007941 000fea0003800200` | fdiv_rn |
| `BSYNC.RECONVERGENT B0` | `0000000000007941 000fea0003800200` | diverge |
| `BSYNC.RECONVERGENT B0` | `0000000000007941 000fea0003800200` | brx |
| `BSYNC.RECONVERGENT B0` | `0000000000007941 000fea0003800200` | bssy_bsync |

### `BSYNC.RECONVERGENT B1` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `BSYNC.RECONVERGENT B1` | `0000000000017941 000fea0003800200` | fdiv_rn |
| `BSYNC.RECONVERGENT B1` | `0000000000017941 000fea0003800200` | diverge |

### `BSYNC.RECONVERGENT B2` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `BSYNC.RECONVERGENT B2` | `0000000000027941 000fea0003800200` | fdiv_rn |

