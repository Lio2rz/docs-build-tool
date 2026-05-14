# AGENTS.md

This file is the canonical entry point for all coding agents working in this
repository. Keep shared agent guidance here and under `.agents/`. Tool-specific
files such as `CLAUDE.md`, `.github/copilot-instructions.md`, and `.codex/`
must point back here instead of carrying separate project rules.

## Project

`docsbuildtool` is a Python package for turning a directory of structured
Markdown documentation into static HTML, and optionally into PDF.

Use the MkDocs ecosystem for site generation. The Python package name is
`mkdocs`; do not introduce an unrelated `mkdoc` dependency unless the user asks
for that exact package after the distinction is explained.

## Repository Layout

- `src/docsbuildtool/`: project source.
- `tests/`: automated tests.
- `pyproject.toml`: Python packaging and dependency metadata.
- `.agents/`: shared agent documentation and operating notes.

## Agent Rules

- Read `.agents/README.md` and the relevant `.agents/*.md` file before making
  non-trivial changes.
- Prefer small, reviewable changes that preserve the current project structure.
- Do not rewrite generated documentation sources unless the user explicitly
  asks to edit source content.
- Keep Markdown input paths, output paths, and MkDocs config paths configurable.
- Use `pathlib` for filesystem work and avoid hard-coded platform separators.
- Treat generated HTML/PDF output as build artifacts unless the user requests
  checked-in examples.
- Add or update tests when behavior changes.

## Expected Commands

Use Poetry when available:

```powershell
poetry install --no-root
poetry run pytest
```

For MkDocs behavior, prefer package code and tests over ad hoc shelling out.
When validating generated sites manually, use:

```powershell
poetry run mkdocs build -f <mkdocs.yml> -d <output-dir>
```

## More Guidance

- `.agents/project.md`: product scope and architecture expectations.
- `.agents/development.md`: dependencies, commands, testing, and build notes.
- `.agents/compatibility.md`: how Codex, Claude, and GitHub Copilot are wired.
