"""Provides a Python abstraction over an ODBC environment handle (HENV)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from odbcffi.odbc.enums import (
    EnvironmentAttribute,
    HandleType,
    SQLAttrConnectionPooling,
    SQLAttrODBCVersion,
)
from odbcffi.odbc.handle import Handle

if TYPE_CHECKING:
    from typing_extensions import Self

    from .driver_manager import DriverManager

__all__ = ["EnvironmentHandle"]


class EnvironmentHandle(Handle):
    """Python abstraction over an ODBC environment handle (HENV)."""

    def __init__(self, driver_manager: DriverManager) -> None:
        """Initialise the EnvironmentHandle instance.

        :param driver_manager: The DriverManager instance that this EnvironmentHandle will be allocated from.
        """
        super().__init__(
            handle_type=HandleType.SQL_HANDLE_ENV,
            driver_manager=driver_manager,
        )

    def __enter__(self) -> Self:
        """Allocate resources before entering the context."""
        super().__enter__()
        # TODO: Does this belong here?
        # An application must set this environment attribute before it calls any function that has an SQLHENV argument,
        # or the call will return SQLSTATE HY010 (Function sequence error). It is driver-specific whether additional
        # behavior exists for these environmental flags.
        self.odbc_version = SQLAttrODBCVersion.SQL_OV_ODBC3
        return self

    @property
    def connection_pooling(self) -> SQLAttrConnectionPooling:
        """Enables/disables connection pooling at the HENV level.

        Note that this must be set before a Connection is allocated.

        To enable connection pooling at the process-level (rather than at the Environment-level), the application must
        call `DriverManager.sql_set_env_attr()` passing in `ffi.NULL` as the environment_handle *before* allocating the
        Environment. Enabling process-level connection pooling is a write-only operation, hence no property is exposed
        for this on the DriverManager abstraction. Process-level connection pooling is automatically "inherited" for all
        connections created within that process, negating the need to set this HENV-specific property on the Environment
        class (except to override it).

        Alternatively, applications with one Environment may simply set this Environment.connection_pooling attribute.
        """
        return self._driver_manager.sql_get_env_attr(
            environment_handle=self,
            attribute=EnvironmentAttribute.SQL_ATTR_CONNECTION_POOLING,
        )

    @connection_pooling.setter
    def connection_pooling(self, value: SQLAttrConnectionPooling) -> None:
        self._driver_manager.sql_set_env_attr(
            environment_handle=self,
            attribute=EnvironmentAttribute.SQL_ATTR_CONNECTION_POOLING,
            value=value,
        )

    @property
    def odbc_version(self) -> SQLAttrODBCVersion:
        """The Environment's ODBC version.

        An application must set this environment attribute before it calls any function that has an SQLHENV argument, or
        the call will return SQLSTATE HY010 (Function sequence error). It is driver-specific whether additional behavior
        exists for these environmental flags.
        """
        return self._driver_manager.sql_get_env_attr(
            environment_handle=self,
            attribute=EnvironmentAttribute.SQL_ATTR_ODBC_VERSION,
        )

    @odbc_version.setter
    def odbc_version(self, value: SQLAttrODBCVersion) -> None:
        self._driver_manager.sql_set_env_attr(
            environment_handle=self,
            attribute=EnvironmentAttribute.SQL_ATTR_ODBC_VERSION,
            value=value,
        )
