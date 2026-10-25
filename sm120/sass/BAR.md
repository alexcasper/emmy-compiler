# BAR (SM120 SASS)

**NVIDIA:** Barrier Synchronization (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: CTA barrier (bar.sync/bar.red) (category: Synchronization / barriers)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x31d, 0xb1d ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4245)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 10 instruction(s) across 10 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `lds_sts`: `ld.shared / st.shared`
- `cp_async`: `cp.async.cg.shared.global + commit_group + wait_group`
- `ldsm`: `ldmatrix.sync.aligned.m8n8.x4.shared.b16`
- `ldsm_trans`: `ldmatrix.sync.aligned.m8n8.x1.trans.shared.b16`
- `stmatrix`: `stmatrix.sync.aligned.m8n8.x1.shared.b16 (sm_90+)`
- `stmatrix_x4`: `stmatrix.sync.aligned.m8n8.x4.shared.b16`
- `cluster_barrier`: `barrier.cluster.arrive/wait.aligned`
- `st_bulk`: `st.bulk (shared-memory init, sm_90+)`
- `bar`: `bar.sync 0`
- `bar_red`: `bar.red.popc.u32`

12-bit opcode field (bits 0-11) values observed: `0xb8d`.

## Encoding observations

**Constant bits across all 10 observed instance(s): 127 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1011100011011110000000000000000000000000000000000000000000000000
00000000000000.0100000000000000000000000001101111111000000000000
```

2 normalized operand form(s) observed:

### `BAR.SYNC.DEFER_BLOCKING IMM` - 9 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `BAR.SYNC.DEFER_BLOCKING 0x0` | `0000000000007b1d 000fec0000010000` | lds_sts |
| `BAR.SYNC.DEFER_BLOCKING 0x0` | `0000000000007b1d 000fec0000010000` | cp_async |
| `BAR.SYNC.DEFER_BLOCKING 0x0` | `0000000000007b1d 000fec0000010000` | ldsm |
| `BAR.SYNC.DEFER_BLOCKING 0x0` | `0000000000007b1d 000fec0000010000` | ldsm_trans |
| ... 5 more instance(s) in results.json | | |

### `BAR.RED.POPC.DEFER_BLOCKING IMM, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `BAR.RED.POPC.DEFER_BLOCKING 0x0, P0` | `0000000000007b1d 000fec0000014000` | bar_red |

