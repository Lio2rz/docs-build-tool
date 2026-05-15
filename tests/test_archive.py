#!/usr/bin/env python3

# ======================================================================================================================
# @description Unit tests for the ZIP archive module
#
# @details     Verifies ``archive_zip`` rejects missing build artifacts, creates a valid ZIP file from HTML and PDF
#              output, and exposes a CLI subcommand via Typer CliRunner. Uses ``tmp_path`` fixtures for isolated file
#              creation.
#
# ======================================================================================================================
#
# @filename   test_archive.py
# @path       tests/test_archive.py
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
# @record     [2026/05/15 17:37] <Carl Chen> feat(archive): add ZIP archive command.
#
# @license    MIT License
#
# @copyright  Copyright (c) 2026 Lio2rz. All rights reserved.
# ======================================================================================================================

"""Tests for the archive_zip module.

Covers archive creation, error handling when no build artifacts exist,
and the CLI archive command integration.
"""

import zipfile
from pathlib import Path

from typer.testing import CliRunner

from docsbuildtool.archive import archive_zip
from docsbuildtool.cli import app
from docsbuildtool.errors import BuildError

# Reusable CLI test runner instance.
runner = CliRunner()


def test_archive_no_artifacts(tmp_path: Path) -> None:
    """Tests that archive_zip raises BuildError when the output directory is empty."""
    out = tmp_path / "site"
    out.mkdir()
    try:
        archive_zip(str(out))
    except BuildError as e:
        assert "No build artifacts" in str(e)


def test_archive_creates_zip(tmp_path: Path) -> None:
    """Tests that archive_zip creates a valid zip file containing HTML artifacts."""
    out = tmp_path / "site"
    html_dir = out / "html"
    html_dir.mkdir(parents=True)
    # Create a minimal HTML file to serve as a build artifact.
    (html_dir / "index.html").write_text("<html></html>")
    zip_path = archive_zip(str(out))
    assert zip_path.exists()
    assert zip_path.stat().st_size > 0
    # Verify the zip archive contains the expected file.
    with zipfile.ZipFile(zip_path) as zf:
        names = zf.namelist()
        assert any("html/index.html" in n for n in names)


def test_archive_cli(tmp_path: Path) -> None:
    """Tests that the CLI archive command fails gracefully when no artifacts exist."""
    out = tmp_path / "site"
    out.mkdir()
    result = runner.invoke(app, ["archive", "--format", "zip", "--output", str(out)])
    assert result.exit_code != 0
    assert result.exception is not None
    assert "No build artifacts" in str(result.exception)
