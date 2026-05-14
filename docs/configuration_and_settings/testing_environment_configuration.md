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

```powershell
poetry install --with test-group
```

<!-- TODO: 增加真实测试后，补充覆盖率目标、测试数据和 CI 执行方式。 -->

<!-- END: auto-generated -->
