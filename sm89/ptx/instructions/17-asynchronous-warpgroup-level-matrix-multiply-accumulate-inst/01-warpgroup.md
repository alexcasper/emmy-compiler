<!-- Generated from https://docs.nvidia.com/cuda/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="asynchronous-warpgroup-level-matrix-instructions-warpgroup"></a>
# 9.7.17.1. Warpgroup

A warpgroup is a set of four contiguous warps such that the *warp-rank* of the first warp is a multiple of 4.

warp-rank of a warp is defined as:

    (%tid.x + %tid.y * %ntid.x  + %tid.z * %ntid.x * %ntid.y) / 32

