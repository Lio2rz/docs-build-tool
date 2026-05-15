"""Exception hierarchy and exit codes for docsbuildtool.

Defines a set of structured exit codes and domain-specific exceptions
so that callers (including the CLI) can map errors to meaningful
process exit codes.
"""

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
        super().__init__(message)
        self.exit_code = exit_code


class ConfigError(DocsError):
    """Raised when configuration is missing, invalid, or inconsistent."""

    def __init__(self, message: str) -> None:
        super().__init__(message, ExitCode.USER_ERROR)


class BuildError(DocsError):
    """Raised when a build step (HTML or PDF) fails."""

    def __init__(self, message: str) -> None:
        super().__init__(message, ExitCode.FAILURE)


class EnvMissingError(DocsError):
    """Raised when a required external tool or Python package is not installed."""

    def __init__(self, message: str) -> None:
        super().__init__(message, ExitCode.ENV_MISSING)
