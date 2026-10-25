# CCTL (SM120 SASS)

**NVIDIA:** Cache Control (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: cache control / prefetch (category: Load / store)

Observed on sm_120: 5 instruction(s) across 5 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cctl`: `prefetch.global.L1`
- `cluster_barrier`: `barrier.cluster.arrive/wait.aligned`
- `fence_cluster`: `fence.acq_rel.cluster`
- `membar`: `membar.gl`
- `fence_sys`: `fence.sc.sys`

12-bit opcode field (bits 0-11) values observed: `0xf19`.

## Encoding observations

**Constant bits across all 5 observed instance(s): 111 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
111100011001111000000000.1......00000000000000000000000000000000
00000000.0000000000000000.000000000000000.0.01111111......000000
```

2 normalized operand form(s) observed:

### `CCTL.IVALL` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `CCTL.IVALL` | `00000000ff00798f 000fe20002000000` | cluster_barrier |
| `CCTL.IVALL` | `00000000ff00798f 03ffe80002000000` | fence_cluster |
| `CCTL.IVALL` | `00000000ff00798f 000fe80002000000` | membar |
| `CCTL.IVALL` | `00000000ff00798f 000fe80002000000` | fence_sys |

### `CCTL.E.PF1 [R]` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `CCTL.E.PF1 [R2]` | `000000000200798f 004fe20000000100` | cctl |

