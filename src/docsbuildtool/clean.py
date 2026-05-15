#!/usr/bin/env python3

# ======================================================================================================================
# @description Safe build-artifact cleaner with filesystem path protection
#
# @details     ``clean_output`` removes html/, pdf/, and archive/ subdirectories plus any temporary docsbuildtool-* work
#              directories under the output root. Built-in path protection prevents accidental deletion of the project
#              root, filesystem root, home directory, or Windows system directory.
#
# ======================================================================================================================
#
# @filename   clean.py
# @path       src/docsbuildtool/clean.py
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
# @record     [2026/05/16 01:26] <Lion> docs(src,tests): add module docstrings, function docstrings, and inline comments
# @record     [2026/05/15 17:34] <Carl Chen> feat(clean): add safe clean command with path protection.
#
# @license    MIT License
#
# @copyright  Copyright (c) 2026 Lio2rz. All rights reserved.
# ======================================================================================================================

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
