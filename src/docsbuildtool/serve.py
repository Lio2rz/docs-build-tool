"""Live-preview server for documentation.

Starts ``mkdocs serve`` using a generated configuration so users can
preview their documentation in a browser with hot-reload.
"""

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
