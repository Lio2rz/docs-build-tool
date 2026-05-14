# 环境配置概述

<!-- BEGIN: auto-generated -->

当前项目没有 `.env.example`、`.env.template` 或专用 `config/` 目录。

## 配置来源

| 来源 | 用途 |
| --- | --- |
| `pyproject.toml` | 项目元数据、依赖分组、测试配置、覆盖率配置、Ruff 配置。 |
| `poetry.lock` | 锁定依赖版本和哈希。 |
| `AGENTS.md` | 编码 agent 的项目级工作规则。 |
| `.agents/` | agent 共享项目知识和开发说明。 |
| `.github/copilot-instructions.md` | GitHub Copilot 指令入口。 |
| `CLAUDE.md` | Claude Code 指令入口。 |
| `.codex/config.toml` | Codex 项目配置占位。 |

<!-- TODO: 实现 CLI 后，补充命令行参数、默认值和配置覆盖顺序。 -->

<!-- END: auto-generated -->
