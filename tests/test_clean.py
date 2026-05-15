"""Tests for the clean module.

Covers the clean_output function behavior for nonexistent, empty, and populated
output directories, as well as the CLI clean command.
"""

from pathlib import Path

from typer.testing import CliRunner

from docsbuildtool.clean import clean_output
from docsbuildtool.cli import app

# Reusable CLI test runner instance.
runner = CliRunner()


def test_clean_nonexistent(tmp_path: Path) -> None:
    """Tests that cleaning a nonexistent directory returns an empty list."""
    out = tmp_path / "nonexistent"
    removed = clean_output(str(out))
    assert removed == []


def test_clean_empty_output(tmp_path: Path) -> None:
    """Tests that cleaning an empty output directory returns an empty list."""
    out = tmp_path / "site"
    out.mkdir()
    removed = clean_output(str(out))
    assert removed == []


def test_clean_removes_html(tmp_path: Path) -> None:
    """Tests that clean_output removes HTML build artifacts from the output directory."""
    out = tmp_path / "site"
    html_dir = out / "html"
    html_dir.mkdir(parents=True)
    # Create a dummy HTML file to simulate a build artifact.
    (html_dir / "index.html").write_text("<html></html>")
    removed = clean_output(str(out))
    assert str(html_dir) in removed


def test_clean_cli(tmp_path: Path) -> None:
    """Tests the CLI clean command reports 'Nothing to clean' for an empty output directory."""
    out = tmp_path / "site"
    out.mkdir()
    result = runner.invoke(app, ["clean", "--output", str(out)])
    assert result.exit_code == 0
    assert "Nothing to clean" in result.stdout
