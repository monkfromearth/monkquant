# examples

Everything that uses the codec but is not the codec: dataset download, the benchmark run, and the
plot. Example-only dependencies (h5py for the ANN-benchmark files, matplotlib for the curve) live
here so the `monkquant` package itself stays numpy-only.

Planned (built in Phase 5, see [docs/roadmap/v1-vector-quantization.md](../docs/roadmap/v1-vector-quantization.md)):

- **datasets** — fetch `glove-100-angular` (1.18M vectors, d=100) and the OpenAI DBpedia set
  (d=1536) in the standard ANN-benchmark HDF5 layout (train / test / ground-truth neighbours).
- **benchmark** — compress with int8 and PQ, score recall@10 against exact ground truth, record
  compression ratio.
- **plot** — the artifact: recall@10 vs compression ratio, int8 as a point, PQ as a curve.

Downloaded data and generated plots are git-ignored (`examples/data/`, `examples/out/`).
