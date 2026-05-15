# 术语列表

<!-- BEGIN: auto-generated -->

| 术语 | 定义 |
| --- | --- |
| 构建产物 | 由工具生成的 HTML、PDF 或 ZIP 归档文件。 |
| 文档源目录 | 包含 Markdown 文件和资源的输入目录（默认 `docs/`）。 |
| 输出目录 | 构建产物存放位置（默认 `site/`，含 html/pdf/archive 子目录）。 |
| 严格模式 | `mkdocs build --strict`，断链或缺失资源时报错。 |
| 适配器 | 封装第三方工具调用的模块边界（如 `generate_pdf_config` 适配 mkdocs-with-pdf）。 |
| 依赖组 | Poetry dependency group，按用途组织（dev-group, doc-group, test-group）。 |
| MkDocs | Python 静态站点生成器，项目 HTML 构建核心。 |
| Material for MkDocs | MkDocs 主题，提供 Material Design 风格界面。 |
| literate-nav | MkDocs 插件，通过 `summary.md` 定义导航结构。 |
| section-index | MkDocs 插件，为目录章节生成索引页。 |
| mkdocs-with-pdf | MkDocs 插件，将文档站点导出为单个 PDF 文件。 |
| Typer | Python CLI 框架，基于类型注解构建命令行接口。 |
| Rich | Python 终端美化库，提供彩色输出和格式化。 |
| Poetry | Python 依赖管理工具，用于管理项目依赖和虚拟环境。 |
| pathlib | Python 标准库模块，面向对象的文件系统路径处理。 |

<!-- END: auto-generated -->
