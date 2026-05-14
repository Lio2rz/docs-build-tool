# 开发计划：ZIP 归档

<!-- BEGIN: auto-generated -->

## 目标

实现 `docs archive --format zip`，将构建生成的文件打包为 zip。只实现正确拼写 `archive`，不实现需求文本中的拼写错误 `achive`。

## 接口/行为

命令：

```powershell
docs archive
docs archive --format zip
docs archive --format zip --source <directory>
docs archive --format zip --output <directory>
```

行为：

- 归档格式第一版仅支持 `zip`，且为默认值；`--format` 与 `build --format` 语义一致。
- `--output <directory>` 表示输出根目录（与 `build`/`serve`/`clean` 一致），归档文件路径固定为 `<output>/archive/docs.zip`。
- 归档内容来自 `<output>/html` 或 `<output>/pdf` 中已存在产物，至少需要一个，**始终跳过 `<output>/archive` 自身**，避免 zip 套 zip。
- 如果没有构建产物，返回非零并提示先运行 build。
- 重复执行时先删除旧 zip 再写入，行为确定。

## 实现步骤

1. 在 CLI 中新增 `archive` 子命令。
2. 定义归档格式枚举 `ArchiveFormat`，第一版仅允许 `zip`，并作为 `--format` 默认值。
3. 校验 `<output>/html` 或 `<output>/pdf` 至少存在一个。
4. 创建 `<output>/archive`，并在归档前删除已存在的 `docs.zip`。
5. 使用 Python 标准库 `zipfile` 打包，遍历时**显式跳过 `<output>/archive` 目录**，避免 zip 套 zip。
6. 保持 zip 内部路径相对输出根目录（例如 `html/index.html`、`pdf/docs.pdf`），统一使用正斜杠。
7. 输出 zip 文件路径和文件大小（通过 `rich`）。

## 影响范围

- 依赖 build 输出布局。
- clean 需要知道 archive 子目录。
- 用户文档需要说明 archive 不会自动构建。

## 测试用例

- HTML 产物存在时生成 zip。
- HTML 和 PDF 产物都存在时 zip 包含两类文件，且**不包含 `archive/` 自身**。
- 无产物时命令失败并提示运行 build。
- 重复执行 archive 覆盖旧 zip（先删除后写入）。
- zip 内路径使用正斜杠，跨平台一致。
- 指定非 zip 格式时报错。
- 不存在 `achive` 命令，调用时报未知命令。

## 验收标准

- `docs archive --format zip` 生成 `<output>/archive/docs.zip`，省略 `--format` 时等价。
- zip 可以被 Python `zipfile` 打开并列出内容。
- zip 内部不包含绝对路径，也不包含 `archive/` 子目录自身。
- 命令只支持 `archive`，不支持 `achive`。

## 风险与注意事项

- `archive` 的 `--format` 与 `build` 的 `--format` 共享同一参数族，避免歧义；`--output` 在所有子命令中统一表示目录。
- 如果后续要支持 tar.gz，需扩展 `ArchiveFormat` 枚举和测试。
- 归档时必须排除 `archive/` 目录，避免 zip 套 zip。

<!-- END: auto-generated -->
