# 软件概述

<!-- BEGIN: auto-generated -->

`docsbuildtool` 是一个由 Poetry 管理依赖的 Python CLI 文档构建工具（v0.1.0），将结构化 Markdown 目录转换为静态 HTML 和 PDF 交付物。项目基于 MkDocs 生态（mkdocs-material + literate-nav + section-index + with-pdf），使用 Typer + Rich 提供命令行界面。

## 目标用户

- 需要维护内部开发文档、项目文档或知识库的开发团队。
- 希望用 Markdown 作为源格式，并生成静态站点或 PDF 交付物的文档维护者。
- 希望在命令行或 CI/CD 流水线中批量构建文档的工程团队。

## 核心能力

| 能力 | 当前状态 | 说明 |
| --- | --- | --- |
| Markdown 目录输入 | 已实现 | `resolve_source()` 自动发现 `docs/` 目录，支持 `--source` 自定义路径。 |
| HTML 静态站点生成 | 已实现 | 通过子进程调用 `mkdocs build`，使用 mkdocs-material 主题，输出至 `<output>/html/`。 |
| PDF 文档生成 | 已实现 | 通过 `mkdocs-with-pdf` 插件生成，输出至 `<output>/pdf/docs.pdf`。PDF 失败不阻塞 HTML 构建。 |
| CLI | 已实现 | 基于 Typer + Rich，提供 4 个子命令：`build`、`serve`、`clean`、`archive`。支持 `--debug`、`--verbose/-v` 全局选项。 |
| 测试 | 已完成 | 6 个测试文件、35 个测试用例全部通过。覆盖 CLI（9）、配置（12）、构建（6）、清理（4）、归档（3）、包导入（1）。 |

## 非目标

- 不在正常构建流程中修改源 Markdown 文件。
- 不把生成的 HTML/PDF 作为默认提交内容。
- 不引入与 MkDocs 无关的 `mkdoc` 包。

<!-- END: auto-generated -->
