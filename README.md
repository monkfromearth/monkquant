<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./public/logo-wordmark-dark.svg" />
    <img src="./public/logo-wordmark.svg" alt="monkquant" width="420" />
  </picture>

  <p><strong>A quantization toolkit built from scratch.</strong></p>

  <p>Store numbers in fewer bits, lose as little accuracy as possible, and measure exactly what the trade costs.</p>

  <p>
    <a href="https://monkfromearth.github.io/monkquant/learn">Course</a> ·
    <a href="https://monkfromearth.github.io/monkquant/docs">Docs</a> ·
    <a href="./docs/roadmap/index.md">Roadmap</a>
  </p>
</div>

---

## What this is

monkquant is a quantization toolkit built from the ground up to make one thing concrete: how much memory
you can save by storing numbers in fewer bits, and exactly how much accuracy that costs. AI systems are
giant piles of numbers (a single embedding is hundreds or thousands of them); if each number fits in a few
bits instead of 32, the data shrinks four to sixty times and still answers almost as well. monkquant builds
the squashing machine from scratch and, just as importantly, the ruler that measures the loss.

The design is one shared compression **core** with **surface** adapters. The core knows nothing about what
it is compressing; a surface points it at a target. v1 ships the easiest, most measurable target — search
vectors — because the quality metric there is clean: recall against exact results, plotted versus the
compression ratio. The same core later points at other targets (an LLM's KV cache, model weights).

## What's different

- **A library, not a search engine.** monkquant compresses and grades; it does not search. That keeps the
  core honest and reusable. A separate Vector Search project imports this codec rather than reinventing it.
- **The ruler is the artifact.** The deliverable is the recall-vs-compression curve on a real embedding
  dataset, not "it compresses." You can read off what every memory budget actually costs you in accuracy.
- **Taught, not just shipped.** A full interactive course ships *with* the code. It teaches the concepts —
  scalar quantization, k-means, product quantization, asymmetric distance — and leaves the implementation
  to you, which is where the understanding sticks. It never hands you the codec's source.
- **A real path to the frontier.** v1 is the textbook baselines (int8, product quantization). v2 climbs to
  the 2026 methods (TurboQuant, Extended RaBitQ) and benchmarks them head-to-head against that baseline on
  the same plot, with a written verdict on the live novelty debate.

## The two stages

| Stage | What it is | Status |
| ----- | ---------- | ------ |
| **v1 — Vector Quantization** | Scalar int8, then product quantization, and a recall-vs-compression benchmark on GloVe and OpenAI embeddings. Small in lines, deep in ideas. | In progress |
| **v2 — TurboQuant vs RaBitQ** | The 2026 methods (random rotation + residual correction; Extended RaBitQ) benchmarked head-to-head against the v1 baseline, plus new surfaces (KV cache, weights). | Planned |

Full detail: [docs/roadmap/](./docs/roadmap/index.md).

## Tech stack

| Part | Stack |
| ---- | ----- |
| **`monkquant` (v1)** | Python + **numpy** — numpy does the array arithmetic, the quantization itself is written by hand. Dev tooling: [uv](https://docs.astral.sh/uv/), pytest, ruff. |
| **Examples** | h5py (ANN-benchmark datasets) and matplotlib, isolated in `examples/` so the codec stays numpy-only. |
| **Knowledge course** | [Astro](https://astro.build) + [Tailwind CSS](https://tailwindcss.com) + [GSAP](https://gsap.com), built with [bun](https://bun.sh). Deployed to GitHub Pages. |

## Learn it: the course

The [`knowledge/`](./knowledge) folder is an interactive course that teaches the concepts behind monkquant,
with animated demos. It is live at **[monkfromearth.github.io/monkquant](https://monkfromearth.github.io/monkquant/)**.

Run it locally:

```bash
cd knowledge
bun install
bun run dev      # http://localhost:4321/monkquant/
```

## Repository layout

```
monkquant/
├── packages/
│   └── codec/         monkquant — the v1 codec (numpy; written by hand)
│       └── src/monkquant/
│           ├── core/      target-agnostic squashers: scalar, kmeans, pq
│           └── surface/   adapters; v1 = vectors (codec + asymmetric distance + recall)
├── examples/         dataset download, the benchmark run, the plot; example-only deps
├── knowledge/        the interactive course (Astro site) — concepts, not implementation
├── docs/roadmap/     phased plan: index + per-phase files
├── public/           brand assets (logo, wordmark)
└── pyproject.toml    uv workspace root + shared dev tooling (pytest, ruff)
```

Develop the codec:

```bash
uv sync            # create the env + install the workspace and dev tools
uv run pytest      # tests (recall + reconstruction checks live here once written)
uv run ruff check  # lint
```

## Status

Early. v1 is in active development; the codec is written by hand against the phased roadmap. Structure and
docs grow with the project.

## License

MIT (see [`LICENSE`](./LICENSE)).

---

<div align="center">
  <sub>Built by <a href="https://monkfrom.earth">Sameer Khan (@monkfromearth)</a> &middot; part of the <a href="https://github.com/monkfromearth">monk</a> family &middot; <a href="https://github.com/monkfromearth/monkquant">source</a></sub>
</div>
