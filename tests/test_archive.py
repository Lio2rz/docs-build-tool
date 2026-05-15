import zipfile
from pathlib import Path

from typer.testing import CliRunner

from docsbuildtool.archive import archive_zip
from docsbuildtool.cli import app
from docsbuildtool.errors import BuildError

runner = CliRunner()


def test_archive_no_artifacts(tmp_path: Path) -> None:
    out = tmp_path / "site"
    out.mkdir()
    try:
        archive_zip(str(out))
    except BuildError as e:
        assert "No build artifacts" in str(e)


def test_archive_creates_zip(tmp_path: Path) -> None:
    out = tmp_path / "site"
    html_dir = out / "html"
    html_dir.mkdir(parents=True)
    (html_dir / "index.html").write_text("<html></html>")
    zip_path = archive_zip(str(out))
    assert zip_path.exists()
    assert zip_path.stat().st_size > 0
    with zipfile.ZipFile(zip_path) as zf:
        names = zf.namelist()
        assert any("html/index.html" in n for n in names)


def test_archive_cli(tmp_path: Path) -> None:
    out = tmp_path / "site"
    out.mkdir()
    result = runner.invoke(app, ["archive", "--format", "zip", "--output", str(out)])
    assert result.exit_code != 0
    assert result.exception is not None
    assert "No build artifacts" in str(result.exception)
