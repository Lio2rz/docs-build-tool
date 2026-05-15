# 测试依赖

<!-- BEGIN: auto-generated -->

## `test-group`

| 包 | 版本约束 | 用途 |
| --- | --- | --- |
| `pytest` | `>=9.0.3,<10.0.0` | Python 测试框架，配置 minversion=8.3, strict-config, strict-markers。 |
| `pytest-cov` | `>=6.0,<8.0` | pytest 覆盖率插件，配置 branch=true, source=["docsbuildtool"], show_missing=true。 |

## 测试概况

当前 `tests/` 目录包含 35 个测试用例，分布在 6 个测试文件中：

| 文件 | 测试数 | 测试内容 |
| --- | --- | --- |
| `test_cli.py` | 9 | CLI 命令入口：--help、--version、未知命令、build/serve/clean/archive 子命令帮助、全局 --verbose 选项。 |
| `test_config.py` | 12 | 配置解析：resolve_source、resolve_output、generate_mkdocs_config、validate_paths（含路径保护）、ResolvedConfig 数据类。 |
| `test_builder.py` | 6 | 构建流程：build_html、build_pdf、build_all（含 PDF 失败非致命场景）、BuildFormat 枚举。 |
| `test_clean.py` | 4 | 输出清理：clean_output 删除 html/pdf/archive 目录及临时目录。 |
| `test_archive.py` | 3 | 归档打包：archive_zip 生成 archive/docs.zip，验证 ZIP_DEFLATED 压缩。 |
| `test_package.py` | 1 | 包元数据：验证版本号为 0.1.0。 |

## 运行测试

```bash
# 运行全部测试
poetry run pytest

# 带详细输出
poetry run pytest -v

# 带覆盖率报告
poetry run pytest --cov=docsbuildtool --cov-report=term-missing

# 运行指定文件
poetry run pytest tests/test_config.py -v
```

测试框架使用 Typer 的 `CliRunner` 进行 CLI 命令测试，使用 pytest 的 `tmp_path` fixture 创建临时文件系统环境。

<!-- END: auto-generated -->
