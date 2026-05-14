# 开发计划：跨平台行为

<!-- BEGIN: auto-generated -->

## 目标

确保 CLI 在 Windows、macOS、Linux 上行为一致，重点覆盖路径、文件删除、压缩、子进程调用和错误消息。

## 接口/行为

跨平台要求适用于全部命令：

- `docs build`
- `docs serve`
- `docs clean`
- `docs archive`

统一规则：

- 所有路径使用 `pathlib.Path`。
- 不拼接 shell 命令字符串。
- 不假设路径分隔符。
- 支持带空格路径。
- 输出和 zip 内部路径稳定。

## 实现步骤

1. 建立路径工具函数，集中处理 resolve、relative、safe delete。
2. 子进程调用使用参数列表或直接 Python API。
3. 归档使用标准库 `zipfile`。
4. 文件删除使用 `shutil`，不使用 shell。
5. CI 增加 `ubuntu-latest`、`windows-latest`、`macos-latest` 矩阵。
6. 使用临时目录测试含空格路径和多层目录。

## 影响范围

- 所有命令实现都要遵循跨平台工具函数。
- CI 运行时间会增加。
- 文档示例应优先使用 PowerShell 兼容命令，并说明其他 shell 可等价执行。

## 测试用例

- Windows 路径含空格时 build 成功。
- Unix 路径含空格时 build 成功。
- clean 在各平台拒绝清理项目根。
- zip 内路径在各平台均为 `html/...`、`pdf/...`。
- CLI 不依赖 `rm`、`cp`、`zip` 等外部命令。
- 非 ASCII 文件名可被复制或构建。

## 验收标准

- GitHub Actions 三平台测试通过。
- 本地 Windows PowerShell 可运行 README 中的命令。
- 构建产物结构在三平台一致。
- 错误消息不包含平台专有实现细节。

## 风险与注意事项

- PDF 渲染跨平台依赖较复杂，可能需要单独标记集成测试。
- 文件权限错误在不同平台表现不同，测试应关注错误类型和用户消息。
- 路径大小写敏感性在 Windows 和 Unix 不同，不能依赖大小写冲突行为。

<!-- END: auto-generated -->
