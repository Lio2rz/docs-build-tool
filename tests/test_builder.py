"""Tests for the builder module.

Covers BuildFormat enum values, the build_html function with minimal fixtures,
and CLI build commands with various format flags including partial success scenarios.
"""

from pathlib import Path

from typer.testing import CliRunner

from docsbuildtool.builder import BuildFormat, build_html
from docsbuildtool.cli import app

# Reusable CLI test runner instance.
runner = CliRunner()
# Path to the shared test fixtures directory.
FIXTURES = Path(__file__).parent / "fixtures"


def test_build_format_enum() -> None:
    """Tests that the BuildFormat enum values match the expected CLI format strings."""
    assert BuildFormat.html == "html"
    assert BuildFormat.pdf == "pdf"
    assert BuildFormat.all == "all"


def test_build_html_minimal(tmp_path: Path) -> None:
    """Tests that build_html produces an index.html from a minimal source fixture."""
    source = FIXTURES / "minimal-docs"
    output = tmp_path / "site"
    html_path = build_html(str(source), str(output))
    assert html_path.exists()
    assert (html_path / "index.html").exists()


def test_cli_build_default(tmp_path: Path) -> None:
    """Tests that the CLI build command (default format) succeeds and creates HTML output."""
    source = FIXTURES / "minimal-docs"
    output = tmp_path / "site"
    result = runner.invoke(app, ["build", "--source", str(source), "--output", str(output)])
    assert result.exit_code == 0
    assert "HTML built" in result.stdout
    assert (output / "html" / "index.html").exists()


def test_cli_build_format_html(tmp_path: Path) -> None:
    """Tests that the CLI build command with --format html succeeds."""
    source = FIXTURES / "minimal-docs"
    output = tmp_path / "site"
    result = runner.invoke(app, ["build", "--format", "html", "--source", str(source), "--output", str(output)])
    assert result.exit_code == 0
    assert "HTML built" in result.stdout


def test_cli_build_pdf_handles_failure(tmp_path: Path) -> None:
    """Tests that --format pdf returns a non-zero exit code when PDF generation is unavailable."""
    source = FIXTURES / "minimal-docs"
    output = tmp_path / "site"
    result = runner.invoke(app, ["build", "--format", "pdf", "--source", str(source), "--output", str(output)])
    assert result.exit_code != 0


def test_cli_build_all_partial(tmp_path: Path) -> None:
    """Tests that --format all reports partial success when HTML succeeds but PDF fails."""
    source = FIXTURES / "minimal-docs"
    output = tmp_path / "site"
    result = runner.invoke(app, ["build", "--format", "all", "--source", str(source), "--output", str(output)])
    assert result.exit_code == 1  # PDF fails, partial success
    assert "HTML" in result.stdout
    assert "Partial success" in result.stdout
