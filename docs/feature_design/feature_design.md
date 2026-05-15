# 特性设计

<!-- BEGIN: auto-generated -->

12 阶段开发已全部完成。当前没有处于设计阶段的新特性。

## 已实现功能

| 特性 | CLI 命令 | 模块 |
| --- | --- | --- |
| Markdown 源解析 | (自动) | `config.py` — `resolve_source()`, `_generate_summary()` |
| MkDocs 配置生成 | (自动) | `config.py` — `generate_mkdocs_config()` |
| HTML 构建 | `docs build --format html` | `builder.py` — `build_html()` |
| PDF 构建 | `docs build --format pdf` | `builder.py` — `build_pdf()` |
| 全量构建 | `docs build --format all` | `builder.py` — `build_all()` |
| 预览服务 | `docs serve` | `serve.py` — `serve_preview()` |
| 清理产物 | `docs clean` | `clean.py` — `clean_output()` |
| ZIP 归档 | `docs archive` | `archive.py` — `archive_zip()` |

## 设计流程

新特性设计请遵循：

1. 明确输入、输出和用户场景
2. 定义 CLI 交互方式（Typer command）
3. 设计核心数据结构和错误模型（DocsError 层级）
4. 编写测试计划（pytest, 优先临时目录）
5. 记录兼容性影响

模板参见 [feature_template.md](feature_template.md)。

<!-- END: auto-generated -->
