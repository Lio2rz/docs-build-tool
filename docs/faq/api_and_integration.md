# API 和集成 FAQ

<!-- BEGIN: auto-generated -->

## 项目是否提供 HTTP API？

不提供。`docsbuildtool` 是纯本地 CLI 工具，通过 Typer 命令行接口交互。无 HTTP 服务、无 REST API、无 GraphQL 端点。

## CLI 即接口

所有功能通过 `poetry run docs <command>` 访问，4 个命令：`build`、`serve`、`clean`、`archive`。

## 可以集成到 CI 吗？

可以，且已配置。GitHub Actions 工作流（`lint.yml` + `tests.yml`）在每次推送时自动运行检查和测试。

## 是否有 Python API 可供导入？

有。`src/docsbuildtool/` 下各模块可独立导入使用：

```python
from docsbuildtool.builder import build_html, build_pdf, build_all, BuildFormat
from docsbuildtool.clean import clean_output
from docsbuildtool.archive import archive_zip
from docsbuildtool.errors import DocsError, ExitCode
```

<!-- END: auto-generated -->
