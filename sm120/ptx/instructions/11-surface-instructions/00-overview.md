<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="surface-instructions"></a>
# 9.7.11. Surface Instructions

This section describes PTX instructions for accessing surfaces. PTX supports the following operations on surface descriptors:

- Static initialization of surface descriptors.

- Module-scope and per-entry scope definitions of surface descriptors.

- Ability to query fields within surface descriptors.

These instructions provide access to surface memory.

- `suld`

- `sust`

- `sured`

- `suq`

