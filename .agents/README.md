# Agent Guidance Root

This directory is the shared home for agent-facing project knowledge. The root
`AGENTS.md` is the entry point; files in this directory hold focused details so
tool-specific instruction files can stay short.

## Files

- `project.md`: what this project is building and the constraints agents should
  preserve.
- `development.md`: dependency, command, testing, and documentation build notes.
- `compatibility.md`: how Codex, Claude Code, and GitHub Copilot should consume
  the shared instructions.

## Maintenance Rules

- Keep durable project rules in `AGENTS.md` or `.agents/`.
- Keep tool-specific files as pointers to this root unless a tool genuinely
  needs unique configuration.
- If a rule is duplicated for compatibility, update the canonical copy first and
  then refresh the duplicate.
- Avoid storing secrets, tokens, local machine paths, or personal preferences in
  this directory.
