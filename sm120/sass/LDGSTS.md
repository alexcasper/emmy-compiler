# LDGSTS (SM120 SASS)

**NVIDIA:** Asynchronous Global to Shared Memcopy (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: cp.async global->shared async copy (category: Load / store)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cp_async`: `cp.async.cg.shared.global + commit_group + wait_group`

12-bit opcode field (bits 0-11) values observed: `0x75f`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0111010111111110101000000100000000000000000000000000000000000000
0110000000011000000110011101000000000000000101111111000100000000
```

1 normalized operand form(s) observed:

### `LDGSTS.E.BYPASS.IMM [R], desc[UR][R.IMM]` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDGSTS.E.BYPASS.128 [R5], desc[UR6][R2.64]` | `0000000002057fae 008fe8000b981806` | cp_async |

