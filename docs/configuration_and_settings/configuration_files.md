# 配置文件

<!-- BEGIN: auto-generated -->

| 文件 | 用途 | 关键内容 |
| --- | --- | --- |
| `pyproject.toml` | Python 项目核心配置 | 项目元数据（name、version、license=MIT）、依赖分组（project、doc-group、test-group、dev-group）、pytest.ini_options、coverage.run/report、Black（line-length=120）、isort（profile=black）、mypy（disallow_untyped_defs=true）、Ruff（line-length=120, select B/E/F/I/UP）。 |
| `poetry.lock` | 依赖锁文件 | 由 Poetry 自动生成，锁定所有依赖版本和哈希，不应手工编辑。 |
| `mkdocs.yml` | MkDocs 文档构建配置 | 站点名称、页脚版权 + MIT License 徽章、Material 主题（language=zh、custom_dir=overrides）、额外 CSS、插件（search、literate-nav、section-index）、Markdown 扩展。 |
| `docs/overrides/` | 模板覆写目录 | 自定义页脚（`partials/footer.html` — 左侧版权 / 右侧 License 徽章）、自定义样式（`stylesheets/extra.css`）。 |
| `LICENSE` | 开源许可证 | MIT License。 |
| `COPYRIGHT` | 版权声明 | Copyright (c) Lio2rz 2026. All rights reserved. |
| `.editorconfig` | 编辑器格式约定 | 文件编码、换行符、缩进等跨编辑器统一规则。 |
| `.gitignore` | Git 忽略规则 | 忽略 Python 缓存、构建产物（site/）、IDE 配置和本地文件。 |
| `.github/workflows/lint.yml` | CI 代码检查流水线 | push/PR 触发，安装 dev-group，执行 poetry check、black --check、isort --check-only、ruff check、mypy、mkdocs build --strict。 |
| `.github/workflows/tests.yml` | CI 测试流水线 | push/PR 触发，安装 test-group，执行 pytest。 |
| `AGENTS.md` | Agent 统一入口 | 项目规则、命令和 agent 子目录指引。 |
| `.agents/*.md` | Agent 共享说明 | 项目目标、开发说明、兼容策略。 |
| `CLAUDE.md` | Claude Code 入口 | 指向 `AGENTS.md` 和 `.agents/`。 |
| `.github/copilot-instructions.md` | Copilot 入口 | 指向统一 agent 规则。 |
| `.codex/config.toml` | Codex 配置占位 | 当前仅包含注释。 |
| `.claude/settings.local.json` | Claude 本地设置 | 当前为空 JSON 对象。 |

<!-- END: auto-generated -->
