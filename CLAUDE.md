# monkquant

A quantization toolkit built from scratch: compress numbers to fewer bits with minimal accuracy loss, and
measure exactly what the trade costs. One shared compression core, many surfaces. Built in two stages — the
textbook baselines (v1), then the 2026 frontier methods (v2). This file is the entry point for any new
session working in this repo.

## Reading order for a new session

1. **This file** — what monkquant is and how we work on it.
2. **[docs/roadmap/index.md](./docs/roadmap/index.md)** — the phased plan; start with the current phase
   ([v1](./docs/roadmap/v1-vector-quantization.md)).
3. **[knowledge/](./knowledge)** — the course that teaches every concept the codec is built on. If writing
   or editing course content, read **[knowledge/AUTHORING.md](./knowledge/AUTHORING.md)** first.

## Collaboration mode (the rule that overrides convenience)

- **v1 is learn-by-building.** The implementation is written by hand, by Sameer. The assistant is a teacher
  and reviewer: guide the theory and the stack, explain plain-English-first then the precise term, scaffold,
  ask Socratic questions, review code, unblock. **The assistant does not write the codec's implementation in
  v1.** numpy is allowed for array arithmetic, but the quantization logic — the int8 mapping, the codebooks,
  the distance estimator — is written by hand, never delegated.
- **The course teaches concepts, never the implementation.** `knowledge/` explains how product quantization
  works (the algorithm, the math, worked examples) but never ships the codec's code. See `knowledge/AUTHORING.md`.
- **v2 is pairing.** Once v1 is done, the research-heavy v2 work (TurboQuant, RaBitQ, the head-to-head and
  the written verdict) is collaborative, code included.

## Scope (locked) — codec, not search

monkquant compresses vectors and grades the loss. It does **not** build a search index. The vector surface
here and the future **Vector Search** project share exactly one piece — vector compression — and the
decision is: build it once, here, and have Vector Search import it later. v1's recall benchmark needs no
index at all (brute-force exact search isolates codec quality); the HNSW/IVF graph is Vector Search's job.
See the workspace planning docs (`projects/quantization-toolkit-plan.md`, `project-decisions.md` decision #8).

## Repository layout

```
monkquant/                 a uv workspace; root pyproject holds shared dev tooling
├── packages/
│   └── codec/             monkquant — the v1 codec (numpy; written by hand)
│       └── src/monkquant/
│           ├── core/      target-agnostic squashers: scalar, kmeans, pq
│           └── surface/   adapters; v1 = vectors (codec + asymmetric distance + recall)
├── examples/              dataset download, benchmark, plot; example-only deps live here
├── knowledge/             the learning course — Astro site, deployed to GitHub Pages
├── docs/roadmap/          phased plan: index + per-phase files
└── public/                brand assets (logo, wordmark)
```

The `core/` is target-agnostic on purpose: a future surface (KV cache, weights) reuses it untouched. The
dataset loading and the plot (h5py, matplotlib) live only in `examples/`, never in the codec.

## Quality bars

- **No hallucinated facts.** Verify method names, paper claims, and numbers against primary sources before
  they reach the README, docs, or course. The headline TurboQuant numbers (6x, "beats FAISS 10-19%") are
  from vendor blogs / repo READMEs, not the primary paper — flag them until verified.
- **Senior-repo bar.** A phase is done with tests (the recall check, the reconstruction check), a benchmark
  or plot that tells a story, a real README, and honest notes on what's left — not just "it runs."
- **The recall-vs-compression curve is the key artifact.** v1 is not done until that plot exists for int8
  and PQ on a real dataset.

## Working with the knowledge site

```bash
cd knowledge
bun install
bun run dev      # local dev at /monkquant/
bun run build    # static build into knowledge/dist (what Pages deploys)
```

The site is served under the `/monkquant/` base path. Brand assets live in `knowledge/public/` (Astro
serves that directory). Animations follow the policy in `knowledge/AUTHORING.md`.

## Stack

- **Knowledge site:** Astro + Tailwind + GSAP, built with bun.
- **Codec:** Python, managed as a uv workspace. v1 (`monkquant`) uses numpy for array math only. Dev
  tooling: uv, pytest, ruff. Run from the repo root: `uv sync`, `uv run pytest`, `uv run ruff check`.
- **Examples:** h5py (ANN-benchmark datasets) and matplotlib, isolated in `examples/`.
