# monkquant Roadmap

The plan for building monkquant, in phases. Each stage has its own file with milestones, a definition of
done, and how we work on it. This index is the map; the phase files are the detail.

## The shape of the project

monkquant is built in two stages, beginner-first: build the textbook compressors to learn how the trade-off
works and earn a clean baseline, then climb to the 2026 frontier methods and benchmark them against that
baseline on the same plot.

| Stage | What it is | Status |
|-------|-----------|--------|
| [v1 — Vector Quantization](./v1-vector-quantization.md) | Scalar int8, then product quantization, and a recall-vs-compression benchmark on GloVe + OpenAI embeddings. Small in lines, deep in ideas. | In progress |
| [v2 — TurboQuant vs RaBitQ](./v2-turboquant-rabitq.md) | The 2026 methods benchmarked head-to-head against the v1 baseline, a written verdict on the novelty debate, then new surfaces (KV cache, weights). | Planned |

The seam between them is exactly **v1 Phase 5's plot**: v1 builds the axes and two baseline curves; v2 drops
three more curves onto the same axes and writes the argument.

## Packaging & structure

One repository, a [uv workspace](https://docs.astral.sh/uv/concepts/workspaces/) with the codec as its first
package:

- **`monkquant`** (`packages/codec/`) — the codec. numpy for array math; the quantization is written by
  hand. Inside, a target-agnostic `core/` (scalar, kmeans, pq) and a `surface/` adapter (v1 = vectors).

Keeping `core/` target-agnostic means the day a second surface arrives (KV cache, weights) it reuses the
core untouched. Example-only dependencies (h5py, matplotlib) live in `examples/`. Version line: `0.x` while
v1 is in development, `1.0` for the first release with the full benchmark.

## Scope (locked) — codec, not search

monkquant compresses and grades; it does not search. The vector surface here and the future **Vector
Search** project share one piece — vector compression — built once, here, and imported there. v1's recall
benchmark needs no search index; brute-force exact search isolates codec quality. See the workspace
planning docs (`projects/quantization-toolkit-plan.md`, `project-decisions.md` decision #8).

## Principles

1. **Beginner-first, then advanced.** v1 is the textbook version built to learn the fundamentals and earn a
   baseline. v2 is the researched, senior angle layered on top. Build v1 first.
2. **Concepts are taught; code is written by hand.** The [knowledge course](../../knowledge) teaches every
   concept. The implementation is written by Sameer, by hand — that is where the understanding sticks. See
   each phase's collaboration mode.
3. **Senior-repo bar.** A phase is not done at "it runs." It's done with tests (the recall check, the
   reconstruction check), a plot that tells a story, a real README, and honest notes on what's left.
4. **No hallucinated facts.** Exact method names, paper claims, and numbers are verified against primary
   sources before they reach the README, docs, or the course. The headline TurboQuant numbers are
   vendor-blog claims until confirmed from the paper.

## Status legend

`[ ]` not started · `[~]` in progress · `[x]` done

## Where this sits

monkquant is part of a larger from-scratch engineering portfolio. It is the **compress** side of an ML
trio (train / run / compress) and the compression layer a future Vector Search engine depends on. The
broader portfolio roadmap lives outside this repo, in the workspace planning docs.
