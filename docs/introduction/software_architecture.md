# 软件架构概览

<!-- BEGIN: auto-generated -->

项目已从骨架阶段演进为完整的 7 模块架构，源码位于 `src/docsbuildtool/`。

## 当前仓库结构

```text
docsbuildtool/
├── src/docsbuildtool/
│   ├── __init__.py
│   ├── cli.py           # Typer CLI（4 命令 + 全局选项）
│   ├── config.py        # 配置解析与 MkDocs 配置生成
│   ├── builder.py       # HTML/PDF 构建编排
│   ├── serve.py         # 本地预览服务器
│   ├── clean.py         # 构建产物清理
│   ├── archive.py       # ZIP 归档
│   └── errors.py        # 统一异常与退出码
├── tests/
│   ├── test_cli.py      (9 tests)
│   ├── test_config.py   (12 tests)
│   ├── test_builder.py  (6 tests)
│   ├── test_clean.py    (4 tests)
│   ├── test_archive.py  (3 tests)
│   └── test_package.py  (1 test)
├── pyproject.toml
├── poetry.lock
├── AGENTS.md
├── .agents/
└── .github/workflows/   # CI: lint + tests
```

## 实际数据流

```text
CLI (cli.py) ── 参数解析、Rich 输出 ──┐
                                       │
      ┌────────────────────────────────┘
      v
配置层 (config.py) ── resolve_source() / resolve_output()
      │                  generate_mkdocs_config()
      │                  validate_paths()
      v
构建层 (builder.py) ── build_html() / build_pdf() / build_all()
      │                 子进程调用 mkdocs build
      v
MkDocs 生态 ── mkdocs-material + literate-nav
                + section-index + with-pdf
      │
      +──> HTML 输出目录 (site/html/)
      +──> PDF 输出文件 (site/pdf/docs.pdf)

辅助命令:
  serve.py   ── mkdocs serve（阻塞式本地预览）
  clean.py   ── 删除 html/ pdf/ archive/ 及临时工作目录
  archive.py ── 将 html/ + pdf/ 打包为 archive/docs.zip
```

## 分层设计

- **CLI 层 (cli.py)**：基于 Typer 定义 4 个命令（build/serve/clean/archive），使用 Rich 美化终端输出，通过 `--debug` 展示完整 traceback。
- **配置层 (config.py)**：实现 `resolve_source()`、`resolve_output()`、`generate_mkdocs_config()`、`generate_pdf_config()` 和 `validate_paths()`，产出 `ResolvedConfig` 数据类。
- **构建层 (builder.py)**：定义 `BuildFormat` 枚举（html/pdf/all），通过 `subprocess.run` 调用 mkdocs 命令行，实现 `build_html()`、`build_pdf()` 和 `build_all()`。
- **服务层 (serve.py)**：`serve_preview()` 通过子进程启动 mkdocs serve。
- **清理层 (clean.py)**：`clean_output()` 删除 html/、pdf/、archive/ 子目录和临时工作目录。
- **归档层 (archive.py)**：`archive_zip()` 使用 zipfile 将构建产物打包为 ZIP。
- **错误层 (errors.py)**：定义 `ExitCode` 枚举（SUCCESS/FAILURE/USER_ERROR/ENV_MISSING）和结构化异常类 `DocsError`、`ConfigError`、`BuildError`、`EnvMissingError`。

<!-- END: auto-generated -->
