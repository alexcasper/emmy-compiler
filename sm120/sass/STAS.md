# STAS (SM120 SASS)

**NVIDIA:** Asynchronous Store to Distributed Shared Memory With Explicit Synchronization (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: st.async shared store with mbarrier completion (new opcode name on sm_120) (category: Load / store)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `st_async`: `st.async.shared::cta.mbarrier::complete_tx::bytes (sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0xbdb`.

## Encoding observations

**Constant bits across all 1 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1011110110111110000000000110000000000000000000000000000000000000
1111111100010000000000000011000000000000010001111111001000000000
```

1 normalized operand form(s) observed:

### `STAS [R.IMM], R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `STAS [R6.64], R0` | `0000000006007dbd 004fe2000c0008ff` | st_async |

