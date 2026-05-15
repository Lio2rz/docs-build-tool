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
_debug = False


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
    global _debug
    _debug = debug
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
    size_mb = zip_path.stat().st_size / (1024 * 1024)
    console.print(f"[green]Archive created:[/green] {zip_path} ({size_mb:.1f} MB)")


def _handle_exception(exc: BaseException) -> None:
    if isinstance(exc, DocsError):
        console.print(f"[red]Error:[/red] {exc}")
        if _debug:
            console.print_exception()
        raise typer.Exit(code=int(exc.exit_code))
    if isinstance(exc, typer.Exit):
        raise
    console.print(f"[red]Unexpected error:[/red] {exc}")
    if _debug:
        console.print_exception()
    raise typer.Exit(code=ExitCode.FAILURE)


def main() -> None:
    try:
        app()
    except Exception as exc:
        _handle_exception(exc)


if __name__ == "__main__":
    main()
