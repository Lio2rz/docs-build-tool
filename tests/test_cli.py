from typer.testing import CliRunner

from docsbuildtool.cli import app

runner = CliRunner()


def test_help() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "build" in result.stdout
    assert "serve" in result.stdout
    assert "clean" in result.stdout
    assert "archive" in result.stdout


def test_version() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "docs v" in result.stdout


def test_unknown_command() -> None:
    result = runner.invoke(app, ["unknown-cmd"])
    assert result.exit_code == 2


def test_build_help() -> None:
    result = runner.invoke(app, ["build", "--help"])
    assert result.exit_code == 0
    assert "--format" in result.stdout
    assert "--source" in result.stdout
    assert "--output" in result.stdout


def test_build_placeholder() -> None:
    result = runner.invoke(app, ["build"])
    assert result.exit_code == 0
    assert "not yet implemented" in result.stdout


def test_serve_help() -> None:
    result = runner.invoke(app, ["serve", "--help"])
    assert result.exit_code == 0
    assert "--source" in result.stdout


def test_clean_help() -> None:
    result = runner.invoke(app, ["clean", "--help"])
    assert result.exit_code == 0
    assert "--output" in result.stdout


def test_archive_help() -> None:
    result = runner.invoke(app, ["archive", "--help"])
    assert result.exit_code == 0
    assert "--format" in result.stdout


def test_main_importable() -> None:
    from docsbuildtool.cli import main

    assert callable(main)
