# 快速入门

<!-- BEGIN: auto-generated -->

当前项目尚未实现 CLI 和构建逻辑，因此快速入门以验证开发环境为主。

## 最小验证流程

```powershell
poetry install --with dev-group
poetry check --lock
poetry run ruff check .
poetry run pytest
```

## 预期结果

- `poetry check --lock` 输出 `All set!`。
- `poetry run ruff check .` 输出 `All checks passed!`。
- `poetry run pytest` 能启动 pytest；在没有测试用例时会报告 `no tests ran`。

## 后续最小功能验证

<!-- TODO: CLI 实现后，在此补充从示例 Markdown 目录生成 HTML/PDF 的命令。 -->

建议未来提供类似命令：

```powershell
poetry run docsbuildtool build-html --source docs-src --output site
poetry run docsbuildtool build-pdf --source docs-src --output docs.pdf
```

<!-- END: auto-generated -->
