from __future__ import annotations

import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml  # type: ignore[import-untyped]

from docsbuildtool.errors import ConfigError

DEFAULT_SOURCE = "docs"
DEFAULT_OUTPUT = "site"
PROJECT_ROOT = Path.cwd()


@dataclass
class ResolvedConfig:
    source: Path
    output: Path
    config_path: Path
    summary_path: Path | None
    work_dir: Path


def resolve_source(source: str | None) -> Path:
    src = Path(source) if source else Path(DEFAULT_SOURCE)
    if not src.exists():
        raise ConfigError(f"Source directory does not exist: {src}")
    if not src.is_dir():
        raise ConfigError(f"Source path is not a directory: {src}")
    return src.resolve()


def resolve_output(output: str | None) -> Path:
    out = Path(output) if output else Path(DEFAULT_OUTPUT)
    return out.resolve()


def _is_path_protected(path: Path) -> bool:
    resolved = path.resolve()
    if resolved == PROJECT_ROOT.resolve():
        return True
    root = Path(resolved.anchor)
    if resolved == root:
        return True
    if resolved == Path.home():
        return True
    windir = os.environ.get("WINDIR")
    if windir and resolved == Path(windir).resolve():
        return True
    return False


def validate_paths(source: Path, output: Path) -> None:
    if source.resolve() == output.resolve():
        raise ConfigError(f"Output directory cannot be the same as source: {output}")
    if _is_path_protected(output):
        raise ConfigError(f"Output directory is a protected path: {output}")


def _load_mkdocs_yaml(path: Path) -> dict[str, Any]:
    content = path.read_text(encoding="utf-8")
    # Strip !!python/name tags — safe_load cannot resolve them and we don't need to.
    content = content.replace("!!python/name:", "")
    return yaml.safe_load(content) or {}


def _generate_summary(source: Path, work_dir: Path) -> Path:
    md_files = sorted(source.rglob("*.md"))
    summary_path = work_dir / "summary.md"
    lines: list[str] = []
    for f in md_files:
        rel = f.resolve().relative_to(source.resolve())
        parts = rel.parts
        indent = "    " * (len(parts) - 1)
        title = parts[-1].replace(".md", "").replace("-", " ").replace("_", " ")
        lines.append(f"{indent}- [{title}]({rel.as_posix()})")
    if lines:
        summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary_path


def _merge_exclude_docs(existing: str | list[str] | None, additions: list[str]) -> str:
    if existing is None:
        result: list[str] = []
    elif isinstance(existing, str):
        result = [line.strip() for line in existing.strip().splitlines() if line.strip()]
    else:
        result = list(existing)
    for a in additions:
        if a not in result:
            result.append(a)
    return "\n".join(f"  {r}" for r in result)


def generate_mkdocs_config(source: Path, output: Path) -> ResolvedConfig:
    validate_paths(source, output)

    work_dir = Path(tempfile.mkdtemp(prefix="docsbuildtool-"))

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
