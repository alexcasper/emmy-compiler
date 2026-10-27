<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="cache-operators"></a>
# 9.7.9.1. Cache Operators

PTX ISA version 2.0 introduced optional cache operators on load and store instructions. The cache operators require a target architecture of `sm_20` or higher.

Cache operators on load or store instructions are treated as performance hints only. The use of a cache operator on an `ld` or `st` instruction does not change the memory consistency behavior of the program.

For `sm_20` and higher, the cache operators have the following definitions and behavior.

[TABLE]

Table 31 Cache Operators for Memory Load Instructions[](#id669 "Permalink to this table") {#id669}

[TABLE]

Table 32 Cache Operators for Memory Store Instructions[](#id670 "Permalink to this table") {#id670}

