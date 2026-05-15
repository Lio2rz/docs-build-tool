#!/usr/bin/env python3

# ======================================================================================================================
# @description Unit tests for the clean command with path protection
#
# @details     Verifies ``clean_output`` handles nonexistent paths gracefully, removes empty output directories, deletes
#              html/ subdirectories, and integrates with the CLI via Typer CliRunner. Uses ``tmp_path`` for isolated tes
#              directories.
#
# ======================================================================================================================
#
# @filename   test_clean.py
# @path       tests/test_clean.py
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
# @version    0.0.2
#
# @record     [2026/05/16 01:26] <Lion> docs(src,tests): add module docstrings, function docstrings, and inline comments
#              [2026/05/15 17:34] <Carl Chen> feat(clean): add safe clean command with path protection.
#
# @license    MIT License
#
# @copyright  Copyright (c) 2026 Lio2rz. All rights reserved.
# ======================================================================================================================

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
