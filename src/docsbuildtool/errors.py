#!/usr/bin/env python3

# ======================================================================================================================
# @description Structured exception hierarchy with POSIX-style exit codes
#
# @details     Defines ``ExitCode`` (IntEnum: SUCCESS=0, FAILURE=1, USER_ERROR=2, ENV_MISSING=3) and a ``DocsError`` bas
#              exception carrying an exit code. Subclasses ``ConfigError``, ``BuildError``, and ``EnvMissingError`` each
#              map to a specific exit code so the CLI error handler can pass them directly to ``typer.Exit``.
#
# ======================================================================================================================
#
# @filename   errors.py
# @path       src/docsbuildtool/errors.py
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

from enum import IntEnum


class ExitCode(IntEnum):
    """Integer exit codes for the docsbuildtool CLI."""

    SUCCESS = 0
    """The operation completed successfully."""
    FAILURE = 1
    """A general runtime failure occurred (e.g. build or subprocess error)."""
    USER_ERROR = 2
    """The user provided invalid configuration or arguments."""
    ENV_MISSING = 3
    """A required runtime dependency is missing from the environment."""


class DocsError(Exception):
    """Base exception for all docsbuildtool errors.

    Carries an :class:`ExitCode` so the CLI layer can map it to the
    appropriate process exit code without inspecting the message string.
    """

    def __init__(self, message: str, exit_code: ExitCode = ExitCode.FAILURE) -> None:
        """Initialize the exception with a message and exit code.

        Args:
            message: Human-readable error description.
            exit_code: The :class:`ExitCode` to return to the shell (default FAILURE).
        """
        super().__init__(message)
        self.exit_code = exit_code


class ConfigError(DocsError):
    """Raised when configuration is missing, invalid, or inconsistent."""

    def __init__(self, message: str) -> None:
        """Initialize with ``USER_ERROR`` exit code."""
        super().__init__(message, ExitCode.USER_ERROR)


class BuildError(DocsError):
    """Raised when a build step (HTML or PDF) fails."""

    def __init__(self, message: str) -> None:
        """Initialize with ``FAILURE`` exit code."""
        super().__init__(message, ExitCode.FAILURE)


class EnvMissingError(DocsError):
    """Raised when a required external tool or Python package is not installed."""

    def __init__(self, message: str) -> None:
        """Initialize with ``ENV_MISSING`` exit code."""
        super().__init__(message, ExitCode.ENV_MISSING)
