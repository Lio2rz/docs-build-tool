#!/usr/bin/env python3

# ======================================================================================================================
# @description ``python -m docsbuildtool`` entry point
#
# @details     Allows the package to be invoked via ``python -m docsbuildtool``. Delegates to ``docsbuildtool.cli.main``
#              and exits with code 0 on successful completion.
#
# ======================================================================================================================
#
# @filename   __main__.py
# @path       src/docsbuildtool/__main__.py
#
# @project    docsbuildtool
# @product    Docs Build Tool
# @encoding   utf-8
#
# @author     Lio2rz
# @email      chen.mo@outlook.com
# @time       2026/05/16 01:26
#
# @vcs        git
# @version    0.0.2
#
# @record     [2026/05/16 01:26] <Lio2rz> docs(src,tests): add module docstrings, function docstrings, and inline comments
#             [2026/05/15 17:03] <Lio2rz> feat(cli): add Typer-based CLI entrypoint with build/serve/clean/archive c
#
# @license    MIT License
#
# @copyright  Copyright (c) 2026 Lio2rz. All rights reserved.
# ======================================================================================================================

import sys

if __name__ == "__main__":
    from docsbuildtool.cli import main

    main()
    sys.exit(0)
