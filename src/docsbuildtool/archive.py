from __future__ import annotations

import zipfile
from pathlib import Path

from docsbuildtool.config import OUTPUT_ARCHIVE, OUTPUT_HTML, OUTPUT_PDF, resolve_output, validate_paths
from docsbuildtool.errors import BuildError


def archive_zip(output_path: str | None) -> Path:
    output = resolve_output(output_path)
    validate_paths(Path("docs"), output)

    html_dir = output / OUTPUT_HTML
    pdf_dir = output / OUTPUT_PDF
    archive_dir = output / OUTPUT_ARCHIVE

    if not html_dir.exists() and not pdf_dir.exists():
        raise BuildError("No build artifacts found. Run 'docs build' first.")

    archive_dir.mkdir(parents=True, exist_ok=True)
    zip_path = archive_dir / "docs.zip"
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for base_dir in [html_dir, pdf_dir]:
            if not base_dir.exists():
                continue
            for file_path in base_dir.rglob("*"):
                if file_path.is_file():
                    arcname = str(file_path.resolve().relative_to(output.resolve()).as_posix())
                    zf.write(file_path, arcname)

    return zip_path
