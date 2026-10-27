<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="introduction"></a>
# 1. Introduction

This document describes PTX, a low-level *parallel thread execution* virtual machine and instruction set architecture (ISA). PTX exposes the GPU as a data-parallel computing *device*.

<a id="scalable-data-parallel-computing-using-gpus"></a>
## 1.1. Scalable Data-Parallel Computing using GPUs

Driven by the insatiable market demand for real-time, high-definition 3D graphics, the programmable GPU has evolved into a highly parallel, multithreaded, many-core processor with tremendous computational horsepower and very high memory bandwidth. The GPU is especially well-suited to address problems that can be expressed as data-parallel computations - the same program is executed on many data elements in parallel - with high arithmetic intensity - the ratio of arithmetic operations to memory operations. Because the same program is executed for each data element, there is a lower requirement for sophisticated flow control; and because it is executed on many data elements and has high arithmetic intensity, the memory access latency can be hidden with calculations instead of big data caches.

Data-parallel processing maps data elements to parallel processing threads. Many applications that process large data sets can use a data-parallel programming model to speed up the computations. In 3D rendering large sets of pixels and vertices are mapped to parallel threads. Similarly, image and media processing applications such as post-processing of rendered images, video encoding and decoding, image scaling, stereo vision, and pattern recognition can map image blocks and pixels to parallel processing threads. In fact, many algorithms outside the field of image rendering and processing are accelerated by data-parallel processing, from general signal processing or physics simulation to computational finance or computational biology.

*PTX* defines a virtual machine and ISA for general purpose parallel thread execution. PTX programs are translated at install time to the target hardware instruction set. The PTX-to-GPU translator and driver enable NVIDIA GPUs to be used as programmable parallel computers.

<a id="goals-of-ptx"></a>
## 1.2. Goals of PTX

*PTX* provides a stable programming model and instruction set for general purpose parallel programming. It is designed to be efficient on NVIDIA GPUs supporting the computation features defined by the NVIDIA Tesla architecture. High level language compilers for languages such as CUDA and C/C++ generate PTX instructions, which are optimized for and translated to native target-architecture instructions.

The goals for PTX include the following:

- Provide a stable ISA that spans multiple GPU generations.

- Achieve performance in compiled applications comparable to native GPU performance.

- Provide a machine-independent ISA for C/C++ and other compilers to target.

- Provide a code distribution ISA for application and middleware developers.

- Provide a common source-level ISA for optimizing code generators and translators, which map PTX to specific target machines.

- Facilitate hand-coding of libraries, performance kernels, and architecture tests.

- Provide a scalable programming model that spans GPU sizes from a single unit to many parallel units.

<a id="ptx-isa-version-8-8"></a>
## 1.3. PTX ISA Version 8.8

PTX ISA version 8.8 introduces the following new features:

- Adds support for `sm_103` target architecture.

- Adds support for target `sm_103a` that supports architecture-specific features.

- Adds support for `sm_121` target architecture.

- Adds support for target `sm_121a` that supports architecture-specific features.

- Introduces family-specific target architectures that are represented with “f” suffix. PTX for family-specific targets is compatible with all subsequent targets in same family. Adds support for `sm_100f`, `sm_101f`, `sm_103f`, `sm_120f`, `sm_121f`.

- Extends `min` and `max` instructions to support three input arguments.

- Extends `tcgen05.mma` instruction to add support for new `scale_vectorsize` qualifiers `.block16` and `.block32` and K dimension 96.

- Extends `.field3` of `tensormap.replace` instruction to support 96B swizzle mode.

- Adds support for `tcgen05.ld.red` instruction.

- Extends `ld`, `ld.global.nc` and `st` instructions to support 256b load/store operations.

- Following table shows the list of features that are supported on family-specific targets:

  | Feature | Supported targets |
  |----|----|
  | `.m16n8`, `.m16n16`, `.m8n16` shapes and `.b8` type for `ldmatrix`/`stmatrix` | `sm_100f`, `sm_101f`, `sm_120f` |
  | Shapes for `tcgen05` `.16x64b` `.16x128b`, `.16x256b`, `.16x32bx2`, `.32x32b`, `.4x256b`, `.32x128b`, `.64x128b`, `.128x256b`, `.128x128b`, `.31x256b` | `sm_100f`, `sm_101f` |
  | `setmaxnreg` | `sm_100f`, `sm_101f`, `sm_120f` |
  | `.cta_group` modifier | `sm_100f`, `sm_101f` |
  | `cvt` with `.e2m1x2`, `.e3m2x2`, `.e2m3x2`, `.ue8m0x2` | `sm_100f`, `sm_101f`, `sm_120f` |
  | `multimem` with `.acc::f16` and `.e5m2`, `.e5m2x2`, `.e5m2x4`, `.e4m3`, `.e4m3x2`, `.e4m3x4` types | `sm_100f`, `sm_101f` |
  | `tensormap.replace` | `sm_100f`, `sm_101f`, `sm_120f` |
  | `tcgen05.ld.red` | `sm_101f`, `sm_103f` |
  | `tcgen05.ld`/`st`/`fence`/ `wait`/`commit`/`cp`/ `alloc`/`dealloc`/ `relinquish_alloc_permit` | `sm_100f`, `sm_101f` |
  | `tcgen05.mma{.ws}{.sp}` (except `kind::mxf4`/ `kind::mxf4nvf4` for `.sp`) | `sm_100f`, `sm_101f` |
  | `tcgen05` `.kind::mxf4nvf4`, `.kind::mxf4`, `.kind::mxf8f6f4`, `.kind::f16`, `.kind::tf32`, `.kind::f8f6f4` | `sm_100f`, `sm_101f` |
  | `.ashift`, `.collector_usage` modifiers for `tcgen05` | `sm_100f`, `sm_101f` |
  | Modifiers `.b8x16`, `.b6x16_p32`, `.b4x16_p64` | `sm_100f`, `sm_101f`, `sm_120f` |
  | `.block_scale` modifier | `sm_100f`, `sm_101f`, `sm_120f` |
  | `mma{.sp}` with `.e3m2`, `.e2m3`, `.e2m1` types and `.kind`, `.block_scale`, `.scale_vec_size` modifiers (except `.sp` with `mxf4`/ `mxf4nvf4`) | `sm_120f` |
  | `.scale_vec::1X`/`2X`/`4X` modifiers | `sm_120f` |
  | `.block16`/`.block32` modifiers (alias to `scale_vec`) | `sm_100f`, `sm_101f` |
  | `.warpx2::02_13`, `.warpx2::01_23`, `.warpx4`, `.pack::16b`, `.unpack::16b` modifiers for `tcgen05` | `sm_100f`, `sm_101f` |
  | `clusterlaunchcontrol.try_cancel` `multicast::cluster::all` | `sm_100f`, `sm_101f`, `sm_120f` |
  | `.tile::scatter4`, `.tile::gather4`, `.im2col::w`, `.im2col::w::128` | `sm_100f`, `sm_101f` |
  | `redux.f32` | `sm_100f` |
  | `scale-input-d` for `tcgen05` | `sm_100f` |

  Table 1 List of features promoted to family-specific architecture[](#id666 "Permalink to this table") {#id666}

<a id="document-structure"></a>
## 1.4. Document Structure

The information in this document is organized into the following Chapters:

- [Programming Model](02-programming-model.md#programming-model) outlines the programming model.

- [PTX Machine Model](03-ptx-machine-model.md#ptx-machine-model) gives an overview of the PTX virtual machine model.

- [Syntax](04-syntax.md#syntax) describes the basic syntax of the PTX language.

- [State Spaces, Types, and Variables](05-state-spaces-types-and-variables.md#state-spaces-types-and-variables) describes state spaces, types, and variable declarations.

- [Instruction Operands](06-instruction-operands.md#instruction-operands) describes instruction operands.

- [Abstracting the ABI](07-abstracting-the-abi.md#abstracting-abi) describes the function and call syntax, calling convention, and PTX support for abstracting the *Application Binary Interface (ABI)*.

- [Instruction Set](09-instruction-set.md#instruction-set) describes the instruction set.

- [Special Registers](10-special-registers.md#special-registers) lists special registers.

- [Directives](11-directives.md#directives) lists the assembly directives supported in PTX.

- [Release Notes](13-release-notes.md#release-notes) provides release notes for PTX ISA versions 2.x and beyond.

References

- 754-2008 IEEE Standard for Floating-Point Arithmetic. ISBN 978-0-7381-5752-8, 2008.

  [http://ieeexplore.ieee.org/servlet/opac?punumber=4610933](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933)

- The OpenCL Specification, Version: 1.1, Document Revision: 44, June 1, 2011.

  [http://www.khronos.org/registry/cl/specs/opencl-1.1.pdf](http://www.khronos.org/registry/cl/specs/opencl-1.1.pdf)

- CUDA Programming Guide.

  [https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)

- CUDA Dynamic Parallelism Programming Guide.

  [https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#cuda-dynamic-parallelism](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#cuda-dynamic-parallelism)

- CUDA Atomicity Requirements.

  [https://nvidia.github.io/cccl/libcudacxx/extended_api/memory_model.html#atomicity](https://nvidia.github.io/cccl/libcudacxx/extended_api/memory_model.html#atomicity)

- PTX Writers Guide to Interoperability.

  [https://docs.nvidia.com/cuda/ptx-writers-guide-to-interoperability/index.html](https://docs.nvidia.com/cuda/ptx-writers-guide-to-interoperability/index.html)

