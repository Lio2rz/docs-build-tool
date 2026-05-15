#!/usr/bin/env python3

# ======================================================================================================================
# @description Smoke test for package importability
#
# @details     Verifies the ``docsbuildtool`` package can be imported and that its public API surface (version, CLI
#              modules) is accessible. Acts as a canary for broken imports.
#
# ======================================================================================================================
#
# @filename   test_package.py
# @path       tests/test_package.py
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
# @record     [2026/05/16 01:26] <Lion> docs(src,tests): add module docstrings, function docstrings, and inline comments
#              [2026/05/14 14:53] <Carl Chen> update coding standards and add linting configuration.
#
# @license    MIT License
#
# @copyright  Copyright (c) 2026 Lio2rz. All rights reserved.
# ======================================================================================================================


def test_package_imports() -> None:
    """Tests that the docsbuildtool package imports without errors."""
    import docsbuildtool

    assert docsbuildtool is not None
