"""Clean build artifacts from the output directory.

Removes the html/, pdf/, and archive/ subdirectories as well as any
temporary work directories created by docsbuildtool.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from docsbuildtool.config import OUTPUT_ARCHIVE, OUTPUT_HTML, OUTPUT_PDF, resolve_output, validate_paths


def clean_output(output_path: str | None) -> list[str]:
    """Remove all generated build artifacts from the output directory.

    Args:
        output_path: Path to the output root directory.  If ``None``,
            the default (``site/``) is used.

    Returns:
        A list of directory path strings that were successfully removed.
    """
    output = resolve_output(output_path)
    # Use a dummy safe source path for validation
    validate_paths(Path("docs"), output)

    removed: list[str] = []
    subdirs = [OUTPUT_HTML, OUTPUT_PDF, OUTPUT_ARCHIVE]

    # Remove the standard build artifact directories.
    for sub in subdirs:
        target = output / sub
        if target.exists():
            shutil.rmtree(target)
            removed.append(str(target))

    # Also clean any temp work dirs created by docsbuildtool in the output
    if not output.exists():
        return removed
    for item in output.iterdir():
        item_path = output / item
        # Temp directories use a "docsbuildtool-" prefix.
        if item_path.is_dir() and item.name.startswith("docsbuildtool-"):
            shutil.rmtree(item_path)
            removed.append(str(item_path))

    return removed
