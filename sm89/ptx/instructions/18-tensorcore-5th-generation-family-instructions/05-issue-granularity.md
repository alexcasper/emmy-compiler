<!-- Generated from https://docs.nvidia.com/cuda/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="tcgen05-issue-granularity"></a>
# 9.7.18.5. Issue Granularity

Each of the `tcgen05` operation has different requirements for the number of threads/warps that needs to issue them.

The following table lists the execution granularity requirements of each of the `tcgen05` operation:

[TABLE]

Table 55 Execution granularity requirements for tcgen05 operations[](#tcgen05-ops-execution-granularity "Permalink to this table") {#tcgen05-ops-execution-granularity}

The following example shows that:

- Before attempting to deallocate Tensor Memory, it suffices to ensure that there are no concurrent Tensor Memory accesses from the [Peer CTA](#tcgen05-peer-cta).

- Warps can immediately exit after deallocating Tensor Memory; no extra synchronization required.

| CTA0 Warp | CTA1 Warp |
|----|----|
| barrier.cluster.arrive; barrier.cluster.wait; tcgen05.dealloc.2cta.sync.aligned; exit; | barrier.cluster.arrive; barrier.cluster.wait; tcgen05.dealloc.2cta.sync.aligned; exit; |

Table 56 Example of deallocating Tensor Memory before CTA exit.[](#tcgen05-example-deallocate-before-exit "Permalink to this table") {#tcgen05-example-deallocate-before-exit}

This example uses a cluster barrier for illustration purposes but in practice other synchronization mechanisms are often used.

The following example illustrates a scenario in which the program exhibits non-deterministic behavior due to incorrect synchronization because `.dealloc` may or may not block:

| CTA0 Warp | CTA1 Warp |
|----|----|
| barrier.cluster.arrive; barrier.cluster.wait; tcgen05.dealloc.2cta.sync.aligned; exit; | tcgen05.dealloc.2cta.sync.aligned; barrier.cluster.arrive; barrier.cluster.wait; exit; |

Table 57 Example of non-determinstic hang due to incorrect synchronization[](#tcgen05-example-non-deterministic-deallocation-hang "Permalink to this table") {#tcgen05-example-non-deterministic-deallocation-hang}

<a id="tcgen05-cta-pair"></a>
## 9.7.18.5.1. CTA Pair

Any 2 CTAs within the cluster whose `%cluster_ctarank` differs by the last bit only is said to form a CTA pair.

Within a CTA pair, the CTA whose last bit in the `%cluster_ctarank` is:

- 0 is termed the even numbered CTA within the CTA pair.

- 1 is termed as the odd numbered CTA within the CTA pair.

Most of the `tcgen05` operations can either execute at a single CTA level granularity OR at a CTA pair level granularity. When a `tcgen05` operation is performed at CTA pair granularity, the Tensor Memory of both the CTAs within the CTA pair are accessed. The set of threads that need to issue the `tcgen05` operation is listed in the [Issue Granularity](#tcgen05-issue-granularity).

<a id="tcgen05-peer-cta"></a>
## 9.7.18.5.2. Peer CTA

The peer CTA of the odd CTA within the CTA pair is the even CTA in the same pair. Similarly, the peer CTA of the even CTA within the CTA pair is the odd CTA in the same pair.

