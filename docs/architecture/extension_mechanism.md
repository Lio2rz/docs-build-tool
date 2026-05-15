# 扩展机制

<!-- BEGIN: auto-generated -->

当前项目 v0.1.0 未实现插件或扩展系统，但架构预留了明确的扩展点。以下基于实际代码结构描述可扩展方向。

## 现有扩展点

| 扩展点 | 位置 | 说明 |
| --- | --- | --- |
| PDF 渲染器替换 | `builder.py` → `build_pdf()` | 当前通过 `mkdocs-with-pdf` 插件实现，可替换为 `generate_pdf_config()` 返回不同的插件配置，或切换为 WeasyPrint 等独立渲染器。 |
| MkDocs 插件扩展 | `config.py` → `generate_mkdocs_config()` | 当前注入 `literate-nav` 和 `section-index` 插件，可在生成配置时注入额外 MkDocs 插件。 |
| Markdown 扩展 | `config.py` → mkdocs.yml 模板 | 当前配置 `pymdown-extensions`，可通过自定义 mkdocs.yml 模板添加更多 Markdown 扩展。 |
| 构建格式 | `builder.py` → `BuildFormat` 枚举 | 当前支持 html/pdf/all，可通过扩展枚举和对应的构建函数支持新格式（如 epub、docx 等）。 |
| 输出目录布局 | `config.py` → `resolve_output()` | 输出子目录结构可通过配置输出路径灵活控制。 |

## MkDocs 插件链

当前模板 `mkdocs.yml` 中启用的插件链：

```yaml
plugins:
  - search              # 站点搜索
  - literate-nav        # SUMMARY.md 导航定义
  - section-index       # 章节索引页
  - with-pdf            # PDF 导出（仅 PDF 构建时）
```

PDF 构建时，`generate_pdf_config()` 在基础上追加 `with-pdf` 插件配置。
HTML 构建时通过 `generate_mkdocs_config()` 仅包含前三项。

## 设计原则

- **子进程隔离**：不直接使用 MkDocs Python API，通过 `subprocess.run` 调用 mkdocs 命令行。这使 MkDocs 本身成为可替换的外部依赖。
- **配置即接口**：扩展主要通过生成不同的 `mkdocs.yml` 配置实现，而非修改源码逻辑。
- **枚举驱动**：`BuildFormat` 枚举（html/pdf/all）驱动构建分支，新增格式只需添加枚举值和对应的构建函数。

## 未来扩展建议

- 为 PDF 构建器定义抽象接口（`Builder` protocol），便于多实现注册。
- 支持 `.md` front matter 中的 per-page 配置覆盖。
- 提供 pre-build / post-build 钩子机制，允许用户在构建前后执行自定义脚本。

<!-- END: auto-generated -->
