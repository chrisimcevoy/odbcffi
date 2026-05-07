"""Python Database API 2.0 exceptions.

https://peps.python.org/pep-0249/#exceptions
"""

from __future__ import annotations

__all__ = [
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
]

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from odbcffi.odbc.errors import ODBCError


class Warning(Exception):  # noqa: A001
    """Exception raised for important warnings like data truncations while inserting, etc."""


class Error(Exception):
    """Exception that is the base class of all other error exceptions."""


class InterfaceError(Error):
    """Exception raised for errors that are related to the database interface rather than the database itself."""


class DatabaseError(Error):
    """Exception raised for errors that are related to the database."""


class DataError(DatabaseError):
    """Exception raised for errors that are due to problems with the processed data.

    For example: division by zero, numeric value out of range, etc.
    """


class OperationalError(DatabaseError):
    """Exception raised for errors that are related to the database's operation.

    The errors may not necessarily under the control of the programmer.
    For example: an unexpected disconnect occurs, the data source name
    is not found, a transaction could not be processed, a memory
    allocation error occurred during processing, etc.
    """


class IntegrityError(DatabaseError):
    """Exception raised when the relational integrity of the database is affected.

    For example: a foreign key check fails.
    """


class InternalError(DatabaseError):
    """Exception raised when the database encounters an internal error.

    For example: the cursor is not valid anymore, the transaction is out of sync, etc.
    """


class ProgrammingError(DatabaseError):
    """Exception raised for programming errors.

    For example: table not found or already exists, syntax error in the SQL statement, wrong number of parameters
    specified, etc.
    """


class NotSupportedError(DatabaseError):
    """Exception raised in case a method or database API was used which is not supported by the database.

    For example: requesting a .rollback() on a connection that does not support transactions, or has transactions turned
    off.
    """


# TODO: move the mapping of odbc sqlstate codes -> db api errors to the odbcffi.db_api module.
# def raise_for_return_code(
#     self,
#     rc: int,
#     what: str,
#     handle_type: HandleType | None = None,
#     handle: Any | None = None,
# ) -> None:
#     """Raise an appropriate error for a given return code, if applicable.
#
#     This method encapsulates common logic for checking the return code from calls made to underlying driver manager
#     functions, inspecting diagnostics where possible where the return code indicates that the call was unsuccessful,
#     and mapping ODBC error codes to Python Database API 2.0 exceptions.
#
#     :param rc: The return code from a call to an underlying driver manager function.
#     :param what: Which underlying driver manager function was called.
#     :param handle_type: The type of handle involved in the function call.
#     :param handle: The specific handle object of type ``handle_type`` involved in the function call.
#     """
#     try:
#         rc_enum = SQLReturn(rc)
#     except ValueError:
#         raise Error(f"{what} failed with unknown SQLRETURN={rc}")
#
#     if rc_enum in (SQLReturn.SQL_SUCCESS, SQLReturn.SQL_SUCCESS_WITH_INFO):
#         return
#
#     if handle_type is not None and handle is not None:
#         diags = self.get_diagnostics(handle_type, handle)
#         if diags:
#             sql_state, _, message_text = diags[0]
#             sql_state_exc_map = {
#                 "01002": OperationalError,
#                 "08001": OperationalError,
#                 "08003": OperationalError,
#                 "08004": OperationalError,
#                 "08007": OperationalError,
#                 "08S01": OperationalError,
#                 "0A000": NotSupportedError,
#                 "28000": InterfaceError,
#                 "40002": IntegrityError,
#                 "22": DataError,
#                 "23": IntegrityError,
#                 "24": ProgrammingError,
#                 "25": ProgrammingError,
#                 "42": ProgrammingError,
#                 "HY001": OperationalError,
#                 "HY014": OperationalError,
#                 "HYT00": OperationalError,
#                 "HYT01": OperationalError,
#                 "IM001": InterfaceError,
#                 "IM002": InterfaceError,
#                 "IM003": InterfaceError,
#             }
#
#             for k, v in sql_state_exc_map.items():
#                 if sql_state.startswith(k):
#                     exc_type = v
#                     break
#             else:
#                 exc_type = Error
#
#             raise exc_type(f"{sql_state} {message_text}")
#
#     raise Error(f"{what} failed with {rc_enum.name}")


def map_odbc_error(exc: ODBCError) -> Error:
    if exc.sql_state is None:
        return Error(str(exc))

    sql_state = exc.sql_state

    if sql_state == "01002":
        return OperationalError(str(exc))
    if sql_state in {"08001", "08003", "08004", "08007", "08S01"}:
        return OperationalError(str(exc))
    if sql_state == "0A000":
        return NotSupportedError(str(exc))
    if sql_state == "28000":
        return InterfaceError(str(exc))
    if sql_state == "40002":
        return IntegrityError(str(exc))
    if sql_state.startswith("22"):
        return DataError(str(exc))
    if sql_state.startswith("23"):
        return IntegrityError(str(exc))
    if sql_state.startswith("24"):
        return ProgrammingError(str(exc))
    if sql_state.startswith("25"):
        return ProgrammingError(str(exc))
    if sql_state.startswith("42"):
        return ProgrammingError(str(exc))
    if sql_state in {"HY001", "HY014", "HYT00", "HYT01"}:
        return OperationalError(str(exc))
    if sql_state in {"IM001", "IM002", "IM003"}:
        return InterfaceError(str(exc))

    return Error(str(exc))
