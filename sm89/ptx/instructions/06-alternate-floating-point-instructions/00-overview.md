<!-- Generated from https://docs.nvidia.com/cuda/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="alternate-floating-point-instructions"></a>
# 9.7.6. Alternate Floating-Point Instructions

Alternate floating-point instructions operate on FP8, FP6, FP4 data types. The register variable to be used for such instruction varies depending upon the data type. Refer [Packed Floating Point Data Types](../../05-state-spaces-types-and-variables.md#packed-floating-point-data-types) for details on the supported data types and their register representations.

The alternate floating-point instructions are:

- `add`

- `sub`

- `mul`

- `fma`

