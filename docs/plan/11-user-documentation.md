# 开发计划：用户文档

<!-- BEGIN: auto-generated -->

## 目标

为 CLI 和构建流程补齐用户文档，使开发者能够安装、构建、预览、清理和归档文档。

## 接口/行为

需要覆盖的文档主题：

- 安装本地 CLI。
- `docs --help`。
- `docs build` 及 format/source/output 参数。
- `docs serve`。
- `docs clean`。
- `docs archive --output zip`。
- 输出目录结构。
- PDF 依赖和跨平台注意事项。

## 实现步骤

1. 更新 README 快速开始，加入 CLI 安装和最小命令。
2. 在 `docs/getting_started/` 增加 CLI 快速入门。
3. 在 `docs/build_and_deployment/` 增加 HTML/PDF 构建说明。
4. 在 `docs/troubleshooting/` 增加常见错误。
5. 在 `docs/summary.md` 中挂载新增用户文档。
6. 准备 `examples/` 或 `tests/fixtures/` 中的示例文档树。

## 影响范围

- README 和 `docs/index.md` 需要继续保持一致。
- 导航文件 `docs/summary.md` 需要同步更新。
- 文档示例必须与真实 CLI 行为一致。

## 测试用例

- `poetry run mkdocs build --strict` 确认文档链接有效。
- README 中列出的命令在本地或 CI smoke test 中可执行。
- 文档中的输出路径与实际实现一致。
- 文档中不出现 `achive` 拼写作为正式命令。

## 验收标准

- 新用户可以按 README 完成安装和 HTML 构建。
- CLI 每个子命令都有文档说明。
- HTML/PDF/all 的输出路径写法一致。
- MkDocs strict build 通过。

## 风险与注意事项

- 计划文档不是用户手册，功能实现后必须将实际用法写入用户文档。
- 文档示例如果早于功能实现，必须明确标注为计划或后续能力。
- README 和 `docs/index.md` 内容一致性需要持续维护。

<!-- END: auto-generated -->
