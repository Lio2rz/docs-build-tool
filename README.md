# docsbuildtool

[![Python](https://img.shields.io/badge/python-%3E%3D3.13-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)
[![Poetry](https://img.shields.io/badge/poetry-package_mode-blue)](https://python-poetry.org/)
[![Typer](https://img.shields.io/badge/typer-0.15-4B8BBE)](https://typer.tiangolo.com/)
[![Rich](https://img.shields.io/badge/rich-15.0.0-4B8BBE)](https://rich.readthedocs.io/)
[![MkDocs](https://img.shields.io/badge/mkdocs-1.6.1-4B8BBE)](https://www.mkdocs.org/)
[![Material](https://img.shields.io/badge/mkdocs--material-9.6-4B8BBE)](https://squidfunk.github.io/mkdocs-material/)
[![PDF](https://img.shields.io/badge/mkdocs--with--pdf-0.9.3-4B8BBE)](https://github.com/orzih/mkdocs-with-pdf)
[![pytest](https://img.shields.io/badge/pytest-35%20passed-4B8BBE)](https://docs.pytest.org/)
[![Black](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/lint-ruff-261230)](https://docs.astral.sh/ruff/)
[![mypy](https://img.shields.io/badge/type%20check-mypy-blue)](https://mypy-lang.org/)
[![Lint CI](https://github.com/Lio2rz/docs-build-tool/actions/workflows/lint.yml/badge.svg)](https://github.com/Lio2rz/docs-build-tool/actions/workflows/lint.yml)
[![Test CI](https://github.com/Lio2rz/docs-build-tool/actions/workflows/tests.yml/badge.svg)](https://github.com/Lio2rz/docs-build-tool/actions/workflows/tests.yml)

`docsbuildtool` is a cross-platform CLI tool that converts a directory of structured Markdown documentation into static HTML and PDF, using the MkDocs ecosystem.

## Quick Start

```powershell
# Install dependencies
poetry install --with dev-group --no-root
pip install -e .

# Build HTML documentation
docs build

# Build PDF
docs build --format pdf

# Build both
docs build --format all

# Preview locally
docs serve

# Archive output
docs archive --format zip

# Clean generated files
docs clean
```

Alternatively, use the fallback entry point:

```powershell
python -m docsbuildtool build
```

## Commands

| Command | Description |
|---------|-------------|
| `docs build` | Build HTML docs (default), or `--format pdf`, `--format all` |
| `docs serve` | Start a local MkDocs preview server |
| `docs clean` | Remove generated build files safely |
| `docs archive --format zip` | Archive built output into a ZIP file |

### Options

| Option | Applies to | Description |
|--------|-----------|-------------|
| `--source <dir>` | build, serve | Source directory (default: `docs`) |
| `--output <dir>` | build, clean, archive | Output root directory (default: `site`) |
| `--format html/pdf/all` | build | Build format (default: `html`) |
| `--format zip` | archive | Archive format |
| `--debug` | all | Show full traceback on error |
| `--verbose` / `-v` | all | Enable verbose output |
| `--version` | all | Show version and exit |

## Output Layout

```
<output>/
├── html/          # HTML build output
├── pdf/
│   └── docs.pdf   # PDF output
└── archive/
    └── docs.zip   # Archive output
```

## Dependencies

| Group | Contents |
|-------|----------|
| `project.dependencies` | `rich`, `typer` |
| `doc-group` | MkDocs, Material theme, literate-nav, section-index, mkdocs-with-pdf |
| `test-group` | `pytest`, `pytest-cov` |
| `dev-group` | All above + black, isort, mypy, ruff |

## Development

```powershell
poetry install --with dev-group --no-root
pip install -e .
```

Quality checks:

```powershell
poetry run black --check .
poetry run isort --check-only .
poetry run ruff check .
poetry run mypy src/
poetry run pytest              # 35 tests
poetry run mkdocs build --strict
```

## License

MIT License — see [LICENSE](LICENSE) for details.

Copyright (c) Lio2rz 2026. All rights reserved.
