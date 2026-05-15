from __future__ import annotations

import shutil
from pathlib import Path

from docsbuildtool.config import OUTPUT_ARCHIVE, OUTPUT_HTML, OUTPUT_PDF, resolve_output, validate_paths


def clean_output(output_path: str | None) -> list[str]:
    output = resolve_output(output_path)
    # Use a dummy safe source path for validation
    validate_paths(Path("docs"), output)

    removed: list[str] = []
    subdirs = [OUTPUT_HTML, OUTPUT_PDF, OUTPUT_ARCHIVE]

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
        if item_path.is_dir() and item.name.startswith("docsbuildtool-"):
            shutil.rmtree(item_path)
            removed.append(str(item_path))

    return removed
