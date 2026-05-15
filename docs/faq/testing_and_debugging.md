# 测试和调试 FAQ

<!-- BEGIN: auto-generated -->

## 如何运行测试？

```powershell
poetry run pytest -v
```

当前 35 个测试全部通过。

## 如何查看测试覆盖率？

```powershell
poetry run pytest --cov=docsbuildtool --cov-report=term-missing
```

## CI 包含什么？

GitHub Actions 两个工作流（`.github/workflows/`）：
- `lint.yml` — ruff 检查 + mypy 类型检查
- `tests.yml` — pytest 测试套件

## 如何调试构建失败？

```powershell
poetry run docs build --format all --verbose --debug
```

会显示完整的异常 traceback。

## 如何检查代码风格？

```powershell
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy src/
```

<!-- END: auto-generated -->
