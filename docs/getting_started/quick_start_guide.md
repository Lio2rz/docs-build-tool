# 快速入门

<!-- BEGIN: auto-generated -->

## 最小验证流程

```shell
poetry install --with dev-group
poetry check --lock
poetry run ruff check .
poetry run pytest
```

## 预期结果

- `poetry check --lock` 输出 `All set!`。
- `poetry run ruff check .` 输出 `All checks passed!`。
- `poetry run pytest` 报告 35 passed。

## 构建当前项目文档

项目自身文档位于 `docs/` 目录，可用自身 CLI 构建：

```shell
# 构建 HTML
poetry run docs build

# 构建 PDF
poetry run docs build --format pdf

# 构建全部格式
poetry run docs build --format all

# 启动本地预览（默认端口 8000）
poetry run docs serve
```

构建完成后：
- HTML 输出位于 `site/html/`
- PDF 输出位于 `site/pdf/docs.pdf`
- ZIP 归档位于 `site/archive/docs.zip`（需执行 `poetry run docs archive`）

## 自定义输入输出

```shell
poetry run docs build --source my-docs --output out
poetry run docs build --format pdf --source my-docs --output out
poetry run docs clean --output out
poetry run docs archive --output out
```

## 调试

```shell
# 显示完整 traceback
poetry run docs build --debug

# 启用详细输出
poetry run docs build -v
```

<!-- END: auto-generated -->
