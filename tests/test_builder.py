#!/usr/bin/env python3

# ======================================================================================================================
# @description Unit tests for the HTML/PDF build orchestrator
#
# @details     Tests ``BuildFormat`` enum values, minimal HTML builds against fixture docs, CLI-level build invocations
#              for html/pdf/all formats, and PDF failure handling when dependencies are absent. Uses ``tmp_path`` and
#              ``CliRunner``.
#
# ======================================================================================================================
#
# @filename   test_builder.py
# @path       tests/test_builder.py
#
# @project    docsbuildtool
# @product    Docs Build Tool
# @encoding   utf-8
#
# @author     Lio2rz
# @email      chen.mo@outlook.com
# @time       2026/05/16 01:26
#
# @vcs        git
# @version    0.0.3
#
# @record     [2026/05/16 01:26] <Lio2rz> docs(src,tests): add module docstrings, function docstrings, and inline comments
#             [2026/05/15 17:29] <Lio2rz> feat(build): add PDF build via mkdocs-with-pdf plugin.
#             [2026/05/15 17:26] <Lio2rz> feat(build): add HTML build via MkDocs subprocess.
#
# @license    MIT License
#
# @copyright  Copyright (c) 2026 Lio2rz. All rights reserved.
# ======================================================================================================================

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
