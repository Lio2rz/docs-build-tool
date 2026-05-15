# 环境配置概述

<!-- BEGIN: auto-generated -->

项目运行时配置全部通过 CLI 命令行参数传入，无需 `.env` 文件或环境变量。

## 配置来源

| 来源 | 用途 |
| --- | --- |
| `pyproject.toml` | 项目元数据（name、version、requires-python>=3.13）、依赖分组（project、doc-group、test-group、dev-group）、Poetry 脚本入口（docs = docsbuildtool.cli:app）、pytest 配置、coverage 配置、Black、isort、mypy、Ruff 配置。 |
| `poetry.lock` | 锁定所有依赖的精确版本和哈希值，由 `poetry lock` 生成。 |
| `mkdocs.yml` | MkDocs 站点配置：Material 主题（zh）、插件（search、literate-nav、section-index）、Markdown 扩展（admonition、pymdownx.superfences 含 mermaid、toc 等）。 |
| `.github/workflows/lint.yml` | CI 代码检查：push/PR 触发，Python 3.13 + Poetry，执行 black、isort、ruff、mypy、mkdocs build --strict。 |
| `.github/workflows/tests.yml` | CI 测试：push/PR 触发，Python 3.13 + Poetry，安装 test-group 后执行 pytest。 |
| `.editorconfig` | 跨编辑器统一缩进、编码、换行符等格式约定。 |
| `.gitignore` | 排除 Python 缓存、构建输出、IDE 配置等。 |
| `AGENTS.md` / `.agents/` | Agent 共享项目规则和开发说明。 |

## CLI 配置覆盖顺序

1. CLI 命令行参数（最高优先级）：`--source`、`--output`、`--format`
2. 代码内置默认值：`resolve_source()` 默认 `"docs"`，`resolve_output()` 默认 `"site"`
3. 用户 `mkdocs.yml`（如存在）：与模板配置合并

无需环境变量或配置文件即可运行所有命令。

<!-- END: auto-generated -->
