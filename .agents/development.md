# Development Notes

## Python

The project currently targets Python `>=3.13` in `pyproject.toml`. Keep new code
compatible with that constraint unless the user asks to change it.

## Dependencies

Expected runtime stack:

- `mkdocs` for static HTML site generation.
- `markdown` and MkDocs-supported Markdown extensions as needed.
- `pymdown-extensions` when richer Markdown behavior is required.
- A PDF path such as `mkdocs-with-pdf`, `weasyprint`, or another renderer chosen
  deliberately for Windows compatibility and CI support.

Before adding dependencies, update `pyproject.toml` and refresh the lock file
with Poetry if dependency resolution is available.

## Commands

Common commands:

```powershell
poetry install --no-root
poetry run pytest
poetry run mkdocs build -f <mkdocs.yml> -d <output-dir>
```

If Poetry is unavailable, use the active Python environment and keep commands
equivalent to the Poetry workflow.

## Testing

Add tests for:

- Markdown directory discovery and ordering.
- MkDocs config generation.
- HTML build orchestration.
- PDF build orchestration, including renderer selection and failure messages.
- Missing input paths, invalid output paths, and broken asset references.

Prefer temporary directories in tests. Do not rely on local absolute paths.

## Generated Output

Do not commit generated HTML or PDF output by default. If examples become useful,
place them under an explicit examples or fixtures directory and document why
they are checked in.
