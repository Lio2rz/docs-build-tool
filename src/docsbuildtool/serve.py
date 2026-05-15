from __future__ import annotations

import subprocess

from docsbuildtool.config import generate_mkdocs_config, resolve_output, resolve_source
from docsbuildtool.errors import BuildError


def serve_preview(source_path: str | None, output_path: str | None) -> None:
    source = resolve_source(source_path)
    output = resolve_output(output_path)
    resolved = generate_mkdocs_config(source, output)

    result = subprocess.run(
        ["mkdocs", "serve", "-f", str(resolved.config_path.resolve())],
        cwd=str(source.resolve()),
    )

    if result.returncode != 0:
        raise BuildError(f"MkDocs serve failed with code {result.returncode}")
