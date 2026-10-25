# Opcode cross-check: sm_120 probes vs Mesa NAK

Reference: Mesa NAK `sm70_encode.rs` at mirror commit `837ab0e30740` (<https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs>), the open-source NVK compiler's unified SM70+ encoder (sm=120 is a first-class branch; NVK has been Vulkan 1.4 conformant on Blackwell consumer since Mesa 25.3, so its encoders are hardware-tested on RTX 50-series). Comparison is on the low 9 opcode bits (NAK adds the operand-form bits 9-11 separately). Our side is the probe corpus (4112 instructions, `tools/sass_probe.py`).

**62/67** same-named opcodes agree on the 9-bit opcode; 3 more are NAK ops that cover several SASS mnemonics and map onto the matching observed ones; 2 differ. 59 observed opcodes have no NAK encoder (NAK does not emit them).

| opcode | result | NAK opcode(s) | observed opcode(s) (bits 0-11) | NAK source |
|---|---|---|---|---|
| ATOM | NAK op maps to ATOMG/ATOMS/REDG | 0x38c 0x38d 0x3a8 0x3a9 0x98c 0x98e 0x9a3 0x9a6 0x9a8 | 0x18a 0x98a | [L3777](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L3777) |
| BAR | agree | 0x31d 0xb1d | 0x11d 0xb1d | [L4245](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4245) |
| BMSK | agree | 0x1b 0x9b | 0x1b 0x21b | [L1518](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1518) |
| BRA | agree | 0x547 0x947 | 0x147 0x547 0x947 | [L4191](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4191) |
| BREV | agree | 0xbe 0x101 | 0x101 0x301 | [L1547](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1547) |
| BSSY | agree | 0x945 | 0x145 0x945 | [L4165](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4165) |
| BSYNC | agree | 0x941 | 0x141 0x941 | [L4179](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4179) |
| CCTL | agree | 0x98f | 0x18f 0x98f | [L4033](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4033) |
| CS2R | agree | 0x805 | 0x5 0x805 | [L4273](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4273) |
| DADD | agree | 0x29 | 0x229 0x29 | [L1215](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1215) |
| DFMA | agree | 0x2b | 0x22b 0x2b | [L1235](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1235) |
| DMUL | agree | 0x28 | 0x228 0x28 | [L1256](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1256) |
| DSETP | agree | 0x2a | 0x22a 0x2a | [L1276](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1276) |
| EXIT | agree | 0x94d | 0x14d 0x94d | [L4218](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4218) |
| F2F | agree | 0x5b 0x104 0x110 | 0x110 0x310 | [L2189](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2189) |
| F2FP | agree | 0x3e 0xba | 0x23e 0x3e | [L2237](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2237) |
| F2I | agree | 0x5c 0x105 0x111 | 0x105 0x305 | [L2282](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2282) |
| FADD | agree | 0x21 0x54 | 0x21 0x221 0x421 | [L849](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L849) |
| FFMA | agree | 0x23 0x55 | 0x223 0x23 0x423 0x823 | [L890](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L890) |
| FLO | agree | 0xbd 0x100 | 0x100 0x300 0xd00 | [L1561](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1561) |
| FMNMX | agree | 0x9 0x50 | 0x209 0x9 | [L925](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L925) |
| FMUL | agree | 0x20 0x56 | 0x20 0x220 0x820 | [L963](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L963) |
| FRND | agree | 0x5d 0x107 0x113 | 0x107 0x307 | [L2371](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2371) |
| FSETP | agree | 0xb 0x53 | 0x20b 0x80b 0xb | [L1089](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1089) |
| HFMA2 | agree | 0x31 | 0x231 0x31 0x431 0x831 | [L1350](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1350) |
| HMMA | agree | 0x23c | 0x23c 0x3c | [L4577](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4577) |
| HMNMX2 | agree | 0x40 | 0x240 0x40 | [L1488](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1488) |
| HSET2 | agree | 0x33 | 0x233 0x33 | [L1403](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1403) |
| HSETP2 | agree | 0x34 | 0x234 0x34 | [L1445](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1445) |
| I2F | agree | 0x5a 0x106 0x112 | 0x112 0x312 | [L2329](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2329) |
| IABS | agree | 0x13 0x4d | 0x13 0x213 | [L1580](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1580) |
| IADD3 | agree | 0x10 0x90 | 0x10 0x210 0x810 0xc10 | [L1595](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1595) |
| IMAD | agree | 0x24 0xa4 | 0x224 0x225 0x227 0x24 0x25 0x27 0x824 0x825 | [L1751](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1751) |
| IMMA | agree | 0x237 | 0x237 0x37 | [L4520](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4520) |
| ISETP | agree | 0xc 0x8c | 0x20c 0x80c 0xc 0xc0c | [L1866](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1866) |
| LD | NAK op maps to LDG/LDL/LDS | 0x381 0x981 0x983 0x984 | 0x180 0x980 | [L3428](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L3428) |
| LDC | agree | 0x582 0x7ac 0xab9 0xb82 0xbac | 0x182 0xb82 | [L3505](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L3505) |
| LDSM | agree | 0x83b | 0x3b 0x83b | [L4622](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4622) |
| LEA | agree | 0x11 0x91 | 0x11 0x211 0x811 0xc11 | [L1923](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1923) |
| LOP3 | agree | 0x12 0x92 | 0x12 0x212 0x812 0xc12 | [L2064](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2064) |
| MATCH | agree | 0x3a1 | 0x1a1 0x3a1 | [L4493](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4493) |
| MEMBAR | agree | 0x992 | 0x192 0x992 | [L4063](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4063) |
| MOV | agree | 0x2 0xc82 | 0x2 0x202 0x802 0xc02 | [L2417](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2417) |
| MOVM | agree | 0x23a | 0x23a 0x3a | [L4663](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4663) |
| MUFU | agree | 0x108 | 0x108 0x308 0x908 | [L1168](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1168) |
| NANOSLEEP | agree | 0x15d | 0x15d 0x35d | [L4679](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4679) |
| NOP | agree | 0x918 | 0x118 0x918 | [L4371](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4371) |
| PLOP3 | agree | 0x81c 0x89c | 0x1c 0x81c | [L2616](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2616) |
| POPC | agree | 0xbf 0x109 | 0x109 0x309 0xd09 | [L2124](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2124) |
| PRMT | agree | 0x16 0x96 | 0x16 0x816 | [L2448](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2448) |
| R2UR | agree | 0x2ca 0x3c2 | 0x2ca 0xca | [L2688](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2688) |
| REDUX | agree | 0x3c4 | 0x1c4 0x3c4 | [L2705](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2705) |
| S2R | agree | 0x919 0x9c3 | 0x119 0x919 | [L4404](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4404) |
| SEL | agree | 0x7 0x87 | 0x207 0x7 0x807 | [L2491](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2491) |
| SGXT | agree | 0x1a 0x9a | 0x1a 0x21a | [L2529](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2529) |
| SHF | agree | 0x19 0x99 | 0x19 0x219 0x819 | [L2141](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2141) |
| SHFL | agree | 0x389 0x589 0x989 0xf89 | 0x189 0x589 0x989 0xf89 | [L2558](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2558) |
| ST | NAK op maps to STG/STL/STS | 0x386 0x387 0x388 0x986 0x987 0x988 | 0x185 0x985 | [L3625](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L3625) |
| SULD | differ | 0x998 0x99a | 0x199 0xf99 | [L3321](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L3321) |
| SUST | differ | 0x99c 0x99e | 0x19d 0xf9d | [L3359](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L3359) |
| TEX | agree | 0x361 0xb60 0xd61 | 0x160 0xf60 | [L2887](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2887) |
| TLD | agree | 0x367 0xb66 0xd67 | 0x166 0xf66 | [L2956](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2956) |
| TLD4 | agree | 0x364 0xb63 0xd64 | 0x163 0xf63 | [L3032](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L3032) |
| TXD | agree | 0x36d 0xb6c 0xd6d | 0x16c 0xf6c | [L3137](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L3137) |
| TXQ | agree | 0x370 0xb6f | 0x16f 0xf6f | [L3198](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L3198) |
| VOTE | agree | 0x806 0x886 | 0x6 0x806 | [L4465](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4465) |
| WARPSYNC | agree | 0x148 | 0x148 0x348 | [L4234](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4234) |

## Differing opcodes

These need a second look: either NAK deliberately re-encodes them on `sm >= 100/120` branches (check the `if e.sm >=` sites at the linked lines) or our normalized opcode extraction mis-splits a mnemonic.

- `SULD`: NAK 0x998 0x99a vs observed 0x199 0xf99
- `SUST`: NAK 0x99c 0x99e vs observed 0x19d 0xf9d

## Notes on the two differing opcodes

`SULD`/`SUST` (and their reduction siblings) are the only same-named mismatches. ptxas on sm_120 emits `SULD.D...` with 12-bit opcode `0xf99` (base bits 0-8 = `0x199`) and `SUST.D...` `0xf9d` (`0x19d`), while NAK sets `0x998`/`0x99a` and `0x99c`/`0x99e` in the same 0..12 field. This pattern is inherited, not new: the sm_89 KB saw exactly the same numbers (kuterdinel listed both the `0x998` and the `0xf99` form, so its family-match logic reported agreement). Either the binary-vs-formatted bit assignment inside the surface-op opcode field differs between NAK's model and ptxas's real encoding, or hardware ignores the differing bits — resolving that needs NAK's hardware tests (`nvk_hw_tests`) or a real Blackwell run, which this repo cannot do.

Note: gitlab.freedesktop.org raw fetches are bot-walled; sources are pulled from the same-day-synced chaotic-cx/mesa-mirror GitHub mirror.

