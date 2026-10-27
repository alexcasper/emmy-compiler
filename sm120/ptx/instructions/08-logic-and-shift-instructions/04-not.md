<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="logic-and-shift-instructions-not"></a>
# 9.7.8.4. Logic and Shift Instructions: `not`

`not`

Bitwise negation; one’s complement.

Syntax

    not.type d, a;

    .type = { .pred, .b16, .b32, .b64 };

Description

Invert the bits in `a`.

Semantics

    d = ~a;

Notes

The size of the operands must match, but not necessarily the type.

Allowed types include predicates.

PTX ISA Notes

Introduced in PTX ISA version 1.0.

Target ISA Notes

Supported on all target architectures.

Examples

    not.b32  mask,mask;
    not.pred  p,q;

