"""ZIP archiving of built HTML and PDF documentation artifacts.

Collects files from the html/ and pdf/ output subdirectories and
bundles them into a single ``docs.zip`` file in the archive/ directory.
"""

from __future__ import annotations

import zipfile
from pathlib import Path

from docsbuildtool.config import OUTPUT_ARCHIVE, OUTPUT_HTML, OUTPUT_PDF, resolve_output, validate_paths
from docsbuildtool.errors import BuildError


def archive_zip(output_path: str | None) -> Path:
    """Create a ZIP archive of all built documentation artifacts.

    Args:
        output_path: Path to the output root directory.  If ``None``,
            the default output directory (``site/``) is used.

    Returns:
        The :class:`Path` to the created ``docs.zip`` file.

    Raises:
        BuildError: If neither the HTML nor PDF output directories
            exist (i.e. nothing has been built yet).
    """
    output = resolve_output(output_path)
    validate_paths(Path("docs"), output)

    html_dir = output / OUTPUT_HTML
    pdf_dir = output / OUTPUT_PDF
    archive_dir = output / OUTPUT_ARCHIVE

    # Require at least one build artifact directory to exist.
    if not html_dir.exists() and not pdf_dir.exists():
        raise BuildError("No build artifacts found. Run 'docs build' first.")

    archive_dir.mkdir(parents=True, exist_ok=True)
    zip_path = archive_dir / "docs.zip"
    # Remove any stale archive so zipfile does not append to it.
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for base_dir in [html_dir, pdf_dir]:
            if not base_dir.exists():
                continue
            for file_path in base_dir.rglob("*"):
                if file_path.is_file():
                    # Store files with paths relative to the output root so the
                    # archive mirrors the flat output directory structure.
                    arcname = str(file_path.resolve().relative_to(output.resolve()).as_posix())
                    zf.write(file_path, arcname)

    return zip_path
