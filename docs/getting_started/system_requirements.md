# 系统要求

<!-- BEGIN: auto-generated -->

## 基础环境

| 项目 | 要求 | 来源 |
| --- | --- | --- |
| Python | `>=3.13` | `pyproject.toml` |
| 包管理器 | Poetry 2.x | `poetry.lock` 由 Poetry 2.3.0 生成 |
| 操作系统 | Windows/macOS/Linux | `pyproject.toml` 标记为 OS Independent |
| 网络 | 需要访问 PyPI 用于首次依赖安装 | Poetry 依赖解析 |

## 运行时依赖

| 包名 | 版本要求 | 用途 |
| --- | --- | --- |
| rich | `>=15.0.0` | CLI 终端美化输出 |
| typer | `>=0.15` | CLI 命令定义与参数解析 |

## 文档构建依赖（doc-group）

| 包名 | 版本要求 | 用途 |
| --- | --- | --- |
| mkdocs | `>=1.6.1` | 静态站点生成引擎 |
| mkdocs-material | `>=9.6` | Material Design 主题 |
| mkdocs-literate-nav | — | 通过 SUMMARY.md 定义导航 |
| mkdocs-section-index | — | 章节索引页支持 |
| mkdocs-with-pdf | — | PDF 导出插件 |
| pymdown-extensions | — | Markdown 语法扩展 |
| markdown | — | Markdown 解析 |
| pyyaml | — | YAML 配置文件解析 |

## 开发依赖（dev-group）

| 包名 | 版本要求 | 用途 |
| --- | --- | --- |
| black | `>=26.0` | 代码格式化（行宽 120） |
| isort | `>=8.0` | import 排序 |
| mypy | `>=2.1.0` | 静态类型检查（strict 模式） |
| ruff | `>=0.9` | 代码检查（规则 B/E/F/I/UP） |

## 测试依赖

| 包名 | 版本要求 | 用途 |
| --- | --- | --- |
| pytest | `>=9.0.3` | 测试框架 |
| pytest-cov | — | 测试覆盖率 |

## 外部服务

当前项目没有数据库、缓存、消息队列或外部服务依赖。PDF 生成依赖 `mkdocs-with-pdf`，无需额外系统级 PDF 渲染依赖。

<!-- END: auto-generated -->
