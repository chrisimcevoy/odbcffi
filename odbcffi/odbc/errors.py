"""Errors raised exclusively from within odbcffi.odbc."""

from __future__ import annotations

__all__ = ["ODBCError"]

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .enums import SQLReturn


class ODBCError(Exception):
    """Error raised by the low-level ODBC layer."""

    def __init__(
        self,
        *,
        what: str,
        sql_state: str | None = None,
        native_error: int | None = None,
        message_text: str,
        return_code: SQLReturn,
    ) -> None:
        """Initialize the ODBCError object.

        :param what: The name of the driver manager function which was called.
        :param sql_state: The ODBC error code from driver manager diagnostics, if available.
        :param native_error: The ODBC native error code from driver manager diagnostics, if available.
        :param message_text: The diagnostic message from the driver manager, or an odbcffi-defined error message if
            diagnostics were not available.
        :param return_code: The return
        """
        self.what = what
        self.sql_state = sql_state
        self.native_error = native_error
        self.message_text = message_text
        self.return_code = return_code
        super().__init__(self._build_message())

    def _build_message(self) -> str:
        prefix = f"{self.what}:"

        parts: list[str] = []

        if self.sql_state:
            parts.append(self.sql_state)

        if self.native_error is not None:
            parts.append(f"({self.native_error})")

        parts.append(f"[{self.return_code.name}]")

        parts.append(self.message_text)

        return f"{prefix} {' '.join(parts)}".strip()
