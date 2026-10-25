# Opcode cross-check: kuterdinel pages vs Mesa NAK

Reference: Mesa NAK `sm70_encode.rs` at commit `e7371b0711bb` (<https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs>), the open-source NVK compiler's SM70+ (Volta-Ada) encoder. Comparison is on the low 9 opcode bits (NAK adds the operand-form bits 9-11 separately).

**80/83** same-named opcodes agree; 3 more are NAK ops that cover several SASS mnemonics and map onto the matching scraped ones; 0 differ. 68 scraped opcodes have no NAK encoder (NAK does not emit them).

| opcode | result | NAK opcode(s) | site opcode(s) (bits 0-11) | NAK source |
|---|---|---|---|---|
| AL2P | agree | 0x920 | 0x920 | [L3915](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3915) |
| ALD | agree | 0x321 | 0x321 0x521 | [L3932](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3932) |
| ATOM | NAK op maps to ATOMG/ATOMS/RED | 0x38c 0x38d 0x3a8 0x3a9 0x98c 0x98e 0x9a3 0x9a6 0x9a8 | 0x38a 0x38b 0x98a | [L3777](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3777) |
| BAR | agree | 0x31d 0xb1d | 0x31d 0x91d 0xb1d | [L4245](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4245) |
| BMOV | agree | 0x355 0x356 | 0x355 0x356 0x357 0x956 0x957 0xb56 0xb57 0xf56 | [L4128](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4128) |
| BMSK | agree | 0x1b 0x9b | 0x21b 0x81b 0xa1b 0xc1b | [L1518](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1518) |
| BRA | agree | 0x547 0x947 | 0x947 | [L4191](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4191) |
| BREAK | agree | 0x942 | 0x942 | [L4152](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4152) |
| BREV | agree | 0xbe 0x101 | 0x301 0x901 0xb01 0xd01 | [L1547](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1547) |
| BSSY | agree | 0x945 | 0x945 | [L4165](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4165) |
| BSYNC | agree | 0x941 | 0x941 | [L4179](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4179) |
| CCTL | agree | 0x98f | 0x98f | [L4033](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4033) |
| CS2R | agree | 0x805 | 0x805 | [L4273](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4273) |
| DADD | agree | 0x29 | 0x229 0x429 0x629 0xe29 | [L1215](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1215) |
| DFMA | agree | 0x2b | 0x22b 0x42b 0x62b 0x82b 0xa2b 0xc2b 0xe2b | [L1235](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1235) |
| DMUL | agree | 0x28 | 0x228 0x828 0xa28 0xc28 | [L1256](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1256) |
| DSETP | agree | 0x2a | 0x22a 0x42a 0x62a 0xe2a | [L1276](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1276) |
| EXIT | agree | 0x94d | 0x94d | [L4218](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4218) |
| F2F | agree | 0x5b 0x104 0x110 | 0x310 0x910 0xb10 0xd10 | [L2189](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2189) |
| F2FP | agree | 0x3e 0xba | 0x23e 0x43e 0x63e 0x83e 0xa3e 0xc3e 0xe3e | [L2237](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2237) |
| F2I | agree | 0x5c 0x105 0x111 | 0x305 0x311 0x905 0x911 0xb05 0xb11 0xd11 | [L2282](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2282) |
| FADD | agree | 0x21 0x54 | 0x221 0x421 0x621 0xe21 | [L849](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L849) |
| FFMA | agree | 0x23 0x55 | 0x223 0x423 0x623 0x823 0xa23 0xc23 0xe23 | [L890](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L890) |
| FLO | agree | 0xbd 0x100 | 0x300 0x900 0xb00 0xd00 | [L1561](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1561) |
| FMNMX | agree | 0x9 0x50 | 0x209 0x809 0xa09 0xc09 | [L925](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L925) |
| FMUL | agree | 0x20 0x56 | 0x220 0x820 0xa20 0xc20 | [L963](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L963) |
| FRND | agree | 0x5d 0x107 0x113 | 0x313 0x913 0xb13 0xd13 | [L2371](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2371) |
| FSET | agree | 0xa 0x52 | 0x20a 0x80a 0xa0a 0xc0a | [L1052](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1052) |
| FSETP | agree | 0xb 0x53 | 0x20b 0x80b 0xa0b 0xc0b | [L1089](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1089) |
| FSWZADD | agree | 0x822 | 0x822 | [L1132](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1132) |
| HADD2 | agree | 0x30 | 0x230 0x430 0x630 0xe30 | [L1316](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1316) |
| HFMA2 | agree | 0x31 | 0x231 0x431 0x631 0x831 0xa31 0xc31 0xe31 | [L1350](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1350) |
| HMMA | agree | 0x23c | 0x23c | [L4577](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4577) |
| HMNMX2 | agree | 0x40 | 0x240 0x840 0xa40 0xc40 | [L1488](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1488) |
| HMUL2 | agree | 0x32 | 0x232 0x832 0xa32 0xc32 | [L1377](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1377) |
| HSET2 | agree | 0x33 | 0x233 0x433 0x633 0xe33 | [L1403](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1403) |
| HSETP2 | agree | 0x34 | 0x234 0x434 0x634 0xe34 | [L1445](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1445) |
| I2F | agree | 0x5a 0x106 0x112 | 0x306 0x312 0x906 0x912 0xb06 0xb12 0xd06 0xd12 | [L2329](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2329) |
| IABS | agree | 0x13 0x4d | 0x213 0x813 0xa13 0xc13 | [L1580](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1580) |
| IADD3 | agree | 0x10 0x90 | 0x210 0x810 0xa10 0xc10 | [L1595](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1595) |
| IMAD | agree | 0x24 0xa4 | 0x224 0x225 0x424 0x624 0x625 0x824 0x825 0xa24 0xa25 0xc24 0xc25 0xe24 0xe25 | [L1751](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1751) |
| IMMA | agree | 0x237 | 0x237 | [L4520](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4520) |
| IMNMX | agree | 0x17 0x85 | 0x217 0x817 0xa17 0xc17 | [L1815](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1815) |
| IPA | agree | 0x326 | 0x326 0x526 0x926 0xb26 | [L3974](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3974) |
| ISBERD | agree | 0x923 | 0x923 | [L4286](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4286) |
| ISETP | agree | 0xc 0x8c | 0x20c 0x80c 0xa0c 0xc0c | [L1866](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1866) |
| LD | NAK op maps to LDG/LDL/LDS | 0x381 0x981 0x983 0x984 | 0x980 | [L3428](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3428) |
| LDC | agree | 0x582 0x7ac 0xab9 0xb82 0xbac | 0x582 0xb82 | [L3505](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3505) |
| LDSM | agree | 0x83b | 0x83b | [L4622](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4622) |
| LDTRAM | agree | 0x3ad | 0x3ad | [L4015](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4015) |
| LEA | agree | 0x11 0x91 | 0x211 0x411 0x811 0xa11 0xc11 | [L1923](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1923) |
| LOP3 | agree | 0x12 0x92 | 0x212 0x812 0xa12 0xc12 | [L2064](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2064) |
| MATCH | agree | 0x3a1 | 0x3a1 | [L4493](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4493) |
| MEMBAR | agree | 0x992 | 0x992 | [L4063](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4063) |
| MOV | agree | 0x2 0xc82 | 0x202 0x802 0xa02 0xc02 | [L2417](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2417) |
| MOVM | agree | 0x23a | 0x23a | [L4663](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4663) |
| MUFU | agree | 0x108 | 0x308 0x908 0xb08 0xd08 | [L1168](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1168) |
| NANOSLEEP | agree | 0x15d | 0x35d 0x95d 0xb5d | [L4679](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4679) |
| NOP | agree | 0x918 | 0x0 0x918 | [L4371](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4371) |
| OUT | agree | 0x124 | 0x324 0x924 0xd24 | [L4421](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4421) |
| PIXLD | agree | 0x925 | 0x925 | [L4381](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4381) |
| PLOP3 | agree | 0x81c 0x89c | 0x21d 0x21e 0x21f 0x81c 0xa1d 0xa1e 0xa1f 0xc1d 0xc1e 0xc1f | [L2616](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2616) |
| POPC | agree | 0xbf 0x109 | 0x309 0x909 0xb09 0xd09 | [L2124](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2124) |
| PRMT | agree | 0x16 0x96 | 0x216 0x416 0x616 0x816 0xa16 0xc16 0xe16 | [L2448](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2448) |
| R2UR | agree | 0x2ca 0x3c2 | 0x3c2 | [L2688](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2688) |
| REDUX | agree | 0x3c4 | 0x3c4 | [L2705](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2705) |
| S2R | agree | 0x919 0x9c3 | 0x919 | [L4404](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4404) |
| SEL | agree | 0x7 0x87 | 0x207 0x807 0xa07 0xc07 | [L2491](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2491) |
| SGXT | agree | 0x1a 0x9a | 0x21a 0x81a 0xa1a 0xc1a | [L2529](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2529) |
| SHF | agree | 0x19 0x99 | 0x219 0x419 0x619 0x819 0xa19 0xc19 0xe19 | [L2141](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2141) |
| SHFL | agree | 0x389 0x589 0x989 0xf89 | 0x389 0x589 0x989 0xf89 | [L2558](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2558) |
| ST | NAK op maps to STG/STL/STS | 0x386 0x387 0x388 0x986 0x987 0x988 | 0x385 0x985 | [L3625](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3625) |
| SUATOM | agree | 0x394 0x396 0x3a0 | 0x394 0x593 0x595 0x793 0x795 0xf93 0xf95 | [L3391](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3391) |
| SULD | agree | 0x998 0x99a | 0x797 0x799 0x998 0xb97 0xb99 0xf97 0xf99 | [L3321](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3321) |
| SUST | agree | 0x99c 0x99e | 0x99c 0xb9d | [L3359](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3359) |
| TEX | agree | 0x361 0xb60 0xd61 | 0x361 0xb60 0xb62 0xf60 | [L2887](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2887) |
| TLD | agree | 0x367 0xb66 0xd67 | 0x367 0xb66 0xb68 0xf66 | [L2956](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2956) |
| TLD4 | agree | 0x364 0xb63 0xd64 | 0x364 0xb63 0xb65 0xf63 | [L3032](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3032) |
| TMML | agree | 0x36a 0xb69 | 0x36a 0xb69 0xb6b 0xf69 | [L3092](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3092) |
| TXD | agree | 0x36d 0xb6c 0xd6d | 0x36d 0xb6c 0xb6e 0xf6c | [L3137](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3137) |
| TXQ | agree | 0x370 0xb6f | 0x370 0xb6f 0xb71 0xf6f | [L3198](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3198) |
| VOTE | agree | 0x806 0x886 | 0x806 | [L4465](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4465) |
| WARPSYNC | agree | 0x148 | 0x348 0x948 0xb48 | [L4234](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4234) |
