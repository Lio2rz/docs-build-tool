# 环境变量

<!-- BEGIN: auto-generated -->

项目所有运行时配置均通过 CLI 命令行参数传入（如 `--source`、`--output`、`--format`），无需环境变量。代码中未读取任何环境变量，也没有 `.env.example` 或 `.env.template` 文件。

| 变量名 | 必填 | 默认值 | 说明 | 使用位置 |
| --- | --- | --- | --- | --- |
| 无 | — | — | 当前项目未定义环境变量，所有配置通过 CLI 参数传递。 | — |

CLI 命令概览（`docs` 为入口）：

| 命令 | 参数 | 说明 |
| --- | --- | --- |
| `docs build` | `--source`（默认 `docs`）、`--output`（默认 `site`）、`--format html/pdf/all` | 构建 HTML/PDF 文档 |
| `docs serve` | `--source`（默认 `docs`） | 启动开发预览服务器 |
| `docs clean` | `--output`（默认 `site`） | 清理构建输出目录 |
| `docs archive` | `--format zip`、`--output` | 打包构建产物为 zip |

全局选项：`--version`、`--debug`、`--verbose` / `-v`。

<!-- END: auto-generated -->
