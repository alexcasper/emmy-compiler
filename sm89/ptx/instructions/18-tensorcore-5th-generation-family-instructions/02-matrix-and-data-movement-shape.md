<!-- Generated from https://docs.nvidia.com/cuda/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="tcgen05-matrix-data-movement-shape"></a>
# 9.7.18.2. Matrix and Data Movement Shape

There are two kinds of shapes involved.

1.  Shapes in the data movement operations

2.  Shapes in the MMA operations

<a id="tcgen05-matrix-shape"></a>
## 9.7.18.2.1. Matrix Shape

The matrix multiply and accumulate operations support a limited set of shapes for the operand matrices `A`, `B` and `D`. The shapes of all three matrix operands are collectively described by the tuple *MxNxK* where `A` is *MxK* matrix, `B` is a *KxN* matrix, and `D` is a *MxN* matrix.

[Table 48](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-kind-shapes) shows matrix shapes that are supported for the specified types for the `tcgen05.mma` operation.

[TABLE]

Table 48 Various combinations of .kind and shapes[](#tcgen05-kind-shapes "Permalink to this table") {#tcgen05-kind-shapes}

<a id="tcgen05-matrix-shape-target-isa-note"></a>
### 9.7.18.2.1.1. Target ISA Note

- K = 96 is only supported for following architecture-specific targets:

  - `sm_103a`.

  - `sm_107a`

- K = 64 for Dense matrix and K = 128 for Sparse matrix with `.kind::f8f6f4`/`.kind::mxf8f6f4` supported on following family-specific architectures:

  - `sm_107f` or higher in the same family

- K = 128 for Dense matrix and K = 192 for Sparse matrix with `.kind::mxf4`/`.kind::mxf4nvf4` supported on following family-specific architectures:

  - `sm_107f` or higher in the same family

<a id="tcgen05-specify-matrix-shape"></a>
## 9.7.18.2.2. Specifying Matrix Shape

*M* and *N* can be specified in the [Instruction descriptor](../../instructions/18-tensorcore-5th-generation-family-instructions/04-matrix-descriptors.md#tcgen05-instruction-descriptor).

*K* can be specified explicitly if there are multiple values of *K* supported for a given MMA variant. Otherwise, if *K* can be uniquely determined as per the [Table 48](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-kind-shapes), then the instruction descriptor bit corresponding to *K* must be set to 0.

<a id="tcgen05-data-movement-shape"></a>
## 9.7.18.2.3. Data Movement Shape

The data movement shape indicates the dimension of the data to be moved to or from the [Tensor Memory](../../instructions/18-tensorcore-5th-generation-family-instructions/01-tensor-memory.md#tensor-memory). These shapes are described as a tuple `lane`` ``x`` ``size` where:

- `lane` indicates the number of rows in the [Tensor Memory](../../instructions/18-tensorcore-5th-generation-family-instructions/01-tensor-memory.md#tensor-memory); and

- `size` indicates the amount of data, in units of bits (b), across the columns in the [Tensor Memory](../../instructions/18-tensorcore-5th-generation-family-instructions/01-tensor-memory.md#tensor-memory).

The following shapes are supported by various tcgen05 operations:

| Shape | tcgen05.\<op\> |
|----|----|
| `.16x64b`, `.16x128b`, `.16x256b`, `.16x32bx2`, `.32x32b` | `.ld` / `.st` |
| `.4x256b`, `.32x128b`, `.64x128b`, `.128x256b`, `.128x128b` | `.cp` |
| `.31x256b` (implicit) | `.shift` |

<a id="tcgen05-memory-layout"></a>
### 9.7.18.2.3.1. Memory Layout

The following shows the layout of the matrix fragments across threads of the warp.

9.7.18.2.3.1.1. [Matrix fragments for shape .32x32b](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-matrix-fragments-shape-3232b)[](#tcgen05-matrix-fragments-shape-3232b "Permalink to this headline")

A `tcgen05{.ld,.st}.32x32b` instruction has the following data vector register.

| Fragment | Elements (low to high) |
|----|----|
| A vector expression containing `.num` number of `.b32` registers as mentioned in the [Table 59](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-num-shapes-ld). | r0, r1, … |

A warp executing `tcgen05{.ld,.st}.32x32b` will access 32 lanes of the Tensor Memory. It loads from or stores to each of the lane (32 \* .num)-bits of data as shown in [Figure 186](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-mma-fragment-3232b).

![](https://docs.nvidia.com/cuda/parallel-thread-execution/_images/tcgen05-mma-fragment-3232b.png)

Figure 186 Matrix Fragment for shape .32x32b[](#tcgen05-mma-fragment-3232b "Permalink to this image")

9.7.18.2.3.1.2. [Matrix fragments for shape .16x64b](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-matrix-fragments-shape-6464b)[](#tcgen05-matrix-fragments-shape-6464b "Permalink to this headline")

A `tcgen05{.ld,.st}.16x64b` instruction has the following data vector register.

| Fragment | Elements (low to high) |
|----|----|
| A vector expression containing `.num` number of `.b32` registers as mentioned in the [Table 59](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-num-shapes-ld). | r0, r1, … |

A warp executing `tcgen05{.ld,.st}.16x64b` will access 16 lanes of the Tensor Memory. It loads from or stores to each of the lane (64 \* .num)-bits of data as shown in [Figure 187](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-mma-fragment-1664b).

![](https://docs.nvidia.com/cuda/parallel-thread-execution/_images/tcgen05-mma-fragment-1664b.png)

Figure 187 Matrix Fragment for shape .16x64b[](#tcgen05-mma-fragment-1664b "Permalink to this image")

9.7.18.2.3.1.3. [Matrix fragments for shape .16x128b](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-matrix-fragments-shape-16128b)[](#tcgen05-matrix-fragments-shape-16128b "Permalink to this headline")

A `tcgen05{.ld,.st}.16x128b` instruction has the following data vector register.

| Fragment | Elements (low to high) |
|----|----|
| A vector expression containing `.num` number of `.b32` registers as mentioned in the [Table 59](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-num-shapes-ld). | r0, r1, … |

A warp executing `tcgen05{.ld,.st}.16x128b` will access 16 lanes of the Tensor Memory. It loads from or stores to each of the lane (128 \* .num)-bits of data as shown in [Figure 188](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-mma-fragment-16128b).

![](https://docs.nvidia.com/cuda/parallel-thread-execution/_images/tcgen05-mma-fragment-16128b.png)

Figure 188 Matrix Fragment for shape .16x128b[](#tcgen05-mma-fragment-16128b "Permalink to this image")

9.7.18.2.3.1.4. [Matrix fragments for shape .16x256b](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-matrix-fragments-shape-16256b)[](#tcgen05-matrix-fragments-shape-16256b "Permalink to this headline")

A `tcgen05{.ld,.st}.16x256b` instruction has the following data vector register.

| Fragment | Elements (low to high) |
|----|----|
| A vector expression containing `.num` number of `.b32` registers as mentioned in the [Table 59](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-num-shapes-ld). | r0, r1, r2, r3, … |

A warp executing `tcgen05{.ld,.st}.16x256b` will access 16 lanes of the Tensor Memory. It loads from or stores to each of the lane (256 \* .num)-bits of data as shown in [Figure 189](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-mma-fragment-16256b).

![](https://docs.nvidia.com/cuda/parallel-thread-execution/_images/tcgen05-mma-fragment-16256b.png)

Figure 189 Matrix Fragment for shape .16x256b[](#tcgen05-mma-fragment-16256b "Permalink to this image")

9.7.18.2.3.1.5. [Matrix fragments for shape .16x32bx2](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-matrix-fragments-shape-1632b2)[](#tcgen05-matrix-fragments-shape-1632b2 "Permalink to this headline")

A `tcgen05{.ld,.st}.16x32bx2` instruction has the following data vector register.

| Fragment | Elements (low to high) |
|----|----|
| A vector expression containing `.num` number of `.b32` registers as mentioned in the [Table 59](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-num-shapes-ld). | r0, r1, … |

A warp executing `tcgen05{.ld,.st}.16x32bx2` will access 16 lanes of the Tensor Memory. It loads from or stores to each of the lane (32 \* .num)-bits of data as shown in [Figure 190](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-mma-fragment-1632b2).

![](https://docs.nvidia.com/cuda/parallel-thread-execution/_images/tcgen05-mma-fragment-1632b2.png)

Figure 190 Matrix Fragment for shape .16x32bx2[](#tcgen05-mma-fragment-1632b2 "Permalink to this image")

