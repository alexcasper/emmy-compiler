<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="descriptions-pragma-strings"></a>
# 12. Descriptions of `.pragma` Strings

This section describes the `.pragma` strings defined by ptxas.

<a id="pragma-strings-nounroll"></a>
## 12.1. Pragma Strings: `"nounroll"`

`"nounroll"`

Disable loop unrolling in optimizing the backend compiler.

Syntax

    .pragma "nounroll";

Description

The `"nounroll"`` ``pragma` is a directive to disable loop unrolling in the optimizing backend compiler.

The `"nounroll"`` ``pragma` is allowed at module, entry-function, and statement levels, with the following meanings:

module scope  
disables unrolling for all loops in module, including loops preceding the `.pragma`.

entry-function scope  
disables unrolling for all loops in the entry function body.

statement-level pragma  
disables unrolling of the loop for which the current block is the loop header.

Note that in order to have the desired effect at statement level, the `"nounroll"` directive must appear before any instruction statements in the loop header basic block for the desired loop. The loop header block is defined as the block that dominates all blocks in the loop body and is the target of the loop backedge. Statement-level `"nounroll"` directives appearing outside of loop header blocks are silently ignored.

PTX ISA Notes

Introduced in PTX ISA version 2.0.

Target ISA Notes

Requires `sm_20` or higher. Ignored for `sm_1x` targets.

Examples

    .entry foo (...)
    .pragma "nounroll";  // do not unroll any loop in this function
    {
    ...
    }

    .func bar (...)
    {
    ...
    L1_head:
         .pragma "nounroll";  // do not unroll this loop
         ...
    @p   bra L1_end;
    L1_body:
         ...
    L1_continue:
         bra L1_head;
    L1_end:
         ...
    }

<a id="pragma-strings-used-bytes-mask"></a>
## 12.2. Pragma Strings: `"used_bytes_mask"`

`"used_bytes_mask"`

Mask for indicating used bytes in data of ld operation.

Syntax

    .pragma "used_bytes_mask mask";

Description

The `"used_bytes_mask"`` ``pragma` is a directive that specifies used bytes in a load operation based on the mask provided.

`"used_bytes_mask"`` ``pragma` needs to be specified prior to a load instruction for which information about bytes used from the load operation is needed. Pragma is ignored if instruction following it is not a load instruction.

For a load instruction without this pragma, all bytes from the load operation are assumed to be used.

Operand `mask` is a 32-bit integer with set bits indicating the used bytes in data of load operation.

Semantics

    Each bit in mask operand corresponds to a byte data where each set bit represents the used byte.
    Most-significant bit corresponds to most-significant byte of data.

    // For 4 bytes load with only lower 3 bytes used
    .pragma "used_bytes_mask 0x7";
    ld.global.u32 %r0, [gbl];     // Higher 1 byte from %r0 is unused

    // For vector load of 16 bytes with lower 12 bytes used
    .pragma "used_bytes_mask 0xfff";
    ld.global.v4.u32 {%r0, %r1, %r2, %r3}, [gbl];  // %r3 unused

PTX ISA Notes

Introduced in PTX ISA version 8.3.

Target ISA Notes

Requires `sm_50` or higher.

Examples

    .pragma "used_bytes_mask 0xfff";
    ld.global.v4.u32 {%r0, %r1, %r2, %r3}, [gbl]; // Only lower 12 bytes used

