<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="tcgen05-matrix-descriptors"></a>
# 9.7.16.4. Matrix Descriptors

There are three kinds of matrix descriptors used by the `tcgen05` family of instructions.

<a id="tcgen05-shared-memory-descriptor"></a>
## 9.7.16.4.1. Shared memory descriptor

The shared memory descriptor describes the properties of multiplicand matrix in shared memory including its location in the shared memory of the current *CTA*. It is a 64-bit value contained in a register with the following layout:

[TABLE]

Table 41 Shared memory descriptor layout[](#tcgen05-shared-memory-desc-layout "Permalink to this table") {#tcgen05-shared-memory-desc-layout}

where matrix-descriptor-encode(x) = (x & 0x3FFFF) \>\> 4

The value of base offset is 0 when the repeating pattern of the specified swizzling mode starts as per shown in [Table 42](https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html#tcgen05-start-addr-swizzle-mode).

| Swizzling mode   | Starting address of the repeating pattern |
|------------------|-------------------------------------------|
| 128-Byte swizzle | 1024-Byte boundary                        |
| 64-Byte swizzle  | 512-Byte boundary                         |
| 32-Byte swizzle  | 256-Byte boundary                         |

Table 42 Starting address of repeating pattern for various swizzling modes[](#tcgen05-start-addr-swizzle-mode "Permalink to this table") {#tcgen05-start-addr-swizzle-mode}

Otherwise, the base offset must be a non-zero value, computed using the following formula: `base`` ``offset`` ``=`` ``(pattern`` ``start`` ``addr`` ``>>`` ``0x7)`` ``&`` ``0x7`

The following must be 16-byte aligned:

1.  Matrix start address

2.  Leading dimension byte offset

3.  Stride dimension byte offset

<a id="tcgen05-shared-memory-descriptor-target-isa-note"></a>
### 9.7.16.4.1.1. Target ISA Note

- The byte address mode for the leading dimension stride is supported on `sm_103a`.

<a id="tcgen05-instruction-descriptor"></a>
## 9.7.16.4.2. Instruction descriptor

The instruction descriptor describes the shapes, types and other details of all the matrices and the matrix-multiplication-and-accumulation operation. It is a 32-bit value in registers and the exact layout is dependent on the MMA-Kind:

[TABLE]

Table 43 Instruction descriptor format for .kind::tf32, .kind::f16, .kind::f8f6f4 and .kind::i8[](#tcgen05-instuction-desc-kind-tf32-f16-f8f6f4 "Permalink to this table") {#tcgen05-instuction-desc-kind-tf32-f16-f8f6f4}

[TABLE]

Table 44 Instruction descriptor format for .kind::mxf8f6f4[](#tcgen05-instuction-desc-kind-mxf8f6f4 "Permalink to this table") {#tcgen05-instuction-desc-kind-mxf8f6f4}

[TABLE]

Table 45 Instruction descriptor format for .kind::mxf4 and .kind::mxf4nvf4[](#tcgen05-instuction-desc-kind-mxf4-mxf4nvf4 "Permalink to this table") {#tcgen05-instuction-desc-kind-mxf4-mxf4nvf4}

<a id="tcgen05-zero-column-mask-descriptor"></a>
## 9.7.16.4.3. Zero-Column Mask Descriptor

The zero-column mask descriptor is used to generate a mask that specifies which columns of `B` matrix will have zero value for the MMA operation regardless of the values present in the shared memory. The total size of the generated mask is N-bits.

A 0-bit in the mask specifies that values of the corresponding column in matrix `B` should be used for the MMA operation. A 1-bit in the mask specifies 0s must be used for the entire column for the MMA operation.

The zero-column mask descriptor is a 64-bit value in registers with the following layout:

[TABLE]

Table 46 Zero-Column Mask descriptor layout[](#tcgen05-zero-column-mask-desc "Permalink to this table") {#tcgen05-zero-column-mask-desc}

The zero-column mask is made up of one or more sub-mask depending on M, as shown in the table:

| M | Zero-Column Mask breakup | Sub-masks | First Span used | Start Column used |
|----|----|----|----|----|
| 128 | Single sub-mask of size N-bits | mask0 | fs0 | sc0 |
| 64 | Two sub-masks, each with size of N/2 bits | mask0, mask1 | fs0, fs1 | sc0, sc1 |
| 32 | Four sub-masks, each with size of N/4 bits | mask0, mask1 mask2, mask3 | fs0, fs1, fs2, fs3 | sc0, sc1, sc2, sc3 |

The following table shows the coverage of the sub-masks across N-dimension:

| Sub-mask | M |  |  |
|----|----|----|----|
|  | 128 | 64 | 32 |
| mask0 | Columns \[0, N-1\] | Columns \[0, N/2-1\] | Columns \[0, N/4-1\] |
| mask1 | – | Columns \[N/2, N-1\] | Columns \[N/4, N/2-1\] |
| mask2 | – | – | Columns \[N/2, (N/4\*3)-1\] |
| mask3 | – | – | Columns \[(N/4\*3), N-1\] |

The following examples shows zero-column mask descriptor and their corresponding mask generated:

1.  Example 1: M = 128

    Input zero-column mask descriptor:

    | Start count  | First span   | Non-Zero Mask | Skip Span | Use Span | Shift |
    |--------------|--------------|---------------|-----------|----------|-------|
    | {0, 0, 0, 0} | {0, 0, 0, 0} | 0             | 4         | 3        | 0     |

    Output zero-column mask: 0x0.

    As Non-Zero Mask field is 0, the mask is 0x0. All the columns of the matrix `B` will be used for the MMA operation.

2.  Example 2: M = 128

    Input zero-column mask descriptor:

    | Start count  | First span   | Non-Zero Mask | Skip Span | Use Span | Shift |
    |--------------|--------------|---------------|-----------|----------|-------|
    | {-, -, -, 0} | {-, -, -, 0} | 1             | 2         | 3        | 0     |

    Output mask0: 0b … 111 0000 111 0000 (size = N)

3.  Example 3: M = 64

    Input zero-column mask descriptor:

    | Start count {.., sc1, sc0} | First span {.., fs1, fs0} | Non-Zero Mask | Skip Span | Use Span | Shift |
    |----|----|----|----|----|----|
    | {-, -, 0, 0} | {-, -, 0, 1} | 1 | 2 | 3 | 0 |

    Output mask0: 0b … 111 0000 111 0000 111

    Output masl1: 0b … 0000 111 0000 111 0000

4.  Example 4: M = 32

    Input zero-column mask descriptor:

    | Start count {sc3, sc2, sc1, sc0} | First span {fs3, fs2, fs1, fs0} | Non-Zero Mask | Skip Span | Use Span | Shift |
    |----|----|----|----|----|----|
    | {1, 2, 1, 0} | {0, 0, 1, 1} | 1 | 2 | 3 | 2 |

    Output mask0: 0b … 0000 111 0000 111

    Output mask1: 0b … 0000 111 0000 11

    Output mask2: 0b … 111 0000 111 00

    Output mask3: 0b … 111 0000 111 000

    If N = 128 then `B` Matrix with columns from 2 to 129 will be used for the MMA operation, due to the shift of 2.

