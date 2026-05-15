# 测试工具

<!-- BEGIN: auto-generated -->

## 测试工具

| 工具 | 版本约束 | 用途 |
| --- | --- | --- |
| pytest | `>=9.0.3,<10.0.0` | 测试运行器，minversion=8.3, --strict-config, --strict-markers, testpaths=["tests"]。 |
| pytest-cov | `>=6.0,<8.0` | 覆盖率统计，branch=true, source=["docsbuildtool"], show_missing=true。 |
| Typer CliRunner | 内置（Typer 附带） | CLI 命令测试运行器，无需启动真实进程即可测试命令解析和输出。 |
| pytest tmp_path | 内置（pytest 附带） | 创建隔离的临时文件系统目录，测试后自动清理。 |

## 命令

```bash
# 运行全部测试
poetry run pytest

# 详细模式
poetry run pytest -v

# 带覆盖率
poetry run pytest --cov=docsbuildtool --cov-report=term-missing

# 仅运行单个文件
poetry run pytest tests/test_config.py -v

# 运行匹配关键字的测试
poetry run pytest -k "build"
```

## 配置（pyproject.toml）

```toml
[tool.pytest.ini_options]
minversion = "8.3"
addopts = "-ra --strict-config --strict-markers"
testpaths = ["tests"]

[tool.coverage.run]
branch = true
source = ["docsbuildtool"]

[tool.coverage.report]
show_missing = true
skip_covered = true
```

<!-- END: auto-generated -->
