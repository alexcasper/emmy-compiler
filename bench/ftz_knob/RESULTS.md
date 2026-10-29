# FTZ knob test — sm_120 silicon (rental-3, bench/sm120_hypotheses follow-up)

Box: RTX PRO 6000 Blackwell Server Edition (CC 12.0), CUDA 13.0, cupy 14.2.0
(timing-only protocol). Handoff 17:36 UTC, bench 17:46–17:55 UTC. Deterministic
in-kernel `%clock64` for micro (min=p50=p90 everywhere), CUDA events (60 reps)
for real kernels.

## Micro suite — the per-op tax (64-op dependent chains, cycles)

| op | .ftz | non-ftz | tax/op |
|---|---|---|---|
| rcp.approx | 1573 | 2857 | **+20.2** |
| lg2.approx | 1573 | 2856 | **+20.1** ← new: lg2 carries the full guard |
| sqrt.approx | 1573 | 2856 | **+20.0** |
| ex2.approx | 1573 | 1593 | +0.3 — **ex2 is guard-free** |

SASS ground truth (static, from the committed .ptx sources): non-ftz rcp/lg2/sqrt
each carry 2×FSETP + 2×FSEL + FMUL/FFMA around every MUFU; ftz forms emit bare
MUFU; ex2 emits bare MUFU in both forms. All four ftz variants time IDENTICALLY
(1573) — one MUFU latency (~20.3 cyc after subtracting the 4.27-cycle FADD), no
per-op differences across the family.

## Real kernels — end-to-end (60-rep CUDA events, µs)

| kernel | rn (default) | approx | approx.ftz |
|---|---|---|---|
| m01_matmul_512 | 22.11 | 22.11 | 21.95 |
| a02_attention_128 | 60.26 | 61.73 | 60.26 |
| a02_attention_128 + ex2.ftz patch | — | — | 60.16 |
| f02_row_softmax | 8.86 | — | 8.51 |
| r03_mean | 11.78 | 11.84 | 11.84 |

Static SASS for r03 (the only kernel with a live float divide): `rn` = MUFU3 +
FCHK + CALL + 6 FSETP (full IEEE apparatus); `approx` = MUFU1 + 1 FSETP;
**`approx.ftz` = MUFU1, zero guards**.

## Verdict

**Per-op: CONFIRMED** — the ~20-cycle non-ftz tax is real on rcp/lg2/sqrt (ex2
exempt). **End-to-end on the benchmark set: NO delta** — every kernel row is
within run noise of every other. Why: the benchmark kernels barely exercise
these ops — m01/a02 have zero float divides (their MUFUs are exp's ex2, which is
guard-free either way — the ex2ftz-patched a02 confirms: 60.16 vs 60.26 =
noise), and r03's divide runs **once per thread** after the reduction, so a
73→20-cycle op delta amortizes to nothing against a 32k-element loop.

**Decision:** keep `div/sqrt/rcp: rn` defaults (correctness-safe, no measurable
cost on the benchmark set). The ftz knob forms stay available for any future
kernel whose hot loop genuinely contains approx ops — where the ~20-cycle/op
tax WILL be real (bench/sm120_hypotheses/RESULTS.md quantifies it). sm_89 side:
infrastructure-blocked this session (Colab L4: 3 failure modes — VM reset,
split upload/exec VMs, silent upload loss; sessions destroyed); the sm_89 PTX
suite is committed and can JIT on any sm_120 host as an approximation row.

## Artifacts

- `lat120_*.ptx` — 8-op micro suite (both forms, sm_120 header)
- `rk_*.ptx` — 12 real-kernel variants (m01/a02/r03/f02 × knob settings + ex2ftz)
- `micro.py`, `suite120.py`, `rkonly.py`, `manifest120.json`, `rkmust.json`
- Meta note: m01/a02's div knob is a compile-time no-op (pow2_shift folds their
  divides to integer ops; zero float div sites survive) — the knob only matters
  where float division is runtime-valued (r03) or approx ops are explicit.
