# v2 — TurboQuant vs RaBitQ

v2 is the research stage and the paper bet. It implements the 2026 frontier quantizers, benchmarks them
head-to-head against the v1 baseline on the same plot, and takes a written position on a live, named debate.
This is collaborative work — pairing, code included — because it is research-heavy.

## Goal

Three more curves on v1 Phase 5's axes (recall@k vs compression): TurboQuant, Extended RaBitQ, and the v1
PQ baseline, on the same GloVe + OpenAI datasets, plus a written verdict on whether TurboQuant is genuinely
novel versus RaBitQ. The bar to clear is public: match or beat the strong baselines on recall-at-compression
and say honestly where each wins.

## Collaboration mode

Pairing. Co-writing code is fine here. The quality bar rises: clean baselines, honest negative results,
reproducible benchmarks. If a result is novel and reproducible, aim a writeup at a workshop.

## The methods (to be verified against primary sources before any public claim)

- **TurboQuant** (Zandieh, Daliri, Hadian, Mirrokni — Google Research; arXiv:2504.19874, ICLR 2026).
  Data-oblivious: random-rotate the vector so coordinates concentrate, apply an optimal per-coordinate
  scalar quantizer, then a 1-bit residual correction for an unbiased inner-product estimate. Reported
  near-optimal MSE distortion (within ~2.7× of the information-theoretic lower bound).
- **Extended RaBitQ** (Gao & Long; follow-on to RaBitQ, SIGMOD 2024 / 2025). Generalizes 1-bit RaBitQ to B
  bits per dimension with a theoretical error bound. Already shipped in Milvus and Elasticsearch ("BBQ").
- **The baseline:** v1's product quantization, the 13-year incumbent (Jégou et al., 2011).

## The debate (the senior hook)

RaBitQ's first author, Jianyang Gao, has publicly questioned whether TurboQuant is genuine innovation or
substantially builds on his prior work. The debate is unresolved. A toolkit that implements both, benchmarks
them head-to-head, and writes a reasoned verdict is contributing to an open argument, not doing a tutorial.

## Milestones (sketch — detailed when v1 lands)

`[ ]` not started · `[~]` in progress · `[x]` done

- `[ ]` **1. TurboQuant on vectors** — random rotation, optimal scalar quantizer, 1-bit residual correction.
- `[ ]` **2. Extended RaBitQ** — B-bit quantization with the asymmetric estimator and re-ranking.
- `[ ]` **3. The head-to-head** — all three on the v1 plot; same datasets, same recall@k, honest per-method
  notes on where each wins.
- `[ ]` **4. The verdict** — a written position on the novelty debate, grounded in the benchmark and the
  primary papers.
- `[ ]` **5. New surfaces** — point the same core at the LLM KV cache (compare vs KIVI / KVQuant on
  LongBench / RULER), then model weights. Each reuses `core/` through a new `surface/` adapter.

## Verification flags (no-hallucination gate)

The headline numbers — "6× memory", "beats FAISS by 10–19%", "99.5% fidelity", the chip-stock impact — are
from vendor blogs and repo READMEs, **not** the primary paper. Every such number is re-confirmed from the
primary source (or dropped / marked "reportedly") before it reaches the README, docs, course, or any post.

## Sources

- TurboQuant: https://arxiv.org/abs/2504.19874
- TurboQuant vs RaBitQ debate writeup: https://milvus.io/blog/turboquant-rabitq-vector-database-cost.md
- Extended RaBitQ: https://github.com/VectorDB-NTU/Extended-RaBitQ
- turbovec (TurboQuant for vector search, Rust): https://github.com/RyanCodrai/turbovec
- FAISS (product quantization reference): https://github.com/facebookresearch/faiss
