<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="miscellaneous-instructions-trap"></a>
# 9.7.19.4. Miscellaneous Instructions: `trap`

`trap`

Perform trap operation.

Syntax

    trap;

Description

Abort execution and generate an interrupt to the host CPU.

PTX ISA Notes

Introduced in PTX ISA version 1.0.

Target ISA Notes

Supported on all target architectures.

Examples

        trap;
    @p  trap;

