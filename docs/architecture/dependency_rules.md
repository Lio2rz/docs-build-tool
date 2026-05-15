# 依赖规则

<!-- BEGIN: auto-generated -->

## 已知约束

- 使用 `pathlib.Path` 处理所有文件系统路径。
- Markdown 输入路径、输出路径和 MkDocs 配置路径均可配置（通过 `--source`、`--output` 选项）。
- 生成 HTML/PDF 时不修改源 Markdown 文件。
- 构建产物默认视为可丢弃输出，不作为源码提交（已在 `.gitignore` 中排除 `site/`）。
- 使用 `mkdocs` 包，绝不引入无关的 `mkdoc` 包。

## 实际依赖方向

```text
cli ──> config, builder, serve, clean, archive, errors
config ──> errors
builder ──> config, errors
serve ──> config, errors
clean ──> (纯 stdlib)
archive ──> (纯 stdlib)
errors ──> (纯 stdlib: enum)
```

## 核心规则

1. **CLI 依赖隔离**：`cli.py` 可以依赖所有应用模块，但应用模块不应依赖 `typer` 或 `rich`。
2. **配置与构建分离**：`config.py` 负责配置生成，`builder.py` 负责执行，两者通过 `ResolvedConfig` 数据类传递信息。
3. **构建器不修改源文件**：`builder.py` 仅读取源文件、生成临时配置、调用 mkdocs 子进程，不修改用户源 Markdown。
4. **错误向上传播**：所有模块通过 `errors.py` 的结构化异常（`DocsError` 及其子类）向上传播错误，CLI 层统一捕获并转换为退出码和用户消息。
5. **PDF 非致命**：`build_all()` 中 PDF 失败不阻塞整体返回，HTML 产物正常保留。
6. **clean/archive 独立**：`clean.py` 和 `archive.py` 仅依赖标准库，可独立使用或测试。
7. **测试不依赖绝对路径**：所有测试使用 `tmp_path` fixture 创建临时目录。

## 工具约束

`pyproject.toml` 中配置的代码质量工具：

| 工具 | 配置 | 说明 |
| --- | --- | --- |
| Ruff | line-length=120, target=py313, rules: B/E/F/I/UP | Lint 检查 |
| Black | line-length=120 | 代码格式化 |
| isort | profile=black, line_length=120 | import 排序 |
| Mypy | strict=true | 静态类型检查 |

<!-- END: auto-generated -->
