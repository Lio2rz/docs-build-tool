# 模块划分

<!-- BEGIN: auto-generated -->

## 实际模块

| 模块 | 路径 | 职责 | 不应承担的责任 |
| --- | --- | --- | --- |
| `docsbuildtool.cli` | `src/docsbuildtool/cli.py` | Typer 应用定义，4 个命令（build/serve/clean/archive），全局选项（--version/--debug/--verbose），Rich 控制台输出 | 不实现构建逻辑、不直接调用外部工具 |
| `docsbuildtool.config` | `src/docsbuildtool/config.py` | 路径解析（`resolve_source`/`resolve_output`），MkDocs 配置生成（`generate_mkdocs_config`/`generate_pdf_config`），SUMMARY.md 生成，路径保护（`_is_path_protected`/`validate_paths`），`ResolvedConfig` 数据类 | 不执行构建命令、不处理 CLI 参数 |
| `docsbuildtool.builder` | `src/docsbuildtool/builder.py` | HTML/PDF 构建编排（`build_html`/`build_pdf`/`build_all`），`BuildFormat` 枚举（html/pdf/all），子进程调用 mkdocs build | 不处理配置生成、不处理输出清理 |
| `docsbuildtool.serve` | `src/docsbuildtool/serve.py` | 本地预览服务器（`serve_preview`），阻塞式 mkdocs serve 子进程 | 不处理批量构建、不生成配置 |
| `docsbuildtool.clean` | `src/docsbuildtool/clean.py` | 构建产物清理（`clean_output`），删除 html/、pdf/、archive/ 子目录和 `docsbuildtool-*` 临时工作目录 | 不构建、不归档 |
| `docsbuildtool.archive` | `src/docsbuildtool/archive.py` | ZIP 归档（`archive_zip`），使用 zipfile.ZIP_DEFLATED 打包 html/ + pdf/ 产物 | 不构建、不清理 |
| `docsbuildtool.errors` | `src/docsbuildtool/errors.py` | `ExitCode` 枚举（SUCCESS/FAILURE/USER_ERROR/ENV_MISSING），`DocsError` 异常基类，`ConfigError`（USER_ERROR）、`BuildError`（FAILURE）、`EnvMissingError`（ENV_MISSING） | 不包含业务流程、不处理 I/O |

## 模块间关系

```text
cli ──imports──> config, builder, serve, clean, archive, errors
config ──imports──> errors
builder ──imports──> config, errors
serve ──imports──> config, errors
clean ──imports──> (stdlib only: pathlib)
archive ──imports──> (stdlib only: pathlib, zipfile)
errors ──imports──> (stdlib only: enum)
```

## 关键边界约束

- `cli.py` 是唯一直接使用 `typer` 和 `rich` 的模块。
- `config.py` 和 `builder.py` 仅依赖 `errors.py` 和标准库，不依赖 CLI 框架。
- `clean.py` 和 `archive.py` 仅依赖标准库（pathlib、zipfile），保持最大可复用性。
- `errors.py` 仅依赖标准库（enum），不形成任何项目内依赖。
- 配置生成逻辑（`config.py`）与构建执行逻辑（`builder.py`）完全分离，可独立测试。

<!-- END: auto-generated -->
