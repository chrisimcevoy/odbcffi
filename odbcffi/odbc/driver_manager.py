"""Python abstractions over foreign function calls to ODBC driver manager libraries."""

from __future__ import annotations

import platform
import sys
from enum import Enum, IntEnum, auto
from functools import cached_property
from typing import TYPE_CHECKING, Any, Final, Literal, overload

from cffi import FFI

from .enums import *
from .errors import ODBCError

if TYPE_CHECKING:
    from collections.abc import Collection, Mapping

    from typing_extensions import Self

    from .connection_handle import ConnectionHandle
    from .environment_handle import EnvironmentHandle
    from .handle import Handle

__all__ = ["DriverManager"]

ffi = FFI()
SQL_NTS = -3
SQL_NULL_HANDLE = ffi.NULL

ffi.cdef(
    r"""
typedef unsigned char       SQLCHAR;
typedef void*               SQLHANDLE;
typedef SQLHANDLE           SQLHENV;
typedef SQLHANDLE           SQLHDBC;
typedef void *              SQLPOINTER;
typedef signed short int    SQLSMALLINT;
typedef signed int          SQLINTEGER;
typedef unsigned short int  SQLUSMALLINT;
typedef unsigned short int  SQLWCHAR;
typedef SQLSMALLINT         SQLRETURN;
typedef void*               SQLHWND;
typedef uintptr_t           SQLULEN;

SQLRETURN SQLAllocHandle(
      SQLSMALLINT   HandleType,
      SQLHANDLE     InputHandle,
      SQLHANDLE *   OutputHandlePtr);

SQLRETURN SQLDisconnect(
     SQLHDBC        ConnectionHandle);

SQLRETURN SQLDriverConnectW(
     SQLHDBC        ConnectionHandle,
     SQLHWND        WindowHandle,
     SQLWCHAR *     InConnectionString,
     SQLSMALLINT    StringLength1,
     SQLWCHAR *     OutConnectionString,
     SQLSMALLINT    BufferLength,
     SQLSMALLINT *  StringLength2Ptr,
     SQLUSMALLINT   DriverCompletion);

SQLRETURN SQLFreeHandle(
     SQLSMALLINT   HandleType,
     SQLHANDLE     Handle);

SQLRETURN SQLGetConnectAttrW(
     SQLHDBC        ConnectionHandle,
     SQLINTEGER     Attribute,
     SQLPOINTER     ValuePtr,
     SQLINTEGER     BufferLength,
     SQLINTEGER *   StringLengthPtr);

SQLRETURN SQLGetDiagRecA(
     SQLSMALLINT     HandleType,
     SQLHANDLE       Handle,
     SQLSMALLINT     RecNumber,
     SQLCHAR *       SQLState,
     SQLINTEGER *    NativeErrorPtr,
     SQLCHAR *       MessageText,
     SQLSMALLINT     BufferLength,
     SQLSMALLINT *   TextLengthPtr);

SQLRETURN SQLGetDiagRecW(
     SQLSMALLINT     HandleType,
     SQLHANDLE       Handle,
     SQLSMALLINT     RecNumber,
     SQLWCHAR *      SQLState,
     SQLINTEGER *    NativeErrorPtr,
     SQLWCHAR *      MessageText,
     SQLSMALLINT     BufferLength,
     SQLSMALLINT *   TextLengthPtr);

SQLRETURN SQLGetEnvAttr(
     SQLHENV        EnvironmentHandle,
     SQLINTEGER     Attribute,
     SQLPOINTER     ValuePtr,
     SQLINTEGER     BufferLength,
     SQLINTEGER *   StringLengthPtr);

SQLRETURN SQLGetInfoW(
     SQLHDBC         ConnectionHandle,
     SQLUSMALLINT    InfoType,
     SQLPOINTER      InfoValuePtr,
     SQLSMALLINT     BufferLength,
     SQLSMALLINT *   StringLengthPtr);

SQLRETURN SQLSetConnectAttrW(
     SQLHDBC      ConnectionHandle,
     SQLINTEGER   Attribute,
     SQLPOINTER   ValuePtr,
     SQLINTEGER   StringLength);

SQLRETURN SQLSetEnvAttr(
     SQLHENV      EnvironmentHandle,
     SQLINTEGER   Attribute,
     SQLPOINTER   ValuePtr,
     SQLINTEGER   StringLength);
"""
)

SQL_GET_INFO_STRING_INFO_TYPES: Final[Collection[InfoType]] = frozenset(
    {
        InfoType.SQL_ACCESSIBLE_PROCEDURES,
        InfoType.SQL_ACCESSIBLE_TABLES,
        InfoType.SQL_CATALOG_NAME_SEPARATOR,
        InfoType.SQL_CATALOG_TERM,
        InfoType.SQL_COLUMN_ALIAS,
        InfoType.SQL_DATA_SOURCE_NAME,
        InfoType.SQL_DATA_SOURCE_READ_ONLY,
        InfoType.SQL_DATABASE_NAME,
        InfoType.SQL_DBMS_NAME,
        InfoType.SQL_DBMS_VER,
        InfoType.SQL_DRIVER_NAME,
        InfoType.SQL_DRIVER_ODBC_VER,
        InfoType.SQL_DRIVER_VER,
        InfoType.SQL_EXPRESSIONS_IN_ORDERBY,
        InfoType.SQL_IDENTIFIER_QUOTE_CHAR,
        InfoType.SQL_INTEGRITY,
        InfoType.SQL_KEYWORDS,
        InfoType.SQL_LIKE_ESCAPE_CLAUSE,
        InfoType.SQL_MAX_ROW_SIZE_INCLUDES_LONG,
        InfoType.SQL_MULT_RESULT_SETS,
        InfoType.SQL_MULTIPLE_ACTIVE_TXN,
        InfoType.SQL_NEED_LONG_DATA_LEN,
        InfoType.SQL_ODBC_VER,
        InfoType.SQL_ORDER_BY_COLUMNS_IN_SELECT,
        InfoType.SQL_OUTER_JOINS,
        InfoType.SQL_PROCEDURE_TERM,
        InfoType.SQL_PROCEDURES,
        InfoType.SQL_ROW_UPDATES,
        InfoType.SQL_SCHEMA_TERM,
        InfoType.SQL_SEARCH_PATTERN_ESCAPE,
        InfoType.SQL_SERVER_NAME,
        InfoType.SQL_SPECIAL_CHARACTERS,
        InfoType.SQL_TABLE_TERM,
        InfoType.SQL_USER_NAME,
    }
)

SQL_GET_INFO_USMALLINT_INFO_TYPES: Final[Collection[InfoType]] = frozenset(
    {
        InfoType.SQL_ACTIVE_ENVIRONMENTS,
        InfoType.SQL_ALTER_DOMAIN,
        InfoType.SQL_ALTER_TABLE,
        InfoType.SQL_BATCH_ROW_COUNT,
        InfoType.SQL_BATCH_SUPPORT,
        InfoType.SQL_BOOKMARK_PERSISTENCE,
        InfoType.SQL_CATALOG_LOCATION,
        InfoType.SQL_CATALOG_USAGE,
        InfoType.SQL_CONCAT_NULL_BEHAVIOR,
        InfoType.SQL_CONVERT_BIGINT,
        InfoType.SQL_CONVERT_BINARY,
        InfoType.SQL_CONVERT_BIT,
        InfoType.SQL_CONVERT_CHAR,
        InfoType.SQL_CONVERT_GUID,
        InfoType.SQL_CONVERT_DATE,
        InfoType.SQL_CONVERT_DECIMAL,
        InfoType.SQL_CONVERT_DOUBLE,
        InfoType.SQL_CONVERT_FLOAT,
        InfoType.SQL_CONVERT_FUNCTIONS,
        InfoType.SQL_CONVERT_INTEGER,
        InfoType.SQL_CONVERT_INTERVAL_YEAR_MONTH,
        InfoType.SQL_CONVERT_INTERVAL_DAY_TIME,
        InfoType.SQL_CONVERT_LONGVARBINARY,
        InfoType.SQL_CONVERT_LONGVARCHAR,
        InfoType.SQL_CONVERT_NUMERIC,
        InfoType.SQL_CONVERT_REAL,
        InfoType.SQL_CONVERT_SMALLINT,
        InfoType.SQL_CONVERT_TIME,
        InfoType.SQL_CONVERT_TIMESTAMP,
        InfoType.SQL_CONVERT_TINYINT,
        InfoType.SQL_CONVERT_VARBINARY,
        InfoType.SQL_CONVERT_VARCHAR,
        InfoType.SQL_CONVERT_WCHAR,
        InfoType.SQL_CONVERT_WVARCHAR,
        InfoType.SQL_CONVERT_WLONGVARCHAR,
        InfoType.SQL_CORRELATION_NAME,
        InfoType.SQL_CREATE_ASSERTION,
        InfoType.SQL_CREATE_CHARACTER_SET,
        InfoType.SQL_CREATE_COLLATION,
        InfoType.SQL_CREATE_DOMAIN,
        InfoType.SQL_CREATE_SCHEMA,
        InfoType.SQL_CREATE_TABLE,
        InfoType.SQL_CREATE_TRANSLATION,
        InfoType.SQL_CREATE_VIEW,
        InfoType.SQL_CURSOR_COMMIT_BEHAVIOR,
        InfoType.SQL_CURSOR_ROLLBACK_BEHAVIOR,
        InfoType.SQL_DATETIME_LITERALS,
        InfoType.SQL_DEFAULT_TXN_ISOLATION,
        InfoType.SQL_DROP_ASSERTION,
        InfoType.SQL_DROP_CHARACTER_SET,
        InfoType.SQL_DROP_COLLATION,
        InfoType.SQL_FILE_USAGE,
        InfoType.SQL_GETDATA_EXTENSIONS,
        InfoType.SQL_GROUP_BY,
        InfoType.SQL_IDENTIFIER_CASE,
        InfoType.SQL_MAX_BINARY_LITERAL_LEN,
        InfoType.SQL_MAX_CATALOG_NAME_LEN,
        InfoType.SQL_MAX_CHAR_LITERAL_LEN,
        InfoType.SQL_MAX_COLUMN_NAME_LEN,
        InfoType.SQL_MAX_COLUMNS_IN_GROUP_BY,
        InfoType.SQL_MAX_COLUMNS_IN_INDEX,
        InfoType.SQL_MAX_COLUMNS_IN_ORDER_BY,
        InfoType.SQL_MAX_COLUMNS_IN_SELECT,
        InfoType.SQL_MAX_COLUMNS_IN_TABLE,
        InfoType.SQL_MAX_CONCURRENT_ACTIVITIES,
        InfoType.SQL_MAX_CURSOR_NAME_LEN,
        InfoType.SQL_MAX_DRIVER_CONNECTIONS,
        InfoType.SQL_MAX_INDEX_SIZE,
        InfoType.SQL_MAX_PROCEDURE_NAME_LEN,
        InfoType.SQL_MAX_ROW_SIZE,
        InfoType.SQL_MAX_SCHEMA_NAME_LEN,
        InfoType.SQL_MAX_STATEMENT_LEN,
        InfoType.SQL_MAX_TABLE_NAME_LEN,
        InfoType.SQL_MAX_TABLES_IN_SELECT,
        InfoType.SQL_MAX_USER_NAME_LEN,
        InfoType.SQL_NON_NULLABLE_COLUMNS,
        InfoType.SQL_NULL_COLLATION,
        InfoType.SQL_NUMERIC_FUNCTIONS,
        InfoType.SQL_ODBC_SAG_CLI_CONFORMANCE,
        InfoType.SQL_ODBC_SQL_CONFORMANCE,
        InfoType.SQL_OJ_CAPABILITIES,
        InfoType.SQL_QUOTED_IDENTIFIER_CASE,
        InfoType.SQL_SCHEMA_USAGE,
        InfoType.SQL_SCROLL_CONCURRENCY,
        InfoType.SQL_SCROLL_OPTIONS,
        InfoType.SQL_SQL_CONFORMANCE,
        InfoType.SQL_STRING_FUNCTIONS,
        InfoType.SQL_SUBQUERIES,
        InfoType.SQL_SYSTEM_FUNCTIONS,
        InfoType.SQL_TIMEDATE_ADD_INTERVALS,
        InfoType.SQL_TIMEDATE_DIFF_INTERVALS,
        InfoType.SQL_TIMEDATE_FUNCTIONS,
        InfoType.SQL_TXN_CAPABLE,
        InfoType.SQL_TXN_ISOLATION_OPTION,
        InfoType.SQL_UNION,
    }
)

SQL_GET_INFO_ENUM_MAP: Mapping[InfoType, type[Enum]] = {
    InfoType.SQL_ALTER_DOMAIN: SQLAlterDomain,
    InfoType.SQL_ALTER_TABLE: SQLAlterTable,
    InfoType.SQL_BATCH_ROW_COUNT: SQLBatchRowCount,
    InfoType.SQL_BATCH_SUPPORT: SQLBatchSupport,
    InfoType.SQL_BOOKMARK_PERSISTENCE: SQLBookmarkPersistence,
    InfoType.SQL_CATALOG_LOCATION: SQLCatalogLocation,
    InfoType.SQL_CATALOG_USAGE: SQLCatalogUsage,
    InfoType.SQL_CONCAT_NULL_BEHAVIOR: SQLConcatNullBehavior,
    InfoType.SQL_CONVERT_BIGINT: SQLConvert,
    InfoType.SQL_CONVERT_BINARY: SQLConvert,
    InfoType.SQL_CONVERT_BIT: SQLConvert,
    InfoType.SQL_CONVERT_CHAR: SQLConvert,
    InfoType.SQL_CONVERT_GUID: SQLConvert,
    InfoType.SQL_CONVERT_DATE: SQLConvert,
    InfoType.SQL_CONVERT_DECIMAL: SQLConvert,
    InfoType.SQL_CONVERT_DOUBLE: SQLConvert,
    InfoType.SQL_CONVERT_FLOAT: SQLConvert,
    InfoType.SQL_CONVERT_FUNCTIONS: SQLConvertFunctions,
    InfoType.SQL_CONVERT_INTEGER: SQLConvert,
    InfoType.SQL_CONVERT_INTERVAL_YEAR_MONTH: SQLConvert,
    InfoType.SQL_CONVERT_INTERVAL_DAY_TIME: SQLConvert,
    InfoType.SQL_CONVERT_LONGVARBINARY: SQLConvert,
    InfoType.SQL_CONVERT_LONGVARCHAR: SQLConvert,
    InfoType.SQL_CONVERT_NUMERIC: SQLConvert,
    InfoType.SQL_CONVERT_REAL: SQLConvert,
    InfoType.SQL_CONVERT_SMALLINT: SQLConvert,
    InfoType.SQL_CONVERT_TIME: SQLConvert,
    InfoType.SQL_CONVERT_TIMESTAMP: SQLConvert,
    InfoType.SQL_CONVERT_TINYINT: SQLConvert,
    InfoType.SQL_CONVERT_VARBINARY: SQLConvert,
    InfoType.SQL_CONVERT_VARCHAR: SQLConvert,
    InfoType.SQL_CONVERT_WCHAR: SQLConvert,
    InfoType.SQL_CONVERT_WLONGVARCHAR: SQLConvert,
    InfoType.SQL_CONVERT_WVARCHAR: SQLConvert,
    InfoType.SQL_CORRELATION_NAME: SQLCorrelationName,
    InfoType.SQL_CREATE_ASSERTION: SQLCreateAssertion,
    InfoType.SQL_CREATE_CHARACTER_SET: SQLCreateCharacterSet,
    InfoType.SQL_CREATE_COLLATION: SQLCreateCollation,
    InfoType.SQL_CREATE_DOMAIN: SQLCreateDomain,
    InfoType.SQL_CREATE_SCHEMA: SQLCreateSchema,
    InfoType.SQL_CREATE_TABLE: SQLCreateTable,
    InfoType.SQL_CREATE_TRANSLATION: SQLCreateTranslation,
    InfoType.SQL_CREATE_VIEW: SQLCreateView,
    InfoType.SQL_CURSOR_COMMIT_BEHAVIOR: SQLCursorCommitBehavior,
    InfoType.SQL_CURSOR_ROLLBACK_BEHAVIOR: SQLCursorRollbackBehavior,
    InfoType.SQL_DATETIME_LITERALS: SQLDatetimeLiterals,
    InfoType.SQL_DEFAULT_TXN_ISOLATION: SQLTxnIsolationOption,
    InfoType.SQL_DROP_ASSERTION: SQLDropAssertion,
    InfoType.SQL_DROP_CHARACTER_SET: SQLDropCharacterSet,
    InfoType.SQL_DROP_COLLATION: SQLDropCollation,
    InfoType.SQL_FILE_USAGE: SQLFileUsage,
    InfoType.SQL_GETDATA_EXTENSIONS: SQLGetDataExtensions,
    InfoType.SQL_GROUP_BY: SQLGroupBy,
    InfoType.SQL_IDENTIFIER_CASE: SQLIdentifierCase,
    InfoType.SQL_NON_NULLABLE_COLUMNS: SQLNonNullableColumns,
    InfoType.SQL_NULL_COLLATION: SQLNullCollation,
    InfoType.SQL_NUMERIC_FUNCTIONS: SQLNumericFunctions,
    InfoType.SQL_ODBC_SQL_CONFORMANCE: SQLOdbcSqlConformance,
    InfoType.SQL_ODBC_SAG_CLI_CONFORMANCE: SQLOdbcSagCliConformance,
    InfoType.SQL_OJ_CAPABILITIES: SQLOuterJoinCapabilities,
    InfoType.SQL_OUTER_JOINS: SQLOuterJoins,
    InfoType.SQL_QUOTED_IDENTIFIER_CASE: SQLIdentifierCase,
    InfoType.SQL_SCHEMA_USAGE: SQLSchemaUsage,
    InfoType.SQL_SCROLL_CONCURRENCY: SQLScrollConcurrency,
    InfoType.SQL_SCROLL_OPTIONS: SQLScrollOptions,
    InfoType.SQL_SQL_CONFORMANCE: SQLSqlConformance,
    InfoType.SQL_STRING_FUNCTIONS: SQLStringFunctions,
    InfoType.SQL_SUBQUERIES: SQLSubqueries,
    InfoType.SQL_SYSTEM_FUNCTIONS: SQLSystemFunctions,
    InfoType.SQL_TIMEDATE_ADD_INTERVALS: SQLTimestampIntervals,
    InfoType.SQL_TIMEDATE_DIFF_INTERVALS: SQLTimestampIntervals,
    InfoType.SQL_TIMEDATE_FUNCTIONS: SQLTimeDateFunctions,
    InfoType.SQL_TXN_CAPABLE: SQLTxnCapable,
    InfoType.SQL_TXN_ISOLATION_OPTION: SQLTxnIsolationOption,
    InfoType.SQL_UNION: SQLUnion,
}

SQLWCHAR_SIZE: Final[int] = ffi.sizeof("SQLWCHAR")
"""The size of SQLWCHAR in bytes."""


def get_sqlwchar_encoding() -> str:
    """Return the Python codec name matching the runtime SQLWCHAR ABI."""
    if SQLWCHAR_SIZE == 2:
        return "utf-16-le" if sys.byteorder == "little" else "utf-16-be"

    if SQLWCHAR_SIZE == 4:
        return "utf-32-le" if sys.byteorder == "little" else "utf-32-be"

    raise RuntimeError(f"Unsupported SQLWCHAR size: {SQLWCHAR_SIZE}")


@overload
def decode_sqlwchar_buffer(buffer: Any, *, num_bytes: int) -> str: ...


@overload
def decode_sqlwchar_buffer(buffer: Any, *, num_chars: int) -> str: ...


def decode_sqlwchar_buffer(buffer: Any, *, num_bytes: int | None = None, num_chars: int | None = None) -> str:
    """Decode a wide-character ODBC buffer into a Python string.

    ODBC functions variously provide buffer lengths in either bytes (for example SQLGetInfoW) or characters (for example
    SQLGetDiagRecW).

    Exactly one of ``num_bytes`` or ``num_chars`` must be provided.

    :param buffer: The SQLWCHAR buffer to decode.
    :param num_bytes: The number of bytes to read from the buffer.
    :param num_chars: The number of characters to read from the buffer.
    :return: The decoded Python string.
    """
    if num_bytes is None and num_chars is None:
        raise ValueError("One of num_bytes or num_chars must be provided.")

    if num_bytes is not None and num_chars is not None:
        raise ValueError("Only one of num_bytes and num_chars can be provided.")

    if num_chars is not None:
        if num_chars < 0:
            raise ValueError("num_chars cannot be negative")

        if num_chars == 0:
            return ""

        num_bytes = num_chars * SQLWCHAR_SIZE

    elif num_bytes is not None:
        if num_bytes < 0:
            raise ValueError("num_bytes cannot be negative")

        if num_bytes == 0:
            return ""

        if num_bytes % SQLWCHAR_SIZE != 0:
            raise ValueError(f"num_bytes ({num_bytes}) must be a multiple of sizeof(SQLWCHAR) ({SQLWCHAR_SIZE})")

    raw: bytes = ffi.buffer(buffer, num_bytes)[:]
    return raw.decode(get_sqlwchar_encoding())


def encode_sqlwchar_buffer(s: str) -> Any:
    """Convert a Python string into a NUL-terminated SQLWCHAR buffer.

    Encodes using the runtime SQLWCHAR ABI (2-byte or 4-byte code units),
    appends a single wide-character NUL terminator, and returns a
    ``SQLWCHAR[]`` buffer suitable for passing to ODBC W APIs.
    """
    encoding = get_sqlwchar_encoding()

    # Encode string
    payload = s.encode(encoding)

    # Append a single wide NUL (size depends on SQLWCHAR)
    terminator = b"\x00" * SQLWCHAR_SIZE
    b = payload + terminator

    # Sanity check
    if len(b) % SQLWCHAR_SIZE != 0:
        raise ValueError(f"Encoded buffer length ({len(b)}) is not a multiple of SQLWCHAR size ({SQLWCHAR_SIZE})")

    # Number of SQLWCHAR elements
    n_wchars = len(b) // SQLWCHAR_SIZE

    buf = ffi.new(f"SQLWCHAR[{n_wchars}]")
    ffi.memmove(buf, b, len(b))

    return buf


DM_LIB_NAMES_MACOS_UNIXODBC = ["libodbc.dylib"]
DM_LIB_NAMES_MACOS_IODBC = ["libiodbc.dylib"]
DM_LIB_NAMES_MACOS = DM_LIB_NAMES_MACOS_UNIXODBC + DM_LIB_NAMES_MACOS_IODBC
DM_LIB_NAMES_NIX_UNIXODBC = [
    "libodbc.so.2",
    "libodbc.so",
]

DM_LIB_NAMES_NIX_IODBC = [
    "libiodbc.so.2",
    "libiodbc.so",
]
DM_LIB_NAMES_NIX = DM_LIB_NAMES_NIX_UNIXODBC + DM_LIB_NAMES_NIX_IODBC
DM_LIB_NAMES_WIN = ["odbc32.dll"]
DM_LIB_NAMES = DM_LIB_NAMES_WIN + DM_LIB_NAMES_MACOS + DM_LIB_NAMES_NIX

DM_LIB_NAMES_UNIXODBC = DM_LIB_NAMES_MACOS_UNIXODBC + DM_LIB_NAMES_NIX_UNIXODBC
DM_LIB_NAMES_IODBC = DM_LIB_NAMES_MACOS_IODBC + DM_LIB_NAMES_NIX_IODBC


class DriverManagerType(IntEnum):
    ODBC32 = auto()
    IODBC = auto()
    UNIXODBC = auto()
    UNKNOWN = auto()


class DriverManager:
    """Represents an ODBC Driver Manager installed on the host system.

    This class is an abstraction over an ODBC driver manager, providing a Python interface which encapsulates the use of
    cffi for foreign function calls.
    """

    def __init__(self, driver_manager_lib_name: str) -> None:
        """Initialise the DriverManager instance.

        :param driver_manager_lib_name: The name of the ODBC driver manager library.
        """
        # TODO: Allow pathlib.Path arg, and handle driver_manager_type detection where there are path separators.
        self.driver_manager_lib_name: Final[str] = driver_manager_lib_name
        self._lib = ffi.dlopen(driver_manager_lib_name)

    @cached_property
    def driver_manager_type(self) -> DriverManagerType:
        """Try to detect the type of Driver Manager library loaded, based on the name of the library."""
        if self.driver_manager_lib_name in DM_LIB_NAMES_WIN:
            return DriverManagerType.ODBC32
        if self.driver_manager_lib_name in DM_LIB_NAMES_UNIXODBC:
            return DriverManagerType.UNIXODBC
        if self.driver_manager_lib_name in DM_LIB_NAMES_IODBC:
            return DriverManagerType.IODBC
        return DriverManagerType.UNKNOWN

    @property
    def is_unixodbc(self) -> bool:
        """True if this driver manager appears to be unixODBC (based on library name)."""
        return self.driver_manager_type == DriverManagerType.UNIXODBC

    @property
    def is_iodbc(self) -> bool:
        """True if this driver manager appears to be iODBC (based on library name)."""
        return self.driver_manager_type == DriverManagerType.IODBC

    @property
    def is_windows_dm(self) -> bool:
        """True if this driver manager appears to be the Windows ODBC Driver Manager (based on library name)."""
        return self.driver_manager_type == DriverManagerType.ODBC32

    @classmethod
    def autoload(cls) -> Self:
        """Create an instance of DriverManager using the first ODBC driver manager detected on the host.

        :return: An instance of DriverManager.
        :raise FileNotFoundError: No driver manager library was auto-detected on the host system.
        """
        last_err: OSError | None = None

        os_family = platform.system()

        if os_family == "Darwin":
            names = DM_LIB_NAMES_MACOS
        elif os_family == "Windows":
            names = DM_LIB_NAMES_WIN
        elif os_family == "Linux":
            names = DM_LIB_NAMES_NIX
        else:
            names = DM_LIB_NAMES

        for name in names:
            try:
                dm = cls(driver_manager_lib_name=name)
                return dm
            except OSError as e:  # noqa: PERF203
                last_err = e
        raise FileNotFoundError(
            "Could not load an ODBC driver manager library. Tried: "
            + ", ".join(names)
            + (f"\nLast error: {last_err}" if last_err else "")
        )

    def raise_for_return_code(
        self,
        return_code: int,
        what: str,
        handle: Handle | None,
    ) -> None:
        """Raise ``ODBCError`` if the provided return code does not indicate success.

        ODBC diagnostics will be included in the error message if they are available from the driver manager.

        :param return_code: The return code from a call to an underlying driver manager function.
        :param what: The name of the driver manager function which was called.
        :param handle: The Handle object involved in the function call.
        :raise ODBCError: If the return code does not indicate success.
        """
        rc_enum = SQLReturn(return_code)

        # TODO: SQL_RETURN_WITH_INFO handling here?
        if rc_enum in (SQLReturn.SQL_SUCCESS, SQLReturn.SQL_SUCCESS_WITH_INFO):
            return

        if handle is not None:
            try:
                diags = self.sql_get_diag_rec_w(handle)
            except ODBCError as diag_error:
                raise ODBCError(
                    what=what,
                    message_text=f"{what} failed with {rc_enum.name}, and SQLGetDiagRecW also failed.",
                    return_code=rc_enum,
                ) from diag_error
            if diags:
                # TODO: We only use the zeroth diagnostic. Can we use them all?
                sql_state, native, message_text = diags[0]
                raise ODBCError(
                    what=what,
                    sql_state=sql_state,
                    native_error=native,
                    message_text=message_text,
                    return_code=rc_enum,
                )

        raise ODBCError(
            what=what,
            message_text=f"{what} failed without diagnostic information",
            return_code=rc_enum,
        )

    def sql_get_diag_rec_a(
        self,
        handle: Handle,
    ) -> list[tuple[str, int, str]]:
        """Get diagnostic information by calling SQLGetDiagRecA.

        SQLGetDiagRecA returns the current values of multiple fields of a diagnostic record that contains error,
        warning, and status information. Unlike SQLGetDiagField, which returns one diagnostic field per call,
        SQLGetDiagRecA returns several commonly used fields of a diagnostic record, including the SQLSTATE, the native
        error code, and the diagnostic message text.

        :param handle: A handle for the diagnostic data structure, of the type indicated by HandleType. If HandleType is
            SQL_HANDLE_ENV, Handle can be either a shared or an unshared environment handle.
        :return: A list of 3-tuples where each tuple contains (i) a five-character SQLSTATE code for the diagnostic
            record, (ii) a native error code which is specific to the data source, and (iii) the diagnostic message
            text.
        """
        diags = []

        buffer_length = default_buffer_length = 1024
        rec_number = 1

        while True:
            sql_state = ffi.new("SQLCHAR[6]")  # 5 chars + NUL
            native_error_ptr = ffi.new("SQLINTEGER *")
            message_text = ffi.new(f"SQLCHAR[{buffer_length}]")
            text_length_ptr = ffi.new("SQLSMALLINT *")

            rc = SQLReturn(
                self._lib.SQLGetDiagRecA(
                    int(handle.handle_type),
                    handle.handle,
                    rec_number,
                    sql_state,
                    native_error_ptr,
                    message_text,
                    buffer_length,
                    text_length_ptr,
                )
            )

            # Dereference the pointers.
            native_error: int = native_error_ptr[0]
            text_length: int = text_length_ptr[0]

            if rc == SQLReturn.SQL_NO_DATA:
                # RecNumber was greater than the number of diagnostic records that existed for the handle specified in
                # Handle. The function also returns SQL_NO_DATA for any positive RecNumber if there are no diagnostic
                # records for Handle.
                break

            if rc == SQLReturn.SQL_INVALID_HANDLE:
                raise ODBCError(
                    what="SQLGetDiagRecA",
                    message_text="SQLGetDiagRecA failed with SQL_INVALID_HANDLE",
                    return_code=rc,
                )

            if rc == SQLReturn.SQL_SUCCESS_WITH_INFO:
                # SQLGetDiagRec documents SQL_SUCCESS_WITH_INFO as message truncation.
                # If TextLength does not indicate truncation, treat that as an unexpected state.
                if text_length >= buffer_length:
                    # Retry for the same rec_number with a right-sized buffer.
                    buffer_length = text_length + 1  # NUL terminator
                    continue
                raise ODBCError(
                    what="SQLGetDiagRecA",
                    message_text=(
                        "SQLGetDiagRecA returned SQL_SUCCESS_WITH_INFO with an unexpected "
                        f"TextLength ({text_length}) for BufferLength ({buffer_length})"
                    ),
                    return_code=rc,
                )

            # Any remaining SQLRETURN here is unexpected for SQLGetDiagRec.
            if rc != SQLReturn.SQL_SUCCESS:
                raise ODBCError(
                    what="SQLGetDiagRecA",
                    message_text=f"SQLGetDiagRecA returned unexpected SQLRETURN {rc.name}",
                    return_code=rc,
                )

            diags.append(
                (
                    ffi.string(sql_state).decode("ascii"),
                    native_error,
                    # TODO: SQLGetDiagRecA returns data in the driver's "ANSI" encoding
                    #  (Windows code page or driver-defined on Unix), not guaranteed UTF-8.
                    #  We currently assume UTF-8 and replace invalid sequences as a pragmatic default.
                    #  Alternatives:
                    #    - use locale.getpreferredencoding()
                    #    - make encoding configurable
                    #    - rely on W APIs for correct Unicode handling
                    ffi.string(message_text, text_length).decode("utf-8", errors="replace"),
                )
            )

            # We successfully retrieved the diagnostics for this rec_number.
            # Move on to the next one.
            rec_number += 1
            # In case we needed to grow the buffer to retrieve a particularly large message_text, reset the
            # buffer_length for the next rec_number.
            buffer_length = default_buffer_length

        return diags

    def sql_get_diag_rec_w(
        self,
        handle: Handle,
    ) -> list[tuple[str, int, str]]:
        """Get diagnostic information by calling SQLGetDiagRecW.

        SQLGetDiagRecW returns the current values of multiple fields of a diagnostic record that contains error,
        warning, and status information. Unlike SQLGetDiagField, which returns one diagnostic field per call,
        SQLGetDiagRecW returns several commonly used fields of a diagnostic record, including the SQLSTATE, the native
        error code, and the diagnostic message text.

        :param handle: A handle for the diagnostic data structure, of the type indicated by HandleType. If HandleType is
            SQL_HANDLE_ENV, Handle can be either a shared or an unshared environment handle.
        :return: A list of 3-tuples where each tuple contains (i) a five-character SQLSTATE code for the diagnostic
            record, (ii) a native error code which is specific to the data source, and (iii) the diagnostic message
            text.
        """
        diags = []

        buffer_length = default_buffer_length = 1024
        rec_number = 1

        while True:
            sql_state = ffi.new("SQLWCHAR[6]")  # 5 chars + NUL
            native_error_ptr = ffi.new("SQLINTEGER *")
            message_text = ffi.new(f"SQLWCHAR[{buffer_length}]")
            text_length_ptr = ffi.new("SQLSMALLINT *")

            rc = SQLReturn(
                self._lib.SQLGetDiagRecW(
                    int(handle.handle_type),
                    handle.handle,
                    rec_number,
                    sql_state,
                    native_error_ptr,
                    message_text,
                    buffer_length,
                    text_length_ptr,
                )
            )

            # Dereference the pointers.
            native_error: int = native_error_ptr[0]
            text_length: int = text_length_ptr[0]

            if rc == SQLReturn.SQL_NO_DATA:
                # RecNumber was greater than the number of diagnostic records that existed for the handle specified in
                # Handle. The function also returns SQL_NO_DATA for any positive RecNumber if there are no diagnostic
                # records for Handle.
                break

            if rc == SQLReturn.SQL_INVALID_HANDLE:
                raise ODBCError(
                    what="SQLGetDiagRecW",
                    message_text="SQLGetDiagRecW failed with SQL_INVALID_HANDLE",
                    return_code=rc,
                )

            if rc == SQLReturn.SQL_SUCCESS_WITH_INFO:
                # SQLGetDiagRec documents SQL_SUCCESS_WITH_INFO as message truncation.
                # If TextLength does not indicate truncation, treat that as an unexpected state.
                if text_length >= buffer_length:
                    # Retry for the same rec_number with a right-sized buffer.
                    buffer_length = text_length + 1  # NUL terminator
                    continue
                raise ODBCError(
                    what="SQLGetDiagRecW",
                    message_text=(
                        "SQLGetDiagRecW returned SQL_SUCCESS_WITH_INFO with an unexpected "
                        f"TextLength ({text_length}) for BufferLength ({buffer_length})"
                    ),
                    return_code=rc,
                )

            # Any remaining SQLRETURN here is unexpected for SQLGetDiagRec.
            if rc != SQLReturn.SQL_SUCCESS:
                raise ODBCError(
                    what="SQLGetDiagRecW",
                    message_text=f"SQLGetDiagRecW returned unexpected SQLRETURN {rc.name}",
                    return_code=rc,
                )

            diags.append(
                (
                    decode_sqlwchar_buffer(buffer=sql_state, num_chars=5),
                    native_error,
                    decode_sqlwchar_buffer(buffer=message_text, num_chars=text_length),
                )
            )

            # We successfully retrieved the diagnostics for this rec_number.
            # Move on to the next one.
            rec_number += 1
            # In case we needed to grow the buffer to retrieve a particularly large message_text, reset the
            # buffer_length for the next rec_number.
            buffer_length = default_buffer_length

        return diags

    def sql_alloc_handle(
        self,
        handle: Handle,
        parent_handle: Handle | None,
    ) -> Any:
        """Allocate an environment, connection, statement, or descriptor handle.

        Environment handles do not have a parent as they are uppermost in the ODBC handle hierarchy.

        All other handle types have a "parent" handle which must be allocated in advance, and passed to this function
        when the child is being allocated.

        :param handle: The handle to allocate.
        :param parent_handle: The parent handle, if applicable.
        :return: The allocated handle.
        """
        output_handle_ptr = ffi.new("SQLHANDLE *")
        rc = self._lib.SQLAllocHandle(
            int(handle.handle_type),
            parent_handle.handle if parent_handle is not None else SQL_NULL_HANDLE,
            output_handle_ptr,
        )
        self.raise_for_return_code(
            return_code=rc,
            what="SQLAllocHandle",
            handle=parent_handle,
        )
        return output_handle_ptr[0]

    def sql_disconnect(self, connection_handle: ConnectionHandle) -> None:
        """Close the connection associated with a specific connection handle.

        :param connection_handle: The connection handle to close the connection for.
        """
        rc = self._lib.SQLDisconnect(connection_handle.handle)
        self.raise_for_return_code(
            return_code=rc,
            what="SQLDisconnect",
            handle=connection_handle,
        )

    def sql_driver_connect_w(
        self,
        connection_handle: ConnectionHandle,
        connection_str: str,
    ) -> None:
        """Connect to a database using a connection string.

        SQLDriverConnect is an alternative to SQLConnect. It supports data sources that require more connection
        information than the three arguments in SQLConnect, dialog boxes to prompt the user for all connection
        information, and data sources that are not defined in the system information.

        :param connection_handle:
        :param connection_str: An ODBC connection string. For syntax details, see https://learn.microsoft.com/en-
            us/sql/odbc/reference/syntax/sqldriverconnect-function#comments
        """
        connection_str_buffer = encode_sqlwchar_buffer(connection_str)
        rc = self._lib.SQLDriverConnectW(
            connection_handle.handle,
            ffi.NULL,  # WindowHandle
            connection_str_buffer,
            SQL_NTS,  # StringLength1: null-terminated
            ffi.NULL,  # OutConnectionString
            0,  # BufferLength (for OutConnectionString)
            ffi.NULL,  # StringLength2Ptr
            int(DriverCompletion.SQL_DRIVER_NOPROMPT),
        )
        self.raise_for_return_code(
            return_code=rc,
            what="SQLDriverConnectW",
            handle=connection_handle,
        )

    def sql_free_handle(self, handle: Handle) -> None:
        """Free resources associated with a specific environment, connection, statement, or descriptor handle.

        :param handle: The handle to free.
        """
        rc = self._lib.SQLFreeHandle(int(handle.handle_type), handle.handle)
        self.raise_for_return_code(
            return_code=rc,
            what="SQLFreeHandle",
            handle=handle,
        )

    @overload
    def sql_get_connect_attr_w(
        self,
        connection_handle: ConnectionHandle,
        attribute: Literal[ConnectionAttribute.SQL_ATTR_ACCESS_MODE],
    ) -> SQLAttrAccessMode: ...

    @overload
    def sql_get_connect_attr_w(
        self,
        connection_handle: ConnectionHandle,
        attribute: Literal[ConnectionAttribute.SQL_ATTR_AUTOCOMMIT],
    ) -> SQLAttrAutocommit: ...

    @overload
    def sql_get_connect_attr_w(
        self,
        connection_handle: ConnectionHandle,
        attribute: Literal[ConnectionAttribute.SQL_ATTR_TRACE],
    ) -> SQLAttrTrace: ...

    def sql_get_connect_attr_w(
        self,
        connection_handle: ConnectionHandle,
        attribute: ConnectionAttribute,
    ) -> Any:
        """Get the value of a connection attribute.

        This method calls SQLGetConnectAttrW in the driver manager, which returns the current setting of a connection
        attribute.

        :param connection_handle: The connection handle (HDBC).
        :param attribute: The attribute to retrieve the value of.
        :return: The value of the connection attribute.
        """
        # "For integer-type attributes, some drivers may only write the lower
        # 32-bit or 16-bit of a buffer and leave the higher-order bit unchanged.
        # Therefore, applications should use a buffer of SQLULEN and initialize
        # the value to 0 before calling this function."
        value = ffi.new("SQLULEN *", 0)

        string_length_ptr = ffi.new("SQLINTEGER *")

        rc = self._lib.SQLGetConnectAttrW(
            ffi.cast("SQLHDBC", connection_handle.handle),
            int(attribute),
            value,
            ffi.sizeof("SQLINTEGER"),
            string_length_ptr,
        )
        self.raise_for_return_code(
            return_code=rc,
            what="SQLGetConnectAttrW",
            handle=connection_handle,
        )
        ret: int = value[0]
        if attribute == ConnectionAttribute.SQL_ATTR_ACCESS_MODE:
            return SQLAttrAccessMode(ret)
        if attribute == ConnectionAttribute.SQL_ATTR_AUTOCOMMIT:
            return SQLAttrAutocommit(ret)
        if attribute == ConnectionAttribute.SQL_ATTR_TRACE:
            return SQLAttrTrace(ret)
        raise RuntimeError(f"Unsupported connection attribute: {attribute}")

    @overload
    def sql_get_env_attr(
        self,
        environment_handle: EnvironmentHandle,
        attribute: Literal[EnvironmentAttribute.SQL_ATTR_CONNECTION_POOLING],
    ) -> SQLAttrConnectionPooling: ...

    @overload
    def sql_get_env_attr(
        self,
        environment_handle: EnvironmentHandle,
        attribute: Literal[EnvironmentAttribute.SQL_ATTR_ODBC_VERSION],
    ) -> SQLAttrODBCVersion: ...

    @overload
    def sql_get_env_attr(
        self,
        environment_handle: EnvironmentHandle,
        attribute: Literal[EnvironmentAttribute.SQL_ATTR_CP_MATCH],
    ) -> SQLAttrCPMatch: ...

    def sql_get_env_attr(
        self,
        environment_handle: EnvironmentHandle,
        attribute: EnvironmentAttribute,
    ) -> Any:
        """Get the value of an environment attribute.

        This method calls SQLGetEnvAttr in the driver manager, which returns the current setting of an environment
        attribute.

        :param environment_handle: The environment handle (HENV).
        :param attribute: The attribute to retrieve the value of.
        :return: The value of the environment attribute.
        """
        value = ffi.new("SQLINTEGER *")
        string_length_ptr = ffi.new("SQLINTEGER *")
        rc = self._lib.SQLGetEnvAttr(
            ffi.cast("SQLHENV", environment_handle.handle),
            int(attribute),
            value,
            ffi.sizeof("SQLINTEGER"),
            string_length_ptr,
        )
        self.raise_for_return_code(
            return_code=rc,
            what="SQLGetEnvAttr",
            handle=environment_handle,
        )
        ret = int(value[0])
        if attribute == EnvironmentAttribute.SQL_ATTR_ODBC_VERSION:
            return SQLAttrODBCVersion(ret)
        if attribute == EnvironmentAttribute.SQL_ATTR_CONNECTION_POOLING:
            return SQLAttrConnectionPooling(ret)
        if attribute == EnvironmentAttribute.SQL_ATTR_CP_MATCH:
            return SQLAttrCPMatch(ret)
        raise RuntimeError(f"Unsupported environment attribute: {attribute}")

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[
            InfoType.SQL_ACCESSIBLE_PROCEDURES,
            InfoType.SQL_ACCESSIBLE_TABLES,
            InfoType.SQL_COLUMN_ALIAS,
            InfoType.SQL_DATA_SOURCE_READ_ONLY,
            InfoType.SQL_EXPRESSIONS_IN_ORDERBY,
            InfoType.SQL_INTEGRITY,
            InfoType.SQL_LIKE_ESCAPE_CLAUSE,
            InfoType.SQL_MAX_ROW_SIZE_INCLUDES_LONG,
            InfoType.SQL_MULT_RESULT_SETS,
            InfoType.SQL_MULTIPLE_ACTIVE_TXN,
            InfoType.SQL_NEED_LONG_DATA_LEN,
            InfoType.SQL_ORDER_BY_COLUMNS_IN_SELECT,
            InfoType.SQL_PROCEDURES,
            InfoType.SQL_ROW_UPDATES,
        ],
    ) -> Literal["Y", "N"]: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[
            InfoType.SQL_CATALOG_NAME_SEPARATOR,
            InfoType.SQL_CATALOG_TERM,
            InfoType.SQL_DATA_SOURCE_NAME,
            InfoType.SQL_DATABASE_NAME,
            InfoType.SQL_DBMS_NAME,
            InfoType.SQL_DBMS_VER,
            InfoType.SQL_DRIVER_NAME,
            InfoType.SQL_DRIVER_ODBC_VER,
            InfoType.SQL_DRIVER_VER,
            InfoType.SQL_IDENTIFIER_QUOTE_CHAR,
            InfoType.SQL_KEYWORDS,
            InfoType.SQL_ODBC_VER,
            InfoType.SQL_PROCEDURE_TERM,
            InfoType.SQL_SCHEMA_TERM,
            InfoType.SQL_SEARCH_PATTERN_ESCAPE,
            InfoType.SQL_SERVER_NAME,
            InfoType.SQL_SPECIAL_CHARACTERS,
            InfoType.SQL_TABLE_TERM,
            InfoType.SQL_USER_NAME,
        ],
    ) -> str: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[
            InfoType.SQL_ACTIVE_ENVIRONMENTS,
            InfoType.SQL_MAX_BINARY_LITERAL_LEN,
            InfoType.SQL_MAX_CATALOG_NAME_LEN,
            InfoType.SQL_MAX_CHAR_LITERAL_LEN,
            InfoType.SQL_MAX_CONCURRENT_ACTIVITIES,
            InfoType.SQL_MAX_COLUMN_NAME_LEN,
            InfoType.SQL_MAX_COLUMNS_IN_GROUP_BY,
            InfoType.SQL_MAX_COLUMNS_IN_INDEX,
            InfoType.SQL_MAX_COLUMNS_IN_ORDER_BY,
            InfoType.SQL_MAX_COLUMNS_IN_SELECT,
            InfoType.SQL_MAX_COLUMNS_IN_TABLE,
            InfoType.SQL_MAX_CURSOR_NAME_LEN,
            InfoType.SQL_MAX_DRIVER_CONNECTIONS,
            InfoType.SQL_MAX_INDEX_SIZE,
            InfoType.SQL_MAX_ROW_SIZE,
            InfoType.SQL_MAX_PROCEDURE_NAME_LEN,
            InfoType.SQL_MAX_SCHEMA_NAME_LEN,
            InfoType.SQL_MAX_STATEMENT_LEN,
            InfoType.SQL_MAX_TABLE_NAME_LEN,
            InfoType.SQL_MAX_TABLES_IN_SELECT,
            InfoType.SQL_MAX_USER_NAME_LEN,
        ],
    ) -> int: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_ALTER_DOMAIN],
    ) -> SQLAlterDomain: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_ALTER_TABLE],
    ) -> SQLAlterTable: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_BATCH_ROW_COUNT],
    ) -> SQLBatchRowCount: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_BATCH_SUPPORT],
    ) -> SQLBatchSupport: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_BOOKMARK_PERSISTENCE],
    ) -> SQLBookmarkPersistence: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CATALOG_LOCATION],
    ) -> SQLCatalogLocation: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CATALOG_USAGE],
    ) -> SQLCatalogUsage: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CONCAT_NULL_BEHAVIOR],
    ) -> SQLConcatNullBehavior: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[
            InfoType.SQL_CONVERT_BIGINT,
            InfoType.SQL_CONVERT_BINARY,
            InfoType.SQL_CONVERT_BIT,
            InfoType.SQL_CONVERT_CHAR,
            InfoType.SQL_CONVERT_GUID,
            InfoType.SQL_CONVERT_DATE,
            InfoType.SQL_CONVERT_DECIMAL,
            InfoType.SQL_CONVERT_DOUBLE,
            InfoType.SQL_CONVERT_FLOAT,
            InfoType.SQL_CONVERT_INTEGER,
            InfoType.SQL_CONVERT_INTERVAL_YEAR_MONTH,
            InfoType.SQL_CONVERT_INTERVAL_DAY_TIME,
            InfoType.SQL_CONVERT_LONGVARBINARY,
            InfoType.SQL_CONVERT_LONGVARCHAR,
            InfoType.SQL_CONVERT_NUMERIC,
            InfoType.SQL_CONVERT_REAL,
            InfoType.SQL_CONVERT_SMALLINT,
            InfoType.SQL_CONVERT_TIME,
            InfoType.SQL_CONVERT_TIMESTAMP,
            InfoType.SQL_CONVERT_TINYINT,
            InfoType.SQL_CONVERT_VARBINARY,
            InfoType.SQL_CONVERT_VARCHAR,
            InfoType.SQL_CONVERT_WCHAR,
            InfoType.SQL_CONVERT_WLONGVARCHAR,
            InfoType.SQL_CONVERT_WVARCHAR,
        ],
    ) -> SQLConvert: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CONVERT_FUNCTIONS],
    ) -> SQLConvertFunctions: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CORRELATION_NAME],
    ) -> SQLCorrelationName: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CREATE_ASSERTION],
    ) -> SQLCreateAssertion: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CREATE_CHARACTER_SET],
    ) -> SQLCreateCharacterSet: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CREATE_COLLATION],
    ) -> SQLCreateCollation: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CREATE_DOMAIN],
    ) -> SQLCreateDomain: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CREATE_SCHEMA],
    ) -> SQLCreateSchema: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CREATE_TABLE],
    ) -> SQLCreateTable: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CREATE_TRANSLATION],
    ) -> SQLCreateTranslation: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CREATE_VIEW],
    ) -> SQLCreateView: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CURSOR_COMMIT_BEHAVIOR],
    ) -> SQLCursorCommitBehavior: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_CURSOR_ROLLBACK_BEHAVIOR],
    ) -> SQLCursorRollbackBehavior: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_DATETIME_LITERALS],
    ) -> SQLDatetimeLiterals: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_DEFAULT_TXN_ISOLATION],
    ) -> SQLTxnIsolationOption: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_DROP_ASSERTION],
    ) -> SQLDropAssertion: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_DROP_CHARACTER_SET],
    ) -> SQLDropCharacterSet: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_DROP_COLLATION],
    ) -> SQLDropCollation: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_FILE_USAGE],
    ) -> SQLFileUsage: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_GETDATA_EXTENSIONS],
    ) -> SQLGetDataExtensions: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_GROUP_BY],
    ) -> SQLGroupBy: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_IDENTIFIER_CASE],
    ) -> SQLIdentifierCase: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_NON_NULLABLE_COLUMNS],
    ) -> SQLNonNullableColumns: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_NULL_COLLATION],
    ) -> SQLNullCollation: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_NUMERIC_FUNCTIONS],
    ) -> SQLNumericFunctions: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_ODBC_SAG_CLI_CONFORMANCE],
    ) -> SQLOdbcSagCliConformance: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_ODBC_SQL_CONFORMANCE],
    ) -> SQLOdbcSqlConformance: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_OJ_CAPABILITIES],
    ) -> SQLOuterJoinCapabilities: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_OUTER_JOINS],
    ) -> SQLOuterJoins: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_QUOTED_IDENTIFIER_CASE],
    ) -> SQLIdentifierCase: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_SCHEMA_USAGE],
    ) -> SQLSchemaUsage: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_SCROLL_CONCURRENCY],
    ) -> SQLScrollConcurrency: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_SCROLL_OPTIONS],
    ) -> SQLScrollOptions: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_SQL_CONFORMANCE],
    ) -> SQLSqlConformance: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_STRING_FUNCTIONS],
    ) -> SQLStringFunctions: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_SUBQUERIES],
    ) -> SQLSubqueries: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_SYSTEM_FUNCTIONS],
    ) -> SQLSystemFunctions: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_TIMEDATE_ADD_INTERVALS, InfoType.SQL_TIMEDATE_DIFF_INTERVALS],
    ) -> SQLTimestampIntervals: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_TIMEDATE_FUNCTIONS],
    ) -> SQLTimeDateFunctions: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_TXN_CAPABLE],
    ) -> SQLTxnCapable: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_TXN_ISOLATION_OPTION],
    ) -> SQLTxnIsolationOption: ...

    @overload
    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: Literal[InfoType.SQL_UNION],
    ) -> SQLUnion: ...

    def sql_get_info_w(
        self,
        connection_handle: ConnectionHandle,
        info_type: InfoType,
    ) -> Any:
        """Return information about the driver and data source associated with a connection.

        :param connection_handle: Connection handle (HDBC).
        :param info_type: Type of information.
        :return: The info for the requested info_type.
        """
        hdbc = connection_handle.handle
        string_length_ptr = ffi.new("SQLSMALLINT *")

        if info_type in SQL_GET_INFO_STRING_INFO_TYPES:
            buffer = ffi.new("SQLWCHAR[]", 2056)
            buffer_nbytes = ffi.sizeof(buffer)

            rc = self._lib.SQLGetInfoW(
                ffi.cast("SQLHDBC", hdbc),
                int(info_type),
                buffer,
                buffer_nbytes,
                string_length_ptr,
            )
            self.raise_for_return_code(
                return_code=rc,
                what="SQLGetInfoW",
                handle=connection_handle,
            )
            # TODO: Grow buffer & retry if payload_nbytes >= buffer_nbytes,
            #  or call with a null buffer and read the StrLenPtr before calling again
            ret = decode_sqlwchar_buffer(buffer, num_bytes=string_length_ptr[0])

            if enum_type := SQL_GET_INFO_ENUM_MAP.get(info_type):
                return enum_type(ret)

            return ret

        if info_type in SQL_GET_INFO_USMALLINT_INFO_TYPES:
            value = ffi.new("SQLUSMALLINT *")
            rc = self._lib.SQLGetInfoW(
                ffi.cast("SQLHDBC", hdbc),
                int(info_type),
                value,
                0,  # ignored for non-strings
                string_length_ptr,
            )
            self.raise_for_return_code(
                return_code=rc,
                what="SQLGetInfoW",
                handle=connection_handle,
            )
            if (enum_type := SQL_GET_INFO_ENUM_MAP.get(info_type)) is not None:
                return enum_type(value[0])
            return value[0]
        raise NotImplementedError(f"Unsupported info type: {info_type}")

    @overload
    def sql_set_connect_attr_w(
        self,
        connection_handle: ConnectionHandle,
        attribute: Literal[ConnectionAttribute.SQL_ATTR_ACCESS_MODE],
        value: SQLAttrAccessMode,
    ) -> None: ...

    @overload
    def sql_set_connect_attr_w(
        self,
        connection_handle: ConnectionHandle,
        attribute: Literal[ConnectionAttribute.SQL_ATTR_AUTOCOMMIT],
        value: SQLAttrAutocommit,
    ) -> None: ...

    @overload
    def sql_set_connect_attr_w(
        self,
        connection_handle: ConnectionHandle,
        attribute: Literal[ConnectionAttribute.SQL_ATTR_TRACE],
        value: SQLAttrTrace,
    ) -> None: ...

    def sql_set_connect_attr_w(
        self,
        connection_handle: ConnectionHandle,
        attribute: ConnectionAttribute,
        value: IntEnum,  # TODO: this can either be an integer or a string
    ) -> None:
        """Set an attribute on a connection.

        This method calls SQLSetConnectAttrW in the driver manager, which sets attributes that govern aspects of
        connections.

        :param connection_handle: Connection handle (HDBC).
        :param attribute: The attribute to set.
        :param value: The value to set. Depending on the value of `attribute`, `value` will either be a 32-bit integer
            or a string.
        """
        hdbc = connection_handle.handle
        rc = self._lib.SQLSetConnectAttrW(
            ffi.cast("SQLHDBC", hdbc),
            int(attribute),
            ffi.cast("SQLPOINTER", int(value)),
            0,
        )
        self.raise_for_return_code(
            return_code=rc,
            what="SQLSetConnectAttrW",
            handle=connection_handle,
        )

    @overload
    def sql_set_env_attr(
        self,
        environment_handle: EnvironmentHandle,
        attribute: Literal[EnvironmentAttribute.SQL_ATTR_ODBC_VERSION],
        value: SQLAttrODBCVersion,
    ) -> None: ...

    @overload
    def sql_set_env_attr(
        self,
        environment_handle: EnvironmentHandle,
        attribute: Literal[EnvironmentAttribute.SQL_ATTR_CONNECTION_POOLING],
        value: SQLAttrConnectionPooling,
    ) -> None: ...

    @overload
    def sql_set_env_attr(
        self,
        environment_handle: EnvironmentHandle,
        attribute: Literal[EnvironmentAttribute.SQL_ATTR_CP_MATCH],
        value: SQLAttrCPMatch,
    ) -> None: ...

    def sql_set_env_attr(
        self,
        environment_handle: EnvironmentHandle,
        attribute: EnvironmentAttribute,
        value: IntEnum,
    ) -> None:
        """Set an attribute on an environment.

        This method calls SQLSetEnvAttr in the driver manager, which sets attributes that govern aspects of
        environments.

        :param environment_handle: Environment handle (HENV).
        :param attribute: The attribute to set.
        :param value: The value to set. Depending on the value of `attribute`, `value` will either be a 32-bit integer
            or a string.
        """
        henv = environment_handle.handle
        rc = self._lib.SQLSetEnvAttr(
            ffi.cast("SQLHENV", henv),
            int(attribute),
            ffi.cast("SQLPOINTER", int(value)),
            0,
        )
        self.raise_for_return_code(
            return_code=rc,
            what="SQLSetEnvAttr",
            handle=environment_handle,
        )
