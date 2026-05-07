"""Provides a Python abstraction over an ODBC statement handle (HSTMT)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from odbcffi.odbc.enums import HandleType
from odbcffi.odbc.handle import Handle

if TYPE_CHECKING:
    from odbcffi.odbc.connection_handle import ConnectionHandle

__all__ = ["StatementHandle"]


class StatementHandle(Handle):
    """Python abstraction over an ODBC statement handle (HSTMT)."""

    def __init__(self, connection_handle: ConnectionHandle) -> None:
        """Initialize the StatementHandle instance.

        :param connection_handle: The parent ConnectionHandle instance.
        """
        super().__init__(
            handle_type=HandleType.SQL_HANDLE_STMT,
            driver_manager=connection_handle._driver_manager,
        )
        self._parent = connection_handle
