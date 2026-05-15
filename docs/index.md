# Docs Build Tool

[![Python](https://img.shields.io/badge/python-%3E%3D3.13-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow)](https://github.com/Lio2rz/docs-build-tool/blob/main/LICENSE)
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

<!-- BEGIN: auto-generated -->

`docsbuildtool` 是一个跨平台 CLI 工具，使用 MkDocs 生态将结构化 Markdown 文档构建为静态 HTML 和 PDF。

## 快速开始

```powershell
poetry install --with dev-group --no-root
pip install -e .
docs build
```

## CLI 命令

| 命令 | 说明 |
|------|------|
| `docs build` | 构建 HTML（默认），`--format pdf` 或 `--format all` |
| `docs serve` | 启动本地 MkDocs 预览服务器 |
| `docs clean` | 安全删除生成的构建文件 |
| `docs archive --format zip` | 将构建输出打包为 ZIP |

## 全局选项

| 选项 | 说明 |
|------|------|
| `--version` | 显示版本号并退出 |
| `--debug` | 错误时显示完整回溯 |
| `--verbose` / `-v` | 启用详细输出 |

## 退出码

| 退出码 | 含义 |
|--------|------|
| 0 | 成功 |
| 1 | 构建失败 |
| 2 | 用户输入错误 |
| 3 | 运行环境缺失 |

## 当前状态

项目 12 个开发阶段已全部完成：

- **Phase 01**: Typer CLI 入口 — 4 条命令 (build/serve/clean/archive) ✓
- **Phase 02**: 源目录解析与 MkDocs 配置生成 ✓
- **Phase 03**: HTML 构建（mkdocs build 子进程） ✓
- **Phase 04**: PDF 构建（mkdocs-with-pdf 插件） ✓
- **Phase 05**: 全量构建与输出目录布局 ✓
- **Phase 06**: 本地预览服务器（mkdocs serve） ✓
- **Phase 07**: 安全清理命令（路径保护） ✓
- **Phase 08**: ZIP 归档 ✓
- **Phase 09**: 跨平台行为统一（pathlib） ✓
- **Phase 10**: 测试套件与 CI — 35 个测试通过 ✓
- **Phase 11**: 用户文档 ✓
- **Phase 12**: 代码审查与进度治理 ✓

## 项目信息

| 项目 | 详情 |
|------|------|
| 项目名 | `docsbuildtool` |
| 版本 | `0.1.0` |
| Python | `>=3.13` |
| CLI 框架 | Typer + Rich |
| 文档引擎 | MkDocs (Material 主题) |
| 源码目录 | `src/docsbuildtool/` |
| 测试目录 | `tests/` |
| 依赖管理 | Poetry（非打包模式） |
| 许可证 | MIT |
| 版权 | Copyright (c) Lio2rz 2026 |
| 开发状态 | Pre-Alpha |

## 文档导航

- [介绍](introduction/introduction.md) — 项目概述与关键术语
- [入门指南](getting_started/getting_started.md) — 环境搭建与快速上手
- [架构设计](architecture/architecture.md) — 系统架构与模块划分
- [开发计划](plan/index.md) — 12 阶段开发计划
- [配置和设置](configuration_and_settings/configuration_and_settings.md) — 配置文件与环境变量
- [项目依赖](project_dependencies/dependencies_overview.md) — 运行时与开发依赖
- [构建和部署](build_and_deployment/build_and_deployment.md) — 构建工具链与 CI/CD
- [版本控制](version_control/version_control_overview.md) — Git 分支与提交规范
- [最佳实践](best_practices/best_practices.md) — 编码标准与设计模式
- [测试](testing/testing.md) — 测试策略与工具
- [安全](security/security.md) — 安全最佳实践
- [运行维护](operations/operations.md) — 日志与运行维护

<!-- END: auto-generated -->
