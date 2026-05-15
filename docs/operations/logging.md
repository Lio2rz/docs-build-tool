# 日志管理

<!-- BEGIN: auto-generated -->

## 当前实现

项目使用 **Rich** 库的 `Console` 对象进行终端输出，非结构化日志系统。

- `Console.print()` — 带 Rich 标记的彩色输出（`[green]`、`[red]`、`[dim]` 等）
- `--verbose` / `-v` / `--debug` — 控制是否显示完整 traceback
- 错误输出通过 `_handle_exception` 统一处理，区分 `DocsError`（可预期）和未预期异常

## 没有实现的功能

- 不写日志文件
- 不使用 Python logging 模块
- 不使用结构化日志（JSON 等）
- 无日志轮转、分级存储

## 诊断命令

```powershell
poetry run docs build --verbose    # 详细构建输出
poetry run mypy src/               # 类型检查
poetry run ruff check .            # 代码 lint
poetry run pytest -v               # 运行测试
```

<!-- END: auto-generated -->
