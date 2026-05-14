# CI/CD

<!-- BEGIN: auto-generated -->

当前 `.github/` 目录只有 `copilot-instructions.md`，没有工作流文件。

## 建议流水线

1. 安装 Python 3.13。
2. 安装 Poetry。
3. 执行 `poetry install --with dev-group`。
4. 执行 `poetry check --lock`。
5. 执行 `poetry run ruff check .`。
6. 执行 `poetry run pytest`。
7. 在需要时构建示例 HTML/PDF 文档。

<!-- TODO: 新增 `.github/workflows/*.yml` 后，在此记录触发条件和阶段。 -->

<!-- END: auto-generated -->
