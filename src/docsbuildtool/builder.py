#!/usr/bin/env python3

# ======================================================================================================================
# @description Build orchestrator for HTML and PDF documentation output
#
# @details     Contains ``BuildFormat`` enum (html/pdf/all) and three build functions that invoke MkDocs via subprocess.
#              ``build_html`` generates static HTML, ``build_pdf`` renders a single PDF via mkdocs-with-pdf, and
#              ``build_all`` runs both with non-fatal PDF failure. All functions resolve paths through the config layer
#              and return the output path on success.
#
# ======================================================================================================================
#
# @filename   builder.py
# @path       src/docsbuildtool/builder.py
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
# @record     [2026/05/16 01:26] <Lion> docs(src,tests): add module docstrings, function docstrings, and inline comments
# @record     [2026/05/15 17:29] <Carl Chen> feat(build): add PDF build via mkdocs-with-pdf plugin.
# @record     [2026/05/15 17:26] <Carl Chen> feat(build): add HTML build via MkDocs subprocess.
#
# @license    MIT License
#
# @copyright  Copyright (c) 2026 Lio2rz. All rights reserved.
# ======================================================================================================================

from __future__ import annotations

import subprocess
from enum import StrEnum
from pathlib import Path

from docsbuildtool.config import (
    OUTPUT_HTML,
    OUTPUT_PDF,
    generate_mkdocs_config,
    generate_pdf_config,
    resolve_output,
    resolve_source,
)
from docsbuildtool.errors import BuildError, EnvMissingError


class BuildFormat(StrEnum):
    """Supported documentation build formats."""

    html = "html"
    """Build HTML output only."""
    pdf = "pdf"
    """Build PDF output only."""
    all = "all"
    """Build both HTML and PDF."""


def build_html(source_path: str | None, output_path: str | None) -> Path:
    """Build HTML documentation via MkDocs.

    Args:
        source_path: Path to the source directory containing Markdown
            files.  Defaults to ``docs/``.
        output_path: Path to the output root directory.  Defaults to
            ``site/``.

    Returns:
        The :class:`Path` to the generated HTML output directory.

    Raises:
        BuildError: If the MkDocs subprocess fails or if ``index.html``
            is not found after the build completes.
    """
    source = resolve_source(source_path)
    output = resolve_output(output_path)
    resolved = generate_mkdocs_config(source, output)

    html_output = output.resolve() / OUTPUT_HTML
    resolved_json = resolved.config_path.resolve()

    result = subprocess.run(
        ["mkdocs", "build", "-f", str(resolved_json), "-d", str(html_output)],
        capture_output=True,
        text=True,
        cwd=str(source.resolve()),
    )

    if result.returncode != 0:
        stderr = result.stderr.strip() or result.stdout.strip()
        raise BuildError(f"MkDocs HTML build failed:\n{stderr}")

    # Verify the build actually produced output.
    if not (html_output / "index.html").exists():
        raise BuildError(f"HTML build completed but index.html not found at {html_output}")

    return html_output


def build_pdf(source_path: str | None, output_path: str | None) -> Path:
    """Build PDF documentation via MkDocs with the ``with-pdf`` plugin.

    Args:
        source_path: Path to the source directory containing Markdown
            files.  Defaults to ``docs/``.
        output_path: Path to the output root directory.  Defaults to
            ``site/``.

    Returns:
        The :class:`Path` to the generated PDF file.

    Raises:
        EnvMissingError: If PDF dependencies (e.g. the ``with-pdf``
            plugin) are not installed.
        BuildError: If the MkDocs subprocess fails or the resulting
            PDF is missing or empty.
    """
    source = resolve_source(source_path)
    output = resolve_output(output_path)
    resolved = generate_pdf_config(source, output)

    pdf_output_dir = output.resolve() / OUTPUT_PDF
    resolved_json = resolved.config_path.resolve()

    result = subprocess.run(
        ["mkdocs", "build", "-f", str(resolved_json), "-d", str(pdf_output_dir)],
        capture_output=True,
        text=True,
        cwd=str(source.resolve()),
    )

    if result.returncode != 0:
        stderr = result.stderr.strip() or result.stdout.strip()
        # Distinguish missing dependency errors from general build failures.
        if "No module named" in stderr or "ModuleNotFoundError" in stderr:
            raise EnvMissingError(f"PDF dependencies missing. Run: poetry install --with doc-group\n\n{stderr}")
        raise BuildError(f"MkDocs PDF build failed:\n{stderr}")

    pdf_file = pdf_output_dir / "docs.pdf"
    if not pdf_file.exists():
        raise BuildError(f"PDF build completed but {pdf_file} not found")
    # Guard against plugin bugs that produce a zero-byte file.
    if pdf_file.stat().st_size == 0:
        raise BuildError(f"PDF build produced empty file: {pdf_file}")

    return pdf_file


def build_all(source_path: str | None, output_path: str | None) -> tuple[Path, Path | None]:
    """Build both HTML and PDF documentation.

    HTML is always built first.  If PDF fails, the HTML result is still
    returned and the PDF result is ``None`` (partial success).

    Args:
        source_path: See :func:`build_html`.
        output_path: See :func:`build_html`.

    Returns:
        A ``(html_path, pdf_path)`` tuple where ``pdf_path`` may be
        ``None`` if the PDF build failed.
    """
    html_path = build_html(source_path, output_path)
    pdf_path = None
    try:
        pdf_path = build_pdf(source_path, output_path)
    except BuildError:
        # Swallow PDF failures so the caller can report partial success.
        pass
    return html_path, pdf_path
