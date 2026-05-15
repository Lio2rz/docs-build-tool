from enum import IntEnum


class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1
    USER_ERROR = 2
    ENV_MISSING = 3


class DocsError(Exception):
    def __init__(self, message: str, exit_code: ExitCode = ExitCode.FAILURE) -> None:
        super().__init__(message)
        self.exit_code = exit_code


class ConfigError(DocsError):
    def __init__(self, message: str) -> None:
        super().__init__(message, ExitCode.USER_ERROR)


class BuildError(DocsError):
    def __init__(self, message: str) -> None:
        super().__init__(message, ExitCode.FAILURE)


class EnvMissingError(DocsError):
    def __init__(self, message: str) -> None:
        super().__init__(message, ExitCode.ENV_MISSING)
