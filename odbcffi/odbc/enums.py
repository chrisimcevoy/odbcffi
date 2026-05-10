"""Enumerations for ODBC.

Most of these are constants defined in ODBC source.

They are logically grouped as Python enums to aid static typing for function arguments and return values.
"""

from __future__ import annotations

from enum import Enum, IntEnum, IntFlag

__all__ = [
    "ConnectionAttribute",
    "DriverCompletion",
    "EnvironmentAttribute",
    "HandleType",
    "InfoType",
    "SQLAlterTable",
    "SQLAttrAccessMode",
    "SQLAttrAutocommit",
    "SQLAttrCPMatch",
    "SQLAttrConnectionPooling",
    "SQLAttrODBCVersion",
    "SQLAttrTrace",
    "SQLBookmarkPersistence",
    "SQLCatalogLocation",
    "SQLCatalogUsage",
    "SQLConcatNullBehavior",
    "SQLConvert",
    "SQLConvertFunctions",
    "SQLCorrelationName",
    "SQLCursorCommitBehavior",
    "SQLCursorRollbackBehavior",
    "SQLFileUsage",
    "SQLGetDataExtensions",
    "SQLGroupBy",
    "SQLIdentifierCase",
    "SQLNonNullableColumns",
    "SQLNullCollation",
    "SQLNumericFunctions",
    "SQLOdbcSagCliConformance",
    "SQLOdbcSqlConformance",
    "SQLOuterJoinCapabilities",
    "SQLOuterJoins",
    "SQLReturn",
    "SQLSchemaUsage",
    "SQLScrollConcurrency",
    "SQLScrollOptions",
    "SQLStringFunctions",
    "SQLSubqueries",
    "SQLSystemFunctions",
    "SQLTimeDateFunctions",
    "SQLTimestampIntervals",
    "SQLTxnCapable",
    "SQLTxnIsolationOption",
    "SQLUnion",
]


class ConnectionAttribute(IntEnum):
    """The attributes of a Connection."""

    SQL_ATTR_ACCESS_MODE = 101
    """An indicator that the connection is not required to support SQL statements that cause updates to occur."""

    SQL_ATTR_AUTOCOMMIT = 102
    """A SQLUINTEGER value that specifies whether to use autocommit or manual- commit mode."""

    SQL_ATTR_TRACE = 104
    """An SQLUINTEGER value telling the Driver Manager whether to perform tracing."""


class DriverCompletion(IntEnum):
    """Driver completion modes for SQLDriverConnect.

    These values control how the ODBC driver completes a connection when using `SQLDriverConnect`, particularly whether
    user interaction (e.g. a dialog prompt) is allowed or required.

    The modes determine whether missing connection information may be requested from the user or must be provided
    programmatically.
    """

    SQL_DRIVER_NOPROMPT = 0
    """If the connection string contains enough information, the driver connects to the data source and copies
    *InConnectionString to *OutConnectionString.

    Otherwise, the driver returns SQL_ERROR for SQLDriverConnect.
    """

    SQL_DRIVER_COMPLETE = 1
    """If the connection string contains enough information, and that information is correct, the driver connects to the
    data source and copies *InConnectionString to *OutConnectionString.

    If any information is missing or incorrect, the driver takes the same actions as it does when DriverCompletion is
    SQL_DRIVER_PROMPT.
    """

    SQL_DRIVER_PROMPT = 2
    """The driver displays a dialog box, using the values from the connection string and system information (if any) as
    initial values.

    When the user exits the dialog box, the driver connects to the data source. It also constructs a connection string
    from the value of the DSN or DRIVER keyword in *InConnectionString and the information returned from the dialog box.
    It places this connection string in the *OutConnectionString buffer.
    """

    SQL_DRIVER_COMPLETE_REQUIRED = 3
    """Same as SQL_DRIVER_COMPLETE, except that the driver disables the controls for any information not required to
    connect to the data source."""


class EnvironmentAttribute(IntEnum):
    """The attributes of an Environment."""

    SQL_ATTR_CONNECTION_POOLING = 201
    """Enables or disables connection pooling at the environment level."""

    SQL_ATTR_CP_MATCH = 202
    """Determines how a connection is chosen from a connection pool."""

    SQL_ATTR_ODBC_VERSION = 200
    """Determines whether certain functionality exhibits ODBC 2.x or
    3.x behavior."""


class HandleType(IntEnum):
    """ODBC handle types (SQLSMALLINT values for SQLAllocHandle).

    These values identify the type of handle being allocated or freed via ODBC functions such as `SQLAllocHandle` and
    `SQLFreeHandle`.

    The ODBC handle hierarchy is:

        Environment (SQL_HANDLE_ENV)
            └── Connection (SQL_HANDLE_DBC)
                    └── Statement (SQL_HANDLE_STMT)
            └── Descriptor (SQL_HANDLE_DESC)

    Each handle type corresponds to a different kind of resource managed by the driver manager.
    """

    SQL_HANDLE_ENV = 1
    """Environment handle (HENV)."""

    SQL_HANDLE_DBC = 2
    """Connection handle (HDBC)."""

    SQL_HANDLE_STMT = 3
    """Statement handle (HSTMT)."""

    SQL_HANDLE_DESC = 4
    """Descriptor handle (HDESC)."""


class InfoType(IntEnum):
    """Types of connection information for use with SQLGetInfo."""

    SQL_MAX_DRIVER_CONNECTIONS = 0
    """An SQLUSMALLINT value that specifies the maximum number of active connections that the driver can support for an
    environment.

    This value can reflect a limitation imposed by either the driver or the data source. If there is no specified limit
    or the limit is unknown, this value is set to zero.

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_ACTIVE_CONNECTIONS.
    """

    SQL_MAX_CONCURRENT_ACTIVITIES = 1
    """An SQLUSMALLINT value that specifies the maximum number of active statements that the driver can support for a
    connection.

    A statement is defined as active if it has results pending, with the term "results" meaning rows from a SELECT
    operation or rows affected by an INSERT, UPDATE, or DELETE operation (such as a row count), or if it is in a
    NEED_DATA state. This value can reflect a limitation imposed by either the driver or the data source. If there is no
    specified limit or the limit is unknown, this value is set to zero.

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_ACTIVE_STATEMENTS.
    """

    SQL_DATA_SOURCE_NAME = 2
    """A character string with the data source name that was used during connection.

    If the application called SQLConnect, this is the value of the szDSN argument. If the application called
    SQLDriverConnect or SQLBrowseConnect, this is the value of the DSN keyword in the connection string passed to the
    driver. If the connection string did not contain the DSN keyword (such as when it contains the DRIVER keyword), this
    is an empty string.
    """

    SQL_DRIVER_HDBC = 3  # deliberately not implemented (exposes driver handles)
    """An SQLULEN value, the driver's connection handle.

    This information type is implemented by the Driver Manager alone.
    """

    SQL_DRIVER_HENV = 4  # deliberately not implemented (exposes driver handles)
    """An SQLULEN value, the driver's environment handle.

    This information type is implemented by the Driver Manager alone.
    """

    SQL_DRIVER_HSTMT = 5  # deliberately not implemented (exposes driver handles)
    """An SQLULEN value, the driver's statement handle determined by the Driver Manager statement handle, which must be
    passed on input in *InfoValuePtr from the application. In this case, InfoValuePtr is both an input and an output
    argument. The input statement handle passed in *InfoValuePtr must have been allocated on the argument
    ConnectionHandle.

    The application should make a copy of the Driver Manager's statement handle before it calls SQLGetInfo with this
    information type, to ensure that the handle is not overwritten on output.

    This information type is implemented by the Driver Manager alone.
    """

    SQL_DRIVER_NAME = 6
    """A character string with the file name of the driver used to access the data source."""

    SQL_DRIVER_VER = 7
    """A character string with the version of the driver and optionally, a description of the driver.

    At a minimum, the version is of the form ##.##.####, where the first two digits are the major version, the next two
    digits are the minor version, and the last four digits are the release version.
    """

    SQL_FETCH_DIRECTION = 8  # Deliberately not implemented (deprecated in ODBC 3.0)
    """An SQLINTEGER bitmask enumerating the supported fetch direction options.

    The following bitmasks are used in conjunction with the flag to determine which options are supported:

    SQL_FD_FETCH_NEXT (ODBC 1.0)
    SQL_FD_FETCH_FIRST (ODBC 1.0)
    SQL_FD_FETCH_LAST (ODBC 1.0)
    SQL_FD_FETCH_PRIOR (ODBC 1.0)
    SQL_FD_FETCH_ABSOLUTE (ODBC 1.0)
    SQL_FD_FETCH_RELATIVE (ODBC 1.0)
    SQL_FD_FETCH_BOOKMARK (ODBC 2.0)
    """

    SQL_ODBC_API_CONFORMANCE = 9  # Deliberately not implemented (deprecated in ODBC 3.0)
    """An SQLSMALLINT value indicating the level of ODBC conformance.

    SQL_OAC_NONE = None

    SQL_OAC_LEVEL1 = Level 1 supported

    SQL_OAC_LEVEL2 = Level 2 supported
    """
    SQL_ODBC_VER = 10
    """A character string with the version of ODBC to which the Driver Manager conforms.

    The version is of the form ##.##.0000, where the first two digits are the major version and the next two digits are
    the minor version. This is implemented only in the Driver Manager.
    """
    SQL_ROW_UPDATES = 11
    """A character string: "Y" if a keyset-driven or mixed cursor maintains row versions or values for all fetched rows
    and therefore can detect any updates that were made to a row by any user since the row was last fetched.

    (This applies only to updates, not to deletions or insertions.) The driver can return the SQL_ROW_UPDATED flag to
    the row status array when SQLFetchScroll is called. Otherwise, "N".
    """
    SQL_ODBC_SAG_CLI_CONFORMANCE = 12
    """The compliance to the functions of the SQL Access Group (SAG) CLI specification.

    A value of:

        SQL_OSCC_NOT_COMPLIANT - the driver is not SAG-compliant.
        SQL_OSCC_COMPLIANT - the driver is SAG-compliant.
    """
    SQL_SERVER_NAME = 13
    """A character string with the actual data source- specific server name; useful when a data source name is used
    during SQLConnect, SQLDriverConnect, and SQLBrowseConnect."""
    SQL_SEARCH_PATTERN_ESCAPE = 14
    """A character string specifying what the driver supports as an escape character that allows the use of the pattern
    match metacharacters underscore (_) and percent sign (%) as valid characters in search patterns. This escape
    character applies only for those catalog function arguments that support search strings. If this string is empty,
    the driver does not support a search- pattern escape character.

    Because this information type does not indicate general support of the escape character in the LIKE predicate,
    SQL-92 does not include requirements for this character string.

    This InfoType is limited to catalog functions. For a description of the use of the escape character in search
    pattern strings, see
    https://learn.microsoft.com/en-us/sql/odbc/reference/develop-app/pattern-value-arguments?view=sql-server-ver17
    """

    SQL_ODBC_SQL_CONFORMANCE = 15
    """An SQLSMALLINT value indicating SQL grammar supported by the driver.

    SQL_OSC_MINIMUM = Minimum grammar supported

    SQL_OSC_CORE = Core grammar supported

    SQL_OSC_EXTENDED = Extended grammar supported.
    """
    SQL_DATABASE_NAME = 16
    """A character string with the name of the current database in use, if the data source defines a named object called
    "database".

    In ODBC 3.x, the value returned for this InfoType can also be returned by calling SQLGetConnectAttr with an
    Attribute argument of SQL_ATTR_CURRENT_CATALOG.

    Several implementations (e.g. unixODBC) mark this info type as deprecated.
    """
    SQL_DBMS_NAME = 17
    """A character string with the name of the DBMS product accessed by the driver."""
    SQL_DBMS_VER = 18
    """A character string that indicates the version of the DBMS product accessed by the driver.

    The version is of the form ##.##.####, where the first two digits
    are the major version, the next two digits are the minor version,
    and the last four digits are the release version. The driver must
    render the DBMS product version in this form but can also append
    the DBMS product-specific version. For example, "04.01.0000 Rdb
    4.1".
    """
    SQL_ACCESSIBLE_TABLES = 19
    """A character string: "Y" if the user is guaranteed SELECT privileges to all tables returned by SQLTables; "N" if
    there may be tables returned that the user cannot access."""
    SQL_ACCESSIBLE_PROCEDURES = 20
    """A character string: "Y" if the user can execute all procedures returned by SQLProcedures; "N" if there may be
    procedures returned that the user cannot execute."""
    SQL_PROCEDURES = 21
    """A character string: "Y" if the data source supports procedures and the driver supports the ODBC procedure
    invocation syntax; "N" otherwise."""

    SQL_CONCAT_NULL_BEHAVIOR = 22
    """An SQLUSMALLINT value that indicates how the data source handles the concatenation of NULL valued character data
    type columns with non-NULL valued character data type columns:

    SQL_CB_NULL = Result is NULL valued.
    SQL_CB_NON_NULL = Result is concatenation of non-NULL valued column or columns.

    A SQL-92 Entry level-conformant driver will always return SQL_CB_NULL.
    """
    SQL_CURSOR_COMMIT_BEHAVIOR = 23
    """An SQLUSMALLINT value that indicates how a COMMIT operation affects cursors and prepared statements in the data
    source (the behavior of the data source when you commit a transaction).

    The value of this attribute will reflect the current state of the next setting: SQL_COPT_SS_PRESERVE_CURSORS.
    """
    SQL_CURSOR_ROLLBACK_BEHAVIOR = 24
    """An SQLUSMALLINT value that indicates how a ROLLBACK operation affects cursors and prepared statements in the data
    source."""
    SQL_DATA_SOURCE_READ_ONLY = 25
    """A character string.

    "Y" if the data source is set to READ ONLY mode, "N" if it is otherwise.
    """
    SQL_DEFAULT_TXN_ISOLATION = 26
    """An SQLUINTEGER value that indicates the default transaction isolation level supported by the driver or data
    source, or zero if the data source does not support transactions.

    The following terms are used to define transaction isolation levels:

    Dirty Read
        Transaction 1 changes a row. Transaction 2 reads the changed row before transaction 1 commits the change.
        If transaction 1 rolls back the change, transaction 2 will have read a row that is considered to have never
        existed.
    Non-repeatable Read
        Transaction 1 reads a row. Transaction 2 updates or deletes that row and commits this change. If
        transaction 1 tries to reread the row, it will receive different row values or discover that the row has been
        deleted.
    Phantom
        Transaction 1 reads a set of rows that satisfy some search criteria. Transaction 2 generates one or more
        rows (through either inserts or updates) that match the search criteria. If transaction 1 re-executes the
        statement that reads the rows, it receives a different set of rows.
    """
    SQL_EXPRESSIONS_IN_ORDERBY = 27
    """ "Y" if the data source supports expressions in the ORDER BY list; "N" if it does not."""
    SQL_IDENTIFIER_CASE = 28
    """An SQLUSMALLINT value indicating the case-sensitivity of object names (such as table-name).

    This should be contrasted with SQL_QUOTED_IDENTIFIER_CASE, which indicates the case-sensitivity of *quoted*
    identifiers.

    Because identifiers in SQL-92 are never case-sensitive, a driver that conforms strictly to SQL-92 (any level) will
    never return the SQL_IC_SENSITIVE option as supported.
    """
    SQL_IDENTIFIER_QUOTE_CHAR = 29
    """The character string that is used as the starting and ending delimiter of a quoted (delimited) identifier in SQL
    statements. (Identifiers passed as arguments to ODBC functions do not have to be quoted.) If the data source does
    not support quoted identifiers, a blank is returned.

    This character string can also be used for quoting catalog function arguments when the connection attribute
    SQL_ATTR_METADATA_ID is set to SQL_TRUE.

    Because the identifier quote character in SQL-92 is the double quotation mark ("), a driver that conforms strictly
    to SQL-92 will always return the double quotation mark character.
    """
    SQL_MAX_COLUMN_NAME_LEN = 30
    """An SQLUSMALLINT value that specifies the maximum length of a column name in the data source.

    If there is no maximum length or the length is unknown, this value is set to zero.

    An FIPS Entry level-conformant driver will return at least 18. An FIPS Intermediate level-conformant driver will
    return at least 128.
    """
    SQL_MAX_CURSOR_NAME_LEN = 31
    """An SQLUSMALLINT value that specifies the maximum length of a cursor name in the data source.

    If there is no maximum length or the length is unknown, this value is set to zero.

    An FIPS Entry level-conformant driver will return at least 18. An FIPS Intermediate level-conformant driver will
    return at least 128.
    """
    SQL_MAX_SCHEMA_NAME_LEN = 32
    """An SQLUSMALLINT value that specifies the maximum length of a schema name in the data source.

    If there is no maximum length or the length is unknown, this value is set to zero.

    An FIPS Entry level-conformant driver will return at least 18. An FIPS Intermediate level-conformant driver will
    return at least 128.

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_MAX_OWNER_NAME_LEN.
    """
    SQL_MAX_PROCEDURE_NAME_LEN = 33
    """An SQLUSMALLINT value that specifies the maximum length of a procedure name in the data source.

    If there is no maximum length or the length is unknown, this value is set to zero.
    """
    SQL_MAX_CATALOG_NAME_LEN = 34
    """An SQLUSMALLINT value that specifies the maximum length of a catalog name in the data source.

    If there is no maximum length or the length is unknown, this value is set to zero.

    An FIPS Full level-conformant driver will return at least 128.

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_MAX_QUALIFIER_NAME_LEN.
    """
    SQL_MAX_TABLE_NAME_LEN = 35
    """An SQLUSMALLINT value that specifies the maximum length of a table name in the data source.

    If there is no maximum length or the length is unknown, this value is set to zero.

    An FIPS Entry level-conformant driver will return at least 18. An FIPS Intermediate level-conformant driver will
    return at least 128.
    """
    SQL_MULT_RESULT_SETS = 36
    """A character string: "Y" if the data source supports multiple result sets, "N" if it does not."""
    SQL_MULTIPLE_ACTIVE_TXN = 37
    """A character string: "Y" if the driver supports more than one active transaction at the same time, "N" if only one
    transaction can be active at any time.

    The information returned for this information type does not apply in the case of distributed transactions.
    """
    SQL_OUTER_JOINS = 38
    """Indicates the level of support for outer joins."""
    SQL_SCHEMA_TERM = 39
    """A character string with the data source vendor's name for a schema; for example, "owner", "Authorization ID", or
    "Schema".

    The character string can be returned in upper, lower, or mixed case.

    A SQL-92 Entry level-conformant driver will always return "schema".

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_OWNER_TERM.
    """
    SQL_PROCEDURE_TERM = 40
    """A character string with the data source vendor's name for a procedure; for example, "database procedure", "stored
    procedure", "procedure", "package", or "stored query"."""
    SQL_CATALOG_NAME_SEPARATOR = 41
    """A character string: the character or characters that the data source defines as the separator between a catalog
    name and the qualified name element that follows or precedes it.

    An empty string is returned if catalogs are not supported by the data source. To determine whether catalogs are
    supported, an application calls SQLGetInfo with the SQL_CATALOG_NAME information type. A SQL-92 Full level-
    conformant driver will always return ".".

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_QUALIFIER_NAME_SEPARATOR.
    """
    SQL_CATALOG_TERM = 42
    """A character string with the data source vendor's name for a catalog; for example, "database" or "directory".

    This string can be in upper, lower, or mixed case.

    An empty string is returned if catalogs are not supported by the data source. To determine whether catalogs are
    supported, an application calls SQLGetInfo with the SQL_CATALOG_NAME information type. A SQL-92 Full level-
    conformant driver will always return "catalog".

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_QUALIFIER_TERM.
    """
    SQL_SCROLL_CONCURRENCY = 43
    """A 32-bit bitmask enumerating the concurrency control options enabled for scrollable cursors."""
    SQL_SCROLL_OPTIONS = 44
    """An SQLUINTEGER bitmask enumerating the scroll options supported for scrollable cursors."""
    SQL_TABLE_TERM = 45
    """A character string with the data source vendor's name for a table; for example, "table" or "file".

    This character string can be in upper, lower, or mixed case.

    A SQL-92 Entry level-conformant driver will always return "table".
    """
    SQL_TXN_CAPABLE = 46
    """An SQLUSMALLINT value describing the transaction support in the driver or data source."""
    SQL_USER_NAME = 47
    """A character string with the name used in a particular database, which can be different from the login name."""
    SQL_CONVERT_FUNCTIONS = 48
    """An SQLUINTEGER bitmask enumerating the scalar conversion functions supported by the driver and associated data
    source."""
    SQL_NUMERIC_FUNCTIONS = 49
    """An SQLUINTEGER bitmask enumerating the scalar numeric functions supported by the driver and associated data
    source."""
    SQL_STRING_FUNCTIONS = 50
    """An SQLUINTEGER bitmask enumerating the scalar string functions supported by the driver and associated data
    source."""
    SQL_SYSTEM_FUNCTIONS = 51
    """An SQLUINTEGER bitmask enumerating the scalar system functions supported by the driver and associated data
    source."""
    SQL_TIMEDATE_FUNCTIONS = 52
    """An SQLUINTEGER bitmask enumerating the scalar date and time functions supported by the driver and associated data
    source."""
    SQL_CONVERT_BIGINT = 53
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_BIGINT.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_BINARY = 54
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_BINARY.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_BIT = 55
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_BIT.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_CHAR = 56
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_CHAR.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_DATE = 57
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_DATE.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_DECIMAL = 58
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_DECIMAL.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_DOUBLE = 59
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_DOUBLE.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_FLOAT = 60
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_FLOAT.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_INTEGER = 61
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_INTEGER.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_LONGVARCHAR = 62
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for
    SQL_LONGVARCHAR.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_NUMERIC = 63
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_NUMERIC.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_REAL = 64
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_REAL.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_SMALLINT = 65
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for
    SQL_SMALLINT.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_TIME = 66
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_TIME.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_TIMESTAMP = 67
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for
    SQL_TIMESTAMP.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_TINYINT = 68
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_TINYINT.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_VARBINARY = 69
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for
    SQL_VARBINARY.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_VARCHAR = 70
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_VARCHAR.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_CONVERT_LONGVARBINARY = 71
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for
    SQL_LONGVARBINARY.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """
    SQL_TXN_ISOLATION_OPTION = 72
    """An SQLUINTEGER bitmask enumerating the transaction isolation levels available from the driver or data source.

    A SQL-92 Entry level-conformant driver will always return SQL_TXN_SERIALIZABLE as supported. A FIPS Transitional
    level-conformant driver will always return all of these options as supported.
    """
    SQL_INTEGRITY = 73
    """A character string: "Y" if the data source supports the Integrity Enhancement Facility; "N" if it does not.

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_ODBC_SQL_OPT_IEF.
    """

    SQL_CORRELATION_NAME = 74
    """An SQLUSMALLINT value that indicates whether table correlation names are supported:

    SQL_CN_NONE = Correlation names are not supported.
    SQL_CN_DIFFERENT = Correlation names are supported but must differ from the names of the tables they represent.
    SQL_CN_ANY = Correlation names are supported and can be any valid user-defined name.

    A SQL-92 Entry level-conformant driver will always return SQL_CN_ANY."""
    SQL_NON_NULLABLE_COLUMNS = 75
    """An SQLUSMALLINT value that specifies whether the data source supports NOT NULL in columns:

    SQL_NNC_NULL = All columns must be nullable.
    SQL_NNC_NON_NULL = Columns cannot be nullable. (The data source supports the NOT NULL column constraint in CREATE
    TABLE statements.)

    A SQL-92 Entry level-conformant driver will return SQL_NNC_NON_NULL.
    """
    SQL_DRIVER_HLIB = 76  # deliberately not implemented (exposes driver handles)
    SQL_DRIVER_ODBC_VER = 77
    """A character string with the version of ODBC that the driver supports.

    The version is of the form ##.##, where the first two digits are the major version and the next two digits are the
    minor version. SQL_SPEC_MAJOR and SQL_SPEC_MINOR define the major and minor version numbers.
    """

    SQL_LOCK_TYPES = 78  # Deliberately not implemented (deprecated in ODBC 3.0)
    SQL_POS_OPERATIONS = 79  # Deliberately not implemented (deprecated in ODBC 3.0)
    SQL_POSITIONED_STATEMENTS = 80  # Deliberately not implemented (deprecated in ODBC 3.0)
    SQL_GETDATA_EXTENSIONS = 81
    """An SQLUINTEGER bitmask enumerating extensions to SQLGetData."""
    SQL_BOOKMARK_PERSISTENCE = 82
    """An SQLUINTEGER bitmask enumerating the operations through which bookmarks persist."""

    SQL_STATIC_SENSITIVITY = 83  # Deliberately not implemented (deprecated in ODBC 3.0)
    SQL_FILE_USAGE = 84
    """An SQLUSMALLINT value that indicates how a single-tier driver directly treats files in a data source.

    An application might use this to determine how users will select data. For example, Xbase users often think of data
    as stored in files, whereas ORACLE and Microsoft Access users generally think of data as stored in tables.

    When a user selects an Xbase data source, the application could display the Windows File Open common dialog box;
    when the user selects a Microsoft Access or ORACLE data source, the application could display a custom Select Table
    dialog box.
    """
    SQL_NULL_COLLATION = 85
    """An SQLUSMALLINT value that specifies where NULLs are sorted in a result set."""

    SQL_ALTER_TABLE = 86
    """An SQLUINTEGER bitmask enumerating the clauses in the ALTER TABLE statement supported by the data source."""

    SQL_COLUMN_ALIAS = 87
    """A character string: "Y" if the data source supports column aliases; otherwise, "N".

    A column alias is an alternative name that can be specified for a column in the select list by using an AS clause.

    A SQL-92 Entry level-conformant driver will always return "Y".
    """

    SQL_GROUP_BY = 88
    """An SQLUSMALLINT value that specifies the relationship between the columns in the GROUP BY clause and the
    nonaggregated columns in the select list.

    A SQL-92 Entry level-conformant driver will always return the SQL_GB_GROUP_BY_EQUALS_SELECT option as supported. A
    SQL-92 Full level-conformant driver will always return the SQL_GB_COLLATE option as supported. If none of the
    options are supported, the GROUP BY clause is not supported by the data source.
    """

    SQL_KEYWORDS = 89
    """A character string that contains a comma-separated list of all data source-specific keywords.

    This list does not contain keywords specific to ODBC or keywords used by both the data source and ODBC. This list
    represents all the reserved keywords; interoperable applications should not use these words in object names.
    """
    SQL_ORDER_BY_COLUMNS_IN_SELECT = 90
    """A character string: "Y" if the columns in the ORDER BY clause must be in the select list; otherwise, "N"."""
    SQL_SCHEMA_USAGE = 91
    """An SQLUINTEGER bitmask enumerating the statements in which schemas can be used.

    SQL_SU_DML_STATEMENTS = Schemas are supported in all Data Manipulation Language statements: SELECT, INSERT, UPDATE,
    DELETE, and if supported, SELECT FOR UPDATE and positioned update and delete statements.

    SQL_SU_PROCEDURE_INVOCATION = Schemas are supported in the ODBC procedure invocation statement.

    SQL_SU_TABLE_DEFINITION = Schemas are supported in all table definition statements: CREATE TABLE, CREATE VIEW, ALTER
    TABLE, DROP TABLE, and DROP VIEW.

    SQL_SU_INDEX_DEFINITION = Schemas are supported in all index definition statements: CREATE INDEX and DROP INDEX.

    SQL_SU_PRIVILEGE_DEFINITION = Schemas are supported in all privilege definition statements: GRANT and REVOKE.

    A SQL-92 Entry level-conformant driver will always return the SQL_SU_DML_STATEMENTS, SQL_SU_TABLE_DEFINITION, and
    SQL_SU_PRIVILEGE_DEFINITION options, as supported.

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_OWNER_USAGE.
    """
    SQL_CATALOG_USAGE = 92
    """An SQLUINTEGER bitmask enumerating the statements in which catalogs can be used.

    The following bitmasks are used to determine where catalogs can be used:

    SQL_CU_DML_STATEMENTS = Catalogs are supported in all Data Manipulation Language statements: SELECT, INSERT, UPDATE,
    DELETE, and if supported, SELECT FOR UPDATE and positioned update and delete statements.

    SQL_CU_PROCEDURE_INVOCATION = Catalogs are supported in the ODBC procedure invocation statement.

    SQL_CU_TABLE_DEFINITION = Catalogs are supported in all table definition statements: CREATE TABLE, CREATE VIEW,
    ALTER TABLE, DROP TABLE, and DROP VIEW.

    SQL_CU_INDEX_DEFINITION = Catalogs are supported in all index definition statements: CREATE INDEX and DROP INDEX.

    SQL_CU_PRIVILEGE_DEFINITION = Catalogs are supported in all privilege definition statements: GRANT and REVOKE.

    A value of 0 is returned if catalogs are not supported by the data source. To determine whether catalogs are
    supported, an application calls SQLGetInfo with the SQL_CATALOG_NAME information type. A SQL-92 Full
    level-conformant driver will always return a bitmask with all of these bits set.

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_QUALIFIER_USAGE.
    """
    SQL_QUOTED_IDENTIFIER_CASE = 93
    """An SQLUSMALLINT value indicating how quoted identifiers are stored in the system catalog.

    This should be contrasted with SQL_IDENTIFIER_CASE, which indicates the case-sensitivity of *unquoted* identifiers.

    - SQL_IC_UPPER = Quoted identifiers in SQL are not case-sensitive and are stored in uppercase in the system catalog.
    - SQL_IC_LOWER = Quoted identifiers in SQL are not case-sensitive and are stored in lowercase in the system catalog.
    - SQL_IC_SENSITIVE = Quoted identifiers in SQL are case sensitive and are stored in mixed case in the system
      catalog. (In a SQL-92-compliant database, quoted identifiers are always case-sensitive.)
    - SQL_IC_MIXED = Quoted identifiers in SQL are not case-sensitive and are stored in mixed case in the system
      catalog.

    A SQL-92 Entry level-conformant driver will always return SQL_IC_SENSITIVE.
    """
    SQL_SPECIAL_CHARACTERS = 94
    """A character string that contains all special characters (that is, all characters except a through z, A through Z,
    0 through 9, and underscore) that can be used in an identifier name, such as a table name, column name, or index
    name, on the data source.

    For example, "#$^". If an identifier contains one or more of these characters, the identifier must be a delimited
    identifier.
    """
    SQL_SUBQUERIES = 95
    """An SQLUINTEGER bitmask enumerating the predicates that support subqueries:

    SQL_SQ_CORRELATED_SUBQUERIES
    SQL_SQ_COMPARISON
    SQL_SQ_EXISTS
    SQL_SQ_IN
    SQL_SQ_QUANTIFIED

    The SQL_SQ_CORRELATED_SUBQUERIES bitmask indicates that all predicates that support subqueries support correlated
    subqueries.

    A SQL-92 Entry level-conformant driver will always return a bitmask in which all of these bits are set.
    """
    SQL_UNION = 96
    """An SQLUINTEGER bitmask enumerating the support for the UNION clause:

    SQL_U_UNION = The data source supports the UNION clause.

    SQL_U_UNION_ALL = The data source supports the ALL keyword in the UNION clause. (SQLGetInfo returns both
    SQL_U_UNION and SQL_U_UNION_ALL in this case.)

    A SQL-92 Entry level-conformant driver will always return both of these options as supported.
    """
    SQL_MAX_COLUMNS_IN_GROUP_BY = 97
    """An SQLUSMALLINT value that specifies the maximum number of columns allowed in a GROUP BY clause.

    If there is no specified limit or the limit is unknown, this value is set to zero.

    An FIPS Entry level-conformant driver will return at least 6. An FIPS Intermediate level-conformant driver will
    return at least 15.
    """
    SQL_MAX_COLUMNS_IN_INDEX = 98
    """An SQLUSMALLINT value that specifies the maximum number of columns allowed in an index.

    If there is no specified limit or the limit is unknown, this value is set to zero.
    """
    SQL_MAX_COLUMNS_IN_ORDER_BY = 99
    """An SQLUSMALLINT value that specifies the maximum number of columns allowed in an ORDER BY clause.

    If there is no specified limit or the limit is unknown, this value is set to zero.

    An FIPS Entry level-conformant driver will return at least 6. An FIPS Intermediate level-conformant driver will
    return at least 15.
    """
    SQL_MAX_COLUMNS_IN_SELECT = 100
    """An SQLUSMALLINT value that specifies the maximum number of columns allowed in a select list.

    If there is no specified limit or the limit is unknown, this value is set to zero.

    An FIPS Entry level-conformant driver will return at least 100. An FIPS Intermediate level-conformant driver will
    return at least 250.
    """
    SQL_MAX_COLUMNS_IN_TABLE = 101
    """An SQLUSMALLINT value that specifies the maximum number of columns allowed in a table.

    If there is no specified limit or the limit is unknown, this value is set to zero.

    An FIPS Entry level-conformant driver will return at least 100. An FIPS Intermediate level-conformant driver will
    return at least 250.
    """
    SQL_MAX_INDEX_SIZE = 102
    """An SQLUINTEGER value that specifies the maximum number of bytes allowed in the combined fields of an index.

    If there is no specified limit or the limit is unknown, this value is set to zero.
    """
    SQL_MAX_ROW_SIZE_INCLUDES_LONG = 103
    """A character string: "Y" if the maximum row size returned for the SQL_MAX_ROW_SIZE information type includes the
    length of all SQL_LONGVARCHAR and SQL_LONGVARBINARY columns in the row; "N" otherwise.
    """
    SQL_MAX_ROW_SIZE = 104
    """An SQLUINTEGER value that specifies the maximum length of a single row in a table.

    If there is no specified limit or the limit is unknown, this value is set to zero.

    An FIPS Entry level-conformant driver will return at least 2,000. An FIPS Intermediate level-conformant driver will
    return at least 8,000.
    """
    SQL_MAX_STATEMENT_LEN = 105
    """An SQLUINTEGER value that specifies the maximum length (number of characters, including white space) of a SQL
    statement.

    If there is no maximum length or the length is unknown, this value is set to zero.
    """
    SQL_MAX_TABLES_IN_SELECT = 106
    """An SQLUSMALLINT value that specifies the maximum number of tables allowed in the FROM clause of a SELECT
    statement.

    If there is no specified limit or the limit is unknown, this value is set to zero.

    An FIPS Entry level-conformant driver will return at least 15. An FIPS Intermediate level-conformant driver will
    return at least 50.
    """
    SQL_MAX_USER_NAME_LEN = 107
    """An SQLUSMALLINT value that specifies the maximum length of a user name in the data source.

    If there is no maximum length or the length is unknown, this value is set to zero.
    """
    SQL_MAX_CHAR_LITERAL_LEN = 108
    """An SQLUINTEGER value that specifies the maximum length (number of characters, excluding the literal prefix and
    suffix returned by SQLGetTypeInfo) of a character literal in a SQL statement.

    If there is no maximum length or the length is unknown, this value is set to zero.
    """
    SQL_TIMEDATE_ADD_INTERVALS = 109
    """An SQLUINTEGER bitmask enumerating the timestamp intervals supported by the driver and associated data source for
    the TIMESTAMPADD scalar function.

    The following bitmasks are used to determine which intervals are supported:

    SQL_FN_TSI_FRAC_SECOND
    SQL_FN_TSI_SECOND
    SQL_FN_TSI_MINUTE
    SQL_FN_TSI_HOUR
    SQL_FN_TSI_DAY
    SQL_FN_TSI_WEEK
    SQL_FN_TSI_MONTH
    SQL_FN_TSI_QUARTER
    SQL_FN_TSI_YEAR

    An FIPS Transitional level-conformant driver will always return a bitmask in which all of these bits are set.
    """
    SQL_TIMEDATE_DIFF_INTERVALS = 110
    """An SQLUINTEGER bitmask enumerating the timestamp intervals supported by the driver and associated data source for
    the TIMESTAMPDIFF scalar function.

    The following bitmasks are used to determine which intervals are supported:

    SQL_FN_TSI_FRAC_SECOND
    SQL_FN_TSI_SECOND
    SQL_FN_TSI_MINUTE
    SQL_FN_TSI_HOUR
    SQL_FN_TSI_DAY
    SQL_FN_TSI_WEEK
    SQL_FN_TSI_MONTH
    SQL_FN_TSI_QUARTER
    SQL_FN_TSI_YEAR

    An FIPS Transitional level-conformant driver will always return a bitmask in which all of these bits are set.
    """
    SQL_NEED_LONG_DATA_LEN = 111
    """A character string: "Y" if the data source needs the length of a long data value (the data type is
    SQL_LONGVARCHAR, SQL_LONGVARBINARY, or a long data source-specific data type) before that value is sent to the data
    source, "N" if it does not.
    """
    SQL_MAX_BINARY_LITERAL_LEN = 112
    """An SQLUINTEGER value that specifies the maximum length (number of hexadecimal characters, excluding the literal
    prefix and suffix returned by SQLGetTypeInfo) of a binary literal in a SQL statement.

    For example, the binary literal 0xFFAA has a length of 4. If there is no maximum length or the length is unknown,
    this value is set to zero.
    """
    SQL_LIKE_ESCAPE_CLAUSE = 113
    """A character string: "Y" if the data source supports an escape character for the percent character (%) and
    underscore character (_) in a LIKE predicate and the driver supports the ODBC syntax for defining a LIKE predicate
    escape character; "N" otherwise."""
    SQL_CATALOG_LOCATION = 114
    """An SQLUSMALLINT value that indicates the position of the catalog in a qualified table name:

    * SQL_CL_START
    * SQL_CL_END

    For example, an Xbase driver returns SQL_CL_START because the directory (catalog) name is at the start of the table
    name, as in \\EMPDATA\\EMP.DBF. An ORACLE Server driver returns SQL_CL_END because the catalog is at the end of the
    table name, as in ADMIN.EMP@EMPDATA.

    A SQL-92 Full level-conformant driver will always return SQL_CL_START. A value of 0 is returned if catalogs are not
    supported by the data source. To determine whether catalogs are supported, an application calls SQLGetInfo with the
    SQL_CATALOG_NAME information type.

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_QUALIFIER_LOCATION.
    """
    SQL_OJ_CAPABILITIES = 115
    """An SQLUINTEGER bitmask enumerating the types of outer joins supported by the driver and data source.

    For information about the support of relational join operators in a SELECT statement, as defined by SQL-92, see
    SQL_SQL92_RELATIONAL_JOIN_OPERATORS.
    """
    SQL_ACTIVE_ENVIRONMENTS = 116
    """An SQLUSMALLINT value that specifies the maximum number of active environments that the driver can support.

    If there is no specified limit or the limit is unknown, this value is set to zero.
    """
    SQL_ALTER_DOMAIN = 117
    SQL_SQL_CONFORMANCE = 118
    SQL_ANSI_SQL_DATETIME_LITERALS = 119
    SQL_BATCH_ROW_COUNT = 120
    SQL_BATCH_SUPPORT = 121
    SQL_CONVERT_WCHAR = 122
    SQL_CONVERT_INTERVAL_DAY_TIME = 123
    SQL_CONVERT_INTERVAL_YEAR_MONTH = 124
    SQL_CONVERT_WLONGVARCHAR = 125
    SQL_CONVERT_WVARCHAR = 126
    SQL_CREATE_ASSERTION = 127
    SQL_CREATE_CHARACTER_SET = 128
    SQL_CREATE_COLLATION = 129
    SQL_CREATE_DOMAIN = 130
    SQL_CREATE_SCHEMA = 131
    SQL_CREATE_TABLE = 132
    SQL_CREATE_TRANSLATION = 133
    SQL_CREATE_VIEW = 134
    SQL_DRIVER_HDESC = 135  # deliberately not implemented (exposes driver handles)
    SQL_DROP_ASSERTION = 136
    SQL_DROP_CHARACTER_SET = 137
    SQL_DROP_COLLATION = 138
    SQL_DROP_DOMAIN = 139
    SQL_DROP_SCHEMA = 140
    SQL_DROP_TABLE = 141
    SQL_DROP_TRANSLATION = 142
    SQL_DROP_VIEW = 143
    SQL_DYNAMIC_CURSOR_ATTRIBUTES1 = 144
    SQL_DYNAMIC_CURSOR_ATTRIBUTES2 = 145
    SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES1 = 146
    SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES2 = 147
    SQL_INDEX_KEYWORDS = 148
    SQL_INFO_SCHEMA_VIEWS = 149
    SQL_KEYSET_CURSOR_ATTRIBUTES1 = 150
    SQL_KEYSET_CURSOR_ATTRIBUTES2 = 151
    SQL_ODBC_INTERFACE_CONFORMANCE = 152
    SQL_PARAM_ARRAY_ROW_COUNTS = 153
    SQL_PARAM_ARRAY_SELECTS = 154
    SQL_SQL92_DATETIME_FUNCTIONS = 155
    SQL_SQL92_FOREIGN_KEY_DELETE_RULE = 156
    SQL_SQL92_FOREIGN_KEY_UPDATE_RULE = 157
    SQL_SQL92_GRANT = 158
    SQL_SQL92_NUMERIC_VALUE_FUNCTIONS = 159
    SQL_SQL92_PREDICATES = 160
    SQL_SQL92_RELATIONAL_JOIN_OPERATORS = 161
    SQL_SQL92_REVOKE = 162
    SQL_SQL92_ROW_VALUE_CONSTRUCTOR = 163
    SQL_SQL92_STRING_FUNCTIONS = 164
    SQL_SQL92_VALUE_EXPRESSIONS = 165
    SQL_STANDARD_CLI_CONFORMANCE = 166
    SQL_STATIC_CURSOR_ATTRIBUTES1 = 167
    SQL_STATIC_CURSOR_ATTRIBUTES2 = 168
    SQL_AGGREGATE_FUNCTIONS = 169
    SQL_DDL_INDEX = 170
    SQL_DM_VER = 171
    SQL_INSERT_STATEMENT = 172
    SQL_CONVERT_GUID = 173
    """An SQLUINTEGER bitmask.

    The bitmask indicates the conversions supported by the data source with the CONVERT scalar function for SQL_GUID.

    If the bitmask equals zero, the data source does not support any conversions from data of that type, including
    conversion to the same data type.
    """

    SQL_XOPEN_CLI_YEAR = 10000
    SQL_CURSOR_SENSITIVITY = 10001
    SQL_DESCRIBE_PARAMETER = 10002
    SQL_CATALOG_NAME = 10003
    SQL_COLLATION_SEQ = 10004
    SQL_MAX_IDENTIFIER_LEN = 10005
    SQL_ASYNC_MODE = 10021
    SQL_MAX_ASYNC_CONCURRENT_STATEMENTS = 10022
    SQL_ASYNC_DBC_FUNCTIONS = 10023
    SQL_DRIVER_AWARE_POOLING_SUPPORTED = 10024
    SQL_ASYNC_NOTIFICATION = 10025


class SQLAlterTable(IntFlag):
    """An SQLUINTEGER bitmask enumerating the clauses in the ALTER TABLE statement supported by the data source.

    The SQL-92 or FIPS conformance level at which this feature must be supported is shown in parentheses next to each
    bitmask.
    """

    #  Suspect some are wrong in Microsoft's sql-docs repo. Others are just absent.
    #  (e.g. SQL_AT_DROP_TABLE_CONSTRAINT_* docstrings reference `<drop column>`
    SQL_AT_ADD_COLUMN = 0x00000001
    """The ability to add multiple columns in a single ALTER TABLE statement is supported.

    This bit does not combine with other SQL_AT_ADD_COLUMN_XXX bits or SQL_AT_CONSTRAINT_XXX bits. (ODBC 2.0)

    Note this flag is deprecated in ODBC 3.x, although drivers must still support it.
    """

    SQL_AT_DROP_COLUMN = 0x00000002
    """The ability to drop columns is supported.

    Whether this results in cascade or restrict behavior is driver-defined. (ODBC 2.0)

    Note this flag is deprecated in ODBC 3.x, although drivers must still support it.
    """

    SQL_AT_ADD_CONSTRAINT = 0x00000008
    """<add column> clause is supported, with facility to specify column constraints (FIPS Transitional level) (ODBC
    3.0)

    If this bit is set, then support for specific <constraint attributes> can be determined via:
    - SQL_AT_CONSTRAINT_INITIALLY_DEFERRED
    - SQL_AT_CONSTRAINT_INITIALLY_IMMEDIATE
    - SQL_AT_CONSTRAINT_DEFERRABLE
    - SQL_AT_CONSTRAINT_NON_DEFERRABLE
    """

    SQL_AT_ADD_COLUMN_SINGLE = 0x00000020
    """<add column> is supported (FIPS Transitional level) (ODBC 3.0)"""

    SQL_AT_ADD_COLUMN_DEFAULT = 0x00000040
    """<add column> clause is supported, with facility to specify column defaults (FIPS Transitional level) (ODBC
    3.0)"""

    SQL_AT_ADD_COLUMN_COLLATION = 0x00000080
    """<add column> clause is supported, with facility to specify column collation (Full level) (ODBC 3.0)"""

    SQL_AT_SET_COLUMN_DEFAULT = 0x00000100
    """<alter column> <set column default clause> is supported (Intermediate level) (ODBC 3.0)"""

    SQL_AT_DROP_COLUMN_DEFAULT = 0x00000200
    """<alter column> <drop column default clause> is supported (Intermediate level) (ODBC 3.0)"""

    SQL_AT_DROP_COLUMN_CASCADE = 0x00000400
    """<drop column> CASCADE is supported (FIPS Transitional level) (ODBC 3.0)"""

    SQL_AT_DROP_COLUMN_RESTRICT = 0x00000800
    """<drop column> RESTRICT is supported (FIPS Transitional level) (ODBC 3.0)"""

    SQL_AT_ADD_TABLE_CONSTRAINT = 0x00001000
    """<add table constraint> clause is supported (FIPS Transitional level) (ODBC 3.0)"""

    SQL_AT_DROP_TABLE_CONSTRAINT_CASCADE = 0x00002000
    """<drop column> CASCADE is supported (FIPS Transitional level) (ODBC 3.0)"""

    SQL_AT_DROP_TABLE_CONSTRAINT_RESTRICT = 0x00004000
    """<drop column> RESTRICT is supported (FIPS Transitional level) (ODBC 3.0)"""

    SQL_AT_CONSTRAINT_NAME_DEFINITION = 0x00008000
    """<constraint name definition> is supported for naming column and table constraints (Intermediate level) (ODBC
    3.0)"""

    SQL_AT_CONSTRAINT_INITIALLY_DEFERRED = 0x00010000
    """The INITIALLY DEFERRED constraint attribute is supported for column or table constraints.

    This bit is meaningful when support for adding column constraints or table constraints is reported by
    SQL_AT_ADD_CONSTRAINT or SQL_AT_ADD_TABLE_CONSTRAINT. (Full level) (ODBC 3.0)
    """

    SQL_AT_CONSTRAINT_INITIALLY_IMMEDIATE = 0x00020000
    """The INITIALLY IMMEDIATE constraint attribute is supported for column or table constraints.

    This bit is meaningful when support for adding column constraints or table constraints is reported by
    SQL_AT_ADD_CONSTRAINT or SQL_AT_ADD_TABLE_CONSTRAINT. (Full level) (ODBC 3.0)
    """

    SQL_AT_CONSTRAINT_DEFERRABLE = 0x00040000
    """The DEFERRABLE constraint attribute is supported for column or table constraints.

    This bit is meaningful when support for adding column constraints or table constraints is reported by
    SQL_AT_ADD_CONSTRAINT or SQL_AT_ADD_TABLE_CONSTRAINT. (Full level) (ODBC 3.0)
    """

    SQL_AT_CONSTRAINT_NON_DEFERRABLE = 0x00080000
    """The NOT DEFERRABLE constraint attribute is supported for column or table constraints.

    This bit is meaningful when support for adding column constraints or table constraints is reported by
    SQL_AT_ADD_CONSTRAINT or SQL_AT_ADD_TABLE_CONSTRAINT. (Full level) (ODBC 3.0)
    """


class SQLAttrAccessMode(IntEnum):
    """Indicates whether the connection is not required to support SQL statements that cause updates to occur."""

    SQL_MODE_READ_WRITE = 0
    """The default access mode."""

    SQL_MODE_READ_ONLY = 1
    """Used by the driver or data source as an indicator that the connection is not required to support SQL statements
    that cause updates to occur.

    This mode can be used to optimize locking strategies, transaction management, or other areas as appropriate to the
    driver or data source. The driver is not required to prevent such statements from being submitted to the data
    source. The behavior of the driver and data source when asked to process SQL statements that are not read- only
    during a read-only connection is implementation- defined.
    """


class SQLAttrAutocommit(IntEnum):
    """A SQLUINTEGER value that specifies whether to use autocommit or manual-commit mode."""

    SQL_AUTOCOMMIT_OFF = 0
    """The driver uses manual-commit mode, and the application must explicitly commit or roll back transactions with
    SQLEndTran."""

    SQL_AUTOCOMMIT_ON = 1
    """The driver uses autocommit mode.

    Each statement is committed immediately after it is executed. This is the default. Any open transactions on the
    connection are committed when SQL_ATTR_AUTOCOMMIT is set to SQL_AUTOCOMMIT_ON to change from manual- commit mode to
    autocommit mode.
    """


class SQLAttrConnectionPooling(IntEnum):
    """A 32-bit SQLUINTEGER value that enables or disables connection pooling at the environment level."""

    SQL_CP_OFF = 0
    """Connection pooling is turned off.

    This is the default.
    """
    SQL_CP_ONE_PER_DRIVER = 1
    """A single connection pool is supported for each driver.

    Every connection in a pool is associated with one driver.
    """
    SQL_CP_ONE_PER_HENV = 2
    """A single connection pool is supported for each environment.

    Every connection in a pool is associated with one environment.
    """
    SQL_CP_DRIVER_AWARE = 3
    """Use the connection-pool awareness feature of the driver, if it is available."""

    SQL_CP_DEFAULT = SQL_CP_OFF
    """Same as SQL_CP_OFF."""


class SQLAttrCPMatch(IntEnum):
    """Values for SQL_ATTR_CP_MATCH.

    A 32-bit SQLUINTEGER value that determines how a connection is chosen from a connection pool. When SQLConnect or
    SQLDriverConnect is called, the Driver Manager determines which connection is reused from the pool. The Driver
    Manager tries to match the connection options in the call and the connection attributes set by the application to
    the keywords and connection attributes of the connections in the pool. The value of this attribute determines the
    level of precision of the matching criteria.
    """

    SQL_CP_STRICT_MATCH = 0
    """Only connections that exactly match the connection options in the call and the connection attributes set by the
    application are reused.

    This is the default.
    """

    SQL_CP_RELAXED_MATCH = 1
    """Connections with matching connection string keywords can be used.

    Keywords must match, but not all connection attributes must match.
    """


class SQLAttrODBCVersion(IntEnum):
    """A 32-bit integer that determines whether certain functionality exhibits ODBC 2.x behavior or ODBC 3.x behavior.

    An application must set this environment attribute before it calls any function that has an SQLHENV argument, or the
    call will return SQLSTATE HY010 (Function sequence error). It is driver-specific whether additional behavior exists
    for these environmental flags.
    """

    SQL_OV_ODBC2 = 2
    """He Driver Manager and driver exhibit the following ODBC 2.x behavior.

    This is especially useful for an ODBC 2.x application working with an ODBC 3.x driver.

    - The driver returns and expects ODBC 2.x codes for date, time, and timestamp.
    - The driver returns ODBC 2.x SQLSTATE codes when SQLError, SQLGetDiagField, or SQLGetDiagRec is called.
    - The CatalogName argument in a call to SQLTables does not accept a search pattern.
    - The Driver Manager does not support C data type extensibility.
    """

    SQL_OV_ODBC3 = 3
    """The Driver Manager and driver exhibit the following ODBC 3.x
    behavior:

    - The driver returns and expects ODBC 3.x codes for date, time, and timestamp.
    - The driver returns ODBC 3.x SQLSTATE codes when SQLError, SQLGetDiagField, or SQLGetDiagRec is called.
    - The CatalogName argument in a call to SQLTables accepts a search pattern.
    - The Driver Manager does not support C data type extensibility.
    """

    SQL_OV_ODBC3_80 = 380
    """The Driver Manager and driver exhibit the following ODBC 3.8
    behavior:

    - The driver returns and expects ODBC 3.x codes for date, time, and timestamp.
    - The driver returns ODBC 3.x SQLSTATE codes when SQLError, SQLGetDiagField, or SQLGetDiagRec is called.
    - The CatalogName argument in a call to SQLTables accepts a search pattern.
    - The Driver Manager supports C data type extensibility.
    """


class SQLAttrTrace(IntEnum):
    """An SQLUINTEGER value telling the Driver Manager whether to perform tracing."""

    SQL_OPT_TRACE_OFF = 0
    """Tracing off (the default)."""

    SQL_OPT_TRACE_ON = 1
    """Tracing on."""


class SQLCatalogLocation(IntEnum):
    r"""An SQLUSMALLINT value that indicates the position of the catalog in a qualified table name.

    For example, an Xbase driver returns SQL_CL_START because the directory (catalog) name is at the start of the table
    name, as in \EMPDATA\EMP.DBF. An ORACLE Server driver returns SQL_CL_END because the catalog is at the end of the
    table name, as in ADMIN.EMP@EMPDATA.

    A SQL-92 Full level-conformant driver will always return SQL_CL_START. A value of 0 is returned if catalogs are not
    supported by the data source. To determine whether catalogs are supported, an application calls SQLGetInfo with the
    SQL_CATALOG_NAME information type.
    """

    UNSUPPORTED = 0
    SQL_CL_START = 0x0001
    SQL_CL_END = 0x0002


class SQLCatalogUsage(IntFlag):
    """An SQLUINTEGER bitmask enumerating the statements in which catalogs can be used.

    A value of 0 is returned if catalogs are not supported by the data source. To determine whether catalogs are
    supported, an application calls SQLGetInfo with the SQL_CATALOG_NAME information type. A SQL-92 Full level-
    conformant driver will always return a bitmask with all of these bits set.
    """

    SQL_CU_DML_STATEMENTS = 0x00000001
    """Catalogs are supported in all Data Manipulation Language statements: SELECT, INSERT, UPDATE, DELETE, and if
    supported, SELECT FOR UPDATE and positioned update and delete statements.
    """
    SQL_CU_PROCEDURE_INVOCATION = 0x00000002
    """Catalogs are supported in the ODBC procedure invocation statement."""
    SQL_CU_TABLE_DEFINITION = 0x00000004
    """Catalogs are supported in all table definition statements: CREATE TABLE, CREATE VIEW, ALTER TABLE, DROP TABLE,
    and DROP VIEW.
    """
    SQL_CU_INDEX_DEFINITION = 0x00000008
    """Catalogs are supported in all index definition statements: CREATE INDEX and DROP INDEX."""
    SQL_CU_PRIVILEGE_DEFINITION = 0x00000010
    """Catalogs are supported in all privilege definition statements: GRANT and REVOKE."""


class SQLConcatNullBehavior(IntEnum):
    """Indicates how the data source handles the concatenation of NULL & non-NULL valued character data type columns."""

    SQL_CB_NULL = 0
    """Result is NULL valued."""

    SQL_CB_NON_NULL = 1
    """Result is concatenation of non-NULL valued column or columns."""


class SQLConvert(IntFlag):
    """Return value for SQL_CONVERT_* arguments passed to SQLGetInfo.

    This bitmask indicates which conversion functions are supported by the data source with the CONVERT scalar function
    for the given SQL_CONVERT_* data type.

    If the bitmask equals zero, the data source does not support any conversions from data of the named type, including
    conversion to the same data type.

    For example, to determine if a data source supports the conversion of SQL_INTEGER data to the SQL_BIGINT data type,
    an application calls SQLGetInfo with the InfoType of SQL_CONVERT_INTEGER. The application performs an AND operation
    with the returned bitmask and SQL_CVT_BIGINT. If the resulting value is nonzero, the conversion is supported.
    """

    SQL_CVT_CHAR = 0x00000001
    SQL_CVT_NUMERIC = 0x00000002
    SQL_CVT_DECIMAL = 0x00000004
    SQL_CVT_INTEGER = 0x00000008
    SQL_CVT_SMALLINT = 0x00000010
    SQL_CVT_FLOAT = 0x00000020
    SQL_CVT_REAL = 0x00000040
    SQL_CVT_DOUBLE = 0x00000080
    SQL_CVT_VARCHAR = 0x00000100
    SQL_CVT_LONGVARCHAR = 0x00000200
    SQL_CVT_BINARY = 0x00000400
    SQL_CVT_VARBINARY = 0x00000800
    SQL_CVT_BIT = 0x00001000
    SQL_CVT_TINYINT = 0x00002000
    SQL_CVT_BIGINT = 0x00004000
    SQL_CVT_DATE = 0x00008000
    SQL_CVT_TIME = 0x00010000
    SQL_CVT_TIMESTAMP = 0x00020000
    SQL_CVT_LONGVARBINARY = 0x00040000
    SQL_CVT_INTERVAL_YEAR_MONTH = 0x00080000
    SQL_CVT_INTERVAL_DAY_TIME = 0x00100000
    SQL_CVT_WCHAR = 0x00200000
    SQL_CVT_WLONGVARCHAR = 0x00400000
    SQL_CVT_WVARCHAR = 0x00800000
    SQL_CVT_GUID = 0x01000000


class SQLConvertFunctions(IntFlag):
    """An SQLUINTEGER bitmask enumerating the scalar conversion functions supported by the driver and data source."""

    SQL_FN_CVT_CONVERT = 1
    SQL_FN_CVT_CAST = 2


class SQLCorrelationName(IntEnum):
    """An SQLUSMALLINT value that indicates whether table correlation names are supported.

    A SQL-92 Entry level-conformant driver will always return SQL_CN_ANY.
    """

    SQL_CN_NONE = 0x0000
    """Correlation names are not supported."""

    SQL_CN_DIFFERENT = 0x0001
    """Correlation names are supported but must differ from the names of the tables they represent."""

    SQL_CN_ANY = 0x0002
    """Correlation names are supported and can be any valid user-defined name."""


class SQLCursorCommitBehavior(IntEnum):
    """Indicates how a COMMIT operation affects cursors and prepared statements in the data source.

    (The behavior of the data source when you commit a transaction.)

    The value of this attribute will reflect the current state of the next setting: SQL_COPT_SS_PRESERVE_CURSORS.
    """

    SQL_CB_DELETE = 0
    """Close cursors and delete prepared statements.

    To use the cursor again, the application must reprepare and re- execute the statement.
    """

    SQL_CB_CLOSE = 1
    """Close cursors.

    For prepared statements, the application can call SQLExecute on the statement without calling SQLPrepare again. The
    default for the SQL ODBC driver is SQL_CB_CLOSE. This means that the SQL ODBC driver will close your cursor(s) when
    you commit a transaction.
    """

    SQL_CB_PRESERVE = 2
    """Preserve cursors in the same position as before the COMMIT operation.

    The application can continue to fetch data, or it can close the cursor and re-execute the statement without
    repreparing it.
    """


class SQLCursorRollbackBehavior(IntEnum):
    """Indicates how a ROLLBACK operation affects cursors and prepared statements in the data source."""

    SQL_CB_DELETE = 0
    """Close cursors and delete prepared statements.

    To use the cursor again, the application must reprepare and re- execute the statement.
    """

    SQL_CB_CLOSE = 1
    """Close cursors.

    For prepared statements, the application can call SQLExecute on the statement without calling SQLPrepare again.
    """

    SQL_CB_PRESERVE = 2
    """Preserve cursors in the same position as before the ROLLBACK operation.

    The application can continue to fetch data, or it can close the cursor and re-execute the statement without
    repreparing it.
    """


class SQLBookmarkPersistence(IntFlag):
    """An SQLUINTEGER bitmask enumerating the operations through which bookmarks persist."""

    SQL_BP_CLOSE = 0x00000001
    """Bookmarks are valid after an application calls SQLFreeStmt with the SQL_CLOSE option, or SQLCloseCursor to close
    the cursor associated with a statement."""
    SQL_BP_DELETE = 0x00000002
    """The bookmark for a row is valid after that row has been deleted."""
    SQL_BP_DROP = 0x00000004
    """Bookmarks are valid after an application calls SQLFreeHandle with a HandleType of SQL_HANDLE_STMT to drop a
    statement."""
    SQL_BP_TRANSACTION = 0x00000008
    """Bookmarks are valid after an application commits or rolls back a transaction."""
    SQL_BP_UPDATE = 0x00000010
    """The bookmark for a row is valid after any column in that row has been updated, including key columns."""
    SQL_BP_OTHER_HSTMT = 0x00000020
    """A bookmark associated with one statement can be used with another statement.

    Unless SQL_BP_CLOSE or SQL_BP_DROP is specified, the cursor on the first statement must be open.
    """

    SQL_BP_SCROLL = 0x00000040
    """Bookmarks are valid after an application scrolls through the result set using SQLFetchScroll or other cursor
    navigation operations."""


class SQLFileUsage(IntEnum):
    """An SQLUSMALLINT value that indicates how a single-tier driver directly treats files in a data source.

    An application might use this to determine how users will select data. For example, Xbase users often think of data
    as stored in files, whereas ORACLE and Microsoft Access users generally think of data as stored in tables.

    When a user selects an Xbase data source, the application could display the Windows File Open common dialog box;
    when the user selects a Microsoft Access or ORACLE data source, the application could display a custom Select Table
    dialog box.
    """

    SQL_FILE_NOT_SUPPORTED = 0x0000
    """The driver is not a single-tier driver.

    For example, an ORACLE driver is a two-tier driver.
    """
    SQL_FILE_TABLE = 0x0001
    """A single-tier driver treats files in a data source as tables.

    For example, an Xbase driver treats each Xbase file as a table.
    """
    SQL_FILE_CATALOG = 0x0002
    """A single-tier driver treats files in a data source as a catalog.

    For example, a Microsoft Access driver treats each Microsoft Access file as a complete database.
    """


class SQLGetDataExtensions(IntFlag):
    """An SQLUINTEGER bitmask enumerating extensions to SQLGetData.

    SQLGetData is required to return data only from unbound columns that occur after the last bound column, are called
    in order of increasing column number, and are not in a row in a block of rows.

    If a driver supports bookmarks (either fixed-length or variable-length), it must support calling SQLGetData on
    column 0. This support is required regardless of what the driver returns for a call to SQLGetInfo with the
    SQL_GETDATA_EXTENSIONS InfoType.
    """

    SQL_GD_ANY_COLUMN = 0x00000001
    """SQLGetData can be called for any unbound column, including those before the last bound column.

    Note that the columns must be called in order of ascending column number unless SQL_GD_ANY_ORDER is also returned.
    """
    SQL_GD_ANY_ORDER = 0x00000002
    """SQLGetData can be called for unbound columns in any order.

    Note that SQLGetData can be called only for columns after the last bound column unless SQL_GD_ANY_COLUMN is also
    returned.
    """
    SQL_GD_BLOCK = 0x00000004
    """SQLGetData can be called for an unbound column in any row in a block (where the rowset size is greater than 1) of
    data after positioning to that row with SQLSetPos."""
    SQL_GD_BOUND = 0x00000008
    """SQLGetData can be called for bound columns in addition to unbound columns.

    A driver cannot return this value unless it also returns SQL_GD_ANY_COLUMN.
    """

    SQL_GD_OUTPUT_PARAMS = 0x00000010
    """SQL_GD_OUTPUT_PARAMS = SQLGetData can be called to return output parameter values."""


class SQLGroupBy(IntEnum):
    """The relationship between the columns in the GROUP BY clause and the nonaggregated columns in the select list.

    A SQL-92 Entry level-conformant driver will always return the SQL_GB_GROUP_BY_EQUALS_SELECT option as supported.

    A SQL-92 Full level-conformant driver will always return the SQL_GB_COLLATE option as supported. If none of the
    options are supported, the GROUP BY clause is not supported by the data source.
    """

    SQL_GB_NOT_SUPPORTED = 0x0000
    """GROUP BY clauses are not supported.

    (ODBC 2.0)
    """
    SQL_GB_GROUP_BY_EQUALS_SELECT = 0x0001
    """The GROUP BY clause must contain all nonaggregated columns in the select list.

    It cannot contain any other columns. For example, SELECT DEPT, MAX(SALARY) FROM EMPLOYEE GROUP BY DEPT. (ODBC 2.0)
    """
    SQL_GB_GROUP_BY_CONTAINS_SELECT = 0x0002
    """The GROUP BY clause must contain all nonaggregated columns in the select list.

    It can contain columns that are not in the select list. For example, SELECT DEPT, MAX(SALARY) FROM EMPLOYEE GROUP BY
    DEPT, AGE. (ODBC 2.0)
    """
    SQL_GB_NO_RELATION = 0x0003
    """The columns in the GROUP BY clause and the select list are not related.

    The meaning of nongrouped, nonaggregated columns in the select list is data source-dependent. For example, SELECT
    DEPT, SALARY FROM EMPLOYEE GROUP BY DEPT, AGE. (ODBC 2.0)
    """
    SQL_GB_COLLATE = 0x0004
    """A COLLATE clause can be specified at the end of each grouping column.

    (ODBC 3.0)
    """


class SQLIdentifierCase(IntEnum):
    """The case-sensitivity of identifiers."""

    SQL_IC_UPPER = 1
    """Identifiers are not case-sensitive and are stored in uppercase in system catalog."""

    SQL_IC_LOWER = 2
    """Identifiers are not case-sensitive and are stored in lowercase in system catalog."""

    SQL_IC_SENSITIVE = 3
    """Identifiers are case-sensitive and are stored in mixed case in system catalog."""

    SQL_IC_MIXED = 4
    """Identifiers are not case-sensitive and are stored in mixed case in system catalog."""


class SQLNonNullableColumns(IntEnum):
    """An SQLUSMALLINT value that specifies whether the data source supports NOT NULL in columns.

    A SQL-92 Entry level-conformant driver will return SQL_NNC_NON_NULL.
    """

    SQL_NNC_NULL = 0x0000
    """All columns must be nullable."""

    SQL_NNC_NON_NULL = 0x0001
    """Columns cannot be nullable.

    (The data source supports the NOT NULL column constraint in CREATE TABLE statements.)
    """


class SQLNumericFunctions(IntFlag):
    """An SQLUINTEGER bitmask enumerating the scalar numeric functions supported by the driver and data source."""

    SQL_FN_NUM_ABS = 0x00000001
    SQL_FN_NUM_ACOS = 0x00000002
    SQL_FN_NUM_ASIN = 0x00000004
    SQL_FN_NUM_ATAN = 0x00000008
    SQL_FN_NUM_ATAN2 = 0x00000010
    SQL_FN_NUM_CEILING = 0x00000020
    SQL_FN_NUM_COS = 0x00000040
    SQL_FN_NUM_COT = 0x00000080
    SQL_FN_NUM_EXP = 0x00000100
    SQL_FN_NUM_FLOOR = 0x00000200
    SQL_FN_NUM_LOG = 0x00000400
    SQL_FN_NUM_MOD = 0x00000800
    SQL_FN_NUM_SIGN = 0x00001000
    SQL_FN_NUM_SIN = 0x00002000
    SQL_FN_NUM_SQRT = 0x00004000
    SQL_FN_NUM_TAN = 0x00008000
    SQL_FN_NUM_PI = 0x00010000
    SQL_FN_NUM_RAND = 0x00020000
    SQL_FN_NUM_DEGREES = 0x00040000
    SQL_FN_NUM_LOG10 = 0x00080000
    SQL_FN_NUM_POWER = 0x00100000
    SQL_FN_NUM_RADIANS = 0x00200000
    SQL_FN_NUM_ROUND = 0x00400000
    SQL_FN_NUM_TRUNCATE = 0x00800000


class SQLNullCollation(IntEnum):
    """An SQLUSMALLINT value that specifies where NULLs are sorted in a result set."""

    SQL_NC_HIGH = 0
    """NULLs are sorted at the high end of the result set, depending on the ASC or DESC keywords."""

    SQL_NC_LOW = 1
    """NULLs are sorted at the low end of the result set, depending on the ASC or DESC keywords."""

    SQL_NC_START = 0x0002
    """NULLs are sorted at the start of the result set, regardless of the ASC or DESC keywords."""

    SQL_NC_END = 0x0004
    """NULLs are sorted at the end of the result set, regardless of the ASC or DESC keywords."""


class SQLOdbcSqlConformance(IntEnum):
    """An SQLSMALLINT value indicating SQL grammar supported by the driver."""

    SQL_OSC_MINIMUM = 0
    """Minimum grammar supported."""

    SQL_OSC_CORE = 1
    """Core grammar supported."""

    SQL_OSC_EXTENDED = 2
    """Extended grammar supported."""


class SQLOdbcSagCliConformance(IntEnum):
    """The compliance to the functions of the SQL Access Group (SAG) CLI specification."""

    SQL_OSCC_NOT_COMPLIANT = 0
    """The driver does not conform to the SAG CLI specification."""

    SQL_OSCC_COMPLIANT = 1
    """The driver conforms to the SAG CLI specification."""


class SQLOuterJoinCapabilities(IntFlag):
    """An SQLUINTEGER bitmask enumerating the types of outer joins supported by the driver and data source."""

    SQL_OJ_LEFT = 0x00000001
    """Left outer joins are supported."""
    SQL_OJ_RIGHT = 0x00000002
    """Right outer joins are supported."""
    SQL_OJ_FULL = 0x00000004
    """Full outer joins are supported."""
    SQL_OJ_NESTED = 0x00000008
    """Nested outer joins are supported."""
    SQL_OJ_NOT_ORDERED = 0x00000010
    """The column names in the ON clause of the outer join do not have to be in the same order as their respective table
    names in the OUTER JOIN clause."""
    SQL_OJ_INNER = 0x00000020
    """The inner table (the right table in a left outer join or the left table in a right outer join) can also be used
    in an inner join.

    This does not apply to full outer joins, which do not have an inner table.
    """
    SQL_OJ_ALL_COMPARISON_OPS = 0x00000040
    """The comparison operator in the ON clause can be any of the ODBC comparison operators.

    If this bit is not set, only the equals (=) comparison operator can be used in outer joins.
    """


class SQLOuterJoins(Enum):
    """Indicated the level of support for outer joins."""

    NO = "N"
    """The data source does not support outer joins."""
    YES = "Y"
    """The data source supports two-table outer joins, and the driver supports the ODBC outer join syntax except for
    nested outer joins.

    However, columns on the left side of the comparison operator in the ON clause must come from the left-hand table in
    the outer join, and columns on the right side of the comparison operator must come from the right-hand table.
    """
    PARTIAL = "P"
    """The data source partially supports nested outer joins, and the driver supports the ODBC outer join syntax.

    However, columns on the left side of the comparison operator in the ON clause must come from the left-hand table in
    the outer join and columns on the right side of the comparison operator must come from the right-hand table. Also,
    the right-hand table of an outer join cannot be included in an inner join.
    """
    FULL = "F"
    """The data source fully supports nested outer joins, and the driver supports the ODBC outer join syntax."""


class SQLReturn(IntEnum):
    """ODBC return codes (SQLRETURN).

    These values are returned by ODBC API functions to indicate the outcome
    of an operation. Most functions return one of these codes, and additional
    diagnostic information can be retrieved via `SQLGetDiagRec` when the
    result is not `SQL_SUCCESS`.

    The most common cases are:

        - SQL_SUCCESS: Operation completed successfully.
        - SQL_SUCCESS_WITH_INFO: Operation succeeded but additional
          diagnostic information is available.
        - SQL_NO_DATA: No more data was available (e.g. end of result set).

    Less common return codes relate to error handling and advanced features
    such as asynchronous execution and data-at-execution parameters.

    Callers should treat `SQL_SUCCESS_WITH_INFO` as a successful result and
    consult diagnostics if needed.
    """

    SQL_SUCCESS = 0
    """Operation completed successfully."""
    SQL_SUCCESS_WITH_INFO = 1
    """Success with diagnostics available."""
    SQL_NO_DATA = 100
    """No more data was available (e.g. end of result set)."""
    SQL_ERROR = -1
    """General error (see diagnostics)."""
    SQL_INVALID_HANDLE = -2
    """Invalid ODBC handle."""
    SQL_STILL_EXECUTING = 2
    """Async operation in progress."""
    SQL_NEED_DATA = 99
    """Data-at-execution required."""


class SQLScrollConcurrency(IntFlag):
    """A 32-bit bitmask enumerating the concurrency control options supported for scrollable cursors."""

    SQL_SCCO_READ_ONLY = 1
    """Cursor is read only.

    No updates are allowed.
    """

    SQL_SCCO_LOCK = 2
    """Cursor uses the lowest level of locking sufficient to ensure that the row can be updated."""

    SQL_SCCO_OPT_ROWVER = 4
    """Cursor uses optimistic concurrency control, comparing row versions, such as SQLBases ROWID or Sybase
    TIMESTAMP."""

    SQL_SCCO_OPT_VALUES = 8
    """Cursor uses optimistic concurrency control, comparing values."""


class SQLScrollOptions(IntFlag):
    """An SQLUINTEGER bitmask enumerating the scroll options supported for scrollable cursors."""

    SQL_SO_FORWARD_ONLY = 1
    """The cursor only scrolls forward.

    (ODBC 1.0)
    """

    SQL_SO_KEYSET_DRIVEN = 2
    """The driver saves and uses the keys for every row in the result set.

    (ODBC 1.0)
    """

    SQL_SO_DYNAMIC = 4
    """The driver keeps the keys for every row in the rowset (the keyset size is the same as the rowset size).

    (ODBC 1.0)
    """

    SQL_SO_MIXED = 8
    """The driver keeps the keys for every row in the keyset, and the keyset size is greater than the rowset size.

    The cursor is keyset-driven inside the keyset and dynamic outside the keyset. (ODBC 1.0)
    """

    SQL_SO_STATIC = 10
    """The data in the result set is static.

    (ODBC 2.0)
    """


class SQLSchemaUsage(IntFlag):
    """An SQLUINTEGER bitmask enumerating the statements in which schemas can be used.

    A SQL-92 Entry level-conformant driver will always return the SQL_SU_DML_STATEMENTS, SQL_SU_TABLE_DEFINITION, and
    SQL_SU_PRIVILEGE_DEFINITION options, as supported.

    This InfoType has been renamed for ODBC 3.0 from the ODBC 2.0 InfoType SQL_OWNER_USAGE.
    """

    SQL_SU_DML_STATEMENTS = 0x00000001
    """Schemas are supported in all Data Manipulation Language statements: SELECT, INSERT, UPDATE, DELETE, and if
    supported, SELECT FOR UPDATE and positioned update and delete statements.
    """
    SQL_SU_PROCEDURE_INVOCATION = 0x00000002
    """Schemas are supported in the ODBC procedure invocation statement."""
    SQL_SU_TABLE_DEFINITION = 0x00000004
    """Schemas are supported in all table definition statements: CREATE TABLE, CREATE VIEW, ALTER TABLE, DROP TABLE,
    and DROP VIEW.
    """
    SQL_SU_INDEX_DEFINITION = 0x00000008
    """Schemas are supported in all index definition statements: CREATE INDEX and DROP INDEX."""
    SQL_SU_PRIVILEGE_DEFINITION = 0x00000010
    """Schemas are supported in all privilege definition statements: GRANT and REVOKE."""


class SQLStringFunctions(IntFlag):
    """An SQLUINTEGER bitmask enumerating the scalar string functions supported by the driver and data source.

    Note: The information type was introduced in ODBC 1.0; each bitmask is labeled with the version in which it was
    introduced.

    Arguments denoted as string_exp can be the name of a column,a character-string-literal, or the result of another
    scalar function, where the underlying data type can be represented as SQL_CHAR, SQL_VARCHAR, or SQL_LONGVARCHAR.

    Arguments denoted as character_exp are a variable-length character string.

    Arguments denoted as start, length, or count can be a numeric-literal or the result of another scalar function,
    where the underlying data type can be represented as SQL_TINYINT, SQL_SMALLINT, or SQL_INTEGER.

    The string functions listed here are 1-based; that is, the first character in the string is character 1.

    The BIT_LENGTH, CHAR_LENGTH, CHARACTER_LENGTH, OCTET_LENGTH, and POSITION string scalar functions have been added
    in ODBC 3.0 to align with SQL-92.
    """

    SQL_FN_STR_CONCAT = 0x00000001
    """CONCAT( string_exp1,string_exp2) (ODBC 1.0)

    Returns a character string that is the result of concatenating string_exp2 to string_exp1. The resulting string is
    DBMS-dependent. For example, if the column represented by string_exp1 contained a NULL value, DB2 would return NULL
    but SQL Server would return the non-NULL string.
    """

    SQL_FN_STR_INSERT = 0x00000002
    """INSERT( string_exp1, start, length, string_exp2) (ODBC 1.0)

    Returns a character string where length characters have been deleted from string_exp1, beginning at start, and where
    string_exp2 has been inserted into string_exp, beginning at start.
    """

    SQL_FN_STR_LEFT = 0x00000004
    """LEFT( string_exp, count) (ODBC 1.0)

    Returns the leftmost count characters of string_exp.
    """

    SQL_FN_STR_LTRIM = 0x00000008
    """LTRIM( string_exp ) (ODBC 1.0)

    Returns the characters of string_exp, with leading blanks removed.
    """

    SQL_FN_STR_LENGTH = 0x00000010
    """LENGTH( string_exp ) (ODBC 1.0)

    Returns the number of characters in string_exp, excluding trailing blanks.

    LENGTH only accepts strings. Therefore will implicitly convert string_exp to a string, and return the length of this
    string (not the internal size of the datatype).
    """

    SQL_FN_STR_LOCATE = 0x00000020
    """LOCATE( string_exp1, string_exp2[, start]) (ODBC 1.0)

    Returns the starting position of the first occurrence of string_exp1 within string_exp2. The search for the first
    occurrence of string_exp1 begins with the first character position in string_exp2 unless the optional argument,
    start, is specified. If start is specified, the search begins with the character position indicated by the value of
    start. The first character position in string_exp2 is indicated by the value 1. If string_exp1 is not found within
    string_exp2, the value 0 is returned.

    If an application can call the LOCATE scalar function with the string_exp1, string_exp2, and start arguments, the
    driver returns SQL_FN_STR_LOCATE when SQLGetInfo is called with an Option of SQL_STRING_FUNCTIONS. If the
    application can call the LOCATE scalar function with only the string_exp1 and string_exp2 arguments, the driver
    returns SQL_FN_STR_LOCATE_2 when SQLGetInfo is called with an Option of SQL_STRING_FUNCTIONS. Drivers that support
    calling the LOCATE function with either two or three arguments return both SQL_FN_STR_LOCATE and
    SQL_FN_STR_LOCATE_2.
    """

    SQL_FN_STR_LCASE = 0x00000040
    """LCASE( string_exp ) (ODBC 1.0)

    Returns a string equal to that in string_exp, with all uppercase characters converted to lowercase.
    """

    SQL_FN_STR_REPEAT = 0x00000080
    """REPEAT( string_exp, count) (ODBC 1.0)

    Returns a character string composed of string_exp repeated count times.
    """

    SQL_FN_STR_REPLACE = 0x00000100
    """REPLACE( string_exp1, string_exp2, string_exp3) (ODBC 1.0)

    Search string_exp1 for occurrences of string_exp2, and replace with string_exp3.
    """

    SQL_FN_STR_RIGHT = 0x00000200
    """RIGHT( string_exp, count) (ODBC 1.0)

    Returns the rightmost count characters of string_exp.
    """

    SQL_FN_STR_RTRIM = 0x00000400
    """RTRIM( string_exp ) (ODBC 1.0)

    Returns the characters of string_exp with trailing blanks removed.
    """

    SQL_FN_STR_SUBSTRING = 0x00000800
    """SUBSTRING( string_exp, start, length**)** (ODBC 1.0)

    Returns a character string that is derived from string_exp, beginning at the character position specified by start
    for length characters.
    """
    SQL_FN_STR_UCASE = 0x00001000
    """UCASE( string_exp ) (ODBC 1.0)

    Returns a string equal to that in string_exp, with all lowercase characters converted to uppercase.
    """
    SQL_FN_STR_ASCII = 0x00002000
    """ASCII( string_exp ) (ODBC 1.0)

    Returns the ASCII code value of the leftmost character of string_exp as an integer.
    """

    SQL_FN_STR_CHAR = 0x00004000
    """CHAR( code ) (ODBC 1.0)

    Returns the character that has the ASCII code value specified by code. The value of code should be between 0 and
    255; otherwise, the return value is data source-dependent.
    """

    SQL_FN_STR_DIFFERENCE = 0x00008000
    """DIFFERENCE( string_exp1,string_exp2) (ODBC 2.0)

    Returns an integer value that indicates the difference between the values returned by the SOUNDEX function for
    string_exp1 and string_exp2.
    """

    SQL_FN_STR_LOCATE_2 = 0x00010000
    """LOCATE( string_exp1, string_exp2[, start]) (ODBC 1.0)

    Returns the starting position of the first occurrence of string_exp1 within string_exp2. The search for the first
    occurrence of string_exp1 begins with the first character position in string_exp2 unless the optional argument,
    start, is specified. If start is specified, the search begins with the character position indicated by the value of
    start. The first character position in string_exp2 is indicated by the value 1. If string_exp1 is not found within
    string_exp2, the value 0 is returned.

    If an application can call the LOCATE scalar function with the string_exp1, string_exp2, and start arguments, the
    driver returns SQL_FN_STR_LOCATE when SQLGetInfo is called with an Option of SQL_STRING_FUNCTIONS. If the
    application can call the LOCATE scalar function with only the string_exp1 and string_exp2 arguments, the driver
    returns SQL_FN_STR_LOCATE_2 when SQLGetInfo is called with an Option of SQL_STRING_FUNCTIONS. Drivers that support
    calling the LOCATE function with either two or three arguments return both SQL_FN_STR_LOCATE and
    SQL_FN_STR_LOCATE_2.
    """

    SQL_FN_STR_SOUNDEX = 0x00020000
    """SOUNDEX( string_exp ) (ODBC 2.0)

    Returns a data source-dependent character string representing the sound of the words in string_exp. For example, SQL
    Server returns a 4-digit SOUNDEX code; Oracle returns a phonetic representation of each word.
    """
    SQL_FN_STR_SPACE = 0x00040000
    """SPACE( count ) (ODBC 2.0)

    Returns a character string consisting of count spaces.
    """
    SQL_FN_STR_BIT_LENGTH = 0x00080000
    """BIT_LENGTH( string_exp ) (ODBC 3.0)

    Returns the length in bits of the string expression.

    Does not work only for string data types, therefore will not implicitly convert string_exp to string but instead
    will return the (internal) size of whatever datatype it is given.
    """

    SQL_FN_STR_CHAR_LENGTH = 0x00100000
    """CHAR_LENGTH( string_exp ) (ODBC 3.0)

    Returns the length in characters of the string expression, if the string expression is of a character data type;
    otherwise, returns the length in bytes of the string expression (the smallest integer not less than the number of
    bits divided by 8). (This function is the same as the CHARACTER_LENGTH function.)
    """

    SQL_FN_STR_CHARACTER_LENGTH = 0x00200000
    """CHARACTER_LENGTH( string_exp ) (ODBC 3.0)

    Returns the length in characters of the string expression, if the string expression is of a character data type;
    otherwise, returns the length in bytes of the string expression (the smallest integer not less than the number of
    bits divided by 8). (This function is the same as the CHAR_LENGTH function.)
    """

    SQL_FN_STR_OCTET_LENGTH = 0x00400000
    """OCTET_LENGTH( string_exp ) (ODBC 3.0)

    Returns the length in bytes of the string expression. The result is the smallest integer not less than the number of
    bits divided by 8.

    Does not work only for string data types, therefore will not implicitly convert string_exp to string but instead
    will return the (internal) size of whatever datatype it is given.
    """

    SQL_FN_STR_POSITION = 0x00800000
    """POSITION( character_exp IN character_exp) (ODBC 3.0)

    Returns the position of the first character expression in the second character expression. The result is an exact
    numeric with an implementation-defined precision and a scale of 0.
    """


class SQLSubqueries(IntFlag):
    """An SQLUINTEGER bitmask enumerating the predicates that support subqueries.

    A SQL-92 Entry level-conformant driver will always return a bitmask in which all of these bits are set.
    """

    SQL_SQ_COMPARISON = 0x00000001
    """The comparison predicate."""
    SQL_SQ_EXISTS = 0x00000002
    """The *exists* predicate."""
    SQL_SQ_IN = 0x00000004
    """The *in* predicate."""
    SQL_SQ_QUANTIFIED = 0x00000008
    """The predicates containing a quantification scalar function."""
    SQL_SQ_CORRELATED_SUBQUERIES = 0x00000010
    """All predicates that support subqueries support correlated subqueries."""


class SQLSystemFunctions(IntFlag):
    """An SQLUINTEGER bitmask enumerating the scalar system functions supported by the driver and data source.

    Arguments denoted as exp can be the name of a column, the result of another scalar function, or a literal, where the
    underlying data type could be represented as SQL_NUMERIC, SQL_DECIMAL, SQL_TINYINT, SQL_SMALLINT, SQL_INTEGER,
    SQL_BIGINT, SQL_FLOAT, SQL_REAL, SQL_DOUBLE, SQL_TYPE_DATE, SQL_TYPE_TIME, or SQL_TYPE_TIMESTAMP.

    Arguments denoted as value can be a literal constant, where the underlying data type can be represented as
    SQL_NUMERIC, SQL_DECIMAL, SQL_TINYINT, SQL_SMALLINT, SQL_INTEGER, SQL_BIGINT, SQL_FLOAT, SQL_REAL, SQL_DOUBLE,
    SQL_TYPE_DATE, SQL_TYPE_TIME, or SQL_TYPE_TIMESTAMP.

    Values returned are represented as ODBC data types.
    """

    SQL_FN_SYS_DBNAME = 0x00000001
    """DATABASE( ) (ODBC 1.0)

    Returns the name of the database corresponding to the connection handle. (The name of the database is also available
    by calling SQLGetConnectOption with the SQL_CURRENT_QUALIFIER connection option.)
    """

    SQL_FN_SYS_IFNULL = 0x00000002
    """IFNULL( exp,value) (ODBC 1.0)

    If exp is null, value is returned. If exp is not null, exp is returned. The possible data type or types of value
    must be compatible with the data type of exp.
    """

    SQL_FN_SYS_USERNAME = 0x00000004
    """USER( ) (ODBC 1.0)

    Returns the user name in the DBMS. (The user name is also available by way of SQLGetInfo by specifying the
    information type: SQL_USER_NAME.) This can be different than the login name.
    """


class SQLTimeDateFunctions(IntFlag):
    """An SQLUINTEGER bitmask enumerating the scalar date and time functions supported by the driver and data source.

    Note: The information type was introduced in ODBC 1.0; each bitmask is labeled with the version in which it was
    introduced.

    Arguments denoted as timestamp_exp can be the name of a column, the result of another scalar function, or an
    ODBC-time-escape, ODBC-date- escape, or ODBC-timestamp-escape, where the underlying data type could be represented
    as SQL_CHAR, SQL_VARCHAR, SQL_TYPE_TIME, SQL_TYPE_DATE, or SQL_TYPE_TIMESTAMP.

    Arguments denoted as date_exp can be the name of a column, the result of another scalar function, or an
    ODBC-date-escape or ODBC-timestamp-escape, where the underlying data type could be represented as SQL_CHAR,
    SQL_VARCHAR, SQL_TYPE_DATE, or SQL_TYPE_TIMESTAMP.

    Arguments denoted as time_exp can be the name of a column, the result of another scalar function, or an
    ODBC-time-escape or ODBC-timestamp-escape, where the underlying data type could be represented as SQL_CHAR,
    SQL_VARCHAR, SQL_TYPE_TIME, or SQL_TYPE_TIMESTAMP.

    The CURRENT_DATE, CURRENT_TIME, and CURRENT_TIMESTAMP timedate scalar functions have been added in ODBC 3.0 to
    align with SQL-92.
    """

    SQL_FN_TD_NOW = 0x00000001
    """NOW( ) (ODBC 1.0)

    Returns current date and time as a timestamp value.
    """

    SQL_FN_TD_CURDATE = 0x00000002
    """CURDATE( ) (ODBC 1.0)

    Returns the current date.
    """

    SQL_FN_TD_DAYOFMONTH = 0x00000004
    """DAYOFMONTH( date_exp ) (ODBC 1.0)

    Returns the day of the month based on the month field in date_exp as an integer value in the range of 1-31.
    """

    SQL_FN_TD_DAYOFWEEK = 0x00000008
    """DAYOFWEEK( date_exp ) (ODBC 1.0)

    Returns the day of the week based on the week field in date_exp as an integer value in the range of 1-7, where 1
    represents Sunday.
    """

    SQL_FN_TD_DAYOFYEAR = 0x00000010
    """DAYOFYEAR( date_exp ) (ODBC 1.0)

    Returns the day of the year based on the year field in date_exp as an integer value in the range of 1-366.
    """

    SQL_FN_TD_MONTH = 0x00000020
    """MONTH( date_exp ) (ODBC 1.0)

    Returns the month based on the month field in date_exp as an integer value in the range of 1-12.
    """

    SQL_FN_TD_QUARTER = 0x00000040
    """QUARTER( date_exp ) (ODBC 1.0)

    Returns the quarter in date_exp as an integer value in the range of 1-4, where 1 represents January 1 through March
    31.
    """

    SQL_FN_TD_WEEK = 0x00000080
    """WEEK( date_exp ) (ODBC 1.0)

    Returns the week of the year based on the week field in date_exp as an integer value in the range of 1-53.
    """

    SQL_FN_TD_YEAR = 0x00000100
    """YEAR( date_exp ) (ODBC 1.0)

    Returns the year based on the year field in date_exp as an integer value. The range is data source-dependent.
    """

    SQL_FN_TD_CURTIME = 0x00000200
    """CURTIME( ) (ODBC 1.0)

    Returns the current local time.
    """

    SQL_FN_TD_HOUR = 0x00000400
    """HOUR( time_exp ) (ODBC 1.0)

    Returns the hour based on the hour field in time_exp as an integer value in the range of 0-23.
    """

    SQL_FN_TD_MINUTE = 0x00000800
    """MINUTE( time_exp ) (ODBC 1.0)

    Returns the minute based on the minute field in time_exp as an integer value in the range of 0-59.
    """

    SQL_FN_TD_SECOND = 0x00001000
    """SECOND( time_exp ) (ODBC 1.0)

    Returns the second based on the second field in time_exp as an integer value in the range of 0-59.
    """

    SQL_FN_TD_TIMESTAMPADD = 0x00002000
    """TIMESTAMPADD( interval, integer_exp, timestamp_exp ) (ODBC 2.0)

    Returns the timestamp calculated by adding integer_exp intervals of type interval to timestamp_exp. Valid values of
    interval are the following keywords:

    SQL_TSI_FRAC_SECOND
    SQL_TSI_SECOND
    SQL_TSI_MINUTE
    SQL_TSI_HOUR
    SQL_TSI_DAY
    SQL_TSI_WEEK
    SQL_TSI_MONTH
    SQL_TSI_QUARTER
    SQL_TSI_YEAR

    where fractional seconds are expressed in billionths of a second. For example, the following SQL statement returns
    the name of each employee and their one-year anniversary date:

    SELECT NAME, {fn TIMESTAMPADD(SQL_TSI_YEAR, 1, HIRE_DATE)} FROM EMPLOYEES

    If timestamp_exp is a time value and interval specifies days, weeks, months, quarters, or years, the date portion
    of timestamp_exp is set to the current date before calculating the resulting timestamp.

    If timestamp_exp is a date value and interval specifies fractional seconds, seconds, minutes, or hours, the time
    portion of timestamp_exp is set to 0 before calculating the resulting timestamp.

    An application determines which intervals a data source supports by calling SQLGetInfo with the
    SQL_TIMEDATE_ADD_INTERVALS option.
    """

    SQL_FN_TD_TIMESTAMPDIFF = 0x00004000
    """TIMESTAMPDIFF( interval, timestamp_exp1, timestamp_exp2 ) (ODBC 2.0)

    Returns the integer number of intervals of type interval by which timestamp_exp2 is greater than timestamp_exp1.
    Valid values of interval are the following keywords:

    SQL_TSI_FRAC_SECOND
    SQL_TSI_SECOND
    SQL_TSI_MINUTE
    SQL_TSI_HOUR
    SQL_TSI_DAY
    SQL_TSI_WEEK
    SQL_TSI_MONTH
    SQL_TSI_QUARTER
    SQL_TSI_YEAR

    where fractional seconds are expressed in billionths of a second. For example, the following SQL statement returns
    the name of each employee and the number of years they have been employed:

    SELECT NAME, {fn TIMESTAMPDIFF(SQL_TSI_YEAR, {fn CURDATE()}, HIRE_DATE)} FROM EMPLOYEES

    If either timestamp expression is a time value and interval specifies days, weeks, months, quarters, or years, the
    date portion of that timestamp is set to the current date before calculating the difference between the timestamps.

    If either timestamp expression is a date value and interval specifies fractional seconds, seconds, minutes, or
    hours, the time portion of that timestamp is set to 0 before calculating the difference between the timestamps.

    An application determines which intervals a data source supports by calling SQLGetInfo with the
    SQL_TIMEDATE_DIFF_INTERVALS option.
    """

    SQL_FN_TD_DAYNAME = 0x00008000
    """DAYNAME( date_exp ) (ODBC 2.0)

    Returns a character string containing the data source-specific name of the day (for example, Sunday through Saturday
    or Sun. through Sat. for a data source that uses English, or Sonntag through Samstag for a data source that uses
    German) for the day portion of date_exp.
    """
    SQL_FN_TD_MONTHNAME = 0x00010000
    """MONTHNAME( date_exp ) (ODBC 2.0)

    Returns a character string containing the data source-specific name of the month (for example, January through
    December or Jan. through Dec. for a data source that uses English, or Januar through Dezember for a data source that
    uses German) for the month portion of date_exp.
    """
    SQL_FN_TD_CURRENT_DATE = 0x00020000
    """CURRENT_DATE( ) (ODBC 3.0)

    Returns the current date.
    """
    SQL_FN_TD_CURRENT_TIME = 0x00040000
    """CURRENT_TIME[( time-precision )] (ODBC 3.0)

    Returns the current local time. The time-precision argument determines the seconds precision of the returned value.
    """

    SQL_FN_TD_CURRENT_TIMESTAMP = 0x00080000
    """CURRENT_TIMESTAMP[( timestamp-precision )] (ODBC 3.0)

    Returns the current local date and local time as a timestamp value. The timestamp-precision argument determines the
    seconds precision of the returned timestamp.
    """

    SQL_FN_TD_EXTRACT = 0x00100000
    """EXTRACT( extract-field FROM extract-source ) (ODBC 3.0)

    Returns the extract-field portion of the extract-source. The extract-source argument is a datetime or interval
    expression. The extract-field argument can be one of the following keywords:

    YEAR MONTH DAY HOUR MINUTE SECOND

    The precision of the returned value is implementation-defined. The scale is 0 unless SECOND is specified, in which
    case the scale is not less than the fractional seconds precision of the extract-source field.
    """


class SQLTimestampIntervals(IntFlag):
    """The timestamp intervals which the driver and data source support for TIMESTAMPADD/TIMESTAMPDIFF scalar functions.

    An FIPS Transitional level-conformant driver will always return a bitmask in which all of these bits are set.
    """

    SQL_FN_TSI_FRAC_SECOND = 0x00000001
    SQL_FN_TSI_SECOND = 0x00000002
    SQL_FN_TSI_MINUTE = 0x00000004
    SQL_FN_TSI_HOUR = 0x00000008
    SQL_FN_TSI_DAY = 0x00000010
    SQL_FN_TSI_WEEK = 0x00000020
    SQL_FN_TSI_MONTH = 0x00000040
    SQL_FN_TSI_QUARTER = 0x00000080
    SQL_FN_TSI_YEAR = 0x00000100


class SQLTxnCapable(IntEnum):
    """An SQLUSMALLINT value describing the transaction support in the driver or data source."""

    SQL_TC_NONE = 0
    """Transactions not supported.

    (ODBC 1.0)
    """
    SQL_TC_DML = 1
    """Transactions can contain only Data Manipulation Language (DML) statements (SELECT, INSERT, UPDATE, DELETE).

    Data Definition Language (DDL) statements encountered in a transaction cause an error. (ODBC 1.0)
    """

    SQL_TC_ALL = 2
    """Transactions can contain DDL statements and DML statements in any order.

    (ODBC 1.0)
    """

    SQL_TC_COMMIT = 3
    """Transactions can contain only DML statements.

    DDL statements (CREATE TABLE, DROP INDEX, and so on) encountered in a transaction cause the transaction to be
    committed. (ODBC 2.0)
    """

    SQL_TC_IGNORE = 4
    """Transactions can contain only DML statements.

    DDL statements encountered in a transaction are ignored. (ODBC 2.0)
    """


class SQLTxnIsolationOption(IntFlag):
    """Bitmask for transaction isolation levels."""

    SQL_TXN_READ_UNCOMMITTED = 0x00000001
    """Dirty reads, non-repeatable reads, and phantoms are possible."""

    SQL_TXN_READ_COMMITTED = 0x00000002
    """Dirty reads are not possible.

    Non-repeatable reads and phantoms are possible.
    """

    SQL_TXN_REPEATABLE_READ = 0x00000004
    """Dirty reads and non-repeatable reads are not possible.

    Phantoms are possible.
    """

    SQL_TXN_SERIALIZABLE = 0x00000008
    """Transactions are serializable.

    Serializable transactions do not allow dirty reads, non-repeatable reads, or phantoms.
    """


class SQLUnion(IntFlag):
    """An SQLUINTEGER bitmask enumerating the support for the UNION clause.

    A SQL-92 Entry level-conformant driver will always return both of the options as supported.
    """

    SQL_U_UNION = 0x00000001
    """The data source supports the UNION clause."""
    SQL_U_UNION_ALL = 0x00000002
    """The data source supports the ALL keyword in the UNION clause.

    (SQLGetInfo returns both SQL_U_UNION and SQL_U_UNION_ALL in this case.)
    """
