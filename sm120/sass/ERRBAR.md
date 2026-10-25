# ERRBAR (SM120 SASS)

**NVIDIA:** Error Barrier (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: error barrier (fence.sc.sys sequences) (category: Synchronization / barriers)

Observed on sm_120: 4 instruction(s) across 4 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cluster_barrier`: `barrier.cluster.arrive/wait.aligned`
- `fence_cluster`: `fence.acq_rel.cluster`
- `membar`: `membar.gl`
- `fence_sys`: `fence.sc.sys`

12-bit opcode field (bits 0-11) values observed: `0xd59`.

## Encoding observations

**Constant bits across all 4 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1101010110011110000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000111111000000000000
```

1 normalized operand form(s) observed:

### `ERRBAR` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ERRBAR` | `00000000000079ab 000fc00000000000` | cluster_barrier |
| `ERRBAR` | `00000000000079ab 000fc00000000000` | fence_cluster |
| `ERRBAR` | `00000000000079ab 000fc00000000000` | membar |
| `ERRBAR` | `00000000000079ab 000fc00000000000` | fence_sys |

