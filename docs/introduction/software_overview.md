# 软件概述

<!-- BEGIN: auto-generated -->

`docsbuildtool` 是一个由 Poetry 管理依赖的 Python 文档构建项目，目标是把指定目录下的结构化 Markdown 文档转换为可发布的静态 HTML 文档，并支持生成 PDF 文档。

## 目标用户

- 需要维护内部开发文档、项目文档或知识库的开发团队。
- 希望用 Markdown 作为源格式，并生成静态站点或 PDF 交付物的文档维护者。
- 希望在命令行或自动化流程中批量构建文档的工程团队。

## 核心能力

| 能力 | 当前状态 | 说明 |
| --- | --- | --- |
| Markdown 目录输入 | 规划中 | 输入应是结构化 Markdown 目录，后续实现需要支持目录发现和导航顺序。 |
| HTML 静态站点生成 | 规划中 | 使用 MkDocs 生态作为基础。 |
| PDF 文档生成 | 规划中 | 当前依赖规划使用 `mkdocs-with-pdf`，实现时应保持可替换性。 |
| CLI | 规划中 | `pyproject.toml` 已包含 `typer`，但当前尚未实现 CLI 模块。 |
| 测试 | 待补充 | `tests/` 目录存在，但暂无测试用例。 |

## 非目标

- 不在正常构建流程中修改源 Markdown 文件。
- 不把生成的 HTML/PDF 作为默认提交内容。
- 不引入与 MkDocs 无关的 `mkdoc` 包。

<!-- END: auto-generated -->
