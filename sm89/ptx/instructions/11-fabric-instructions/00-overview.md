<!-- Generated from https://docs.nvidia.com/cuda/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="fabric-instructions"></a>
# 9.7.11. Fabric Instructions

*NVLink* failures encountered by pointer-address-based memory operations are fatal to the application. The CUDA Compute Fabric Transport (CUDA CFT) programming model introduces fabric operations that report failures directly to the application, enabling them to be resilient over *NVLink* failures. How to handle these failures is entirely up to the application and may include aborting or cleanly tearing the process down, or attempting to recover from transient failures by retrying the operation.

Refer to the [Logical Endpoint section of the CUDA Driver API](https://docs.nvidia.com/cuda/cuda-driver-api/group__CUDA__LOGICAL__ENDPOINT.html#logical-endpoint) for the host-side programming model.

