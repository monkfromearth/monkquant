"""monkquant — the from-scratch quantization codec (v1, learning edition).

Compress vectors to fewer bits, then estimate closeness from the squashed form. numpy does the
array arithmetic; the quantization itself is written by hand while working through the knowledge
course (see ../../knowledge). This package starts intentionally empty.

The structure mirrors the toolkit thesis: a target-agnostic `core/` (the squashers) and a
`surface/` adapter that points the core at a target (v1 = vectors).

Build order (see docs/roadmap/v1-vector-quantization.md):
    Phase 0  surface/vectors: brute-force exact nearest-k + recall@k scorer (the measuring stick)
    Phase 1  core/scalar: int8 quantize / dequantize
    Phase 2  core/kmeans: Lloyd's algorithm + k-means++ (tested in isolation on 2D blobs)
    Phase 3  core/pq: product quantization — split, train codebooks, encode, decode
    Phase 4  surface/vectors: asymmetric (lookup-table) distance estimator + the PQ curve
    Phase 5  examples/: the artifact — recall-vs-compression plot on GloVe + OpenAI
"""

__version__ = "0.1.0"
