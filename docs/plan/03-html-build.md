# 开发计划：HTML 构建

<!-- BEGIN: auto-generated -->

## 目标

实现 `docs build --format html`，将结构化 Markdown 文档构建为静态 HTML 站点。`docs build` 不指定格式时默认执行 HTML 构建。

## 接口/行为

命令：

```powershell
docs build
docs build --format html
docs build --source <directory> --output <directory>
```

行为：

- 默认源目录：`docs`。
- 默认输出根目录：`site`。
- HTML 输出目录：`<output>/html`。
- 使用源配置解析模块生成 MkDocs 配置。
- 调用 MkDocs 构建 HTML，不直接 shell 拼接字符串。

## 实现步骤

1. 定义 `BuildFormat` 枚举，包含 `html`、`pdf`、`all`。
2. 在 Typer build 命令中将默认 format 设置为 `html`。
3. 调用源配置解析模块，得到临时 MkDocs 配置。
4. 将 `site_dir` 设置为 `<output>/html`。
5. 调用 MkDocs Python API 或安全的子进程封装执行构建。
6. 收集构建结果，输出 HTML 目录位置。
7. 将失败转换为统一 `BUILD_FAILED` 错误。

## 影响范围

- `docs build` 的默认行为会被锁定为 HTML。
- `site/html` 成为后续 serve、archive、clean 的默认 HTML 产物位置。
- CI 可使用 HTML 构建作为最小集成验证。

## 测试用例

- `docs build` 生成 `<output>/html/index.html`。
- `docs build --format html` 与默认行为一致。
- 指定 `--source` 使用自定义源目录构建成功。
- 指定 `--output` 输出到自定义目录。
- 源目录为空时报错。
- MkDocs 构建失败时返回非零退出码。
- 构建不修改源 Markdown 文件。

## 验收标准

- HTML 构建可在 Windows、macOS、Linux 运行。
- 输出目录结构稳定为 `<output>/html`。
- `docs build` 帮助信息说明默认格式为 `html`。
- 构建成功后控制台输出可读的产物路径。

## 风险与注意事项

- MkDocs 的 warning 在 strict 模式下可能升级为失败，测试需明确是否启用 strict。
- 如果源目录使用自定义主题或插件，可能需要额外依赖；错误消息需指导用户。
- HTML 输出目录存在时的清理/覆盖策略需与 `clean` 文档保持一致。

<!-- END: auto-generated -->
