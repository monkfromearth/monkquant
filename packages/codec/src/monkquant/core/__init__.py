"""core — the squashers, target-agnostic by design.

These know nothing about "vectors" or "search". They take numbers and store them in fewer bits.
The same core is reused unchanged the day a new surface (KV cache, weights) arrives.

Written by hand per the roadmap:
    scalar  int8 scalar quantization                 (Phase 1)
    kmeans  Lloyd's algorithm + k-means++            (Phase 2)
    pq      product quantization on top of kmeans    (Phase 3)
"""
