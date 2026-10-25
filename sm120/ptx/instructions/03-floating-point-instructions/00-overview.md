<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="floating-point-instructions"></a>
# 9.7.3. Floating-Point Instructions

Floating-point instructions operate on `.f32` and `.f64` register operands and constant immediate values. The floating-point instructions are:

- `testp`

- `copysign`

- `add`

- `sub`

- `mul`

- `fma`

- `mad`

- `div`

- `abs`

- `neg`

- `min`

- `max`

- `rcp`

- `sqrt`

- `rsqrt`

- `sin`

- `cos`

- `lg2`

- `ex2`

- `tanh`

Instructions that support rounding modifiers are IEEE-754 compliant. Double-precision instructions support subnormal inputs and results. Single-precision instructions support subnormal inputs and results by default for `sm_20` and subsequent targets, and flush subnormal inputs and results to sign-preserving zero for `sm_1x` targets. The optional `.ftz` modifier on single-precision instructions provides backward compatibility with `sm_1x` targets by flushing subnormal inputs and results to sign-preserving zero regardless of the target architecture.

Single-precision `add`, `sub`, `mul`, and `mad` support saturation of results to the range \[0.0, 1.0\], with `NaN`s being flushed to positive zero. `NaN` payloads are supported for double-precision instructions (except for `rcp.approx.ftz.f64` and `rsqrt.approx.ftz.f64`, which maps input `NaN`s to a canonical `NaN`). Single-precision instructions return an unspecified `NaN`. Note that future implementations may support `NaN` payloads for single-precision instructions, so PTX programs should not rely on the specific single-precision `NaN`s being generated.

[Table 30](https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html#floating-point-instructions-summary-of-floating-point-instructions) summarizes floating-point instructions in PTX.

[TABLE]

Table 30 Summary of Floating-Point Instructions[](#floating-point-instructions-summary-of-floating-point-instructions "Permalink to this table") {#floating-point-instructions-summary-of-floating-point-instructions}

