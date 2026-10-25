<!-- Generated from https://docs.nvidia.com/cuda/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="cft-handles"></a>
# 9.7.11.1. CFT Handles

A CUDA Fabric Transport Handle is composed of two objects:

- `leId`, a logical endpoint identifier: a 32-bit unsigned integer reference to a logical endpoint

- `off`, a resource offset: a 64-bit unsigned integer reference to a resource within the logical endpoint.

