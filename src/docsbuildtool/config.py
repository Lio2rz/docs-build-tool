"""Configuration resolution and mkdocs.yml generation.

Resolves source and output paths, validates them against safety
constraints, and generates temporary MkDocs configuration files for
both HTML and PDF builds.  The generated configs merge a project-level
``mkdocs.yml`` template with any user overrides found in the source
directory.
"""

from __future__ import annotations

import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml  # type: ignore[import-untyped]

from docsbuildtool.errors import ConfigError

# Default directory names used as fallbacks when the user does not
# provide explicit paths.
DEFAULT_SOURCE = "docs"
DEFAULT_OUTPUT = "site"
PROJECT_ROOT = Path.cwd()
# Subdirectory names within the output root that hold each artifact type.
OUTPUT_HTML = "html"
OUTPUT_PDF = "pdf"
OUTPUT_ARCHIVE = "archive"


@dataclass
class ResolvedConfig:
    """Result of resolving and merging configuration for a build.

    Attributes:
        source: Absolute path to the source Markdown directory.
        output: Absolute path to the output root directory.
        config_path: Path to the generated ``mkdocs.yml``.
        summary_path: Path to a ``summary.md`` navigation file if one
            exists or was generated; ``None`` otherwise.
        work_dir: Temporary working directory that holds the generated
            config file (caller is responsible for cleanup).
    """

    source: Path
    output: Path
    config_path: Path
    summary_path: Path | None
    work_dir: Path


def resolve_source(source: str | None) -> Path:
    """Resolve and validate the documentation source directory.

    Args:
        source: A path string or ``None`` to use the default (``docs/``).

    Returns:
        The absolute, resolved :class:`Path` to the source directory.

    Raises:
        ConfigError: If the path does not exist or is not a directory.
    """
    src = Path(source) if source else Path(DEFAULT_SOURCE)
    if not src.exists():
        raise ConfigError(f"Source directory does not exist: {src}")
    if not src.is_dir():
        raise ConfigError(f"Source path is not a directory: {src}")
    return src.resolve()


def resolve_output(output: str | None) -> Path:
    """Resolve the output root directory.

    Args:
        output: A path string or ``None`` to use the default (``site/``).

    Returns:
        The absolute, resolved :class:`Path` to the output directory.
    """
    out = Path(output) if output else Path(DEFAULT_OUTPUT)
    return out.resolve()


def _is_path_protected(path: Path) -> bool:
    """Check whether *path* is a protected location that must not be cleaned.

    Protected paths include the project root, the filesystem root, the
    user's home directory, and the Windows system directory.

    Args:
        path: A path to check.

    Returns:
        ``True`` if the path is protected.
    """
    resolved = path.resolve()
    # Never allow the project root to be used as an output directory.
    if resolved == PROJECT_ROOT.resolve():
        return True
    # Guard against filesystem root (e.g. "/" on Unix, "C:\\" on Windows).
    root = Path(resolved.anchor)
    if resolved == root:
        return True
    # Guard against the user's home directory.
    if resolved == Path.home():
        return True
    # Guard against the Windows system directory (e.g. "C:\\Windows").
    windir = os.environ.get("WINDIR")
    if windir and resolved == Path(windir).resolve():
        return True
    return False


def validate_paths(source: Path, output: Path) -> None:
    """Validate that *source* and *output* are safe and distinct.

    Args:
        source: Resolved source directory path.
        output: Resolved output directory path.

    Raises:
        ConfigError: If the output path equals the source path or is a
            protected system location.
    """
    if source.resolve() == output.resolve():
        raise ConfigError(f"Output directory cannot be the same as source: {output}")
    if _is_path_protected(output):
        raise ConfigError(f"Output directory is a protected path: {output}")


def _load_mkdocs_yaml(path: Path) -> dict[str, Any]:
    """Load a YAML file, stripping ``!!python/name:`` tags.

    MkDocs configuration often includes ``!!python/name:`` tags for
    Python object references.  These cannot be resolved by
    :func:`yaml.safe_load`, so we strip them before parsing.

    Args:
        path: Path to a YAML file.

    Returns:
        A dictionary of the parsed YAML content, or an empty dict if
        the file is empty.
    """
    content = path.read_text(encoding="utf-8")
    # Strip !!python/name tags — safe_load cannot resolve them and we don't need to.
    content = content.replace("!!python/name:", "")
    return yaml.safe_load(content) or {}


def _generate_summary(source: Path, work_dir: Path) -> Path:
    """Generate a ``summary.md`` navigation file from Markdown files.

    Scans *source* recursively for ``*.md`` files, sorts them by name,
    and writes a nested bullet list where each entry links to the
    relative path of the Markdown file.  Indentation reflects directory
    depth.

    Args:
        source: The source Markdown directory.
        work_dir: The temporary working directory where the summary
            file will be written.

    Returns:
        The :class:`Path` to the generated ``summary.md``.
    """
    md_files = sorted(source.rglob("*.md"))
    summary_path = work_dir / "summary.md"
    lines: list[str] = []
    for f in md_files:
        rel = f.resolve().relative_to(source.resolve())
        parts = rel.parts
        # One indentation level per directory depth.
        indent = "    " * (len(parts) - 1)
        # Convert the filename into a human-readable title.
        title = parts[-1].replace(".md", "").replace("-", " ").replace("_", " ")
        lines.append(f"{indent}- [{title}]({rel.as_posix()})")
    if lines:
        summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary_path


def _merge_exclude_docs(existing: str | list[str] | None, additions: list[str]) -> str:
    """Merge additional exclusion patterns into the ``exclude_docs`` list.

    Args:
        existing: The current value of ``exclude_docs`` from the
            MkDocs config (a multi-line string, a list, or ``None``).
        additions: Extra glob patterns to add.

    Returns:
        A multi-line string suitable for the ``exclude_docs`` YAML key.
    """
    if existing is None:
        result: list[str] = []
    elif isinstance(existing, str):
        # MkDocs may store exclude_docs as a multi-line string.
        result = [line.strip() for line in existing.strip().splitlines() if line.strip()]
    else:
        result = list(existing)
    for a in additions:
        if a not in result:
            result.append(a)
    # Each entry is indented by two spaces for YAML list formatting.
    return "\n".join(f"  {r}" for r in result)


def generate_mkdocs_config(source: Path, output: Path) -> ResolvedConfig:
    """Generate a merged ``mkdocs.yml`` for an HTML build.

    Merges the project-level ``mkdocs.yml`` with any user overrides in
    the source directory, sets the correct ``docs_dir`` and ``site_dir``,
    and ensures the required plugins (``literate-nav``, ``section-index``)
    are present.

    Args:
        source: Resolved source directory path.
        output: Resolved output directory path.

    Returns:
        A :class:`ResolvedConfig` with the generated config and
        temporary working directory.

    Raises:
        ConfigError: Via :func:`validate_paths` if paths are invalid.
    """
    validate_paths(source, output)

    # Create a temp directory that outlives this function call.
    work_dir = Path(tempfile.mkdtemp(prefix="docsbuildtool-"))

    source_mkdocs = source / "mkdocs.yml"
    if source_mkdocs.exists():
        user_config = _load_mkdocs_yaml(source_mkdocs)
    else:
        user_config = {}

    template = _load_mkdocs_yaml(PROJECT_ROOT / "mkdocs.yml")

    # Start with the project template, then layer user overrides on top.
    merged: dict[str, Any] = dict(template)
    merged.update(user_config)
    merged["docs_dir"] = source.resolve().as_posix()
    merged["site_dir"] = output.resolve().as_posix()

    # Resolve theme custom_dir relative to project root so it works
    # when MkDocs reads the config from a temp directory.
    theme = merged.get("theme")
    if isinstance(theme, dict) and theme.get("custom_dir"):
        custom_dir = Path(theme["custom_dir"])
        if not custom_dir.is_absolute():
            theme["custom_dir"] = (PROJECT_ROOT / custom_dir).resolve().as_posix()

    resolved_summary: Path | None = None
    source_summary = source / "summary.md"
    if source_summary.exists():
        resolved_summary = source_summary
    else:
        # Auto-generate a summary.md if the user hasn't provided one.
        resolved_summary = _generate_summary(source, work_dir)

    # Exclude the summary file and the generated config from the build.
    extra_excludes = ["/summary.md"]
    if not source_summary.exists() and resolved_summary.parent == work_dir:
        try:
            extra_excludes.append("/" + resolved_summary.resolve().relative_to(source.resolve()).as_posix())
        except ValueError:
            # The generated summary is not under the source tree; nothing to exclude.
            pass

    merged["exclude_docs"] = _merge_exclude_docs(template.get("exclude_docs"), extra_excludes)

    # Ensure the required plugins are present.
    plugins = merged.get("plugins", [])
    if isinstance(plugins, list):
        plugin_names: set[str] = set()
        for p in plugins:
            if isinstance(p, dict):
                plugin_names.update(p.keys())
            elif isinstance(p, str):
                plugin_names.add(p)
        if "literate-nav" not in plugin_names:
            plugins.append({"literate-nav": {"nav_file": resolved_summary.name}})
        if "section-index" not in plugin_names:
            plugins.append("section-index")
    merged["plugins"] = plugins

    config_path = work_dir / "mkdocs.yml"
    with open(config_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(merged, f, allow_unicode=True)

    return ResolvedConfig(
        source=source,
        output=output,
        config_path=config_path,
        summary_path=resolved_summary if resolved_summary.exists() else None,
        work_dir=work_dir,
    )


def generate_pdf_config(source: Path, output: Path) -> ResolvedConfig:
    """Generate a merged ``mkdocs.yml`` for a PDF build.

    Same as :func:`generate_mkdocs_config` but additionally includes
    the ``with-pdf`` plugin to produce a PDF output.

    Args:
        source: Resolved source directory path.
        output: Resolved output directory path.

    Returns:
        A :class:`ResolvedConfig` with the generated config and
        temporary working directory.

    Raises:
        ConfigError: Via :func:`validate_paths` if paths are invalid.
    """
    validate_paths(source, output)

    # Use a separate temp prefix so PDF temp dirs are distinguishable.
    work_dir = Path(tempfile.mkdtemp(prefix="docsbuildtool-pdf-"))

    source_mkdocs = source / "mkdocs.yml"
    if source_mkdocs.exists():
        user_config = _load_mkdocs_yaml(source_mkdocs)
    else:
        user_config = {}

    template = _load_mkdocs_yaml(PROJECT_ROOT / "mkdocs.yml")

    merged: dict[str, Any] = dict(template)
    merged.update(user_config)
    merged["docs_dir"] = source.resolve().as_posix()
    merged["site_dir"] = output.resolve().as_posix()

    # Resolve theme custom_dir relative to project root so it works
    # when MkDocs reads the config from a temp directory.
    theme = merged.get("theme")
    if isinstance(theme, dict) and theme.get("custom_dir"):
        custom_dir = Path(theme["custom_dir"])
        if not custom_dir.is_absolute():
            theme["custom_dir"] = (PROJECT_ROOT / custom_dir).resolve().as_posix()

    resolved_summary: Path | None = None
    source_summary = source / "summary.md"
    if source_summary.exists():
        resolved_summary = source_summary
    else:
        resolved_summary = _generate_summary(source, work_dir)

    extra_excludes = ["/summary.md"]
    if not source_summary.exists() and resolved_summary.parent == work_dir:
        try:
            extra_excludes.append("/" + resolved_summary.resolve().relative_to(source.resolve()).as_posix())
        except ValueError:
            pass

    merged["exclude_docs"] = _merge_exclude_docs(template.get("exclude_docs"), extra_excludes)

    # Ensure all required plugins are present, including with-pdf.
    plugins = merged.get("plugins", [])
    if isinstance(plugins, list):
        plugin_names: set[str] = set()
        for p in plugins:
            if isinstance(p, dict):
                plugin_names.update(p.keys())
            elif isinstance(p, str):
                plugin_names.add(p)
        if "literate-nav" not in plugin_names:
            plugins.append({"literate-nav": {"nav_file": resolved_summary.name}})
        if "section-index" not in plugin_names:
            plugins.append("section-index")
        if "with-pdf" not in plugin_names:
            plugins.append({"with-pdf": {"output_path": "docs.pdf"}})
    merged["plugins"] = plugins

    config_path = work_dir / "mkdocs.yml"
    with open(config_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(merged, f, allow_unicode=True)

    return ResolvedConfig(
        source=source,
        output=output,
        config_path=config_path,
        summary_path=resolved_summary if resolved_summary.exists() else None,
        work_dir=work_dir,
    )
