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
    src = resolve_source(None)
    assert src.name == "docs"
    assert src.exists()


def test_resolve_source_custom(tmp_path: Path) -> None:
    custom = tmp_path / "my-docs"
    custom.mkdir()
    src = resolve_source(str(custom))
    assert src == custom.resolve()


def test_resolve_source_not_exists() -> None:
    with pytest.raises(ConfigError, match="does not exist"):
        resolve_source("/nonexistent/path/abc123xyz")


def test_resolve_source_is_file(tmp_path: Path) -> None:
    f = tmp_path / "file.txt"
    f.write_text("hello")
    with pytest.raises(ConfigError, match="not a directory"):
        resolve_source(str(f))


def test_resolve_output_default() -> None:
    out = resolve_output(None)
    assert out.name == "site"


def test_validate_output_equals_source(tmp_path: Path) -> None:
    src = tmp_path / "src"
    src.mkdir()
    with pytest.raises(ConfigError, match="cannot be the same as source"):
        validate_paths(src, src)


def test_validate_output_is_project_root() -> None:
    with pytest.raises(ConfigError, match="protected path"):
        validate_paths(Path("docs"), Path.cwd())


def test_generate_config_with_user_mkdocs(tmp_path: Path) -> None:
    source = tmp_path / "docs"
    source.mkdir()
    (source / "index.md").write_text("# Test\n")
    (source / "summary.md").write_text("* [Home](index.md)\n")
    (source / "mkdocs.yml").write_text("site_name: Custom\n")

    output = tmp_path / "site"
    result = generate_mkdocs_config(source, output)

    assert result.config_path.exists()
    assert result.summary_path == source / "summary.md"


def test_generate_config_without_summary(tmp_path: Path) -> None:
    source = tmp_path / "docs"
    source.mkdir()
    (source / "index.md").write_text("# Test\n")

    output = tmp_path / "site"
    result = generate_mkdocs_config(source, output)

    assert result.config_path.exists()
    assert result.summary_path is not None
    assert result.summary_path.exists()


def test_generate_config_output_structure(tmp_path: Path) -> None:
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
    assert config["use_directory_urls"] is False
    assert any("literate-nav" in (p if isinstance(p, str) else str(p)) for p in (config.get("plugins") or []))


def test_validate_output_is_home() -> None:
    with pytest.raises(ConfigError, match="protected path"):
        validate_paths(Path("docs"), Path.home())


def test_source_with_spaces(tmp_path: Path) -> None:
    source = tmp_path / "my docs source"
    source.mkdir()
    (source / "index.md").write_text("# Test\n")

    output = tmp_path / "output site"
    result = generate_mkdocs_config(source, output)

    assert result.config_path.exists()
