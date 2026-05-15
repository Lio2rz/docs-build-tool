from pathlib import Path

from typer.testing import CliRunner

from docsbuildtool.clean import clean_output
from docsbuildtool.cli import app

runner = CliRunner()


def test_clean_nonexistent(tmp_path: Path) -> None:
    out = tmp_path / "nonexistent"
    removed = clean_output(str(out))
    assert removed == []


def test_clean_empty_output(tmp_path: Path) -> None:
    out = tmp_path / "site"
    out.mkdir()
    removed = clean_output(str(out))
    assert removed == []


def test_clean_removes_html(tmp_path: Path) -> None:
    out = tmp_path / "site"
    html_dir = out / "html"
    html_dir.mkdir(parents=True)
    (html_dir / "index.html").write_text("<html></html>")
    removed = clean_output(str(out))
    assert str(html_dir) in removed


def test_clean_cli(tmp_path: Path) -> None:
    out = tmp_path / "site"
    out.mkdir()
    result = runner.invoke(app, ["clean", "--output", str(out)])
    assert result.exit_code == 0
    assert "Nothing to clean" in result.stdout
