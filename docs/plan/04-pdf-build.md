# 开发计划：PDF 构建

<!-- BEGIN: auto-generated -->

## 目标

实现 `docs build --format pdf`，使用 `mkdocs-with-pdf` 从 Markdown 文档生成 PDF 文件。

## 接口/行为

命令：

```powershell
docs build --format pdf
docs build --format pdf --source <directory> --output <directory>
```

行为：

- PDF 输出目录：`<output>/pdf`。
- PDF 文件路径：`<output>/pdf/docs.pdf`。
- 使用与 HTML 相同的源配置解析逻辑。
- 使用 `mkdocs-with-pdf` 插件生成 PDF。
- PDF 构建失败时给出依赖或渲染错误提示。

## 实现步骤

1. 在构建配置中启用 `mkdocs-with-pdf` 插件，仅用于 PDF 构建。
2. 将 HTML 中间输出和 PDF 输出隔离到 `<output>/pdf` 工作目录。
3. 配置 PDF 文件名为 `docs.pdf`。
4. 调用 MkDocs 构建流程生成 PDF。
5. 构建后检查 `<output>/pdf/docs.pdf` 是否存在且非空。
6. 捕获 WeasyPrint、字体、图片资源等常见失败并转换为清晰错误。

## 影响范围

- `doc-group` 中的 PDF 依赖成为运行该功能的必要条件。
- CI 如果执行 PDF 集成测试，需要确认 Linux 环境满足渲染依赖。
- 用户文档需要说明 PDF 构建的系统依赖风险。

## 测试用例

- 最小 Markdown 源目录生成非空 `docs.pdf`。
- 包含图片、表格、代码块的源目录生成 PDF。
- 缺失图片时错误可读。
- 指定输出目录时 PDF 写入 `<output>/pdf/docs.pdf`。
- PDF 插件不可用时提示安装 `doc-group`。
- Windows/macOS/Linux 至少执行轻量 PDF smoke test；如 CI 环境不稳定，可将完整 PDF 测试标记为集成测试。

## 验收标准

- `docs build --format pdf` 成功生成 `docs.pdf`。
- PDF 构建不影响 HTML 输出目录。
- PDF 文件路径固定且在命令输出中展示。
- 失败时返回非零退出码并说明原因。

## 风险与注意事项

- PDF 渲染依赖比 HTML 更复杂，跨平台字体和图片处理是主要风险。
- `mkdocs-with-pdf` 插件会影响 MkDocs 插件列表，必须避免污染 HTML 构建配置。
- PDF 构建速度较慢，不应作为 `docs build` 默认行为。

<!-- END: auto-generated -->
