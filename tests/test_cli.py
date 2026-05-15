#!/usr/bin/env python3

# ======================================================================================================================
# @description CLI integration tests for the docsbuildtool Typer application
#
# @details     Tests the ``docs`` CLI: help output, version flag, unknown command handling, and help text for all four
#              subcommands (build, serve, clean, archive). Also verifies the ``main`` entry point is importable. Uses
#              ``CliRunner`` for all command invocations.
#
# ======================================================================================================================
#
# @filename   test_cli.py
# @path       tests/test_cli.py
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
# @version    0.0.3
#
# @record     [2026/05/16 01:26] <Lio2rz> docs(src,tests): add module docstrings, function docstrings, and inline comments
#             [2026/05/15 17:26] <Lio2rz> feat(build): add HTML build via MkDocs subprocess.
#             [2026/05/15 17:03] <Lio2rz> feat(cli): add Typer-based CLI entrypoint with build/serve/clean/archive c
#
# @license    MIT License
#
# @copyright  Copyright (c) 2026 Lio2rz. All rights reserved.
# ======================================================================================================================

from typer.testing import CliRunner

from docsbuildtool.cli import app

# Reusable CLI test runner instance.
runner = CliRunner()


def test_help() -> None:
    """Tests that --help lists all available subcommands (build, serve, clean, archive)."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "build" in result.stdout
    assert "serve" in result.stdout
    assert "clean" in result.stdout
    assert "archive" in result.stdout


def test_version() -> None:
    """Tests that --version prints the version string."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "docs v" in result.stdout


def test_unknown_command() -> None:
    """Tests that an unknown subcommand returns exit code 2 (Typer usage error)."""
    result = runner.invoke(app, ["unknown-cmd"])
    assert result.exit_code == 2


def test_build_help() -> None:
    """Tests that 'build --help' shows the expected build options."""
    result = runner.invoke(app, ["build", "--help"])
    assert result.exit_code == 0
    assert "--format" in result.stdout
    assert "--source" in result.stdout
    assert "--output" in result.stdout


def test_build_no_source() -> None:
    """Tests that building with a nonexistent source path returns a non-zero exit code."""
    result = runner.invoke(app, ["build", "--source", "/no/such/path"])
    assert result.exit_code != 0


def test_serve_help() -> None:
    """Tests that 'serve --help' shows the --source option."""
    result = runner.invoke(app, ["serve", "--help"])
    assert result.exit_code == 0
    assert "--source" in result.stdout


def test_clean_help() -> None:
    """Tests that 'clean --help' shows the --output option."""
    result = runner.invoke(app, ["clean", "--help"])
    assert result.exit_code == 0
    assert "--output" in result.stdout


def test_archive_help() -> None:
    """Tests that 'archive --help' shows the --format option."""
    result = runner.invoke(app, ["archive", "--help"])
    assert result.exit_code == 0
    assert "--format" in result.stdout


def test_main_importable() -> None:
    """Tests that the main entry point function is importable and callable."""
    from docsbuildtool.cli import main

    assert callable(main)
