# MEMBAR (SM120 SASS)

**NVIDIA:** Memory Barrier (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: memory fence (membar/fence.sc/acq_rel) (category: Synchronization / barriers)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x992 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4063)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 4 instruction(s) across 4 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cluster_barrier`: `barrier.cluster.arrive/wait.aligned`
- `fence_cluster`: `fence.acq_rel.cluster`
- `membar`: `membar.gl`
- `fence_sys`: `fence.sc.sys`

12-bit opcode field (bits 0-11) values observed: `0x499`.

## Encoding observations

**Constant bits across all 4 observed instance(s): 126 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0100100110011110000000000000000000000000000000000000000000000000
000000000000.10.000000000000000000000000001101111111000000000000
```

3 normalized operand form(s) observed:

### `MEMBAR.ALL.GPU` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MEMBAR.ALL.GPU` | `0000000000007992 000fec000000a000` | cluster_barrier |
| `MEMBAR.ALL.GPU` | `0000000000007992 000fec000000a000` | fence_cluster |

### `MEMBAR.SC.GPU` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MEMBAR.SC.GPU` | `0000000000007992 000fec0000002000` | membar |

### `MEMBAR.SC.SYS` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MEMBAR.SC.SYS` | `0000000000007992 000fec0000003000` | fence_sys |

