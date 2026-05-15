# CLI Quick Start

`docs` 是 `docsbuildtool` 的命令行入口，支持构建、预览、清理和归档文档。

## 安装

```powershell
poetry install --with dev-group --no-root
pip install -e .
```

验证安装：

```powershell
docs --help
python -m docsbuildtool --help
```

## 常用命令

### 构建 HTML

```powershell
docs build
docs build --format html
docs build --source my-docs --output out
```

### 构建 PDF

```powershell
docs build --format pdf
```

PDF 输出为 `<output>/pdf/docs.pdf`。

### 构建全部

```powershell
docs build --format all
```

先生成 HTML，再生成 PDF。HTML 失败则停止；PDF 失败则保留 HTML 并返回部分成功状态。

### 本地预览

```powershell
docs serve
docs serve --source my-docs
```

启动 MkDocs 本地预览服务器，Ctrl+C 停止。

### 清理产物

```powershell
docs clean
docs clean --output out
```

清理 `html/`、`pdf/`、`archive/` 子目录。

### 归档

```powershell
docs archive --format zip
docs archive --format zip --output out
```

将 `html/` 和 `pdf/` 子目录下的构建产物打包为 ZIP 文件（使用 `zipfile.ZIP_DEFLATED` 压缩），输出到 `<output>/archive/docs.zip`。ZIP 内目录结构：

```
docs.zip
├── html/
│   └── ...（静态站点文件）
└── pdf/
    └── docs.pdf
```

## 退出码

项目在 `errors.py` 中定义了 `ExitCode` 枚举，所有命令遵循统一的退出码规范：

| 码 | 枚举常量 | 含义 | 触发场景 |
|----|---------|------|----------|
| 0 | `SUCCESS` | 成功 | 命令正常完成 |
| 1 | `FAILURE` | 构建/运行时失败 | `BuildError`：mkdocs 子进程返回非零 |
| 2 | `USER_ERROR` | 用户输入错误 | `ConfigError`：路径保护冲突、配置无效 |
| 3 | `ENV_MISSING` | 依赖或环境缺失 | `EnvMissingError`：mkdocs 未安装等 |

## 异常类型

项目使用结构化异常层次，便于上层统一处理错误：

| 异常类 | 基类 | 默认退出码 | 用途 |
| --- | --- | --- | --- |
| `DocsError` | `Exception` | — | 所有异常的基类，携带 `exit_code` 属性 |
| `ConfigError` | `DocsError` | 2 (`USER_ERROR`) | 配置相关错误（路径保护、配置生成失败等） |
| `BuildError` | `DocsError` | 1 (`FAILURE`) | 构建流程错误（mkdocs 命令执行失败） |
| `EnvMissingError` | `DocsError` | 3 (`ENV_MISSING`) | 环境缺失（mkdocs 未安装等） |

## 路径保护

为防止误操作，`config.py` 中的 `_is_path_protected()` 函数禁止将以下路径作为输出目录：
- 项目根目录
- 文件系统根目录
- 用户 HOME 目录
- `%WINDIR%`（Windows 系统目录，仅 Windows）

## 全局选项

使用 `--debug` 显示完整 traceback（适合定位问题）：

```powershell
docs build --debug
```

使用 `--verbose` / `-v` 启用详细输出（显示 Rich 日志）：

```powershell
docs build -v
```

使用 `--version` 查看当前版本：

```powershell
docs --version
```

## 错误处理示例

当出现错误时，CLI 会返回非零退出码并输出 Rich 风格化的错误信息：

```powershell
$ docs build --source nonexistent
# 返回码: 2 (USER_ERROR)
# 输出: 错误提示 + 使用 --debug 查看详情的建议

$ docs build --debug --source nonexistent
# 返回码: 2 (USER_ERROR)
# 输出: 完整 Python traceback
```
