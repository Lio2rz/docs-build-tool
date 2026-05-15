"""Tests for package-level imports.

Verifies that the top-level docsbuildtool package can be imported successfully.
"""


def test_package_imports() -> None:
    """Tests that the docsbuildtool package imports without errors."""
    import docsbuildtool

    assert docsbuildtool is not None
