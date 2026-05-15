# 项目依赖

<!-- BEGIN: auto-generated -->

本章节说明项目依赖分组、运行期依赖、文档构建依赖、测试依赖和依赖管理规则。项目使用 Poetry 管理依赖，`package-mode = false`，不打包发布到 PyPI。

## 依赖分组

| 分组 | 用途 | 内容 |
| --- | --- | --- |
| `project.dependencies` | CLI 运行期核心依赖 | rich（>=15.0.0,<16.0）、typer（>=0.15,<1.0） |
| `doc-group` | 文档构建依赖 | markdown、mkdocs、mkdocs-material、mkdocs-literate-nav、mkdocs-section-index、mkdocs-with-pdf、pymdown-extensions、pyyaml |
| `test-group` | 测试和覆盖率依赖 | pytest（>=9.0.3,<10.0.0）、pytest-cov（>=6.0,<8.0） |
| `dev-group` | 开发环境聚合组，包含以上所有 | doc-group（include-group）+ test-group（include-group）+ black（>=26.0）、isort（>=8.0）、mypy（>=2.1.0）、ruff（>=0.9） |

## 子文档

- [依赖列表](dependencies_list.md) — 完整依赖清单与版本约束
- [开发依赖](development_dependencies.md) — Lint 工具配置详情
- [测试依赖](testing_dependencies.md) — 测试框架与覆盖率工具
- [依赖管理](dependency_management.md) — Poetry 命令与策略

<!-- END: auto-generated -->
