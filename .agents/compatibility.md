# Agent Compatibility

## Canonical Source

The canonical shared instructions are:

1. `AGENTS.md`
2. `.agents/README.md`
3. Focused files under `.agents/`

All tool-specific instruction files should point to those files.

## Codex

Codex reads the repository `AGENTS.md`. Keep Codex-specific runtime settings in
`.codex/` only when needed. Do not duplicate project rules in `.codex/`.

## Claude Code

Claude Code reads the repository `CLAUDE.md` as project memory. This repository
uses `CLAUDE.md` as a shim that points Claude back to `AGENTS.md` and `.agents/`.

## GitHub Copilot

GitHub Copilot uses `.github/copilot-instructions.md` for repository-wide
instructions and can also consume `AGENTS.md` in supported agent workflows. Keep
the Copilot file short and self-contained, with a pointer to `AGENTS.md`.

## Updating Instructions

When project behavior changes:

1. Update `AGENTS.md` for rules every agent must see.
2. Update the focused `.agents/*.md` document for details.
3. Update tool-specific files only if their pointer or unique integration note
   needs to change.
