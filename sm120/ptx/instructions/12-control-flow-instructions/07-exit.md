<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="control-flow-instructions-exit"></a>
# 9.7.12.7. Control Flow Instructions: `exit`

`exit`

Terminate a thread.

Syntax

    exit;

Description

Ends execution of a thread.

As threads exit, barriers waiting on all threads are checked to see if the exiting threads are the only threads that have not yet made it to a barrier{.cta} for all threads in the CTA or to a `barrier.cluster` for all threads in the cluster. If the exiting threads are holding up the barrier, the barrier is released.

PTX ISA Notes

Introduced in PTX ISA version 1.0.

Target ISA Notes

Supported on all target architectures.

Examples

        exit;
    @p  exit;

