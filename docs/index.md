# docsbuildtool

![Python](https://img.shields.io/badge/python-%3E%3D3.13-3776AB)
![Rich](https://img.shields.io/badge/rich-15.0.0-4B8BBE)
![Typer](https://img.shields.io/badge/typer-0.25.1-4B8BBE)
![Markdown](https://img.shields.io/badge/markdown-3.10.2-4B8BBE)
![MkDocs](https://img.shields.io/badge/mkdocs-1.6.1-4B8BBE)
![mkdocs-literate-nav](https://img.shields.io/badge/mkdocs--literate--nav-0.6.3-4B8BBE)
![mkdocs-material](https://img.shields.io/badge/mkdocs--material-9.7.6-4B8BBE)
![mkdocs-section-index](https://img.shields.io/badge/mkdocs--section--index-0.3.12-4B8BBE)
![mkdocs-with-pdf](https://img.shields.io/badge/mkdocs--with--pdf-0.9.3-4B8BBE)
![pymdown-extensions](https://img.shields.io/badge/pymdown--extensions-10.21.3-4B8BBE)
![PyYAML](https://img.shields.io/badge/pyyaml-6.0.3-4B8BBE)
![pytest](https://img.shields.io/badge/pytest-9.0.3-4B8BBE)
![pytest-cov](https://img.shields.io/badge/pytest--cov-7.1.0-4B8BBE)
![Ruff](https://img.shields.io/badge/ruff-0.15.12-4B8BBE)

`docsbuildtool` 是一个 Python 文档构建工具项目，目标是将指定目录中的结构化 Markdown 文档转换为静态 HTML 文档，并支持生成 PDF 文档。

## 项目目标

- 使用 MkDocs 生态生成静态 HTML 文档站点。
- 使用 `docs/summary.md` 作为 MkDocs 导航源，避免在 `mkdocs.yml` 中硬编码完整导航。
- 支持通过 `mkdocs-with-pdf` 从同一套 Markdown 文档生成 PDF。
- 保持输入目录、输出目录和 MkDocs 配置路径可配置。
- 构建过程中不修改源 Markdown 文档。

## 当前状态

项目目前处于早期骨架阶段：

- Python 包名：`docsbuildtool`
- 源码目录：`src/docsbuildtool/`
- 测试目录：`tests/`
- 开发文档目录：`docs/`
- MkDocs 配置：`mkdocs.yml`
- 导航定义：`docs/summary.md`

## 依赖分组

项目使用 Poetry 管理依赖：

- `project.dependencies`：运行期基础依赖，包括 `rich` 和 `typer`。
- `doc-group`：文档构建依赖，包括 MkDocs、Material 主题、导航插件和 PDF 插件。
- `test-group`：测试依赖，包括 `pytest` 和 `pytest-cov`。
- `dev-group`：开发聚合组，包含 `doc-group`、`test-group` 和 `ruff`。

## 快速验证

```powershell
poetry install --with dev-group
poetry check --lock
poetry run ruff check .
poetry run pytest
poetry run mkdocs build
```

当前 `tests/` 目录还没有测试用例，因此 `poetry run pytest` 可能显示 `no tests ran`。

## 文档构建

HTML 文档构建：

```powershell
poetry run mkdocs build
```

构建输出目录为 `site/`。该目录是构建产物，默认不提交到版本控制。
