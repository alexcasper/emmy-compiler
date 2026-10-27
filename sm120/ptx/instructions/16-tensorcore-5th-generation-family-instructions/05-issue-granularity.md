<!-- Generated from https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html by tools/build_ptx.py; do not edit. -->

<a id="tcgen05-issue-granularity"></a>
# 9.7.16.5. Issue Granularity

Each of the `tcgen05` operation has different requirements for the number of threads/warps that needs to issue them.

The following table lists the execution granularity requirements of each of the `tcgen05` operation:

[TABLE]

Table 47 Execution granularity requirements for tcgen05 operations[](#tcgen05-ops-execution-granularity "Permalink to this table") {#tcgen05-ops-execution-granularity}

<a id="tcgen05-cta-pair"></a>
## 9.7.16.5.1. CTA Pair

Any 2 CTAs within the cluster whose `%cluster_ctarank` differs by the last bit only is said to form a CTA pair.

Within a CTA pair, the CTA whose last bit in the `%cluster_ctarank` is:

- 0 is termed the even numbered CTA within the CTA pair.

- 1 is termed as the odd numbered CTA within the CTA pair.

Most of the `tcgen05` operations can either execute at a single CTA level granularity OR at a CTA pair level granularity. When a `tcgen05` operation is performed at CTA pair granularity, the Tensor Memory of both the CTAs within the CTA pair are accessed. The set of threads that need to issue the `tcgen05` operation is listed in the [Issue Granularity](#tcgen05-issue-granularity).

<a id="tcgen05-peer-cta"></a>
## 9.7.16.5.2. Peer CTA

The peer CTA of the odd CTA within the CTA pair is the even CTA in the same pair. Similarly, the peer CTA of the even CTA within the CTA pair is the odd CTA in the same pair.

