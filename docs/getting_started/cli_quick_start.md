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

将构建产物打包为 ZIP，输出到 `<output>/archive/docs.zip`。

## 退出码

| 码 | 含义 |
|----|------|
| 0 | 成功 |
| 1 | 构建/运行失败 |
| 2 | 用户输入错误 |
| 3 | 依赖或环境缺失 |

## 调试

使用 `--debug` 显示完整 traceback：

```powershell
docs build --debug
```

使用 `--verbose` / `-v` 启用详细输出：

```powershell
docs build -v
```
