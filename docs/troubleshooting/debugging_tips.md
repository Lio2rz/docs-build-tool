# 调试技巧

<!-- BEGIN: auto-generated -->

## 类型检查

```powershell
poetry run mypy src/
```

## 代码风格

```powershell
poetry run ruff check .
poetry run ruff format --check .
```

## 测试

```powershell
poetry run pytest -v --tb=short        # 详细输出
poetry run pytest -vv --tb=long        # 完整 traceback
poetry run pytest --cov=docsbuildtool  # 覆盖率
```

## 构建验证

```powershell
poetry run mkdocs build -f mkdocs.yml --strict  # 严格模式（断链报错）
poetry run docs build --verbose                 # 详细构建输出
poetry run docs build --format all --debug      # 全量构建 + 调试
```

## 依赖诊断

```powershell
poetry run python -c "import mkdocs; print(mkdocs.__version__)"
poetry run python -c "import yaml; print(yaml.__version__)"
poetry check --lock
```

## 清理

```powershell
poetry run docs clean --output site/    # 清理构建产物
```

<!-- END: auto-generated -->
