from pathlib import Path

from typer.testing import CliRunner

from docsbuildtool.builder import BuildFormat, build_html
from docsbuildtool.cli import app

runner = CliRunner()
FIXTURES = Path(__file__).parent / "fixtures"


def test_build_format_enum() -> None:
    assert BuildFormat.html == "html"
    assert BuildFormat.pdf == "pdf"
    assert BuildFormat.all == "all"


def test_build_html_minimal(tmp_path: Path) -> None:
    source = FIXTURES / "minimal-docs"
    output = tmp_path / "site"
    html_path = build_html(str(source), str(output))
    assert html_path.exists()
    assert (html_path / "index.html").exists()


def test_cli_build_default(tmp_path: Path) -> None:
    source = FIXTURES / "minimal-docs"
    output = tmp_path / "site"
    result = runner.invoke(app, ["build", "--source", str(source), "--output", str(output)])
    assert result.exit_code == 0
    assert "HTML built" in result.stdout
    assert (output / "html" / "index.html").exists()


def test_cli_build_format_html(tmp_path: Path) -> None:
    source = FIXTURES / "minimal-docs"
    output = tmp_path / "site"
    result = runner.invoke(app, ["build", "--format", "html", "--source", str(source), "--output", str(output)])
    assert result.exit_code == 0
    assert "HTML built" in result.stdout


def test_cli_build_pdf_handles_failure(tmp_path: Path) -> None:
    source = FIXTURES / "minimal-docs"
    output = tmp_path / "site"
    result = runner.invoke(app, ["build", "--format", "pdf", "--source", str(source), "--output", str(output)])
    assert result.exit_code != 0


def test_cli_build_all_partial(tmp_path: Path) -> None:
    source = FIXTURES / "minimal-docs"
    output = tmp_path / "site"
    result = runner.invoke(app, ["build", "--format", "all", "--source", str(source), "--output", str(output)])
    assert result.exit_code == 1  # PDF fails, partial success
    assert "HTML" in result.stdout
    assert "Partial success" in result.stdout
