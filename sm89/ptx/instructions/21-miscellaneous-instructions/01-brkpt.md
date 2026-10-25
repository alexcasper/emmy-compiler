<!-- Generated from https://docs.nvidia.com/cuda/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="miscellaneous-instructions-brkpt"></a>
# 9.7.21.1. Miscellaneous Instructions: `brkpt`

`brkpt`

Breakpoint.

Syntax

    brkpt;

Description

Suspends execution.

PTX ISA Notes

Introduced in PTX ISA version 1.0.

Target ISA Notes

`brkpt` requires `sm_11` or higher.

Examples

        brkpt;
    @p  brkpt;

