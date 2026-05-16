"""DB-API 2.0 cursor interface."""

from collections.abc import Sequence
from typing import Any, Literal

__all__ = ["Cursor"]


class Cursor:
    """A DB-API 2.0 Cursor object.

    https://peps.python.org/pep-0249/#cursor-objects

    Under normal usage, users should not create instances of this class directly. Rather, instances ought to be created
    via the ``Connection.cursor()`` factory method.
    """

    def __init__(self, arraysize: int = 1) -> None:
        """Initialise the Cursor object.

        :param arraysize: The number of rows to fetch at a time with ``.fetchmany()``.
        """
        self.arraysize = arraysize

    @property
    def description(
        self,
    ) -> (
        Sequence[
            tuple[
                str,  # name
                Any,  # type_code
                int | None,  # display_size
                int | None,  # internal_size
                int | None,  # precision
                int | None,  # scale
                bool | None,  # null_ok
            ]
        ]
        | None
    ):
        """A sequence of 7-item sequences, each describing one result column.

        The first two items (name and type_code) are mandatory.

        The other five (display_size, internal_size, precision, scale, null_ok) are optional and are set to None if no
        meaningful values can be provided.

        :return: None for operations that do not return rows or if the cursor has not had an operation invoked via the
            .execute*() method yet. Otherwise, a sequence of 7-item sequences, where each inner sequence describes a
            result column.
        """
        raise NotImplementedError

    @property
    def rowcount(self) -> int:
        """The number of rows that the last statement produced or affected.

        Defaults to -1 in the case that no ``.execute*()`` has been performed, or the rowcount of the last operation
        cannot be determined.
        """
        raise NotImplementedError

    def close(self) -> None:
        """Close the cursor now (rather than whenever __del__ is called)."""
        raise NotImplementedError

    def execute(self, statement: str, *parameters: Any) -> None:
        """Prepare and execute a database operation (query or command)."""
        raise NotImplementedError

    def executemany(self, statement: str, *parameters: Any) -> None:
        """Prepare a database operation (query or command) and then execute it against all parameters."""
        raise NotImplementedError

    def fetchone(self) -> Any | None:
        """Fetch the next row of a query result set, returning a single sequence (or None)."""
        raise NotImplementedError

    def fetchmany(self, size: int | None = None) -> Any:
        """Fetch the next set of rows of a query result set, returning a sequence of sequences."""
        if size is None:
            size = self.arraysize
        raise NotImplementedError

    def fetchall(self) -> Any:
        """Fetch all (remaining) rows of a query result, returning them as a sequence of sequences."""
        raise NotImplementedError

    def nextset(self) -> Literal[True] | None:
        """Make the cursor skip to the next available result set, discarding any remaining rows from the current set."""
        raise NotImplementedError

    def setinputsizes(self, *sizes: Any) -> None:
        """Predefine memory areas for the parameters of ``.execute*()`` operations."""
        raise NotImplementedError

    def setoutputsize(self, size: Any, column: int | None = None) -> None:
        """Set a column buffer size for fetches of large columns (e.g. LONGs, BLOBs, etc.)."""
        raise NotImplementedError
