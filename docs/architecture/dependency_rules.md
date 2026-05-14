# 依赖规则

<!-- BEGIN: auto-generated -->

## 已知约束

- 使用 `pathlib.Path` 处理文件系统路径。
- 保持 Markdown 输入路径、输出路径和 MkDocs 配置路径可配置。
- 生成 HTML/PDF 时不修改源 Markdown 文件。
- 构建产物默认视为可丢弃输出，不作为源码提交。
- 使用 `mkdocs` 包，而不是无关的 `mkdoc` 包。

## 推荐依赖方向

```text
cli -> application services -> sources/config/builders -> third-party tools
```

## 规则

- `cli` 可以依赖应用服务，但应用服务不应依赖 `typer`。
- 文档扫描逻辑不应依赖 MkDocs 插件，便于单元测试。
- PDF 构建应通过适配器封装，避免核心流程绑定单一插件。
- 错误消息应在边界处转为用户可读文本，核心逻辑保留结构化异常。
- 测试不应依赖本机绝对路径。

## 工具约束

`pyproject.toml` 当前配置了 Ruff：

- 行宽：88
- Python target：`py313`
- lint 规则：`B`、`E`、`F`、`I`、`UP`

<!-- END: auto-generated -->
