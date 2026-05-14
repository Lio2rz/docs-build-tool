# 开发计划：清理构建产物

<!-- BEGIN: auto-generated -->

## 目标

实现 `docs clean`，安全清理 CLI 管理的构建产物，避免误删源文件或项目文件。

## 接口/行为

命令：

```powershell
docs clean
docs clean --output <directory>
```

行为：

- 默认清理 `site`。
- 只允许清理构建输出根目录下的 `html`、`pdf`、`archive` 和 CLI 临时工作目录。
- 不清理源目录。
- 不清理项目根目录。
- 删除前解析绝对路径并做安全校验。

## 实现步骤

1. 定义输出布局常量：`html`、`pdf`、`archive`。
2. 实现路径解析，得到 output 的绝对路径。
3. 校验 output 不等于项目根、不等于 source、不为空、不为磁盘根。
4. 仅删除受管理子目录，不递归删除任意传入路径本身。
5. 使用 `shutil.rmtree` 和 `Path`，避免 shell 删除命令。
6. 输出删除摘要。

## 影响范围

- `build` 和 `archive` 依赖同一输出布局。
- 测试需要覆盖高风险路径。
- 用户文档必须强调 clean 的作用范围。

## 测试用例

- 默认清理 `site/html`、`site/pdf`、`site/archive`。
- output 不存在时成功返回并提示无内容可清理。
- output 指向 source 时拒绝。
- output 指向项目根时拒绝。
- output 指向磁盘根或 home 目录时拒绝。
- 含只读文件时返回清晰错误。
- Windows 和 Unix 路径分隔符均可处理。

## 验收标准

- clean 不会删除源 Markdown。
- clean 不会删除项目根文件。
- clean 可重复执行。
- clean 成功后 build 可重新生成产物。

## 风险与注意事项

- 这是最危险的命令，必须优先实现路径保护测试。
- 不要通过 shell 命令删除文件。
- 后续如果允许 `--force`，必须单独设计，不在第一版实现。

<!-- END: auto-generated -->
