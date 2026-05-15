# 测试环境配置

<!-- BEGIN: auto-generated -->

测试配置位于 `pyproject.toml`：

```toml
[tool.pytest.ini_options]
minversion = "8.3"
addopts = "-ra --strict-config --strict-markers"
testpaths = ["tests"]
```

覆盖率配置：

```toml
[tool.coverage.run]
branch = true
source = ["docsbuildtool"]

[tool.coverage.report]
show_missing = true
skip_covered = true
```

## 测试依赖安装

```bash
poetry install --with test-group --no-root
```

## 测试文件结构

```
tests/
├── __init__.py              # 包标记
├── fixtures/
│   └── minimal-docs/        # 测试用最小 Markdown 文档树
│       ├── index.md
│       └── summary.md
├── test_cli.py              # CLI 命令测试（9 个）
├── test_config.py           # 配置解析测试（12 个）
├── test_builder.py          # HTML/PDF 构建测试（6 个）
├── test_clean.py            # 清理输出测试（4 个）
├── test_archive.py          # 归档打包测试（3 个）
└── test_package.py          # 包版本元数据测试（1 个）
```

共计 35 个测试用例，使用 Typer `CliRunner` 和 `tmp_path` fixture。

## 运行测试

```bash
# 运行全部测试
poetry run pytest

# 带覆盖率报告
poetry run pytest --cov=docsbuildtool --cov-report=term-missing

# 运行单个测试文件
poetry run pytest tests/test_config.py -v
```

## CI 测试配置

CI 测试通过 `.github/workflows/tests.yml` 在工作流中执行，安装 `test-group` 后运行 `poetry run pytest`。代码检查由独立的 `lint.yml` 工作流负责。

<!-- END: auto-generated -->
