# 测试类型

<!-- BEGIN: auto-generated -->

当前测试目录结构：

```text
tests/
├── __init__.py          # 包标记（空文件）
├── fixtures/
│   └── minimal-docs/    # 最小 Markdown 文档树（测试用）
│       ├── index.md
│       └── summary.md
├── test_cli.py          # CLI 命令测试（9 个用例）
├── test_config.py       # 配置解析测试（12 个用例）
├── test_builder.py      # HTML/PDF 构建测试（6 个用例）
├── test_clean.py        # 清理输出测试（4 个用例）
├── test_archive.py      # 归档打包测试（3 个用例）
└── test_package.py      # 包版本元数据测试（1 个用例）
```

## 测试文件详情

| 文件 | 用例数 | 测试范围 |
| --- | --- | --- |
| `test_cli.py` | 9 | `--help` 输出包含 4 条命令、`--version` 显示版本号、未知命令返回退出码 2、子命令 `build --help`/`serve --help`/`clean --help`/`archive --help`、全局 `--verbose`/`-v` 选项。 |
| `test_config.py` | 12 | `resolve_source()` 默认值/cwd/自定义、`resolve_output()` 默认值/cwd/自定义、`generate_mkdocs_config()` 生成有效 YAML、`validate_paths()` 路径保护拒绝（项目根/系统根/HOME/WINDIR）、`ResolvedConfig` 数据类字段。 |
| `test_builder.py` | 6 | `BuildFormat` 枚举值、`build_html()` 成功构建、`build_pdf()` PDF 输出、`build_all()` HTML+PDF 同时构建、PDF 失败非致命（HTML 仍成功）、子进程错误映射为 BuildError。 |
| `test_clean.py` | 4 | `clean_output()` 删除 html/ 目录、删除 pdf/ 目录、删除 archive/ 目录、删除临时 `docsbuildtool-*` 目录。 |
| `test_archive.py` | 3 | `archive_zip()` 生成 `archive/docs.zip`、zip 文件包含 html/ 和 pdf/ 内容、使用 ZIP_DEFLATED 压缩。 |
| `test_package.py` | 1 | 验证包版本号为 `0.1.0`，与 `pyproject.toml` 一致。 |

<!-- END: auto-generated -->
