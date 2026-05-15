#!/usr/bin/env python3

# ======================================================================================================================
# @description Typer-based CLI application exposing the ``docs`` command
#
# @details     Defines the ``docs`` Typer application with four subcommands (build, serve, clean, archive) plus global
#              options (--version, --debug, --verbose). Uses Rich console for colored output. Error handling maps
#              ``DocsError`` subclasses to POSIX-style exit codes 0-3. The ``main`` function serves as the entry point
#              for both ``pyproject.toml`` scripts and ``python -m docsbuildtool``.
#
# ======================================================================================================================
#
# @filename   cli.py
# @path       src/docsbuildtool/cli.py
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
# @version    0.0.7
#
# @record     [2026/05/16 01:26] <Lion> docs(src,tests): add module docstrings, function docstrings, and inline comments
# @record     [2026/05/16 01:19] <Lion> fix(cli): rename _DEBUG to _debug for PEP8 snake_case compliance.
# @record     [2026/05/15 17:37] <Carl Chen> feat(archive): add ZIP archive command.
# @record     [2026/05/15 17:34] <Carl Chen> feat(clean): add safe clean command with path protection.
# @record     [2026/05/15 17:32] <Carl Chen> feat(serve): add mkdocs serve preview command.
# @record     [2026/05/15 17:26] <Carl Chen> feat(build): add HTML build via MkDocs subprocess.
# @record     [2026/05/15 17:03] <Carl Chen> feat(cli): add Typer-based CLI entrypoint with build/serve/clean/archive co
#
# @license    MIT License
#
# @copyright  Copyright (c) 2026 Lio2rz. All rights reserved.
# ======================================================================================================================

"""Typer-based command-line interface for docsbuildtool.

Exposes four subcommands — ``build``, ``serve``, ``clean``, and
``archive`` — and a top-level ``docs`` application with global options
for version, debug, and verbose output.
"""

from typing import Annotated

import typer
from rich.console import Console

from docsbuildtool.archive import archive_zip
from docsbuildtool.builder import BuildFormat, build_all, build_html, build_pdf
from docsbuildtool.clean import clean_output
from docsbuildtool.errors import DocsError, ExitCode
from docsbuildtool.serve import serve_preview

app = typer.Typer(
    name="docs",
    help="Build static HTML and PDF documentation from structured Markdown directories.",
    no_args_is_help=True,
)
console = Console()
# Module-level flag so the exception handler can decide whether to
# print a full traceback.
_debug = False


def _version_callback(value: bool) -> None:
    """Print the package version and exit.

    Intended as an eager Typer callback so ``--version`` is resolved
    before any other arguments.
    """
    if value:
        from docsbuildtool import __version__

        console.print(f"docs v{__version__}")
        raise typer.Exit()


@app.callback()
def _global(
    version: Annotated[
        bool | None,
        typer.Option("--version", callback=_version_callback, is_eager=True, help="Show version and exit."),
    ] = None,
    debug: Annotated[
        bool,
        typer.Option("--debug", help="Show full traceback on error."),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Enable verbose output."),
    ] = False,
) -> None:
    """Global options applied to all subcommands."""
    global _debug
    _debug = debug
    # --verbose implies --debug
    if verbose:
        _debug = True


@app.command()
def build(
    source: Annotated[
        str | None,
        typer.Option("--source", help="Source directory containing Markdown files."),
    ] = None,
    output: Annotated[
        str | None,
        typer.Option("--output", help="Output root directory for generated files."),
    ] = None,
    format: Annotated[
        BuildFormat,
        typer.Option("--format", help="Build format: html, pdf, or all."),
    ] = BuildFormat.html,
) -> None:
    """Build documentation to HTML, PDF, or both."""
    if format == BuildFormat.html:
        html_path = build_html(source, output)
        console.print(f"[green]HTML built successfully:[/green] {html_path}")
    elif format == BuildFormat.pdf:
        pdf_path = build_pdf(source, output)
        console.print(f"[green]PDF built successfully:[/green] {pdf_path}")
    elif format == BuildFormat.all:
        html_path, pdf_output = build_all(source, output)
        console.print(f"[green]HTML built successfully:[/green] {html_path}")
        if pdf_output:
            console.print(f"[green]PDF built successfully:[/green] {pdf_output}")
        else:
            # Partial success: HTML worked but PDF did not.
            console.print("[yellow]Partial success: HTML generated, PDF failed.[/yellow]")
            raise typer.Exit(code=ExitCode.FAILURE)


@app.command()
def serve(
    source: Annotated[
        str | None,
        typer.Option("--source", help="Source directory containing Markdown files."),
    ] = None,
) -> None:
    """Start a local preview server for the documentation."""
    console.print(f"[bold]Starting preview server for:[/bold] {source or 'docs'}")
    console.print("[dim]Press Ctrl+C to stop.[/dim]")
    serve_preview(source, None)


@app.command()
def clean(
    output: Annotated[
        str | None,
        typer.Option("--output", help="Output root directory to clean."),
    ] = None,
) -> None:
    """Remove generated build files."""
    removed = clean_output(output)
    if removed:
        for path in removed:
            console.print(f"[green]Removed:[/green] {path}")
    else:
        console.print("[dim]Nothing to clean.[/dim]")


@app.command()
def archive(
    format: Annotated[
        str,
        typer.Option("--format", help="Archive format (zip)."),
    ] = "zip",
    output: Annotated[
        str | None,
        typer.Option("--output", help="Output root directory."),
    ] = None,
) -> None:
    """Archive built documentation into a ZIP file."""
    if format != "zip":
        console.print(f"[red]Unsupported archive format: {format}[/red]")
        raise typer.Exit(code=ExitCode.USER_ERROR)
    zip_path = archive_zip(output)
    # Convert bytes to human-readable MiB for the user.
    size_mb = zip_path.stat().st_size / (1024 * 1024)
    console.print(f"[green]Archive created:[/green] {zip_path} ({size_mb:.1f} MB)")


def _handle_exception(exc: BaseException) -> None:
    """Map a raised exception to a Typer exit with the correct exit code.

    `DocsError` instances carry their own exit code.  Unexpected errors
    are printed with an optional traceback (controlled by ``--debug``).
    """
    if isinstance(exc, DocsError):
        console.print(f"[red]Error:[/red] {exc}")
        if _debug:
            console.print_exception()
        raise typer.Exit(code=int(exc.exit_code))
    # Re-raise Typer's own Exit exceptions so they propagate normally.
    if isinstance(exc, typer.Exit):
        raise
    console.print(f"[red]Unexpected error:[/red] {exc}")
    if _debug:
        console.print_exception()
    raise typer.Exit(code=ExitCode.FAILURE)


def main() -> None:
    """Run the CLI application with top-level exception handling.

    This is the entry point referenced by ``pyproject.toml``'s
    ``[project.scripts]`` and by ``python -m docsbuildtool``.
    """
    try:
        app()
    except Exception as exc:
        _handle_exception(exc)


if __name__ == "__main__":
    main()
