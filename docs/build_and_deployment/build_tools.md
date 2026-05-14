# 构建工具

<!-- BEGIN: auto-generated -->

| 工具 | 用途 |
| --- | --- |
| Poetry | 依赖管理、包安装、构建后端配置。 |
| MkDocs | 生成静态 HTML 文档站点。 |
| `mkdocs-with-pdf` | 规划用于 PDF 输出。 |
| Ruff | 代码检查。 |
| pytest | 测试运行。 |

## 常用命令

```powershell
poetry check --lock
poetry run ruff check .
poetry run pytest
poetry run mkdocs build -f <mkdocs.yml> -d <output-dir>
```

<!-- END: auto-generated -->
