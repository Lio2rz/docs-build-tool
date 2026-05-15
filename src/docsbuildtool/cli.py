from typing import Annotated

import typer
from rich.console import Console

from docsbuildtool.errors import DocsError, ExitCode

app = typer.Typer(
    name="docs",
    help="Build static HTML and PDF documentation from structured Markdown directories.",
    no_args_is_help=True,
)
console = Console()
_DEBUG = False


def _version_callback(value: bool) -> None:
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
    global _DEBUG
    _DEBUG = debug
    if verbose:
        _DEBUG = True


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
        str | None,
        typer.Option("--format", help="Build format: html, pdf, or all."),
    ] = None,
) -> None:
    """Build documentation to HTML, PDF, or both."""
    console.print("[yellow]build command is not yet implemented.[/yellow]")


@app.command()
def serve(
    source: Annotated[
        str | None,
        typer.Option("--source", help="Source directory containing Markdown files."),
    ] = None,
) -> None:
    """Start a local preview server for the documentation."""
    console.print("[yellow]serve command is not yet implemented.[/yellow]")


@app.command()
def clean(
    output: Annotated[
        str | None,
        typer.Option("--output", help="Output root directory to clean."),
    ] = None,
) -> None:
    """Remove generated build files."""
    console.print("[yellow]clean command is not yet implemented.[/yellow]")


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
    console.print("[yellow]archive command is not yet implemented.[/yellow]")


def _handle_exception(exc: BaseException) -> None:
    if isinstance(exc, DocsError):
        console.print(f"[red]Error:[/red] {exc}")
        if _DEBUG:
            console.print_exception()
        raise typer.Exit(code=int(exc.exit_code))
    if isinstance(exc, typer.Exit):
        raise
    console.print(f"[red]Unexpected error:[/red] {exc}")
    if _DEBUG:
        console.print_exception()
    raise typer.Exit(code=ExitCode.FAILURE)


def main() -> None:
    try:
        app()
    except Exception as exc:
        _handle_exception(exc)


if __name__ == "__main__":
    main()
