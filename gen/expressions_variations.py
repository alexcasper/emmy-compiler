"""Hidden-set-style VARIATIONS of the five categories, for transform
generalization testing. Generated with the tracer (emmy compile -c), never
submitted: test/bench oracle use only (AGENTS.md testing exception)."""
import numpy as np

REDUCE_KNOBS = "WORK=t128,REDUCE=coop"


def _softmax(x, axis=-1):
    m = x.max(axis=axis, keepdims=True)
    e = np.exp(x - m)
    return e / e.sum(axis=axis, keepdims=True)


VARIATIONS = [
    # category 1: pointwise, different size + op mix
    dict(id="gp1_pointwise_8192",
         code="x = torch.randn(8192); y = torch.randn(8192); torch.relu(x - 0.25) * y + 1.0",
         ref=lambda x, y: [(np.maximum(x - np.float32(0.25), 0) * y + np.float32(1.0)).astype(np.float32)],
         rtol=0, atol=0),
    # category 2: reductions, different shapes
    dict(id="gr1_rows_32x1024",
         code="torch.randn(32, 1024).sum(-1)",
         ref=lambda x: [x.astype(np.float64).sum(-1).astype(np.float32)],
         rtol=1e-4, atol=1e-4, knobs=REDUCE_KNOBS),
    dict(id="gr2_sum_131072",
         code="torch.randn(131072).sum()",
         ref=lambda x: [x.astype(np.float64).sum().astype(np.float32)],
         rtol=1e-3, atol=1e-3, knobs=REDUCE_KNOBS),
    # category 3: matmul, different aspect ratios
    dict(id="gm1_matmul_256",
         code="torch.randn(256, 512) @ torch.randn(512, 256)",
         ref=lambda a, b: [(a.astype(np.float64) @ b.astype(np.float64)).astype(np.float32)],
         rtol=1e-3, atol=1e-3),
    dict(id="gm2_matmul_skinny",
         code="torch.randn(64, 1024) @ torch.randn(1024, 64)",
         ref=lambda a, b: [(a.astype(np.float64) @ b.astype(np.float64)).astype(np.float32)],
         rtol=1e-3, atol=1e-3),
    # category 4: fused, different shapes
    dict(id="gf1_rmsnorm_32x2048",
         code="x = torch.randn(32, 2048); w = torch.randn(2048); "
              "x / torch.sqrt((x * x).mean(-1, keepdim=True) + 1e-5) * w",
         ref=lambda x, w: [(x / np.sqrt((x.astype(np.float64) ** 2).mean(-1, keepdims=True) + 1e-5)
                            * w).astype(np.float32)],
         rtol=1e-3, atol=1e-4),
    dict(id="gf2_softmax_128x128",
         code="torch.softmax(torch.randn(128, 128), dim=-1)",
         ref=lambda x: [_softmax(x.astype(np.float64)).astype(np.float32)],
         rtol=1e-3, atol=1e-5),
    # category 5: attention, different head sizes
    dict(id="ga1_attention_32x128",
         code="q = torch.randn(32, 128); kt = torch.randn(128, 32); v = torch.randn(32, 32); "
              "torch.softmax(q @ kt / 11.313708, dim=-1) @ v",
         ref=lambda q, kt, v: [(_softmax((q.astype(np.float64) @ kt.astype(np.float64)) / 11.313708)
                                @ v.astype(np.float64)).astype(np.float32)],
         rtol=1e-3, atol=1e-4),
    dict(id="ga2_attention_96x16",
         code="q = torch.randn(96, 16); kt = torch.randn(16, 96); v = torch.randn(96, 16); "
              "torch.softmax(q @ kt / 4.0, dim=-1) @ v",
         ref=lambda q, kt, v: [(_softmax((q.astype(np.float64) @ kt.astype(np.float64)) / 4.0)
                                @ v.astype(np.float64)).astype(np.float32)],
         rtol=1e-3, atol=1e-4),
    # ---- transform stress cases: non-power-of-2 shapes stress pow2_shift's
    # non-negative index assumption and unroll divisibility fallbacks ----
    dict(id="gx1_pointwise_333",
         code="torch.randn(333) * 2.0 + 1.0",
         ref=lambda x: [(x * np.float32(2.0) + np.float32(1.0)).astype(np.float32)],
         rtol=0, atol=0),
    dict(id="gx2_sum_100000",
         code="torch.randn(100000).sum()",
         ref=lambda x: [x.astype(np.float64).sum().astype(np.float32)],
         rtol=1e-3, atol=1e-3, knobs=REDUCE_KNOBS),
    dict(id="gx3_matmul_233",
         code="torch.randn(233, 448) @ torch.randn(448, 233)",
         ref=lambda a, b: [(a.astype(np.float64) @ b.astype(np.float64)).astype(np.float32)],
         rtol=1e-3, atol=1e-3),
    dict(id="gx4_softmax_100x300",
         code="torch.softmax(torch.randn(100, 300), dim=-1)",
         ref=lambda x: [_softmax(x.astype(np.float64)).astype(np.float32)],
         rtol=1e-3, atol=1e-5),
]
