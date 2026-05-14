# 开发环境搭建

<!-- BEGIN: auto-generated -->

## 步骤

1. 克隆仓库并进入项目根目录。
2. 确认 Python 版本满足 `>=3.13`。
3. 安装 Poetry。
4. 安装开发依赖：

   ```powershell
   poetry install --with dev-group
   ```

5. 运行配置检查：

   ```powershell
   poetry check --lock
   ```

6. 运行 lint：

   ```powershell
   poetry run ruff check .
   ```

7. 运行测试：

   ```powershell
   poetry run pytest
   ```

当前 `tests/` 目录还没有测试用例，因此测试命令可能显示 `no tests ran`。

<!-- END: auto-generated -->
