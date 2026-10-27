<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="floating-point-instructions-copysign"></a>
# 9.7.3.2. Floating Point Instructions: `copysign`

`copysign`

Copy sign of one input to another.

Syntax

    copysign.type  d, a, b;

    .type = { .f32, .f64 };

Description

Copy sign bit of `a` into value of `b`, and return the result as `d`.

PTX ISA Notes

Introduced in PTX ISA version 2.0.

Target ISA Notes

Requires `sm_20` or higher.

Examples

    copysign.f32  x, y, z;
    copysign.f64  A, B, C;

