"""A thin abstraction over ODBC driver managers built on cffi, implementing the Python DB-API 2.0 interface."""

from __future__ import annotations

import threading
from typing import Final, Literal

from . import odbc
from .db_api import (
    Connection,
    Cursor,
    DatabaseError,
    DataError,
    Error,
    IntegrityError,
    InterfaceError,
    InternalError,
    NotSupportedError,
    OperationalError,
    ProgrammingError,
    Warning,  # noqa: A004
)

__all__ = [
    "Connection",
    "Cursor",
    "DataError",
    "DatabaseError",
    "Error",
    "IntegrityError",
    "InterfaceError",
    "InternalError",
    "NotSupportedError",
    "OperationalError",
    "ProgrammingError",
    "Warning",
    "apilevel",
    "db_api",
    "odbc",
]

# region DB-API 2.0

# See https://peps.python.org/pep-0249/#module-interface

apilevel: Final[Literal["2.0"]] = "2.0"
"""String constant stating the supported DB API level."""

threadsafety: Final[Literal[1]] = 1
"""Integer constant stating the level of thread safety the interface supports."""

paramstyle: Final[Literal["qmark"]] = "qmark"
"""String constant stating the type of parameter marker formatting expected by the interface."""

__default_environment: odbc.EnvironmentHandle | None = None
__default_environment_lock = threading.Lock()


def __get_or_create_default_environment_handle() -> odbc.EnvironmentHandle:
    global __default_environment
    if (env := __default_environment) is None:
        with __default_environment_lock:
            if (env := __default_environment) is None:
                env = __default_environment = odbc.EnvironmentHandle(odbc.DriverManager.autoload())
                env.__enter__()
    return env


def connect(connection_string: str) -> Connection:
    """Create and open a database connection.

    This is the module-level DB-API 2.0 connection constructor. I

    :param connection_string: ODBC connection string.
    :return: A ``Connection`` object.
    """
    environment_handle: odbc.EnvironmentHandle = __get_or_create_default_environment_handle()
    connection_handle = odbc.ConnectionHandle(environment_handle=environment_handle)
    connection_handle.__enter__()
    raise NotImplementedError("Pending redisign into separate odbc/db_api sub-packages.")


# endregion
