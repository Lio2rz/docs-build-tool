from __future__ import annotations

import subprocess
from enum import StrEnum
from pathlib import Path

from docsbuildtool.config import generate_mkdocs_config, resolve_output, resolve_source
from docsbuildtool.errors import BuildError


class BuildFormat(StrEnum):
    html = "html"
    pdf = "pdf"
    all = "all"


OUTPUT_HTML = "html"
OUTPUT_PDF = "pdf"
OUTPUT_ARCHIVE = "archive"


def build_html(source_path: str | None, output_path: str | None) -> Path:
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

    if not (html_output / "index.html").exists():
        raise BuildError(f"HTML build completed but index.html not found at {html_output}")

    return html_output


def build_pdf(source_path: str | None, output_path: str | None) -> Path:
    raise BuildError("PDF build is not yet implemented.")


def build_all(source_path: str | None, output_path: str | None) -> tuple[Path, Path | None]:
    html_path = build_html(source_path, output_path)
    pdf_path = None
    try:
        pdf_path = build_pdf(source_path, output_path)
    except BuildError:
        pass
    return html_path, pdf_path
