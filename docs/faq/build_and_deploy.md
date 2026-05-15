# 构建和部署 FAQ

<!-- BEGIN: auto-generated -->

## 如何构建 HTML？

```powershell
poetry run docs build --format html
```

## 如何构建 PDF？

```powershell
poetry run docs build --format pdf
```

PDF 构建需要 `doc-group` 依赖（`mkdocs-with-pdf` 插件）。

## 如何同时构建 HTML 和 PDF？

```powershell
poetry run docs build --format all
```

## 输出结构是怎样的？

```
site/
  html/       # HTML 静态站点（含 index.html）
  pdf/        # PDF 文件（docs.pdf）
  archive/    # ZIP 归档（docs.zip）
```

## 构建产物应该提交到 Git 吗？

默认不提交。`site/` 目录已在 `.gitignore` 中。HTML 和 PDF 是可重复生成的构建产物。

## 如何预览文档？

```powershell
poetry run docs serve
```

启动本地服务器后浏览器访问 `http://127.0.0.1:8000`。

## 如何清理构建产物？

```powershell
poetry run docs clean --output site/
```

<!-- END: auto-generated -->
