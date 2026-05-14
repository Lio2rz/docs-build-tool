# GitHub Copilot Instructions

Use `AGENTS.md` as the canonical project instruction file. Additional shared
agent notes live under `.agents/`.

Project summary: `docsbuildtool` is a Python package that converts structured
Markdown documentation directories into static HTML with MkDocs and can also
produce PDF documentation output.

Follow the repository rules in `AGENTS.md`: keep paths configurable, use
`pathlib`, preserve source Markdown content during builds, and add tests for
behavior changes.
