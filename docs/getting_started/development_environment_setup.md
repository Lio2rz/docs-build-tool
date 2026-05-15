# 开发环境搭建

<!-- BEGIN: auto-generated -->

## 前提条件

- Python >= 3.13
- Poetry 2.x（推荐 2.3.0+）
- Git

## 步骤

1. 克隆仓库并进入项目根目录：

   ```shell
   git clone https://github.com/Lio2rz/docs-build-tool.git docsbuildtool
   cd docsbuildtool
   ```

2. 确认 Python 版本满足 `>=3.13`：

   ```shell
   python --version
   ```

3. 安装 Poetry（如已安装可跳过）：

   ```shell
   pip install poetry
   ```

4. 安装全部开发依赖（非 package 模式，`package-mode=false`）：

   ```shell
   poetry install --with dev-group
   ```

   这将安装 runtime、doc、test 和 dev 四组依赖。

5. 验证 lock 文件一致性：

   ```shell
   poetry check --lock
   ```

   应输出 `All set!`。

6. 运行代码检查：

   ```shell
   poetry run ruff check .
   poetry run black --check .
   poetry run isort --check .
   poetry run mypy src/
   ```

7. 运行测试：

   ```shell
   poetry run pytest
   ```

   35 个测试用例全部通过。预期输出类似：

   ```
   ========================== 35 passed in X.XXs ==========================
   ```

8. 验证 CLI 可用：

   ```shell
   poetry run docs --help
   ```

   应显示 4 个子命令：`build`、`serve`、`clean`、`archive`。

## 编辑器配置

建议在 IDE 中配置以下工具以获得实时检查：
- Ruff（lint）
- Black（formatter，行宽 120）
- Mypy（type checking，strict 模式）

<!-- END: auto-generated -->
