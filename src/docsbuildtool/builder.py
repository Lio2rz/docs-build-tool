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
    html = "html"
    pdf = "pdf"
    all = "all"


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
        if "No module named" in stderr or "ModuleNotFoundError" in stderr:
            raise EnvMissingError(f"PDF dependencies missing. Run: poetry install --with doc-group\n\n{stderr}")
        raise BuildError(f"MkDocs PDF build failed:\n{stderr}")

    pdf_file = pdf_output_dir / "docs.pdf"
    if not pdf_file.exists():
        raise BuildError(f"PDF build completed but {pdf_file} not found")
    if pdf_file.stat().st_size == 0:
        raise BuildError(f"PDF build produced empty file: {pdf_file}")

    return pdf_file


def build_all(source_path: str | None, output_path: str | None) -> tuple[Path, Path | None]:
    html_path = build_html(source_path, output_path)
    pdf_path = None
    try:
        pdf_path = build_pdf(source_path, output_path)
    except BuildError:
        pass
    return html_path, pdf_path
