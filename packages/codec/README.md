# monkquant (v1 — the codec)

The from-scratch quantization core behind monkquant — the **learning edition**.

It does one job: take vectors, store them in far fewer bits, and still estimate "how close are
these two?" accurately from the squashed form. It does **not** search — that is a separate concern
(a future Vector Search repo imports this codec). v1 compresses search vectors only; the same core
later points at other targets (KV cache, weights).

numpy does the array arithmetic. The quantization itself — the int8 mapping, the k-means codebooks,
the asymmetric distance estimator — is written by hand while working through the
[knowledge course](../../knowledge). That is where the understanding sticks. This package starts
intentionally empty.

## Layout (the toolkit thesis, made visible)

```
src/monkquant/
├── core/        surface-agnostic squashers (know nothing about "vectors" or "search")
│   ├── scalar   int8 scalar quantization
│   ├── kmeans   Lloyd's algorithm + k-means++ (used to train PQ codebooks)
│   └── pq        product quantization: split, codebook, encode, decode
└── surface/     adapters that point the core at a target
    └── vectors  the vector adapter: codec + asymmetric distance + recall@k
```

`core/` stays target-agnostic on purpose: the day a KV-cache surface arrives, it reuses `core/`
untouched.

## Develop

From the repo root (uv workspace):

```bash
uv sync                 # create the env, install the workspace and dev tools
uv run pytest           # run tests (the recall + reconstruction checks live here once written)
uv run ruff check .     # lint
uv run ruff format .    # format
```

Build order and definition of done: [docs/roadmap/v1-vector-quantization.md](../../docs/roadmap/v1-vector-quantization.md).
Dataset loading and the plot (matplotlib, h5py) belong in the repo's `examples/`, never in this codec.
