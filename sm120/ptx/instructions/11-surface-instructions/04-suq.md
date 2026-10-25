<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="surface-instructions-suq"></a>
# 9.7.11.4. Surface Instructions: `suq`

`suq`

Query a surface attribute.

Syntax

    suq.query.b32   d, [a];

    .query = { .width, .height, .depth,
               .channel_data_type, .channel_order,
               .array_size, .memory_layout };

Description

Query an attribute of a surface. Operand `a` is a `.surfref` variable or a `.u64` register.

[TABLE]

Indirect surface access

Beginning with PTX ISA version 3.1, indirect surface access is supported for target architecture `sm_20` or higher. In indirect access, operand `a` is a `.u64` register holding the address of a `.surfref` variable.

PTX ISA Notes

Introduced in PTX ISA version 1.5.

Channel data type and channel order queries added in PTX ISA version 2.1.

Indirect surface access introduced in PTX ISA version 3.1.

The `.array_size` query was added in PTX ISA version 4.1.

The `.memory_layout` query was added in PTX ISA version 4.2.

Target ISA Notes

Supported on all target architectures.

Indirect surface access requires `sm_20` or higher.

Examples

    suq.width.b32       %r1, [surf_A];

