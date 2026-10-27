<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="floating-point-instructions-div"></a>
# 9.7.3.8. Floating Point Instructions: `div`

`div`

Divide one value by another.

Syntax

    div.approx{.ftz}.f32  d, a, b;  // fast, approximate divide
    div.full{.ftz}.f32    d, a, b;  // full-range approximate divide
    div.rnd{.ftz}.f32     d, a, b;  // IEEE 754 compliant rounding
    div.rnd.f64           d, a, b;  // IEEE 754 compliant rounding

    .rnd = { .rn, .rz, .rm, .rp };

Description

Divides `a` by `b`, stores result in `d`.

Semantics

    d = a / b;

Notes

Fast, approximate single-precision divides:

- `div.approx.f32` implements a fast approximation to divide, computed as `d`` ``=`` ``a`` ``*`` ``(1/b)`. For `|b|` in \[2⁻¹²⁶, 2¹²⁶\], the maximum `ulp` error is 2. For 2¹²⁶ \< `|b|` \< 2¹²⁸, if `a` is infinity, `div.approx.f32` returns `NaN`, otherwise it returns 0.

- `div.full.f32` implements a relatively fast, full-range approximation that scales operands to achieve better accuracy, but is not fully IEEE 754 compliant and does not support rounding modifiers. The maximum `ulp` error is 2 across the full range of inputs.

- Subnormal inputs and results are flushed to sign-preserving zero. Fast, approximate division by zero creates a value of infinity (with same sign as `a`).

Divide with IEEE 754 compliant rounding:

Rounding modifiers (no default):

`.rn`  
mantissa LSB rounds to nearest even

`.rz`  
mantissa LSB rounds towards zero

`.rm`  
mantissa LSB rounds towards negative infinity

`.rp`  
mantissa LSB rounds towards positive infinity

Subnormal numbers:

`sm_20+`  
By default, subnormal numbers are supported.

`div.ftz.f32` flushes subnormal inputs and results to sign-preserving zero.

`sm_1x`  
`div.f64` supports subnormal numbers.

`div.f32` flushes subnormal inputs and results to sign-preserving zero.

PTX ISA Notes

`div.f32` and `div.f64` introduced in PTX ISA version 1.0.

Explicit modifiers `.approx`, `.full`, `.ftz`, and rounding introduced in PTX ISA version 1.4.

For PTX ISA version 1.4 and later, one of `.approx`, `.full`, or `.rnd` is required.

For PTX ISA versions 1.0 through 1.3, `div.f32` defaults to `div.approx.ftz.f32`, and `div.f64` defaults to `div.rn.f64`.

Target ISA Notes

`div.approx.f32` and `div.full.f32` supported on all target architectures.

`div.rnd.f32` requires `sm_20` or higher.

`div.rn.f64` requires `sm_13` or higher, or `.target`` ``map_f64_to_f32`.

`div.{rz,rm,rp}.f64` requires `sm_20` or higher.

Examples

    div.approx.ftz.f32  diam,circum,3.14159;
    div.full.ftz.f32    x, y, z;
    div.rn.f64          xd, yd, zd;

