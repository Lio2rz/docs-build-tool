#!/usr/bin/env python3

# ======================================================================================================================
# @description Unit tests for configuration resolution and MkDocs YAML generation
#
# @details     Tests ``resolve_source``, ``resolve_output``, path validation (output cannot equal source, cannot be
#              protected path), config generation with and without user mkdocs.yml, summary generation, and output
#              directory structure. All tests use ``tmp_path`` fixtures and the ``minimal-docs`` fixture set.
#
# ======================================================================================================================
#
# @filename   test_config.py
# @path       tests/test_config.py
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
# @record     [2026/05/15 17:11] <Carl Chen> feat(config): add source directory resolution and MkDocs config generation.
#
# @license    MIT License
#
# @copyright  Copyright (c) 2026 Lio2rz. All rights reserved.
# ======================================================================================================================

"""Tests for the config module.

Covers source and output path resolution, path validation (protected paths,
equality checks), and mkdocs config generation including user-provided configs,
auto-generated summaries, and paths with spaces.
"""

from pathlib import Path

import pytest

from docsbuildtool.config import (
    generate_mkdocs_config,
    resolve_output,
    resolve_source,
    validate_paths,
)
from docsbuildtool.errors import ConfigError


def test_resolve_source_default() -> None:
    """Tests that resolve_source with None returns the default 'docs' directory."""
    src = resolve_source(None)
    assert src.name == "docs"
    assert src.exists()


def test_resolve_source_custom(tmp_path: Path) -> None:
    """Tests that resolve_source returns the resolved path to a custom source directory."""
    custom = tmp_path / "my-docs"
    custom.mkdir()
    src = resolve_source(str(custom))
    assert src == custom.resolve()


def test_resolve_source_not_exists() -> None:
    """Tests that resolve_source raises ConfigError for a nonexistent path."""
    with pytest.raises(ConfigError, match="does not exist"):
        resolve_source("/nonexistent/path/abc123xyz")


def test_resolve_source_is_file(tmp_path: Path) -> None:
    """Tests that resolve_source raises ConfigError when the path is a file, not a directory."""
    f = tmp_path / "file.txt"
    f.write_text("hello")
    with pytest.raises(ConfigError, match="not a directory"):
        resolve_source(str(f))


def test_resolve_output_default() -> None:
    """Tests that resolve_output with None returns the default 'site' directory name."""
    out = resolve_output(None)
    assert out.name == "site"


def test_validate_output_equals_source(tmp_path: Path) -> None:
    """Tests that validate_paths raises ConfigError when output equals source."""
    src = tmp_path / "src"
    src.mkdir()
    with pytest.raises(ConfigError, match="cannot be the same as source"):
        validate_paths(src, src)


def test_validate_output_is_project_root() -> None:
    """Tests that validate_paths raises ConfigError when output is the project root (protected)."""
    with pytest.raises(ConfigError, match="protected path"):
        validate_paths(Path("docs"), Path.cwd())


def test_generate_config_with_user_mkdocs(tmp_path: Path) -> None:
    """Tests generate_mkdocs_config when the user provides a custom mkdocs.yml and summary."""
    source = tmp_path / "docs"
    source.mkdir()
    (source / "index.md").write_text("# Test\n")
    (source / "summary.md").write_text("* [Home](index.md)\n")
    # User-provided mkdocs config.
    (source / "mkdocs.yml").write_text("site_name: Custom\n")

    output = tmp_path / "site"
    result = generate_mkdocs_config(source, output)

    assert result.config_path.exists()
    assert result.summary_path == source / "summary.md"


def test_generate_config_without_summary(tmp_path: Path) -> None:
    """Tests generate_mkdocs_config auto-generates a summary.md when none is provided."""
    source = tmp_path / "docs"
    source.mkdir()
    (source / "index.md").write_text("# Test\n")

    output = tmp_path / "site"
    result = generate_mkdocs_config(source, output)

    assert result.config_path.exists()
    assert result.summary_path is not None
    assert result.summary_path.exists()


def test_generate_config_output_structure(tmp_path: Path) -> None:
    """Tests that the generated mkdocs config includes correct docs_dir, site_dir, and literate-nav plugin."""
    source = tmp_path / "docs"
    source.mkdir()
    (source / "index.md").write_text("# Test\n")
    sub = source / "guide"
    sub.mkdir()
    (sub / "setup.md").write_text("# Setup\n")

    output = tmp_path / "site"
    result = generate_mkdocs_config(source, output)

    assert result.config_path.exists()
    import yaml

    with open(result.config_path) as f:
        config = yaml.safe_load(f)
    assert config["docs_dir"] == source.resolve().as_posix()
    assert config["site_dir"] == output.resolve().as_posix()
    # Verify the literate-nav plugin is present for navigation.
    assert config["use_directory_urls"] is False
    assert any("literate-nav" in (p if isinstance(p, str) else str(p)) for p in (config.get("plugins") or []))


def test_validate_output_is_home() -> None:
    """Tests that validate_paths raises ConfigError when output is the user's home directory (protected)."""
    with pytest.raises(ConfigError, match="protected path"):
        validate_paths(Path("docs"), Path.home())


def test_source_with_spaces(tmp_path: Path) -> None:
    """Tests that generate_mkdocs_config works correctly with paths containing spaces."""
    source = tmp_path / "my docs source"
    source.mkdir()
    (source / "index.md").write_text("# Test\n")

    output = tmp_path / "output site"
    result = generate_mkdocs_config(source, output)

    assert result.config_path.exists()
