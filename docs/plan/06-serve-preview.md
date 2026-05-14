# 开发计划：本地预览

<!-- BEGIN: auto-generated -->

## 目标

实现 `docs serve`，用于本地预览 Markdown 文档生成的 HTML 站点。

## 接口/行为

命令：

```powershell
docs serve
docs serve --source <directory>
docs serve --output <directory>
```

行为：

- 默认源目录为 `docs`。
- 复用源配置解析模块生成临时 MkDocs 配置。
- 默认预览 HTML，不触发 PDF 构建。
- 监听和端口先使用 MkDocs 默认值，后续可扩展参数。
- 命令为长运行进程，用户使用 Ctrl+C 停止。

## 实现步骤

1. 在 CLI 中新增 `serve` 子命令。
2. 复用配置解析逻辑，将 `site_dir` 指向 `<output>/html`。
3. 调用 MkDocs serve 流程。
4. 处理 KeyboardInterrupt，正常退出。
5. 输出本地预览地址和源目录。
6. 为测试提供可 mock 的 MkDocs 调用边界。

## 影响范围

- 需要构建服务暴露 serve 入口。
- 测试不能启动真实阻塞服务器，必须 mock。
- 用户文档需要说明 serve 是本地预览，不生成 PDF。

## 测试用例

- `docs serve --help` 显示 source/output 选项。
- mock MkDocs serve，断言传入配置文件路径正确。
- source 不存在时返回非零。
- Ctrl+C 时退出不输出 traceback。
- 含空格路径的 source 可传入 serve。

## 验收标准

- 本地执行 `docs serve` 可预览默认 `docs` 目录。
- 命令复用 `summary.md` 导航和 Material 主题。
- 测试不会因真实服务器阻塞。
- 停止服务后不会留下源目录改动。

## 风险与注意事项

- 端口冲突由 MkDocs 默认行为处理；后续如需要再扩展 `--dev-addr`。
- Windows 下 Ctrl+C 行为与 Unix 不完全一致，需要手动或 CI smoke 验证。
- serve 输出目录可能包含临时文件，需与 clean 规则兼容。

<!-- END: auto-generated -->
