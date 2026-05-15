# 常见问题与症状

<!-- BEGIN: auto-generated -->

| 症状 | 可能原因 | 处理方式 |
| --- | --- | --- |
| PDF 构建失败：`No module named` | 缺少 PDF 依赖（`doc-group` 未安装） | `poetry install --with doc-group --no-root` |
| `mkdocs: command not found` | mkdocs 未在 PATH 中 | 使用 `poetry run mkdocs` 或 `poetry install --with dev-group --no-root` |
| `poetry lock` 提示 lock 过期 | 修改了依赖版本但未刷新 | `poetry lock --no-update` |
| `pyproject.toml` 验证失败 | `requires-python` 不兼容 | 确认使用 Python 3.13+ |
| HTML 构建完成但 `index.html` 不存在 | MkDocs 构建异常但未报错 | 检查 `mkdocs.yml` 配置和源目录结构 |
| `Output directory is a protected path` | 输出路径指向系统目录 | 更换输出目录，避免使用 `/`、`~`、`C:\Windows` 等 |
| 测试发现 0 个用例 | 测试依赖未安装 | `poetry install --with test-group --no-root` |
| `zipfile.BadZipFile` | 构建产物不完整 | 运行 `docs build --format all` 后重新 `docs archive` |

<!-- END: auto-generated -->
