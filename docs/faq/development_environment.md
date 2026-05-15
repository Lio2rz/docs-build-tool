# 开发环境 FAQ

<!-- BEGIN: auto-generated -->

## 如何安装完整开发依赖？

```powershell
poetry install --with dev-group --no-root
```

这会安装所有开发依赖（代码格式化、类型检查、测试、文档构建）。

## 只安装文档构建依赖？

```powershell
poetry install --with doc-group --no-root
```

## 为什么使用 Python 3.13？

`pyproject.toml` 声明 `requires-python = ">=3.13"`。项目使用了 Python 3.11+ 的 `StrEnum` 等特性。

## 为什么 `package-mode = false`？

项目不发布为 pip 包，仅作为 Poetry 管理的本地工具运行。`poetry install --no-root` 只安装依赖，不安装项目本身。CLI 入口通过 `poetry run docs` 调用。

## 如何验证环境正确？

```powershell
poetry run python -c "import docsbuildtool; print(docsbuildtool.__version__)"
poetry run mkdocs --version
poetry run pytest --version
```

<!-- END: auto-generated -->
