#!/usr/bin/env python3

# ======================================================================================================================
# @description Local preview server via ``mkdocs serve`` subprocess
#
# @details     ``serve_preview`` runs MkDocs in serve mode for local documentation preview. It blocks until the user
#              presses Ctrl+C. Output from the MkDocs process is streamed directly to the terminal by design so the
#              user sees the live-reload URL immediately.
#
# ======================================================================================================================
#
# @filename   serve.py
# @path       src/docsbuildtool/serve.py
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
# @record     [2026/05/16 01:26] <Lio2rz> docs(src,tests): add module docstrings, function docstrings, and inline comments
#             [2026/05/15 17:32] <Lio2rz> feat(serve): add mkdocs serve preview command.
#
# @license    MIT License
#
# @copyright  Copyright (c) 2026 Lio2rz. All rights reserved.
# ======================================================================================================================

from __future__ import annotations

import subprocess

from docsbuildtool.config import generate_mkdocs_config, resolve_output, resolve_source
from docsbuildtool.errors import BuildError


def serve_preview(source_path: str | None, output_path: str | None) -> None:
    """Start an MkDocs development server for live preview.

    This runs ``mkdocs serve`` in the foreground.  The subprocess is
    not captured so that its output streams appear directly in the
    terminal.

    Args:
        source_path: Path to the source directory containing Markdown
            files.  Defaults to ``docs/``.
        output_path: Path to the output root directory (used only for
            config generation; ``mkdocs serve`` does not write to disk).
            Defaults to ``site/``.

    Raises:
        BuildError: If the MkDocs subprocess exits with a non-zero
            return code.
    """
    source = resolve_source(source_path)
    output = resolve_output(output_path)
    resolved = generate_mkdocs_config(source, output)

    # Note: output is NOT captured so the user sees MkDocs' own
    # coloured output and can interact via Ctrl+C.
    result = subprocess.run(
        ["mkdocs", "serve", "-f", str(resolved.config_path.resolve())],
        cwd=str(source.resolve()),
    )

    if result.returncode != 0:
        raise BuildError(f"MkDocs serve failed with code {result.returncode}")
