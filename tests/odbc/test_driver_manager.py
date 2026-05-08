from contextlib import nullcontext
from typing import Literal

import pytest

from odbcffi.odbc import *
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

    def test_sql_alter_table(self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle) -> None:

        actual: SQLAlterTable = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_ALTER_TABLE,
        )

        assert isinstance(actual, SQLAlterTable)

    def test_sql_bookmark_persistence(
        self, driver_manager: DriverManager, open_connection_handle: ConnectionHandle
    ) -> None:

        actual: SQLBookmarkPersistence = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_BOOKMARK_PERSISTENCE,
        )

        assert isinstance(actual, SQLBookmarkPersistence)

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
        # Microsoft's ODBC driver is the only one that supports it.
        ctx = (
            pytest.raises(ODBCError)
            if not (
                connection_info.driver.startswith("ODBC Driver ") and connection_info.driver.endswith(" for SQL Server")
            )
            else nullcontext()
        )

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

    def test_correlation_name(
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

        actual: str = driver_manager.sql_get_info_w(
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
        connection_info: ConnectionInfo,
    ) -> None:

        # TODO: This will break as and when new driver versions are released.
        #  Think about testing this a different way, or pinning the versions.
        expected = {
            "ODBC Driver 17 for SQL Server": "libmsodbcsql-17.11.so.1.1",
            "ODBC Driver 18 for SQL Server": "libmsodbcsql-18.6.so.2.1",
            "FreeTDS": "libtdsodbc.so",
            "MySQL ODBC 9.7 ANSI Driver": "libmyodbc9a.so",
            "MySQL ODBC 9.7 Unicode Driver": "libmyodbc9w.so",
            "PostgreSQL ANSI": "psqlodbca.so",
            "PostgreSQL Unicode": "psqlodbcw.so",
        }[connection_info.driver]

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_DRIVER_NAME,
        )

        assert actual == expected

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
        connection_info: ConnectionInfo,
    ) -> None:

        expected: str = {
            "FreeTDS": (
                # https://github.com/FreeTDS/freetds/blob/048c76b4d48156168c74843e6a1c90b8287ae0ab/src/odbc/odbc.c#L5848-L5860
                "BREAK,BROWSE,BULK,CHECKPOINT,CLUSTERED,COMMITTED,COMPUTE,CONFIRM,CONTROLROW,DATABASE,DBCC,DISK,DISTRIBUTED,DUMMY,DUMP,ERRLVL,ERROREXIT,EXIT,FILE,FILLFACTOR,FLOPPY,HOLDLOCK,IDENTITY_INSERT,IDENTITYCOL,IF,KILL,LINENO,LOAD,MIRROREXIT,NONCLUSTERED,OFF,OFFSETS,ONCE,OVER,PERCENT,PERM,PERMANENT,PLAN,PRINT,PROC,PROCESSEXIT,RAISERROR,READ,READTEXT,RECONFIGURE,REPEATABLE,RETURN,ROWCOUNT,RULE,SAVE,SERIALIZABLE,SETUSER,SHUTDOWN,STATISTICS,TAPE,TEMP,TEXTSIZE,TRAN,TRIGGER,TRUNCATE,TSEQUEL,UNCOMMITTED,UPDATETEXT,USE,WAITFOR,WHILE,WRITETEXT"
            ),
            "MySQL ODBC 9.7 ANSI Driver": (
                "ACCESSIBLE,ANALYZE,ASENSITIVE,BEFORE,BIGINT,BINARY,BLOB,CALL,CHANGE,CONDITION,DATABASE,DATABASES,DAY_HOUR,DAY_MICROSECOND,DAY_MINUTE,DAY_SECOND,DELAYED,DETERMINISTIC,DISTINCTROW,DIV,DUAL,EACH,ELSEIF,ENCLOSED,ESCAPED,EXIT,EXPLAIN,FLOAT4,FLOAT8,FORCE,FULLTEXT,GENERAL,GET,HIGH_PRIORITY,HOUR_MICROSECOND,HOUR_MINUTE,HOUR_SECOND,IF,IGNORE,IGNORE_SERVER_IDS,INFILE,INOUT,INT1,INT2,INT3,INT4,INT8,IO_AFTER_GTIDS,IO_BEFORE_GTIDS,ITERATE,KEYS,KILL,LEAVE,LIMIT,LINEAR,LINES,LOAD,LOCALTIME,LOCALTIMESTAMP,LOCK,LONG,LONGBLOB,LONGTEXT,LOOP,LOW_PRIORITY,SOURCE_BIND,SOURCE_HEARTBEAT_PERIOD,SOURCE_SSL_VERIFY_SERVER_CERT,MAXVALUE,MEDIUMBLOB,MEDIUMINT,MEDIUMTEXT,MIDDLEINT,MINUTE_MICROSECOND,MINUTE_SECOND,MOD,MODIFIES,NO_WRITE_TO_BINLOG,NONBLOCKING,ONE_SHOT,OPTIMIZE,OPTIONALLY,OUT,OUTFILE,PARTITION,PURGE,RANGE,READ_ONLY,READS,READ_WRITE,REGEXP,RELEASE,RENAME,REPEAT,REPLACE,REQUIRE,RESIGNAL,RETURN,RLIKE,SCHEMAS,SECOND_MICROSECOND,SENSITIVE,SEPARATOR,SHOW,SIGNAL,SLOW,SPATIAL,SPECIFIC,SQL_AFTER_GTIDS,SQL_BEFORE_GTIDS,SQL_BIG_RESULT,SQL_CALC_FOUND_ROWS,SQLEXCEPTION,SQL_SMALL_RESULT,SSL,STARTING,STRAIGHT_JOIN,TERMINATED,TINYBLOB,TINYINT,TINYTEXT,TRIGGER,UNDO,UNLOCK,UNSIGNED,USE,UTC_DATE,UTC_TIME,UTC_TIMESTAMP,VARBINARY,VARCHARACTER,WHILE,X509,XOR,YEAR_MONTH,ZEROFILL"
            ),
            "MySQL ODBC 9.7 Unicode Driver": (
                "ACCESSIBLE,ANALYZE,ASENSITIVE,BEFORE,BIGINT,BINARY,BLOB,CALL,CHANGE,CONDITION,DATABASE,DATABASES,DAY_HOUR,DAY_MICROSECOND,DAY_MINUTE,DAY_SECOND,DELAYED,DETERMINISTIC,DISTINCTROW,DIV,DUAL,EACH,ELSEIF,ENCLOSED,ESCAPED,EXIT,EXPLAIN,FLOAT4,FLOAT8,FORCE,FULLTEXT,GENERAL,GET,HIGH_PRIORITY,HOUR_MICROSECOND,HOUR_MINUTE,HOUR_SECOND,IF,IGNORE,IGNORE_SERVER_IDS,INFILE,INOUT,INT1,INT2,INT3,INT4,INT8,IO_AFTER_GTIDS,IO_BEFORE_GTIDS,ITERATE,KEYS,KILL,LEAVE,LIMIT,LINEAR,LINES,LOAD,LOCALTIME,LOCALTIMESTAMP,LOCK,LONG,LONGBLOB,LONGTEXT,LOOP,LOW_PRIORITY,SOURCE_BIND,SOURCE_HEARTBEAT_PERIOD,SOURCE_SSL_VERIFY_SERVER_CERT,MAXVALUE,MEDIUMBLOB,MEDIUMINT,MEDIUMTEXT,MIDDLEINT,MINUTE_MICROSECOND,MINUTE_SECOND,MOD,MODIFIES,NO_WRITE_TO_BINLOG,NONBLOCKING,ONE_SHOT,OPTIMIZE,OPTIONALLY,OUT,OUTFILE,PARTITION,PURGE,RANGE,READ_ONLY,READS,READ_WRITE,REGEXP,RELEASE,RENAME,REPEAT,REPLACE,REQUIRE,RESIGNAL,RETURN,RLIKE,SCHEMAS,SECOND_MICROSECOND,SENSITIVE,SEPARATOR,SHOW,SIGNAL,SLOW,SPATIAL,SPECIFIC,SQL_AFTER_GTIDS,SQL_BEFORE_GTIDS,SQL_BIG_RESULT,SQL_CALC_FOUND_ROWS,SQLEXCEPTION,SQL_SMALL_RESULT,SSL,STARTING,STRAIGHT_JOIN,TERMINATED,TINYBLOB,TINYINT,TINYTEXT,TRIGGER,UNDO,UNLOCK,UNSIGNED,USE,UTC_DATE,UTC_TIME,UTC_TIMESTAMP,VARBINARY,VARCHARACTER,WHILE,X509,XOR,YEAR_MONTH,ZEROFILL"
            ),
            "ODBC Driver 17 for SQL Server": (
                "BACKUP,BREAK,BROWSE,BULK,CHECKPOINT,CLUSTERED,COMMITTED,COMPUTE,CONFIRM,CONTROLROW,DATABASE,DBCC,DISK,DISTRIBUTED,DUMMY,ERRLVL,ERROREXIT,EXIT,FILE,FILLFACTOR,FLOPPY,HOLDLOCK,IDENTITY_INSERT,IDENTITYCOL,IF,KILL,LINENO,MERGE,MIRROREXIT,NONCLUSTERED,OFF,OFFSETS,ONCE,OVER,PERCENT,PERM,PERMANENT,PLAN,PRINT,PROC,PROCESSEXIT,RAISERROR,READ,READTEXT,RECONFIGURE,REPEATABLE,RESTORE,RETURN,ROWCOUNT,RULE,SAVE,SERIALIZABLE,SETUSER,SHUTDOWN,STATISTICS,TAPE,TEMP,TEXTSIZE,TOP,TRAN,TRIGGER,TRUNCATE,TSEQUEL,UNCOMMITTED,UPDATETEXT,USE,WAITFOR,WHILE,WRITETEXT"
            ),
            "ODBC Driver 18 for SQL Server": (
                "BACKUP,BREAK,BROWSE,BULK,CHECKPOINT,CLUSTERED,COMMITTED,COMPUTE,CONFIRM,CONTROLROW,DATABASE,DBCC,DISK,DISTRIBUTED,DUMMY,ERRLVL,ERROREXIT,EXIT,FILE,FILLFACTOR,FLOPPY,HOLDLOCK,IDENTITY_INSERT,IDENTITYCOL,IF,KILL,LINENO,MERGE,MIRROREXIT,NONCLUSTERED,OFF,OFFSETS,ONCE,OVER,PERCENT,PERM,PERMANENT,PLAN,PRINT,PROC,PROCESSEXIT,RAISERROR,READ,READTEXT,RECONFIGURE,REPEATABLE,RESTORE,RETURN,ROWCOUNT,RULE,SAVE,SERIALIZABLE,SETUSER,SHUTDOWN,STATISTICS,TAPE,TEMP,TEXTSIZE,TOP,TRAN,TRIGGER,TRUNCATE,TSEQUEL,UNCOMMITTED,UPDATETEXT,USE,WAITFOR,WHILE,WRITETEXT"
            ),
            # psqlodbc just returns an empty string.
            # https://github.com/postgresql-interfaces/psqlodbc/blob/863a0e938dd50c7b68208484bdc3ef8b00735a92/info.c#L348-L350
            "PostgreSQL ANSI": "",
            "PostgreSQL Unicode": "",
        }[connection_info.driver]

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_KEYWORDS,
        )

        assert actual == expected

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

    def test_sql_mult_result_sets(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MULT_RESULT_SETS,
        )

        assert actual in ("Y", "N")

    def test_sql_multiple_active_txn(
        self,
        driver_manager: DriverManager,
        open_connection_handle: ConnectionHandle,
    ) -> None:

        actual: str = driver_manager.sql_get_info_w(
            connection_handle=open_connection_handle,
            info_type=InfoType.SQL_MULTIPLE_ACTIVE_TXN,
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
