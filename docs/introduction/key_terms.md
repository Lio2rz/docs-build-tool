# 关键术语

<!-- BEGIN: auto-generated -->

| 术语 | 说明 |
| --- | --- |
| Markdown 源目录 | 用户提供的结构化 `.md` 文件目录，是 HTML/PDF 构建的输入。默认路径为 `docs/`。 |
| MkDocs | Python 文档站点生成器，本项目通过子进程调用 `mkdocs build` / `mkdocs serve` 生成静态 HTML。 |
| mkdocs-material | MkDocs 主题插件，提供 Material Design 风格的文档站点外观。 |
| literate-nav | MkDocs 插件，通过 `SUMMARY.md` 定义导航结构，替代手动配置 nav。 |
| section-index | MkDocs 插件，使目录节点可点击并指向对应章节首页。 |
| mkdocs-with-pdf | MkDocs 插件，将文档站点导出为单页 PDF 文件。 |
| `mkdocs.yml` | MkDocs 的站点配置文件，定义站点标题、导航、主题、插件和扩展。由 `generate_mkdocs_config()` 自动生成。 |
| `SUMMARY.md` | 由配置层自动生成的导航清单文件，定义文档目录树和页面顺序。 |
| 静态 HTML | 可直接由静态文件服务器托管的文档站点输出，位于 `<output>/html/`。 |
| PDF 输出 | 从同一套 Markdown 文档构建出的 PDF 交付物，位于 `<output>/pdf/docs.pdf`。 |
| 构建产物 | HTML 目录、PDF 文件等可重复生成的输出内容，默认位于 `site/`。 |
| Typer | Python CLI 框架，基于类型注解定义命令参数。本项目用其构建 `docs` 命令行入口。 |
| Rich | Python 终端美化库，提供彩色输出、进度条、表格渲染。本项目用于 CLI 输出格式化。 |
| pathlib | Python 标准库模块，提供面向对象的文件系统路径操作。本项目所有路径处理均使用 `pathlib.Path`。 |
| Poetry | Python 依赖管理和打包工具。本项目使用 Poetry 2.x 管理依赖组（dev-group、doc-group、test-group）。 |
| Agent 指令 | `AGENTS.md` 和 `.agents/` 中维护的 AI 编码助手项目约束。 |

<!-- END: auto-generated -->
