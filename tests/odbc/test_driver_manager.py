from contextlib import nullcontext
from typing import Any, Literal

import pytest

from odbcffi.odbc.connection_handle import ConnectionHandle
from odbcffi.odbc.driver_manager import DriverManager
from odbcffi.odbc.dto import DriverInfo
from odbcffi.odbc.enums import *
from odbcffi.odbc.enums import SQLDropTable
from odbcffi.odbc.environment_handle import EnvironmentHandle
from odbcffi.odbc.errors import ODBCError
from odbcffi.odbc.statement_handle import StatementHandle
from tests.conftest import ConnectionInfo


class TestSQLDriversW:
    def test_sql_drivers_w(self, driver_manager: DriverManager, environment_handle: EnvironmentHandle) -> None:

        actual: list[DriverInfo] = driver_manager.sql_drivers_w(environment_handle=environment_handle)

        assert isinstance(actual, list)
        assert len(actual) > 0
        assert all(isinstance(driver_info, DriverInfo) for driver_info in actual)
        assert all(driver_info.description for driver_info in actual)
        assert all(isinstance(driver_info.attributes, dict) for driver_info in actual)


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

    def test_sql_aggregate_functions(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLAggregateFunctions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_AGGREGATE_FUNCTIONS,
        )

        assert isinstance(actual, SQLAggregateFunctions)

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

    def test_sql_async_dbc_functions(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        ctx = (
            pytest.raises(ODBCError)
            if connection_info.driver == "FreeTDS"
            or connection_info.driver.startswith("PostgreSQL")
            or connection_info.driver == "SQL Server"
            else nullcontext()
        )

        with ctx:
            actual: SQLAsyncDbcFunctions = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle,
                info_type=InfoType.SQL_ASYNC_DBC_FUNCTIONS,
            )

            assert isinstance(actual, SQLAsyncDbcFunctions)

    def test_sql_async_mode(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLAsyncMode = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ASYNC_MODE,
        )

        assert isinstance(actual, SQLAsyncMode)

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

    def test_sql_catalog_name(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CATALOG_NAME,
        )

        assert actual in ("Y", "N")

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

    def test_sql_collation_seq(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle, connection_info: ConnectionInfo
    ) -> None:

        # Not implemented in FreeTDS
        # https://github.com/FreeTDS/freetds/blob/217ffa7674ae3462c5d663ae2df579a98f44c348/src/odbc/odbc.c#L5551-L5554
        ctx = pytest.raises(ODBCError) if connection_info.driver == "FreeTDS" else nullcontext()

        with ctx:
            actual: str = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle,
                info_type=InfoType.SQL_COLLATION_SEQ,
            )

            assert isinstance(actual, str)

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

    def test_sql_create_schema(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLCreateSchema = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CREATE_SCHEMA,
        )

        assert isinstance(actual, SQLCreateSchema)

    def test_sql_create_table(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLCreateTable = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CREATE_TABLE,
        )

        assert isinstance(actual, SQLCreateTable)

    def test_sql_create_translation(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCreateTranslation = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CREATE_TRANSLATION,
        )

        assert isinstance(actual, SQLCreateTranslation)

    def test_sql_create_view(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLCreateView = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_CREATE_VIEW,
        )

        assert isinstance(actual, SQLCreateView)

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

    def test_sql_cursor_sensitivity(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        ctx = pytest.raises(ODBCError) if connection_info.driver.startswith("PostgreSQL") else nullcontext()

        with ctx:
            actual: SQLCursorSensitivity = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle,
                info_type=InfoType.SQL_CURSOR_SENSITIVITY,
            )

            assert actual in list(SQLCursorSensitivity)

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

    def test_sql_ddl_index(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLDdlIndex = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DDL_INDEX,
        )

        assert isinstance(actual, SQLDdlIndex)

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

    def test_sql_driver_aware_pooling_supported(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        # Only implemented by windows driver managers, seemingly...
        ctx = pytest.raises(ODBCError) if not driver_manager.is_windows_dm else nullcontext()

        with ctx:
            actual: SQLDriverAwarePoolingSupported = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle,
                info_type=InfoType.SQL_DRIVER_AWARE_POOLING_SUPPORTED,
            )

            assert isinstance(actual, SQLDriverAwarePoolingSupported)

    def test_sql_describe_parameter(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: Literal["Y", "N"] = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DESCRIBE_PARAMETER,
        )

        assert actual in ("Y", "N")

    def test_sql_dm_ver(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DM_VER,
        )

        assert isinstance(actual, str)
        assert actual

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

    def test_sql_drop_assertion(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLDropAssertion = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DROP_ASSERTION,
        )

        assert isinstance(actual, SQLDropAssertion)

    def test_sql_drop_character_set(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLDropCharacterSet = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DROP_CHARACTER_SET,
        )

        assert isinstance(actual, SQLDropCharacterSet)

    def test_sql_drop_collation(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLDropCollation = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DROP_COLLATION,
        )

        assert isinstance(actual, SQLDropCollation)

    def test_sql_drop_domain(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLDropDomain = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DROP_DOMAIN,
        )

        assert isinstance(actual, SQLDropDomain)

    def test_sql_drop_schema(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLDropSchema = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DROP_SCHEMA,
        )

        assert isinstance(actual, SQLDropSchema)

    def test_sql_drop_table(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLDropTable = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DROP_TABLE,
        )

        assert isinstance(actual, SQLDropTable)

    def test_sql_drop_translation(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLDropTranslation = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DROP_TRANSLATION,
        )

        assert isinstance(actual, SQLDropTranslation)

    def test_sql_drop_view(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLDropView = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DROP_VIEW,
        )

        assert isinstance(actual, SQLDropView)

    def test_sql_dynamic_cursor_attributes_1(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCursorAttributes1 = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DYNAMIC_CURSOR_ATTRIBUTES1,
        )

        assert isinstance(actual, SQLCursorAttributes1)

    def test_sql_dynamic_cursor_attributes_2(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCursorAttributes2 = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DYNAMIC_CURSOR_ATTRIBUTES2,
        )

        assert isinstance(actual, SQLCursorAttributes2)

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

    def test_sql_forward_only_cursor_attributes_1(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCursorAttributes1 = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES1,
        )

        assert isinstance(actual, SQLCursorAttributes1)

    def test_sql_forward_only_cursor_attributes_2(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCursorAttributes2 = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES2,
        )

        assert isinstance(actual, SQLCursorAttributes2)

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

    def test_sql_index_keywords(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLIndexKeywords = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_INDEX_KEYWORDS,
        )

        assert isinstance(actual, SQLIndexKeywords)

    def test_sql_info_schema_views(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLInfoSchemaViews = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_INFO_SCHEMA_VIEWS,
        )

        assert isinstance(actual, SQLInfoSchemaViews)

    def test_sql_insert_statement(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLInsertStatement = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_INSERT_STATEMENT,
        )

        assert isinstance(actual, SQLInsertStatement)

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

    def test_sql_keyset_cursor_attributes_1(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCursorAttributes1 = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_KEYSET_CURSOR_ATTRIBUTES1,
        )

        assert isinstance(actual, SQLCursorAttributes1)

    def test_sql_keyset_cursor_attributes_2(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCursorAttributes2 = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_KEYSET_CURSOR_ATTRIBUTES2,
        )

        assert isinstance(actual, SQLCursorAttributes2)

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

    def test_sql_max_async_concurrent_statements(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        # Not implemented in psqlodbc

        ctx = pytest.raises(ODBCError) if connection_info.driver.startswith("PostgreSQL") else nullcontext()

        with ctx:
            actual: int = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle,
                info_type=InfoType.SQL_MAX_ASYNC_CONCURRENT_STATEMENTS,
            )

            assert actual >= 0

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

    def test_sql_max_identifier_len(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: int = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MAX_IDENTIFIER_LEN,
        )

        assert actual >= 0

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

    def test_sql_odbc_interface_conformance(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLOdbcInterfaceConformance = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ODBC_INTERFACE_CONFORMANCE,
        )

        assert isinstance(actual, SQLOdbcInterfaceConformance)

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

    def test_sql_param_array_row_counts(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLParamArrayRowCounts = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_PARAM_ARRAY_ROW_COUNTS,
        )

        assert isinstance(actual, SQLParamArrayRowCounts)

    def test_sql_param_array_selects(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLParamArraySelects = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_PARAM_ARRAY_SELECTS,
        )

        assert isinstance(actual, SQLParamArraySelects)

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

    def test_sql_sql92_datetime_functions(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSql92DatetimeFunctions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL92_DATETIME_FUNCTIONS,
        )

        assert isinstance(actual, SQLSql92DatetimeFunctions)

    def test_sql_sql92_foreign_key_delete_rule(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSql92ForeignKeyDeleteRule = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL92_FOREIGN_KEY_DELETE_RULE,
        )

        assert isinstance(actual, SQLSql92ForeignKeyDeleteRule)

    def test_sql_sql92_foreign_key_update_rule(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSql92ForeignKeyUpdateRule = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL92_FOREIGN_KEY_UPDATE_RULE,
        )

        assert isinstance(actual, SQLSql92ForeignKeyUpdateRule)

    def test_sql_sql92_grant(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSql92Grant = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL92_GRANT,
        )

        assert isinstance(actual, SQLSql92Grant)

    def test_sql_sql92_numeric_value_functions(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSql92NumericValueFunctions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL92_NUMERIC_VALUE_FUNCTIONS,
        )

        assert isinstance(actual, SQLSql92NumericValueFunctions)

    def test_sql_sql92_predicates(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSql92Predicates = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL92_PREDICATES,
        )

        assert isinstance(actual, SQLSql92Predicates)

    def test_sql_sql92_relational_join_operators(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSql92RelationalJoinOperators = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL92_RELATIONAL_JOIN_OPERATORS,
        )

        assert isinstance(actual, SQLSql92RelationalJoinOperators)

    def test_sql_sql92_revoke(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSql92Revoke = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL92_REVOKE,
        )

        assert isinstance(actual, SQLSql92Revoke)

    def test_sql_sql92_row_value_constructor(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSql92RowValueConstructor = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL92_ROW_VALUE_CONSTRUCTOR,
        )

        assert isinstance(actual, SQLSql92RowValueConstructor)

    def test_sql_sql92_string_functions(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSql92StringFunctions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL92_STRING_FUNCTIONS,
        )

        assert isinstance(actual, SQLSql92StringFunctions)

    def test_sql_sql92_value_expressions(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: SQLSql92ValueExpressions = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_SQL92_VALUE_EXPRESSIONS,
        )

        assert isinstance(actual, SQLSql92ValueExpressions)

    def test_sql_standard_cli_conformance(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        # Not implemented in psqlodbc
        # https://github.com/postgresql-interfaces/psqlodbc/blob/863a0e938dd50c7b68208484bdc3ef8b00735a92/info.c#L1065

        ctx = pytest.raises(ODBCError) if connection_info.driver.startswith("PostgreSQL") else nullcontext()

        with ctx:
            actual: SQLStandardCliConformance = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle,
                info_type=InfoType.SQL_STANDARD_CLI_CONFORMANCE,
            )

            assert isinstance(actual, SQLStandardCliConformance)

    def test_sql_static_cursor_attributes_1(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCursorAttributes1 = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_STATIC_CURSOR_ATTRIBUTES1,
        )

        assert isinstance(actual, SQLCursorAttributes1)

    def test_sql_static_cursor_attributes_2(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLCursorAttributes2 = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_STATIC_CURSOR_ATTRIBUTES2,
        )

        assert isinstance(actual, SQLCursorAttributes2)

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

    def test_xopen_cli_year(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
        connection_info: ConnectionInfo,
    ) -> None:

        # Not sure why, but it only fails with pgsql on Windows...
        ctx = (
            pytest.raises(ODBCError)
            if driver_manager.is_windows_dm and connection_info.driver.startswith("PostgreSQL")
            else nullcontext()
        )

        with ctx:
            actual: str = driver_manager.sql_get_info_w(
                connection_handle=open_connection_handle,
                info_type=InfoType.SQL_XOPEN_CLI_YEAR,
            )

            assert isinstance(actual, str)
            assert actual


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


class TestSQLGetTypeInfoW:
    def test_sql_all_types(
        self, connection_info: ConnectionInfo, driver_manager: DriverManager, statement_handle: StatementHandle
    ) -> None:

        driver_manager.sql_get_type_info_w(statement_handle=statement_handle, data_type=SQLDataType.SQL_UNKNOWN_TYPE)

        num_cols = driver_manager.sql_num_result_cols(statement_handle=statement_handle)

        assert num_cols > 0

        column_descriptions = [
            driver_manager.sql_describe_col_w(statement_handle=statement_handle, column_number=i)
            for i in range(1, num_cols + 1)
        ]

        results: list[dict[str, Any]] = []

        while driver_manager.sql_fetch(statement_handle=statement_handle):
            row: dict[str, Any | None] = {}

            for column_description in column_descriptions:
                value = driver_manager.sql_get_data(
                    statement_handle=statement_handle,
                    col_or_param_num=column_description.column_number,
                    target_type=column_description.data_type.to_c_data_type(),
                )

                if column_description.column_name == "DATA_TYPE" or column_description.column_name == "SQL_DATATYPE":
                    value = SQLDataType(value)
                elif column_description.column_name == "SQL_DATETIME_SUB":
                    data_type = row["DATA_TYPE"]
                    assert isinstance(data_type, SQLDataType)
                    if data_type in (
                        SQLDataType.SQL_TYPE_DATE,
                        SQLDataType.SQL_TYPE_TIME,
                        SQLDataType.SQL_TYPE_TIMESTAMP,
                        SQLDataType.SQL_TIMESTAMP,
                        SQLDataType.SQL_DATETIME,
                        SQLDataType.SQL_INTERVAL,
                        SQLDataType.SQL_SS_TIME2,
                        SQLDataType.SQL_SS_TIMESTAMPOFFSET,
                    ):
                        value = SQLDataType(value)
                    else:
                        # `value` should be None, and that _should_ be reflected in the assert statement below.
                        # However, mysql-connector-odbc returns a hard-coded 0 instead for char types...
                        # Maybe that was intended as SQLDataType.UNKNOWN, but who knows for sure.
                        # In any case, it doesn't comply with the spec.
                        # https://github.com/mysql/mysql-connector-odbc/issues/17
                        assert value in (None, 0), (data_type, value)

                row[column_description.column_name] = value

            results.append(row)

        # Each row in the result set should have at least the 19 mandatory columns in the spec.
        # The spec allows for additional, driver-dependent columns to be provided.
        # So far, only SQL Server does so, with its "USERTYPE" column.
        assert all(len(row) >= 19 for row in results)
        for column_name in {
            "AUTO_UNIQUE_VALUE",
            "CASE_SENSITIVE",
            "COLUMN_SIZE",
            "CREATE_PARAMS",
            "DATA_TYPE",
            "FIXED_PREC_SCALE",
            "INTERVAL_PRECISION",
            "LITERAL_PREFIX",
            "LITERAL_SUFFIX",
            "LOCAL_TYPE_NAME",
            "MAXIMUM_SCALE",
            "MINIMUM_SCALE",
            "NULLABLE",
            "NUM_PREC_RADIX",
            "SEARCHABLE",
            # mysql-connector-odbc returns a SQL_DATATYPE column in the result set.
            # https://github.com/mysql/mysql-connector-odbc/pull/19
            "SQL_DATA_TYPE" if connection_info.dbms_name != "MySQL" else "SQL_DATATYPE",
            "SQL_DATETIME_SUB",
            "TYPE_NAME",
            "UNSIGNED_ATTRIBUTE",
        }:
            for row in results:
                assert column_name in row

        # TODO: Should really break this out into a SQL Server specific test (along with PostgreSQL and MySQL tests),
        #  but that's a different PR.
        if connection_info.dbms_name == "Microsoft SQL Server":
            assert results == [
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 34,
                    "CREATE_PARAMS": "scale",
                    "DATA_TYPE": SQLDataType.SQL_SS_TIMESTAMPOFFSET,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "datetimeoffset",
                    "MAXIMUM_SCALE": 7,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 3,
                    "SQL_DATA_TYPE": -155,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_UNKNOWN_TYPE,
                    "TYPE_NAME": "datetimeoffset",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 16,
                    "CREATE_PARAMS": "scale",
                    "DATA_TYPE": SQLDataType.SQL_SS_TIME2,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "time",
                    "MAXIMUM_SCALE": 7,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 3,
                    "SQL_DATA_TYPE": -154,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_UNKNOWN_TYPE,
                    "TYPE_NAME": "time",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 1,
                    "COLUMN_SIZE": 0,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_SS_XML,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "N'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "xml",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 0,
                    "SQL_DATA_TYPE": -152,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "xml",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 8000,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_SS_VARIANT,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "sql_variant",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": -150,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "sql_variant",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 36,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_GUID,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "uniqueidentifier",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": -11,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "uniqueidentifier",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 1073741823,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_WLONGVARCHAR,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "N'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "ntext",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 1,
                    "SQL_DATA_TYPE": -10,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "ntext",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 4000,
                    "CREATE_PARAMS": "max length",
                    "DATA_TYPE": SQLDataType.SQL_WVARCHAR,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "N'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "nvarchar",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 3,
                    "SQL_DATA_TYPE": -9,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "nvarchar",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 128,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_WVARCHAR,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "N'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "sysname",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 0,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 3,
                    "SQL_DATA_TYPE": -9,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "sysname",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 18,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 4000,
                    "CREATE_PARAMS": "length",
                    "DATA_TYPE": SQLDataType.SQL_WCHAR,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "N'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "nchar",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 3,
                    "SQL_DATA_TYPE": -8,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "nchar",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 1,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_BIT,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "bit",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": -7,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "bit",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 16,
                },
                {
                    "AUTO_UNIQUE_VALUE": 0,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 3,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_TINYINT,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "tinyint",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": -6,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "tinyint",
                    "UNSIGNED_ATTRIBUTE": 1,
                    "USERTYPE": 5,
                },
                {
                    "AUTO_UNIQUE_VALUE": 1,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 3,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_TINYINT,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "tinyint identity",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 0,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": -6,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "tinyint identity",
                    "UNSIGNED_ATTRIBUTE": 1,
                    "USERTYPE": 5,
                },
                {
                    "AUTO_UNIQUE_VALUE": 0,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 19,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_BIGINT,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "bigint",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": -5,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "bigint",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": 1,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 19,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_BIGINT,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "bigint identity",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 0,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": -5,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "bigint identity",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 2147483647,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_LONGVARBINARY,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "0x",
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "image",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 0,
                    "SQL_DATA_TYPE": -4,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "image",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 20,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 8000,
                    "CREATE_PARAMS": "max length",
                    "DATA_TYPE": SQLDataType.SQL_VARBINARY,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "0x",
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "varbinary",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": -3,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "varbinary",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 4,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 8000,
                    "CREATE_PARAMS": "length",
                    "DATA_TYPE": SQLDataType.SQL_BINARY,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "0x",
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "binary",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": -2,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "binary",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 3,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 8,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_BINARY,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "0x",
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "timestamp",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 0,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": -2,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "timestamp",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 80,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 2147483647,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_LONGVARCHAR,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "text",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 1,
                    "SQL_DATA_TYPE": -1,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "text",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 19,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 8000,
                    "CREATE_PARAMS": "length",
                    "DATA_TYPE": SQLDataType.SQL_CHAR,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "char",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 3,
                    "SQL_DATA_TYPE": 1,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "char",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 1,
                },
                {
                    "AUTO_UNIQUE_VALUE": 0,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 38,
                    "CREATE_PARAMS": "precision,scale",
                    "DATA_TYPE": SQLDataType.SQL_NUMERIC,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "numeric",
                    "MAXIMUM_SCALE": 38,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 2,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "numeric",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 10,
                },
                {
                    "AUTO_UNIQUE_VALUE": 1,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 38,
                    "CREATE_PARAMS": "precision",
                    "DATA_TYPE": SQLDataType.SQL_NUMERIC,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "numeric() identity",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 0,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 2,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "numeric() identity",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 10,
                },
                {
                    "AUTO_UNIQUE_VALUE": 0,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 38,
                    "CREATE_PARAMS": "precision,scale",
                    "DATA_TYPE": SQLDataType.SQL_DECIMAL,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "decimal",
                    "MAXIMUM_SCALE": 38,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 3,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "decimal",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 24,
                },
                {
                    "AUTO_UNIQUE_VALUE": 0,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 19,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_DECIMAL,
                    "FIXED_PREC_SCALE": 1,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "$",
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "money",
                    "MAXIMUM_SCALE": 4,
                    "MINIMUM_SCALE": 4,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 3,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "money",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 11,
                },
                {
                    "AUTO_UNIQUE_VALUE": 0,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 10,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_DECIMAL,
                    "FIXED_PREC_SCALE": 1,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "$",
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "smallmoney",
                    "MAXIMUM_SCALE": 4,
                    "MINIMUM_SCALE": 4,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 3,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "smallmoney",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 21,
                },
                {
                    "AUTO_UNIQUE_VALUE": 1,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 38,
                    "CREATE_PARAMS": "precision",
                    "DATA_TYPE": SQLDataType.SQL_DECIMAL,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "decimal() identity",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 0,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 3,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "decimal() identity",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 24,
                },
                {
                    "AUTO_UNIQUE_VALUE": 0,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 10,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_INTEGER,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "int",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 4,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "int",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 7,
                },
                {
                    "AUTO_UNIQUE_VALUE": 1,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 10,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_INTEGER,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "int identity",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 0,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 4,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "int identity",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 7,
                },
                {
                    "AUTO_UNIQUE_VALUE": 0,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 5,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_SMALLINT,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "smallint",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 5,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "smallint",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 6,
                },
                {
                    "AUTO_UNIQUE_VALUE": 1,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 5,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_SMALLINT,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "smallint identity",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 0,
                    "NUM_PREC_RADIX": 10,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 5,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "smallint identity",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 6,
                },
                {
                    "AUTO_UNIQUE_VALUE": 0,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 53,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_FLOAT,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "float",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": 2,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 6,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "float",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 8,
                },
                {
                    "AUTO_UNIQUE_VALUE": 0,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 24,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_REAL,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "LOCAL_TYPE_NAME": "real",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": 2,
                    "SEARCHABLE": 2,
                    "SQL_DATA_TYPE": 7,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "real",
                    "UNSIGNED_ATTRIBUTE": 0,
                    "USERTYPE": 23,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 8000,
                    "CREATE_PARAMS": "max length",
                    "DATA_TYPE": SQLDataType.SQL_VARCHAR,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "varchar",
                    "MAXIMUM_SCALE": None,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 3,
                    "SQL_DATA_TYPE": 12,
                    "SQL_DATETIME_SUB": None,
                    "TYPE_NAME": "varchar",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 2,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 10,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_TYPE_DATE,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "date",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": None,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 3,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_CHAR,
                    "TYPE_NAME": "date",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 27,
                    "CREATE_PARAMS": "scale",
                    "DATA_TYPE": SQLDataType.SQL_TYPE_TIMESTAMP,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "datetime2",
                    "MAXIMUM_SCALE": 7,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 3,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_DECIMAL,
                    "TYPE_NAME": "datetime2",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 0,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 23,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_TYPE_TIMESTAMP,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "datetime",
                    "MAXIMUM_SCALE": 3,
                    "MINIMUM_SCALE": 3,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 3,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_DECIMAL,
                    "TYPE_NAME": "datetime",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 12,
                },
                {
                    "AUTO_UNIQUE_VALUE": None,
                    "CASE_SENSITIVE": 0,
                    "COLUMN_SIZE": 16,
                    "CREATE_PARAMS": None,
                    "DATA_TYPE": SQLDataType.SQL_TYPE_TIMESTAMP,
                    "FIXED_PREC_SCALE": 0,
                    "INTERVAL_PRECISION": None,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "LOCAL_TYPE_NAME": "smalldatetime",
                    "MAXIMUM_SCALE": 0,
                    "MINIMUM_SCALE": 0,
                    "NULLABLE": 1,
                    "NUM_PREC_RADIX": None,
                    "SEARCHABLE": 3,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_DECIMAL,
                    "TYPE_NAME": "smalldatetime",
                    "UNSIGNED_ATTRIBUTE": None,
                    "USERTYPE": 22,
                },
            ]
