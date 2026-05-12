# v1 — Vector Quantization

v1 builds the two textbook compressors (scalar int8, then product quantization) and the ruler that grades
them: a recall-vs-compression benchmark on a real embedding dataset. Small in lines (~300–500 of Python),
deep in ideas. It deliberately stops before any 2026 method — rotation, residual correction, RaBitQ all
belong to v2. The point of v1 is to feel the trade-off in your own hands and earn a clean baseline.

## Goal

A single plot — recall@10 on the y-axis, compression ratio on the x-axis — with int8 as a point and product
quantization as a curve, on GloVe and OpenAI embeddings. From it you can read what every memory budget costs
in accuracy. That plot is the artifact, and the exact frame v2 plugs into.

## Collaboration mode

Learn-by-building. The implementation is written by hand, by Sameer. The assistant teaches the math
(plain-English first, then the precise term), scaffolds, reviews, and unblocks, but does **not** write the
codec. numpy is allowed for array arithmetic; the quantization itself is written by hand.

## The phases

Ordered so the measuring stick exists before the compressors (recall is graded against exact ground truth,
so ground truth comes first) and so k-means is isolated on its own phase (the usual wall). Each phase ends
with a runnable checkpoint.

### Milestones

`[ ]` not started · `[~]` in progress · `[x]` done

- `[ ]` **Phase 0 — Data + the measuring stick.** Load `glove-100-angular` (1.18M vectors, d=100);
  unit-normalize so cosine closeness becomes plain Euclidean distance. Build brute-force exact nearest-k and
  a recall@k scorer over a query batch.
  **Checkpoint:** exact-vs-itself recall = **1.0** — the anchor point (1× compression, perfect recall).

- `[ ]` **Phase 1 — int8 scalar quantization.** Map each value's range onto 256 levels (1 byte): `scale =
  (max − min) / 255`; quantize, dequantize. Try per-vector vs per-dimension calibration. Run it through the
  Phase 0 scorer.
  **Checkpoint:** lands near **4× compression, ~0.97–0.99 recall@10**. (Numbers illustrative; yours come
  from the run.)

- `[ ]` **Phase 2 — k-means, isolated.** Lloyd's algorithm with k-means++ initialization (next centroid
  chosen with probability proportional to its squared distance from the nearest already-chosen centroid).
  Tested on its own before PQ depends on it.
  **Checkpoint:** on **toy 2D blobs** you generate, the centroids land dead-center in the blobs (plot it).

- `[ ]` **Phase 3 — Product quantization: the codebook.** Split each vector into M chunks; train k=256
  centroids per chunk position with Phase 2's k-means (a codebook per chunk). Encode a vector to M bytes
  (nearest centroid index per chunk); decode by stitching centroids back.
  **Checkpoint:** encode→decode **reconstruction error** is small and shrinks as M rises. Debug the codebook
  in isolation, separate from search.

- `[ ]` **Phase 4 — Asymmetric distance + the PQ curve.** The lookup-table estimator: keep the query
  full-precision, precompute its distance to all 256 centroids per chunk (a 256×M table), then any stored
  vector's distance = M table lookups summed. Feed the Phase 0 scorer; sweep M.
  **Checkpoint:** sweeping M yields a **(compression, recall@10) curve** — recall climbs as compression
  drops. The central trade-off, now visible.

- `[ ]` **Phase 5 — The artifact.** One plot: int8 as a point, PQ as a curve. Re-run on **OpenAI DBpedia**
  (d=1536) for the high-dim case. Short writeup: what you'd pick at each memory budget.
  **Checkpoint / v1 DONE:** the plot exists for both datasets, and you can state a true trade-off sentence
  per memory budget.

- `[ ]` **Phase 6 (optional) — Re-ranking.** PQ picks ~100 rough candidates, re-score them with exact
  distance, return top-10. Recall jumps for almost free. A "v1.5" polish; skip to close v1.

## Definition of done

The recall-vs-compression plot exists for **both** int8 and product quantization on **both** GloVe and
OpenAI embeddings; the recall@k scorer, the int8 round-trip, k-means (toy-data check), and PQ (reconstruction
check) all have hand-written tests; the README and a short results note state the trade-off honestly.

## Stack

- Python 3.11+, **numpy** for array arithmetic (the quantization is written by hand).
- Dev tooling: uv (workspace), pytest, ruff. Run from the repo root: `uv sync`, `uv run pytest`,
  `uv run ruff check`.
- Datasets and the plot use h5py and matplotlib, isolated in `examples/` — never in the codec.
- Datasets: `glove-100-angular` and OpenAI DBpedia, in the standard ANN-benchmark HDF5 layout (train / test
  / ground-truth neighbours).
