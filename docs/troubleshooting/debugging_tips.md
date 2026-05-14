# 调试技巧

<!-- BEGIN: auto-generated -->

## 依赖问题

```powershell
poetry check --lock
poetry show --only dev-group --tree
poetry show --only doc-group --tree
poetry show --only test-group --tree
```

## 代码检查

```powershell
poetry run ruff check .
```

## 测试

```powershell
poetry run pytest -ra
```

## 构建问题

<!-- TODO: 实现构建命令后，补充最小复现输入和 verbose 调试参数。 -->

<!-- END: auto-generated -->
