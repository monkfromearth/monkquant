"""surface — adapters that point the core at a target.

A surface wraps a core squasher with the things that target needs. v1 ships one:

    vectors  the vector adapter: wrap a codec, add the asymmetric (lookup-table) distance
             estimator, and the brute-force recall@k measuring stick.   (Phases 0 + 4)

Future surfaces (KV cache, weights) live here too, each reusing core/ untouched.
"""
