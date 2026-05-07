"""Common abstraction over ODBC handle resource management."""

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Any, Final

if TYPE_CHECKING:
    from types import TracebackType

    from typing_extensions import Self

    from odbcffi.odbc.driver_manager import DriverManager
    from odbcffi.odbc.enums import HandleType

__all__ = ["Handle"]


class Handle(ABC):
    """Base context manager for ODBC handle resource management."""

    def __init__(self, driver_manager: DriverManager, handle_type: HandleType) -> None:
        """Initialize the handler."""
        self._driver_manager = driver_manager
        self.handle_type: Final[HandleType] = handle_type
        self._handle: Any | None = None
        self._parent: Handle | None = None

    def __enter__(self) -> Self:
        """Allocate resources before entering the context."""
        if self._handle is not None:
            raise RuntimeError("Cannot enter context manager twice")
        self._handle = self._driver_manager.sql_alloc_handle(
            handle=self,
            parent_handle=self._parent if self._parent is not None else None,
        )
        return self

    def __exit__(
        self,
        exc_type: type[Exception] | None,
        exc_val: Exception | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Ensure resources are cleaned up on exit."""
        if self._handle is None or (self._parent is not None and self._parent._handle is None):
            return None
        self._driver_manager.sql_free_handle(handle=self)
        self._handle = None
        return None

    @property
    def handle(self) -> Any:
        """Return the underlying handle which was allocated by a DriverManager.

        :raise RuntimeError: If the underlying handle has not been allocated yet.
        """
        if (handle := self._handle) is None:
            raise RuntimeError(f"{self.__class__.__name__} not allocated yet.")
        return handle
