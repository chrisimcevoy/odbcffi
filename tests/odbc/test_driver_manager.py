from contextlib import nullcontext
from typing import Literal

import pytest

from odbcffi.odbc.connection_handle import ConnectionHandle
from odbcffi.odbc.driver_manager import DriverManager
from odbcffi.odbc.enums import *
from odbcffi.odbc.environment_handle import EnvironmentHandle
from odbcffi.odbc.errors import ODBCError
from tests.conftest import ConnectionInfo


class TestSQLGetInfoW:
    def test_sql_accessible_procedures(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ACCESSIBLE_PROCEDURES,
        )

        assert actual in {"Y", "N"}

    def test_sql_accessible_tables(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ACCESSIBLE_TABLES,
        )

        assert actual in {"Y", "N"}

    def test_sql_active_environments(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ACTIVE_ENVIRONMENTS,
        )

        assert isinstance(actual, int)
        assert actual >= 0

    def test_sql_alter_domain(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLAlterDomain = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ALTER_DOMAIN,
        )

        assert isinstance(actual, SQLAlterDomain)

    def test_sql_alter_table(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLAlterTable = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ALTER_TABLE,
        )

        assert isinstance(actual, SQLAlterTable)

    def test_sql_batch_row_count(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLBatchRowCount = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_BATCH_ROW_COUNT,
        )

        assert isinstance(actual, SQLBatchRowCount)

    def test_sql_batch_support(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLBatchSupport = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_BATCH_SUPPORT,
        )

        assert isinstance(actual, SQLBatchSupport)

    def test_sql_bookmark_persistence(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLBookmarkPersistence = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_BOOKMARK_PERSISTENCE,
        )

        assert isinstance(actual, SQLBookmarkPersistence)

    def test_sql_catalog_location(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCatalogLocation = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CATALOG_LOCATION,
        )

        assert isinstance(actual, SQLCatalogLocation)

    def test_sql_catalog_name_separator(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CATALOG_NAME_SEPARATOR,
        )

        assert isinstance(actual, str)
        assert actual

    def test_sql_catalog_term(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CATALOG_TERM,
        )

        assert isinstance(actual, str)
        assert actual

    def test_sql_catalog_usage(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLCatalogUsage = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CATALOG_USAGE,
        )

        assert isinstance(actual, SQLCatalogUsage)

    def test_sql_column_alias(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_COLUMN_ALIAS,
        )

        assert actual in ("Y", "N")

    def test_sql_concat_null_behavior(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLConcatNullBehavior = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CONCAT_NULL_BEHAVIOR,
        )

        assert actual in list(SQLConcatNullBehavior)

    def test_sql_convert_bigint(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle, connection_info: ConnectionInfo
    ) -> None:

        # At time of writing, this is not supported in FreeTDS.
        # https://github.com/FreeTDS/freetds/blob/217ffa7674ae3462c5d663ae2df579a98f44c348/src/odbc/odbc.c#L5564
        ctx = pytest.raises(ODBCError) if connection_info.driver == "FreeTDS" else nullcontext()

        with ctx:
            actual: SQLConvert = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_BIGINT
            )

            assert isinstance(actual, SQLConvert)

    def test_sql_convert_binary(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_BINARY
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_bit(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_BIT
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_char(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_CHAR
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_date(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle, connection_info: ConnectionInfo
    ) -> None:

        # At time of writing, this is not supported in FreeTDS.
        # https://github.com/FreeTDS/freetds/blob/217ffa7674ae3462c5d663ae2df579a98f44c348/src/odbc/odbc.c#L5564
        ctx = pytest.raises(ODBCError) if connection_info.driver == "FreeTDS" else nullcontext()

        with ctx:
            actual: SQLConvert = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_DATE
            )

            assert isinstance(actual, SQLConvert)

    def test_sql_convert_decimal(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_DECIMAL
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_double(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle, connection_info: ConnectionInfo
    ) -> None:

        # At time of writing, FreeTDS does not implement SQL_CONVERT_DOUBLE
        ctx = pytest.raises(ODBCError) if connection_info.driver == "FreeTDS" else nullcontext()

        with ctx:
            actual: SQLConvert = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_DOUBLE
            )

            assert isinstance(actual, SQLConvert)

    def test_sql_convert_float(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_FLOAT
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_functions(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLConvertFunctions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CONVERT_FUNCTIONS,
        )

        assert isinstance(actual, SQLConvertFunctions)

    def test_sql_convert_guid(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle, connection_info: ConnectionInfo
    ) -> None:

        # At time of writing, this is not supported in FreeTDS.
        # https://github.com/FreeTDS/freetds/blob/217ffa7674ae3462c5d663ae2df579a98f44c348/src/odbc/odbc.c#L5564
        #
        # psqlodbc and mysqlodbc do not implement it either.
        #
        # Microsoft's ODBC driver and MDAC are the only ones that support it.
        ctx = nullcontext() if "SQL Server" in connection_info.driver else pytest.raises(ODBCError)

        with ctx:
            actual: SQLConvert = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_GUID
            )

            assert isinstance(actual, SQLConvert)

    def test_sql_convert_integer(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_INTEGER
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_interval_day_time(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle, connection_info: ConnectionInfo
    ) -> None:

        ctx = (
            pytest.raises(ODBCError)
            if connection_info.driver
            in (
                "FreeTDS",
                "PostgreSQL Unicode",
                "PostgreSQL ANSI",
            )
            else nullcontext()
        )

        with ctx:
            actual: SQLConvert = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_INTERVAL_DAY_TIME
            )

            assert isinstance(actual, SQLConvert)

    def test_sql_convert_interval_year_month(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        ctx = (
            pytest.raises(ODBCError)
            if connection_info.driver
            in (
                "FreeTDS",
                "PostgreSQL Unicode",
                "PostgreSQL ANSI",
            )
            else nullcontext()
        )

        with ctx:
            actual: SQLConvert = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_INTERVAL_YEAR_MONTH
            )

            assert isinstance(actual, SQLConvert)

    def test_sql_convert_longvarbinary(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_LONGVARBINARY
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_longvarchar(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_LONGVARCHAR
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_numeric(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_NUMERIC
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_real(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_REAL
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_smallint(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_SMALLINT
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_time(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle, connection_info: ConnectionInfo
    ) -> None:

        ctx = pytest.raises(ODBCError) if connection_info.driver == "FreeTDS" else nullcontext()

        with ctx:
            actual: SQLConvert = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_TIME
            )

            assert isinstance(actual, SQLConvert)

    def test_sql_convert_timestamp(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_TIMESTAMP
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_tinyint(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_TINYINT
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_varbinary(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_VARBINARY
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_varchar(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLConvert = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_VARCHAR
        )

        assert isinstance(actual, SQLConvert)

    def test_sql_convert_wchar(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle, connection_info: ConnectionInfo
    ) -> None:

        ctx = pytest.raises(ODBCError) if connection_info.driver == "PostgreSQL ANSI" else nullcontext()

        with ctx:
            actual: SQLConvert = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_WCHAR
            )

            assert isinstance(actual, SQLConvert)

    def test_sql_convert_wlongvarchar(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle, connection_info: ConnectionInfo
    ) -> None:

        ctx = pytest.raises(ODBCError) if connection_info.driver == "PostgreSQL ANSI" else nullcontext()

        with ctx:
            actual: SQLConvert = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_WLONGVARCHAR
            )

            assert isinstance(actual, SQLConvert)

    def test_sql_convert_wvarchar(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle, connection_info: ConnectionInfo
    ) -> None:

        ctx = pytest.raises(ODBCError) if connection_info.driver == "PostgreSQL ANSI" else nullcontext()

        with ctx:
            actual: SQLConvert = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle, info_type=InfoType.SQL_CONVERT_WVARCHAR
            )

            assert isinstance(actual, SQLConvert)

    def test_sql_cursor_commit_behavior(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLCursorCommitBehavior = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CURSOR_COMMIT_BEHAVIOR,
        )

        assert actual in list(SQLCursorCommitBehavior)

    def test_sql_correlation_name(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLCorrelationName = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CORRELATION_NAME,
        )

        assert isinstance(actual, SQLCorrelationName)
        assert actual in list(SQLCorrelationName)

    def test_sql_create_assertion(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCreateAssertion = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CREATE_ASSERTION,
        )

        assert isinstance(actual, SQLCreateAssertion)

    def test_sql_create_character_set(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCreateCharacterSet = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CREATE_CHARACTER_SET,
        )

        assert isinstance(actual, SQLCreateCharacterSet)

    def test_sql_create_collation(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCreateCollation = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CREATE_COLLATION,
        )

        assert isinstance(actual, SQLCreateCollation)

    def test_sql_create_domain(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLCreateDomain = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CREATE_DOMAIN,
        )

        assert isinstance(actual, SQLCreateDomain)

    def test_sql_cursor_rollback_behavior(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLCursorRollbackBehavior = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CURSOR_ROLLBACK_BEHAVIOR,
        )

        assert actual in list(SQLCursorRollbackBehavior)

    def test_sql_data_source_name(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DATA_SOURCE_NAME,
        )

        assert actual == ""

    def test_sql_data_source_read_only(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DATA_SOURCE_READ_ONLY,
        )

        assert actual in ("Y", "N")

    def test_sql_database_name(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        expected: str = {
            "Microsoft SQL Server": "master",
            "MySQL": "null",
            "PostgreSQL": "",
        }[connection_info.dbms_name]

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DATABASE_NAME,
        )

        assert actual == expected

    def test_sql_datetime_literals(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        # Not implemented in psqlodbc
        # https://github.com/postgresql-interfaces/psqlodbc/blob/863a0e938dd50c7b68208484bdc3ef8b00735a92/info.c#L1057
        ctx = pytest.raises(ODBCError) if connection_info.driver.startswith("PostgreSQL") else nullcontext()

        with ctx:
            actual: SQLDatetimeLiterals = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle,
                info_type=InfoType.SQL_DATETIME_LITERALS,
            )

            assert isinstance(actual, SQLDatetimeLiterals)

    def test_sql_dbms_name(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DBMS_NAME,
        )

        assert actual == connection_info.dbms_name

    def test_sql_dbms_ver(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DBMS_VER,
        )

        assert isinstance(actual, str)
        assert actual

    def test_sql_default_txn_isolation(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        expected = (
            SQLTxnIsolationOption.SQL_TXN_READ_COMMITTED
            if connection_info.dbms_name != "MySQL"
            # Per ODBC spec: 0 means transaction isolation is unsupported
            else SQLTxnIsolationOption(0)
        )

        actual: SQLTxnIsolationOption = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DEFAULT_TXN_ISOLATION,
        )

        assert actual == expected

    def test_sql_driver_name(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DRIVER_NAME,
        )

        assert isinstance(actual, str)
        assert actual

    def test_sql_driver_odbc_ver(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle, info_type=InfoType.SQL_DRIVER_ODBC_VER
        )

        assert isinstance(actual, str)
        assert actual

    def test_sql_driver_ver(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DRIVER_VER,
        )

        assert isinstance(actual, str)
        assert actual

    def test_sql_expressions_in_order_by(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_EXPRESSIONS_IN_ORDERBY,
        )

        assert actual in ("Y", "N")

    def test_sql_file_usage(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLFileUsage = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_FILE_USAGE,
        )

        assert isinstance(actual, SQLFileUsage)
        assert actual in list(SQLFileUsage)

    def test_sql_getdata_extensions(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLGetDataExtensions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_GETDATA_EXTENSIONS,
        )

        assert isinstance(actual, SQLGetDataExtensions)

    def test_sql_group_by(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLGroupBy = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_GROUP_BY,
        )

        assert isinstance(actual, SQLGroupBy)

    def test_sql_identifier_case(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLIdentifierCase = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_IDENTIFIER_CASE,
        )

        assert actual in list(SQLIdentifierCase)

    def test_sql_identifier_quote_char(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        expected = "`" if connection_info.dbms_name == "MySQL" else '"'

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_IDENTIFIER_QUOTE_CHAR,
        )

        assert actual == expected

    def test_sql_integrity(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_INTEGRITY,
        )

        assert actual in ("Y", "N")

    def test_sql_keywords(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_KEYWORDS,
        )

        assert isinstance(actual, str)
        # no `assert actual` here because postgres returns an empty string.

    def test_sql_like_escape_clause(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_LIKE_ESCAPE_CLAUSE,
        )

        assert actual in ("Y", "N")

    def test_sql_max_binary_literal_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_BINARY_LITERAL_LEN,
        )

        assert actual >= 0

    def test_sql_max_catalog_name_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_CATALOG_NAME_LEN,
        )

        assert actual >= 0

    def test_sql_max_char_literal_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_CHAR_LITERAL_LEN,
        )

        assert actual >= 0

    def test_sql_max_column_name_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_COLUMN_NAME_LEN,
        )

        assert actual >= 0

    def test_sql_max_columns_in_group_by(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_COLUMNS_IN_GROUP_BY,
        )

        assert actual >= 0

    def test_sql_max_columns_in_index(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_COLUMNS_IN_INDEX,
        )

        assert actual >= 0

    def test_sql_max_columns_in_order_by(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_COLUMNS_IN_ORDER_BY,
        )

        assert actual >= 0

    def test_sql_max_columns_in_select(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_COLUMNS_IN_SELECT,
        )

        assert actual >= 0

    def test_sql_max_columns_in_table(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_COLUMNS_IN_TABLE,
        )

        assert actual >= 0

    def test_sql_max_concurrent_activities(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_CONCURRENT_ACTIVITIES,
        )

        assert actual in (0, 1)

    def test_sql_max_cursor_name_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_CURSOR_NAME_LEN,
        )

        assert actual >= 0

    def test_sql_max_driver_connections(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_DRIVER_CONNECTIONS,
        )

        assert actual == 0

    def test_sql_max_index_size(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_INDEX_SIZE,
        )

        assert actual >= 0

    def test_sql_max_procedure_name_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_PROCEDURE_NAME_LEN,
        )

        assert actual >= 0

    def test_sql_max_row_size(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_ROW_SIZE,
        )

        assert actual >= 0

    def test_sql_max_row_size_includes_long(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_ROW_SIZE_INCLUDES_LONG,
        )

        assert actual in ("Y", "N")

    def test_sql_max_schema_name_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_SCHEMA_NAME_LEN,
        )

        assert actual >= 0

    def test_sql_max_statement_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_STATEMENT_LEN,
        )

        assert actual >= 0

    def test_sql_max_table_name_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_TABLE_NAME_LEN,
        )

        assert actual >= 0

    def test_sql_max_tables_in_select(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_TABLES_IN_SELECT,
        )

        assert actual >= 0

    def test_sql_max_user_name_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_USER_NAME_LEN,
        )

        assert actual >= 0

    def test_sql_mult_result_sets(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MULT_RESULT_SETS,
        )

        assert actual in ("Y", "N")

    def test_sql_multiple_active_txn(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MULTIPLE_ACTIVE_TXN,
        )

        assert actual in ("Y", "N")

    def test_sql_need_long_data_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_NEED_LONG_DATA_LEN,
        )

        assert actual in ("Y", "N")

    def test_sql_non_nullable_columns(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLNonNullableColumns = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_NON_NULLABLE_COLUMNS,
        )

        assert isinstance(actual, SQLNonNullableColumns)
        assert actual in list(SQLNonNullableColumns)

    def test_sql_null_collation(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLNullCollation = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_NULL_COLLATION,
        )

        assert isinstance(actual, SQLNullCollation)
        assert actual in list(SQLNullCollation)

    def test_sql_numeric_functions(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLNumericFunctions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_NUMERIC_FUNCTIONS,
        )

        assert isinstance(actual, SQLNumericFunctions)

    def test_sql_odbc_sag_cli_conformance(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        expected = (
            SQLOdbcSagCliConformance.SQL_OSCC_COMPLIANT
            if connection_info.dbms_name == "MySQL"
            else SQLOdbcSagCliConformance.SQL_OSCC_NOT_COMPLIANT
        )

        actual: SQLOdbcSagCliConformance = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ODBC_SAG_CLI_CONFORMANCE,
        )

        assert actual == expected

    def test_sql_odbc_sql_conformance(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLOdbcSqlConformance = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ODBC_SQL_CONFORMANCE,
        )

        assert actual == SQLOdbcSqlConformance.SQL_OSC_CORE

    def test_sql_odbc_ver(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ODBC_VER,
        )

        assert isinstance(actual, str)
        assert actual

    def test_sql_oj_capabilities(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLOuterJoinCapabilities = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_OJ_CAPABILITIES,
        )

        assert isinstance(actual, SQLOuterJoinCapabilities)

    def test_sql_order_by_columns_in_select(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ORDER_BY_COLUMNS_IN_SELECT,
        )

        assert actual in ("Y", "N")

    def test_sql_outer_joins(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLOuterJoins = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_OUTER_JOINS,
        )

        assert isinstance(actual, SQLOuterJoins)

    def test_sql_procedure_term(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:
        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_PROCEDURE_TERM,
        )

        assert isinstance(actual, str)
        assert actual

    def test_sql_procedures(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_PROCEDURES,
        )

        assert actual in ("Y", "N")

    def test_sql_quoted_identifier_case(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLIdentifierCase = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_QUOTED_IDENTIFIER_CASE,
        )

        assert isinstance(actual, SQLIdentifierCase)

    def test_sql_row_updates(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ROW_UPDATES,
        )

        assert actual in ("Y", "N")

    def test_sql_schema_term(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        expected = {
            "Microsoft SQL Server": "owner",
            "MySQL": "",
            "PostgreSQL": "schema",
        }[connection_info.dbms_name]

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SCHEMA_TERM,
        )

        assert actual == expected

    def test_sql_schema_usage(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLSchemaUsage = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SCHEMA_USAGE,
        )

        assert isinstance(actual, SQLSchemaUsage)

    def test_sql_scroll_concurrency(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLScrollConcurrency = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SCROLL_CONCURRENCY,
        )

        assert isinstance(actual, SQLScrollConcurrency)

    def test_sql_scroll_options(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLScrollOptions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SCROLL_OPTIONS,
        )

        assert isinstance(actual, SQLScrollOptions)

    def test_sql_search_pattern_escape(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SEARCH_PATTERN_ESCAPE,
        )

        assert actual == "\\"

    def test_sql_server_name(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SERVER_NAME,
        )

        assert isinstance(actual, str)
        assert actual

    def test_sql_special_characters(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SPECIAL_CHARACTERS,
        )

        assert isinstance(actual, str)
        assert actual

    def test_sql_sql_conformance(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSqlConformance = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL_CONFORMANCE,
        )

        assert isinstance(actual, SQLSqlConformance)

    def test_sql_string_functions(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLStringFunctions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_STRING_FUNCTIONS,
        )

        assert isinstance(actual, SQLStringFunctions)

    def test_sql_subqueries(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSubqueries = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SUBQUERIES,
        )

        assert isinstance(actual, SQLSubqueries)

    def test_sql_system_functions(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSystemFunctions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SYSTEM_FUNCTIONS,
        )

        assert isinstance(actual, SQLSystemFunctions)

    def test_sql_table_term(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_TABLE_TERM,
        )

        assert isinstance(actual, str)
        assert actual

    def test_sql_timedate_add_intervals(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLTimestampIntervals = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_TIMEDATE_ADD_INTERVALS,
        )

        assert isinstance(actual, SQLTimestampIntervals)

    def test_sql_timedate_diff_intervals(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLTimestampIntervals = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_TIMEDATE_DIFF_INTERVALS,
        )

        assert isinstance(actual, SQLTimestampIntervals)

    def test_sql_timedate_functions(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLTimeDateFunctions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_TIMEDATE_FUNCTIONS,
        )

        assert isinstance(actual, SQLTimeDateFunctions)

    def test_sql_txn_capable(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLTxnCapable = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_TXN_CAPABLE,
        )

        assert isinstance(actual, SQLTxnCapable)
        assert actual in SQLTxnCapable

    def test_sql_txn_isolation_option(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLTxnIsolationOption = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_TXN_ISOLATION_OPTION,
        )

        assert isinstance(actual, SQLTxnIsolationOption)

    def test_sql_union(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLUnion = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_UNION,
        )

        assert isinstance(actual, SQLUnion)

    def test_sql_user_name(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_USER_NAME,
        )

        assert isinstance(actual, str)


class TestSQLGetSetConnectAttr:
    @pytest.mark.parametrize("expected", list(SQLAttrAutocommit))
    def test_sql_attr_autocommit(
        self,
        driver_manager: DriverManager,
        isolated_connection_handle: ConnectionHandle,
        expected: SQLAttrAutocommit,
    ) -> None:
        driver_manager.sql_set_connect_attr_w(
            connection_handle=isolated_connection_handle,
            attribute=ConnectionAttribute.SQL_ATTR_AUTOCOMMIT,
            value=expected,
        )

        actual: SQLAttrAutocommit = driver_manager.sql_get_connect_attr_w(
            connection_handle=isolated_connection_handle,
            attribute=ConnectionAttribute.SQL_ATTR_AUTOCOMMIT,
        )

        assert actual == expected

    @pytest.mark.parametrize("expected", list(SQLAttrTrace))
    def test_sql_attr_trace(
        self,
        driver_manager: DriverManager,
        isolated_connection_handle: ConnectionHandle,
        expected: SQLAttrTrace,
    ) -> None:
        driver_manager.sql_set_connect_attr_w(
            connection_handle=isolated_connection_handle,
            attribute=ConnectionAttribute.SQL_ATTR_TRACE,
            value=expected,
        )

        actual: SQLAttrTrace = driver_manager.sql_get_connect_attr_w(
            connection_handle=isolated_connection_handle,
            attribute=ConnectionAttribute.SQL_ATTR_TRACE,
        )

        assert actual == expected


class TestSQLGetSetEnvAttr:
    @pytest.mark.parametrize("expected", list(SQLAttrConnectionPooling))
    def test_sql_attr_connection_pooling(
        self,
        driver_manager: DriverManager,
        isolated_environment_handle: EnvironmentHandle,
        expected: SQLAttrConnectionPooling,
    ) -> None:

        if expected is SQLAttrConnectionPooling.SQL_CP_DRIVER_AWARE and not driver_manager.is_windows_dm:
            with pytest.raises(ODBCError, match="Invalid attribute value"):
                driver_manager.sql_set_env_attr(
                    environment_handle=isolated_environment_handle,
                    attribute=EnvironmentAttribute.SQL_ATTR_CONNECTION_POOLING,
                    value=expected,
                )
            return

        driver_manager.sql_set_env_attr(
            environment_handle=isolated_environment_handle,
            attribute=EnvironmentAttribute.SQL_ATTR_CONNECTION_POOLING,
            value=expected,
        )

        actual: SQLAttrConnectionPooling = driver_manager.sql_get_env_attr(
            environment_handle=isolated_environment_handle,
            attribute=EnvironmentAttribute.SQL_ATTR_CONNECTION_POOLING,
        )

        assert actual == expected

    @pytest.mark.parametrize("expected", list(SQLAttrCPMatch))
    def test_sql_attr_cp_match(
        self,
        driver_manager: DriverManager,
        isolated_environment_handle: EnvironmentHandle,
        expected: SQLAttrCPMatch,
    ) -> None:

        driver_manager.sql_set_env_attr(
            environment_handle=isolated_environment_handle,
            attribute=EnvironmentAttribute.SQL_ATTR_CP_MATCH,
            value=expected,
        )

        actual: SQLAttrCPMatch = driver_manager.sql_get_env_attr(
            environment_handle=isolated_environment_handle,
            attribute=EnvironmentAttribute.SQL_ATTR_CP_MATCH,
        )

        assert actual == expected

    @pytest.mark.parametrize("expected", list(SQLAttrODBCVersion))
    def test_sql_attr_odbc_version(
        self,
        driver_manager: DriverManager,
        isolated_environment_handle: EnvironmentHandle,
        expected: SQLAttrODBCVersion,
    ) -> None:

        driver_manager.sql_set_env_attr(
            environment_handle=isolated_environment_handle,
            attribute=EnvironmentAttribute.SQL_ATTR_ODBC_VERSION,
            value=expected,
        )

        actual: SQLAttrODBCVersion = driver_manager.sql_get_env_attr(
            environment_handle=isolated_environment_handle,
            attribute=EnvironmentAttribute.SQL_ATTR_ODBC_VERSION,
        )

        assert actual == expected
