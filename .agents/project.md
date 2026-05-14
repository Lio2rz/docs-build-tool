# Project Notes

## Product Goal

Build a Python documentation conversion tool with two primary workflows:

1. Convert a specified directory of structured Markdown documents into a static
   HTML documentation site.
2. Convert the same kind of Markdown documentation source into PDF output.

The implementation should use MkDocs as the HTML generation foundation. PDF
support may be implemented through an MkDocs-compatible plugin or through a
separate PDF rendering step, but it must preserve navigation order, headings,
links, code blocks, images, and tables as much as practical.

## Source Documents

Assume the input directory contains human-authored Markdown arranged in a
structured hierarchy. Future implementation should make these concerns explicit:

- input directory path
- output directory or output file path
- generated or supplied `mkdocs.yml`
- navigation order
- project/site title
- assets directory handling
- strict mode for broken links or missing assets

Do not mutate source Markdown files during normal build operations.

## Architecture Expectations

- Keep CLI orchestration separate from conversion/build logic.
- Prefer typed functions with explicit path parameters.
- Use `pathlib.Path` for filesystem operations.
- Keep MkDocs configuration generation deterministic.
- Keep PDF generation pluggable so the project can switch between an MkDocs
  plugin and another renderer if needed.
- Treat build output as disposable unless the user asks for examples to be
  committed.

## Naming

The project is named `docsbuildtool`. Keep package imports under
`docsbuildtool`. Use "MkDocs" in user-facing docs and `mkdocs` in dependency
metadata.
