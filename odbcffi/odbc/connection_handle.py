"""Provides a Python abstraction over an ODBC connection handle (HDBC)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .enums import (
    ConnectionAttribute,
    HandleType,
    InfoType,
    SQLAttrAccessMode,
    SQLAttrAutocommit,
)
from .handle import Handle

if TYPE_CHECKING:
    from types import TracebackType

    from typing_extensions import Self

    from .environment_handle import EnvironmentHandle

__all__ = ["ConnectionHandle"]


class ConnectionHandle(Handle):
    """Python abstraction over an ODBC connection handle (HDBC)."""

    def __init__(self, environment_handle: EnvironmentHandle) -> None:
        """Initialise the ConnectionHandle instance, bound to the given ``EnvironmentHandle`` instance.

        The underlying HDBC handle is not allocated until the connection is entered as a context manager. Likewise, no
        connection to the data source is established until ``open`` is called.

        :param environment_handle: The parent EnvironmentHandle instance.
        """
        super().__init__(
            handle_type=HandleType.SQL_HANDLE_DBC,
            driver_manager=environment_handle._driver_manager,
        )
        self._parent = environment_handle
        self.__open = False

    def __exit__(
        self,
        exc_type: type[Exception] | None,
        exc_val: Exception | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Close the connection and free the underlying handle on context exit.

        If the connection is currently open, ``close`` is called before delegating to the base ``Handle`` implementation
        to release the HDBC handle.

        Any exception raised within the context is propagated unchanged.
        """
        try:
            self.close()
        finally:
            super().__exit__(exc_type, exc_val, exc_tb)
        return None

    def open(self, connection_string: str) -> Self:
        """Establish a connection using the given connection string.

        This method invokes ``SQLDriverConnectW`` on the underlying HDBC handle. It must be called after entering the
        context manager (i.e. after the handle has been allocated), and may only be called once per instance.

        :param connection_string: The ODBC connection string.
        :return: This ``Connection`` instance.
        :raise RuntimeError: If called outside a ``with`` block or if the connection is already open.
        """
        if self.__open:
            raise RuntimeError("Cannot open connection twice")
        self._driver_manager.sql_driver_connect_w(
            self,
            connection_string,
        )
        self.__open = True
        return self

    def close(self) -> None:
        """Disconnect the current connection if it is open.

        This calls ``SQLDisconnect`` on the underlying HDBC handle. If the connection is not open or the handle has not
        been allocated, this method does nothing.

        It is safe to call this method multiple times.
        """
        if not self.__open:
            return
        if self._handle is None:
            return
        self._driver_manager.sql_disconnect(self)
        self.__open = False

    @property
    def access_mode(self) -> SQLAttrAccessMode:
        """A ``SQLAttrAccessMode`` instance representing the access mode of the underlying connection."""
        return self._driver_manager.sql_get_connect_attr_w(
            connection_handle=self,
            attribute=ConnectionAttribute.SQL_ATTR_ACCESS_MODE,
        )

    @access_mode.setter
    def access_mode(self, value: SQLAttrAccessMode) -> None:
        self._driver_manager.sql_set_connect_attr_w(
            connection_handle=self,
            attribute=ConnectionAttribute.SQL_ATTR_ACCESS_MODE,
            value=value,
        )

    @property
    def autocommit(self) -> SQLAttrAutocommit:
        """A ``SQLAttrAutocommit`` indicating whether autocommit is enabled or disabled."""
        return self._driver_manager.sql_get_connect_attr_w(
            connection_handle=self,
            attribute=ConnectionAttribute.SQL_ATTR_AUTOCOMMIT,
        )

    @autocommit.setter
    def autocommit(self, value: SQLAttrAutocommit) -> None:
        self._driver_manager.sql_set_connect_attr_w(
            connection_handle=self,
            attribute=ConnectionAttribute.SQL_ATTR_AUTOCOMMIT,
            value=value,
        )

    @property
    def max_concurrent_activities(self) -> int:
        """The maximum number of concurrent activities that the driver can support for a connection.

        This value can reflect a limitation imposed by either the driver or the data source. If there is no specified
        limit or the limit is unknown, this value is set to ``0``.

        The ConnectionHandle must have an open connection before this property is accessed.

        :raise ODBCError: The connection is not open yet.
        """
        return self._driver_manager.sql_get_info_w(
            connection_handle=self,
            info_type=InfoType.SQL_MAX_CONCURRENT_ACTIVITIES,
        )
