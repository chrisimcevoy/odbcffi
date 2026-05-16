"""DB-API 2.0 connection interface."""

from .cursor import Cursor

__all__ = ["Connection"]


class Connection:
    """A DB-API 2.0 Connection object.

    https://peps.python.org/pep-0249/#connection-objects

    Under normal usage, users should not create instances of this class directly. Rather, instances ought to be created
    via the ``odbcffi.connect()`` factory method.
    """

    def commit(self) -> None:
        """Commit any pending transaction to the database."""
        raise NotImplementedError

    def cursor(self) -> Cursor:
        """Return a new Cursor object using this connection."""
        raise NotImplementedError

    def close(self) -> None:
        """Close the connection now (rather than whenever ``.__del__()`` is called)."""
        raise NotImplementedError

    def rollback(self) -> None:
        """Rollback any pending transaction to the database."""
        raise NotImplementedError
