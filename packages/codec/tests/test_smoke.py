"""Smoke test: the package is importable. The real tests — recall@k against exact ground
truth, PQ reconstruction error shrinking as M rises, the int8 round-trip — get written by
hand as the codec is built (see docs/roadmap/v1-vector-quantization.md)."""


def test_package_imports():
    import monkquant

    assert monkquant.__version__
