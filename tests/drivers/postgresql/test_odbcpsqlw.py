from collections.abc import Mapping
from typing import Any

import pytest

from odbcffi.odbc.enums import *
from odbcffi.odbc.errors import ODBCError
from tests.drivers.base import DriverTest


@pytest.fixture(scope="module")
def driver() -> str:
    return "PostgreSQL Unicode"


class TestOdbcPsqlW(DriverTest):
    @property
    def expected_sql_get_info_w_return_values(self) -> Mapping[InfoType, Any]:
        return {
            InfoType.SQL_ACCESSIBLE_PROCEDURES: "N",
            InfoType.SQL_ACCESSIBLE_TABLES: "N",
            InfoType.SQL_ACTIVE_ENVIRONMENTS: 0,
            InfoType.SQL_AGGREGATE_FUNCTIONS: SQLAggregateFunctions.SQL_AF_ALL,
            InfoType.SQL_ALTER_DOMAIN: SQLAlterDomain(0),
            InfoType.SQL_ALTER_TABLE: SQLAlterTable.SQL_AT_ADD_COLUMN
            | SQLAlterTable.SQL_AT_DROP_COLUMN
            | SQLAlterTable.SQL_AT_ADD_CONSTRAINT
            | SQLAlterTable.SQL_AT_ADD_COLUMN_SINGLE
            | SQLAlterTable.SQL_AT_DROP_COLUMN_CASCADE
            | SQLAlterTable.SQL_AT_DROP_COLUMN_RESTRICT
            | SQLAlterTable.SQL_AT_ADD_TABLE_CONSTRAINT
            | SQLAlterTable.SQL_AT_DROP_TABLE_CONSTRAINT_CASCADE
            | SQLAlterTable.SQL_AT_DROP_TABLE_CONSTRAINT_RESTRICT,
            InfoType.SQL_ASYNC_DBC_FUNCTIONS: ODBCError(
                what="SQLGetInfoW",
                sql_state="HYC00",
                native_error=209,
                message_text="Unrecognized key passed to PGAPI_GetInfo.",
                return_code=SQLReturn.SQL_ERROR,
            ),
            InfoType.SQL_ASYNC_MODE: SQLAsyncMode.SQL_AM_NONE,
            InfoType.SQL_ASYNC_NOTIFICATION: ODBCError(
                what="SQLGetInfoW",
                sql_state="HYC00",
                native_error=209,
                message_text="Unrecognized key passed to PGAPI_GetInfo.",
                return_code=SQLReturn.SQL_ERROR,
            ),
            InfoType.SQL_BATCH_ROW_COUNT: SQLBatchRowCount.SQL_BRC_EXPLICIT,
            InfoType.SQL_BATCH_SUPPORT: SQLBatchSupport.SQL_BS_SELECT_EXPLICIT
            | SQLBatchSupport.SQL_BS_ROW_COUNT_EXPLICIT,
            InfoType.SQL_BOOKMARK_PERSISTENCE: SQLBookmarkPersistence.SQL_BP_DELETE
            | SQLBookmarkPersistence.SQL_BP_TRANSACTION
            | SQLBookmarkPersistence.SQL_BP_UPDATE
            | SQLBookmarkPersistence.SQL_BP_SCROLL,
            InfoType.SQL_CATALOG_LOCATION: SQLCatalogLocation.SQL_CL_START,
            InfoType.SQL_CATALOG_NAME: "Y",
            InfoType.SQL_CATALOG_NAME_SEPARATOR: ".",
            InfoType.SQL_CATALOG_TERM: "catalog",
            InfoType.SQL_CATALOG_USAGE: SQLCatalogUsage.SQL_CU_DML_STATEMENTS,
            InfoType.SQL_COLLATION_SEQ: "",
            InfoType.SQL_COLUMN_ALIAS: "Y",
            InfoType.SQL_CONCAT_NULL_BEHAVIOR: SQLConcatNullBehavior.SQL_CB_NON_NULL,
            InfoType.SQL_CONVERT_BIGINT: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIGINT,
            InfoType.SQL_CONVERT_BINARY: SQLConvert(0),
            InfoType.SQL_CONVERT_BIT: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIT,
            InfoType.SQL_CONVERT_CHAR: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIT
            | SQLConvert.SQL_CVT_BIGINT,
            InfoType.SQL_CONVERT_DATE: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_DATE,
            InfoType.SQL_CONVERT_DECIMAL: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIGINT,
            InfoType.SQL_CONVERT_DOUBLE: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIGINT,
            InfoType.SQL_CONVERT_FLOAT: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIGINT,
            InfoType.SQL_CONVERT_FUNCTIONS: SQLConvertFunctions.SQL_FN_CVT_CONVERT,
            InfoType.SQL_CONVERT_GUID: ODBCError(
                what="SQLGetInfoW",
                sql_state="HYC00",
                native_error=209,
                message_text="Unrecognized key passed to PGAPI_GetInfo.",
                return_code=SQLReturn.SQL_ERROR,
            ),
            InfoType.SQL_CONVERT_INTEGER: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIT
            | SQLConvert.SQL_CVT_BIGINT,
            InfoType.SQL_CONVERT_INTERVAL_DAY_TIME: ODBCError(
                what="SQLGetInfoW",
                sql_state="HYC00",
                native_error=209,
                message_text="Unrecognized key passed to PGAPI_GetInfo.",
                return_code=SQLReturn.SQL_ERROR,
            ),
            InfoType.SQL_CONVERT_INTERVAL_YEAR_MONTH: ODBCError(
                what="SQLGetInfoW",
                sql_state="HYC00",
                native_error=209,
                message_text="Unrecognized key passed to PGAPI_GetInfo.",
                return_code=SQLReturn.SQL_ERROR,
            ),
            InfoType.SQL_CONVERT_LONGVARBINARY: SQLConvert(0),
            InfoType.SQL_CONVERT_LONGVARCHAR: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIT
            | SQLConvert.SQL_CVT_BIGINT,
            InfoType.SQL_CONVERT_NUMERIC: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIGINT,
            InfoType.SQL_CONVERT_REAL: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIGINT,
            InfoType.SQL_CONVERT_SMALLINT: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIGINT,
            InfoType.SQL_CONVERT_TIME: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR,
            InfoType.SQL_CONVERT_TIMESTAMP: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_DATE,
            InfoType.SQL_CONVERT_TINYINT: SQLConvert(0),
            InfoType.SQL_CONVERT_VARBINARY: SQLConvert(0),
            InfoType.SQL_CONVERT_VARCHAR: SQLConvert.SQL_CVT_CHAR
            | SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_VARCHAR
            | SQLConvert.SQL_CVT_LONGVARCHAR
            | SQLConvert.SQL_CVT_BIT
            | SQLConvert.SQL_CVT_BIGINT,
            InfoType.SQL_CONVERT_WCHAR: SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_BIT
            | SQLConvert.SQL_CVT_BIGINT
            | SQLConvert.SQL_CVT_DATE,
            InfoType.SQL_CONVERT_WLONGVARCHAR: SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_BIT
            | SQLConvert.SQL_CVT_BIGINT
            | SQLConvert.SQL_CVT_DATE,
            InfoType.SQL_CONVERT_WVARCHAR: SQLConvert.SQL_CVT_NUMERIC
            | SQLConvert.SQL_CVT_DECIMAL
            | SQLConvert.SQL_CVT_INTEGER
            | SQLConvert.SQL_CVT_SMALLINT
            | SQLConvert.SQL_CVT_FLOAT
            | SQLConvert.SQL_CVT_REAL
            | SQLConvert.SQL_CVT_DOUBLE
            | SQLConvert.SQL_CVT_BIT
            | SQLConvert.SQL_CVT_BIGINT
            | SQLConvert.SQL_CVT_DATE,
            InfoType.SQL_CORRELATION_NAME: SQLCorrelationName.SQL_CN_ANY,
            InfoType.SQL_CREATE_ASSERTION: SQLCreateAssertion(0),
            InfoType.SQL_CREATE_CHARACTER_SET: SQLCreateCharacterSet(0),
            InfoType.SQL_CREATE_COLLATION: SQLCreateCollation(0),
            InfoType.SQL_CREATE_DOMAIN: SQLCreateDomain(0),
            InfoType.SQL_CREATE_SCHEMA: SQLCreateSchema.SQL_CS_CREATE_SCHEMA | SQLCreateSchema.SQL_CS_AUTHORIZATION,
            InfoType.SQL_CREATE_TABLE: SQLCreateTable.SQL_CT_CREATE_TABLE
            | SQLCreateTable.SQL_CT_GLOBAL_TEMPORARY
            | SQLCreateTable.SQL_CT_CONSTRAINT_INITIALLY_DEFERRED
            | SQLCreateTable.SQL_CT_CONSTRAINT_INITIALLY_IMMEDIATE
            | SQLCreateTable.SQL_CT_CONSTRAINT_DEFERRABLE
            | SQLCreateTable.SQL_CT_COLUMN_CONSTRAINT
            | SQLCreateTable.SQL_CT_COLUMN_DEFAULT
            | SQLCreateTable.SQL_CT_TABLE_CONSTRAINT
            | SQLCreateTable.SQL_CT_CONSTRAINT_NAME_DEFINITION,
            InfoType.SQL_CREATE_TRANSLATION: SQLCreateTranslation(0),
            InfoType.SQL_CREATE_VIEW: SQLCreateView.SQL_CV_CREATE_VIEW,
            InfoType.SQL_CURSOR_COMMIT_BEHAVIOR: SQLCursorCommitBehavior.SQL_CB_PRESERVE,
            InfoType.SQL_CURSOR_ROLLBACK_BEHAVIOR: SQLCursorRollbackBehavior.SQL_CB_PRESERVE,
            InfoType.SQL_CURSOR_SENSITIVITY: ODBCError(
                what="SQLGetInfoW",
                sql_state="HYC00",
                native_error=209,
                message_text="Unrecognized key passed to PGAPI_GetInfo.",
                return_code=SQLReturn.SQL_ERROR,
            ),
            InfoType.SQL_DATABASE_NAME: "",
            InfoType.SQL_DATA_SOURCE_NAME: "",
            InfoType.SQL_DATA_SOURCE_READ_ONLY: "N",
            InfoType.SQL_DATETIME_LITERALS: ODBCError(
                what="SQLGetInfoW",
                sql_state="HYC00",
                native_error=209,
                message_text="Unrecognized key passed to PGAPI_GetInfo.",
                return_code=SQLReturn.SQL_ERROR,
            ),
            InfoType.SQL_DBMS_NAME: "PostgreSQL",
            InfoType.SQL_DBMS_VER: "18.0.3",
            InfoType.SQL_DDL_INDEX: SQLDdlIndex.SQL_DI_CREATE_INDEX | SQLDdlIndex.SQL_DI_DROP_INDEX,
            InfoType.SQL_DEFAULT_TXN_ISOLATION: SQLTxnIsolationOption.SQL_TXN_READ_COMMITTED,
            InfoType.SQL_DESCRIBE_PARAMETER: "N",
            InfoType.SQL_DM_VER: "03.52.0002.0003",
            InfoType.SQL_DRIVER_AWARE_POOLING_SUPPORTED: ODBCError(
                what="SQLGetInfoW",
                sql_state="HYC00",
                native_error=209,
                message_text="Unrecognized key passed to PGAPI_GetInfo.",
                return_code=SQLReturn.SQL_ERROR,
            ),
            InfoType.SQL_DRIVER_HDBC: NotImplementedError("Unsupported InfoType: 3"),
            InfoType.SQL_DRIVER_HDESC: NotImplementedError("Unsupported InfoType: 135"),
            InfoType.SQL_DRIVER_HENV: NotImplementedError("Unsupported InfoType: 4"),
            InfoType.SQL_DRIVER_HLIB: NotImplementedError("Unsupported InfoType: 76"),
            InfoType.SQL_DRIVER_HSTMT: NotImplementedError("Unsupported InfoType: 5"),
            InfoType.SQL_DRIVER_NAME: "psqlodbcw.so",
            InfoType.SQL_DRIVER_ODBC_VER: "03.51",
            InfoType.SQL_DRIVER_VER: "17.00.0004",
            InfoType.SQL_DROP_ASSERTION: SQLDropAssertion(0),
            InfoType.SQL_DROP_CHARACTER_SET: SQLDropCharacterSet(0),
            InfoType.SQL_DROP_COLLATION: SQLDropCollation(0),
            InfoType.SQL_DROP_DOMAIN: SQLDropDomain(0),
            InfoType.SQL_DROP_SCHEMA: SQLDropSchema.SQL_DS_CASCADE
            | SQLDropSchema.SQL_DS_RESTRICT
            | SQLDropSchema.SQL_DS_DROP_SCHEMA,
            InfoType.SQL_DROP_TABLE: SQLDropTable.SQL_DT_CASCADE
            | SQLDropTable.SQL_DT_RESTRICT
            | SQLDropTable.SQL_DT_DROP_TABLE,
            InfoType.SQL_DROP_TRANSLATION: SQLDropTranslation(0),
            InfoType.SQL_DROP_VIEW: SQLDropView.SQL_DV_CASCADE
            | SQLDropView.SQL_DV_RESTRICT
            | SQLDropView.SQL_DV_DROP_VIEW,
            InfoType.SQL_DYNAMIC_CURSOR_ATTRIBUTES1: SQLCursorAttributes1(0),
            InfoType.SQL_DYNAMIC_CURSOR_ATTRIBUTES2: SQLCursorAttributes2(0),
            InfoType.SQL_EXPRESSIONS_IN_ORDERBY: "Y",
            InfoType.SQL_FETCH_DIRECTION: NotImplementedError("Unsupported InfoType: 8"),
            InfoType.SQL_FILE_USAGE: SQLFileUsage.SQL_FILE_NOT_SUPPORTED,
            InfoType.SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES1: SQLCursorAttributes1.SQL_CA1_NEXT,
            InfoType.SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES2: SQLCursorAttributes2.SQL_CA2_READ_ONLY_CONCURRENCY
            | SQLCursorAttributes2.SQL_CA2_CRC_EXACT,
            InfoType.SQL_GETDATA_EXTENSIONS: SQLGetDataExtensions.SQL_GD_ANY_COLUMN
            | SQLGetDataExtensions.SQL_GD_ANY_ORDER
            | SQLGetDataExtensions.SQL_GD_BLOCK
            | SQLGetDataExtensions.SQL_GD_BOUND,
            InfoType.SQL_GROUP_BY: SQLGroupBy.SQL_GB_GROUP_BY_EQUALS_SELECT,
            InfoType.SQL_IDENTIFIER_CASE: SQLIdentifierCase.SQL_IC_LOWER,
            InfoType.SQL_IDENTIFIER_QUOTE_CHAR: '"',
            InfoType.SQL_INDEX_KEYWORDS: SQLIndexKeywords.SQL_IK_NONE,
            InfoType.SQL_INFO_SCHEMA_VIEWS: SQLInfoSchemaViews(0),
            InfoType.SQL_INSERT_STATEMENT: SQLInsertStatement.SQL_IS_INSERT_LITERALS
            | SQLInsertStatement.SQL_IS_INSERT_SEARCHED
            | SQLInsertStatement.SQL_IS_SELECT_INTO,
            InfoType.SQL_INTEGRITY: "N",
            InfoType.SQL_KEYSET_CURSOR_ATTRIBUTES1: SQLCursorAttributes1.SQL_CA1_NEXT
            | SQLCursorAttributes1.SQL_CA1_ABSOLUTE
            | SQLCursorAttributes1.SQL_CA1_RELATIVE
            | SQLCursorAttributes1.SQL_CA1_BOOKMARK
            | SQLCursorAttributes1.SQL_CA1_LOCK_NO_CHANGE
            | SQLCursorAttributes1.SQL_CA1_POS_POSITION
            | SQLCursorAttributes1.SQL_CA1_POS_UPDATE
            | SQLCursorAttributes1.SQL_CA1_POS_DELETE
            | SQLCursorAttributes1.SQL_CA1_POS_REFRESH,
            InfoType.SQL_KEYSET_CURSOR_ATTRIBUTES2: SQLCursorAttributes2.SQL_CA2_READ_ONLY_CONCURRENCY
            | SQLCursorAttributes2.SQL_CA2_OPT_ROWVER_CONCURRENCY
            | SQLCursorAttributes2.SQL_CA2_SENSITIVITY_ADDITIONS
            | SQLCursorAttributes2.SQL_CA2_SENSITIVITY_DELETIONS
            | SQLCursorAttributes2.SQL_CA2_SENSITIVITY_UPDATES
            | SQLCursorAttributes2.SQL_CA2_CRC_EXACT,
            InfoType.SQL_KEYWORDS: "",
            InfoType.SQL_LIKE_ESCAPE_CLAUSE: "Y",
            InfoType.SQL_LOCK_TYPES: NotImplementedError("Unsupported InfoType: 78"),
            InfoType.SQL_MAX_ASYNC_CONCURRENT_STATEMENTS: ODBCError(
                what="SQLGetInfoW",
                sql_state="HYC00",
                native_error=209,
                message_text="Unrecognized key passed to PGAPI_GetInfo.",
                return_code=SQLReturn.SQL_ERROR,
            ),
            InfoType.SQL_MAX_BINARY_LITERAL_LEN: 0,
            InfoType.SQL_MAX_CATALOG_NAME_LEN: 0,
            InfoType.SQL_MAX_CHAR_LITERAL_LEN: 0,
            InfoType.SQL_MAX_COLUMNS_IN_GROUP_BY: 0,
            InfoType.SQL_MAX_COLUMNS_IN_INDEX: 0,
            InfoType.SQL_MAX_COLUMNS_IN_ORDER_BY: 0,
            InfoType.SQL_MAX_COLUMNS_IN_SELECT: 0,
            InfoType.SQL_MAX_COLUMNS_IN_TABLE: 0,
            InfoType.SQL_MAX_COLUMN_NAME_LEN: 63,
            InfoType.SQL_MAX_CONCURRENT_ACTIVITIES: 0,
            InfoType.SQL_MAX_CURSOR_NAME_LEN: 32,
            InfoType.SQL_MAX_DRIVER_CONNECTIONS: 0,
            InfoType.SQL_MAX_IDENTIFIER_LEN: 63,
            InfoType.SQL_MAX_INDEX_SIZE: 0,
            InfoType.SQL_MAX_PROCEDURE_NAME_LEN: 0,
            InfoType.SQL_MAX_ROW_SIZE: 0,
            InfoType.SQL_MAX_ROW_SIZE_INCLUDES_LONG: "Y",
            InfoType.SQL_MAX_SCHEMA_NAME_LEN: 63,
            InfoType.SQL_MAX_STATEMENT_LEN: 0,
            InfoType.SQL_MAX_TABLES_IN_SELECT: 0,
            InfoType.SQL_MAX_TABLE_NAME_LEN: 63,
            InfoType.SQL_MAX_USER_NAME_LEN: 0,
            InfoType.SQL_MULTIPLE_ACTIVE_TXN: "Y",
            InfoType.SQL_MULT_RESULT_SETS: "Y",
            InfoType.SQL_NEED_LONG_DATA_LEN: "N",
            InfoType.SQL_NON_NULLABLE_COLUMNS: SQLNonNullableColumns.SQL_NNC_NON_NULL,
            InfoType.SQL_NULL_COLLATION: SQLNullCollation.SQL_NC_HIGH,
            InfoType.SQL_NUMERIC_FUNCTIONS: SQLNumericFunctions.SQL_FN_NUM_ABS
            | SQLNumericFunctions.SQL_FN_NUM_ACOS
            | SQLNumericFunctions.SQL_FN_NUM_ASIN
            | SQLNumericFunctions.SQL_FN_NUM_ATAN
            | SQLNumericFunctions.SQL_FN_NUM_ATAN2
            | SQLNumericFunctions.SQL_FN_NUM_CEILING
            | SQLNumericFunctions.SQL_FN_NUM_COS
            | SQLNumericFunctions.SQL_FN_NUM_COT
            | SQLNumericFunctions.SQL_FN_NUM_EXP
            | SQLNumericFunctions.SQL_FN_NUM_FLOOR
            | SQLNumericFunctions.SQL_FN_NUM_LOG
            | SQLNumericFunctions.SQL_FN_NUM_MOD
            | SQLNumericFunctions.SQL_FN_NUM_SIGN
            | SQLNumericFunctions.SQL_FN_NUM_SIN
            | SQLNumericFunctions.SQL_FN_NUM_SQRT
            | SQLNumericFunctions.SQL_FN_NUM_TAN,
            InfoType.SQL_ODBC_API_CONFORMANCE: NotImplementedError("Unsupported InfoType: 9"),
            InfoType.SQL_ODBC_INTERFACE_CONFORMANCE: SQLOdbcInterfaceConformance.SQL_OIC_CORE,
            InfoType.SQL_ODBC_SAG_CLI_CONFORMANCE: SQLOdbcSagCliConformance.SQL_OSCC_NOT_COMPLIANT,
            InfoType.SQL_ODBC_SQL_CONFORMANCE: SQLOdbcSqlConformance.SQL_OSC_CORE,
            InfoType.SQL_ODBC_VER: "03.52",
            InfoType.SQL_OJ_CAPABILITIES: SQLOuterJoinCapabilities.SQL_OJ_ALL_COMPARISON_OPS
            | SQLOuterJoinCapabilities.SQL_OJ_INNER
            | SQLOuterJoinCapabilities.SQL_OJ_NOT_ORDERED
            | SQLOuterJoinCapabilities.SQL_OJ_NESTED
            | SQLOuterJoinCapabilities.SQL_OJ_FULL
            | SQLOuterJoinCapabilities.SQL_OJ_RIGHT
            | SQLOuterJoinCapabilities.SQL_OJ_LEFT,
            InfoType.SQL_ORDER_BY_COLUMNS_IN_SELECT: "Y",
            InfoType.SQL_OUTER_JOINS: SQLOuterJoins.YES,
            InfoType.SQL_PARAM_ARRAY_ROW_COUNTS: SQLParamArrayRowCounts.SQL_PARC_BATCH,
            InfoType.SQL_PARAM_ARRAY_SELECTS: SQLParamArraySelects.SQL_PAS_BATCH,
            InfoType.SQL_POSITIONED_STATEMENTS: NotImplementedError("Unsupported InfoType: 80"),
            InfoType.SQL_POS_OPERATIONS: NotImplementedError("Unsupported InfoType: 79"),
            InfoType.SQL_PROCEDURES: "Y",
            InfoType.SQL_PROCEDURE_TERM: "procedure",
            InfoType.SQL_QUOTED_IDENTIFIER_CASE: SQLIdentifierCase.SQL_IC_SENSITIVE,
            InfoType.SQL_ROW_UPDATES: "Y",
            InfoType.SQL_SCHEMA_TERM: "schema",
            InfoType.SQL_SCHEMA_USAGE: SQLSchemaUsage.SQL_SU_DML_STATEMENTS
            | SQLSchemaUsage.SQL_SU_TABLE_DEFINITION
            | SQLSchemaUsage.SQL_SU_INDEX_DEFINITION
            | SQLSchemaUsage.SQL_SU_PRIVILEGE_DEFINITION,
            InfoType.SQL_SCROLL_CONCURRENCY: SQLScrollConcurrency.SQL_SCCO_READ_ONLY
            | SQLScrollConcurrency.SQL_SCCO_OPT_ROWVER,
            InfoType.SQL_SCROLL_OPTIONS: SQLScrollOptions.SQL_SO_FORWARD_ONLY
            | SQLScrollOptions.SQL_SO_KEYSET_DRIVEN
            | SQLScrollOptions.SQL_SO_STATIC,
            InfoType.SQL_SEARCH_PATTERN_ESCAPE: "\\",
            InfoType.SQL_SERVER_NAME: "postgresql",
            InfoType.SQL_SPECIAL_CHARACTERS: "_",
            InfoType.SQL_SQL92_DATETIME_FUNCTIONS: SQLSql92DatetimeFunctions.SQL_SDF_CURRENT_DATE
            | SQLSql92DatetimeFunctions.SQL_SDF_CURRENT_TIME
            | SQLSql92DatetimeFunctions.SQL_SDF_CURRENT_TIMESTAMP,
            InfoType.SQL_SQL92_FOREIGN_KEY_DELETE_RULE: SQLSql92ForeignKeyDeleteRule.SQL_SFKD_CASCADE
            | SQLSql92ForeignKeyDeleteRule.SQL_SFKD_NO_ACTION
            | SQLSql92ForeignKeyDeleteRule.SQL_SFKD_SET_DEFAULT
            | SQLSql92ForeignKeyDeleteRule.SQL_SFKD_SET_NULL,
            InfoType.SQL_SQL92_FOREIGN_KEY_UPDATE_RULE: SQLSql92ForeignKeyUpdateRule.SQL_SFKD_CASCADE
            | SQLSql92ForeignKeyUpdateRule.SQL_SFKD_NO_ACTION
            | SQLSql92ForeignKeyUpdateRule.SQL_SFKD_SET_DEFAULT
            | SQLSql92ForeignKeyUpdateRule.SQL_SFKD_SET_NULL,
            InfoType.SQL_SQL92_GRANT: SQLSql92Grant.SQL_SG_DELETE_TABLE
            | SQLSql92Grant.SQL_SG_INSERT_TABLE
            | SQLSql92Grant.SQL_SG_REFERENCES_TABLE
            | SQLSql92Grant.SQL_SG_SELECT_TABLE
            | SQLSql92Grant.SQL_SG_UPDATE_TABLE,
            InfoType.SQL_SQL92_NUMERIC_VALUE_FUNCTIONS: SQLSql92NumericValueFunctions.SQL_SNVF_BIT_LENGTH
            | SQLSql92NumericValueFunctions.SQL_SNVF_CHAR_LENGTH
            | SQLSql92NumericValueFunctions.SQL_SNVF_CHARACTER_LENGTH
            | SQLSql92NumericValueFunctions.SQL_SNVF_EXTRACT
            | SQLSql92NumericValueFunctions.SQL_SNVF_OCTET_LENGTH
            | SQLSql92NumericValueFunctions.SQL_SNVF_POSITION,
            InfoType.SQL_SQL92_PREDICATES: SQLSql92Predicates.SQL_SP_EXISTS
            | SQLSql92Predicates.SQL_SP_ISNOTNULL
            | SQLSql92Predicates.SQL_SP_ISNULL
            | SQLSql92Predicates.SQL_SP_OVERLAPS
            | SQLSql92Predicates.SQL_SP_LIKE
            | SQLSql92Predicates.SQL_SP_IN
            | SQLSql92Predicates.SQL_SP_BETWEEN
            | SQLSql92Predicates.SQL_SP_COMPARISON
            | SQLSql92Predicates.SQL_SP_QUANTIFIED_COMPARISON,
            InfoType.SQL_SQL92_RELATIONAL_JOIN_OPERATORS: SQLSql92RelationalJoinOperators.SQL_SRJO_CROSS_JOIN
            | SQLSql92RelationalJoinOperators.SQL_SRJO_EXCEPT_JOIN
            | SQLSql92RelationalJoinOperators.SQL_SRJO_FULL_OUTER_JOIN
            | SQLSql92RelationalJoinOperators.SQL_SRJO_INNER_JOIN
            | SQLSql92RelationalJoinOperators.SQL_SRJO_INTERSECT_JOIN
            | SQLSql92RelationalJoinOperators.SQL_SRJO_LEFT_OUTER_JOIN
            | SQLSql92RelationalJoinOperators.SQL_SRJO_NATURAL_JOIN
            | SQLSql92RelationalJoinOperators.SQL_SRJO_RIGHT_OUTER_JOIN
            | SQLSql92RelationalJoinOperators.SQL_SRJO_UNION_JOIN,
            InfoType.SQL_SQL92_REVOKE: SQLSql92Revoke.SQL_SR_DELETE_TABLE
            | SQLSql92Revoke.SQL_SR_INSERT_TABLE
            | SQLSql92Revoke.SQL_SR_REFERENCES_TABLE
            | SQLSql92Revoke.SQL_SR_SELECT_TABLE
            | SQLSql92Revoke.SQL_SR_UPDATE_TABLE,
            InfoType.SQL_SQL92_ROW_VALUE_CONSTRUCTOR: SQLSql92RowValueConstructor.SQL_SRVC_VALUE_EXPRESSION
            | SQLSql92RowValueConstructor.SQL_SRVC_NULL,
            InfoType.SQL_SQL92_STRING_FUNCTIONS: SQLSql92StringFunctions.SQL_SSF_TRIM_TRAILING
            | SQLSql92StringFunctions.SQL_SSF_TRIM_LEADING
            | SQLSql92StringFunctions.SQL_SSF_TRIM_BOTH
            | SQLSql92StringFunctions.SQL_SSF_TRANSLATE
            | SQLSql92StringFunctions.SQL_SSF_SUBSTRING
            | SQLSql92StringFunctions.SQL_SSF_UPPER
            | SQLSql92StringFunctions.SQL_SSF_LOWER
            | SQLSql92StringFunctions.SQL_SSF_CONVERT,
            InfoType.SQL_SQL92_VALUE_EXPRESSIONS: SQLSql92ValueExpressions.SQL_SVE_NULLIF
            | SQLSql92ValueExpressions.SQL_SVE_COALESCE
            | SQLSql92ValueExpressions.SQL_SVE_CAST
            | SQLSql92ValueExpressions.SQL_SVE_CASE,
            InfoType.SQL_SQL_CONFORMANCE: SQLSqlConformance.SQL_SC_SQL92_ENTRY,
            InfoType.SQL_STANDARD_CLI_CONFORMANCE: ODBCError(
                what="SQLGetInfoW",
                sql_state="HYC00",
                native_error=209,
                message_text="Unrecognized key passed to PGAPI_GetInfo.",
                return_code=SQLReturn.SQL_ERROR,
            ),
            InfoType.SQL_STATIC_CURSOR_ATTRIBUTES1: SQLCursorAttributes1.SQL_CA1_NEXT
            | SQLCursorAttributes1.SQL_CA1_ABSOLUTE
            | SQLCursorAttributes1.SQL_CA1_RELATIVE
            | SQLCursorAttributes1.SQL_CA1_BOOKMARK
            | SQLCursorAttributes1.SQL_CA1_LOCK_NO_CHANGE
            | SQLCursorAttributes1.SQL_CA1_POS_POSITION
            | SQLCursorAttributes1.SQL_CA1_POS_UPDATE
            | SQLCursorAttributes1.SQL_CA1_POS_DELETE
            | SQLCursorAttributes1.SQL_CA1_POS_REFRESH,
            InfoType.SQL_STATIC_CURSOR_ATTRIBUTES2: SQLCursorAttributes2.SQL_CA2_READ_ONLY_CONCURRENCY
            | SQLCursorAttributes2.SQL_CA2_OPT_ROWVER_CONCURRENCY
            | SQLCursorAttributes2.SQL_CA2_SENSITIVITY_ADDITIONS
            | SQLCursorAttributes2.SQL_CA2_SENSITIVITY_DELETIONS
            | SQLCursorAttributes2.SQL_CA2_SENSITIVITY_UPDATES
            | SQLCursorAttributes2.SQL_CA2_CRC_EXACT,
            InfoType.SQL_STATIC_SENSITIVITY: NotImplementedError("Unsupported InfoType: 83"),
            InfoType.SQL_STRING_FUNCTIONS: SQLStringFunctions.SQL_FN_STR_CONCAT
            | SQLStringFunctions.SQL_FN_STR_INSERT
            | SQLStringFunctions.SQL_FN_STR_LEFT
            | SQLStringFunctions.SQL_FN_STR_LTRIM
            | SQLStringFunctions.SQL_FN_STR_LENGTH
            | SQLStringFunctions.SQL_FN_STR_LOCATE
            | SQLStringFunctions.SQL_FN_STR_LCASE
            | SQLStringFunctions.SQL_FN_STR_REPEAT
            | SQLStringFunctions.SQL_FN_STR_RIGHT
            | SQLStringFunctions.SQL_FN_STR_RTRIM
            | SQLStringFunctions.SQL_FN_STR_SUBSTRING
            | SQLStringFunctions.SQL_FN_STR_UCASE
            | SQLStringFunctions.SQL_FN_STR_ASCII
            | SQLStringFunctions.SQL_FN_STR_CHAR,
            InfoType.SQL_SUBQUERIES: SQLSubqueries.SQL_SQ_COMPARISON
            | SQLSubqueries.SQL_SQ_EXISTS
            | SQLSubqueries.SQL_SQ_IN
            | SQLSubqueries.SQL_SQ_QUANTIFIED,
            InfoType.SQL_SYSTEM_FUNCTIONS: SQLSystemFunctions.SQL_FN_SYS_DBNAME
            | SQLSystemFunctions.SQL_FN_SYS_USERNAME,
            InfoType.SQL_TABLE_TERM: "table",
            InfoType.SQL_TIMEDATE_ADD_INTERVALS: SQLTimestampIntervals.SQL_FN_TSI_FRAC_SECOND
            | SQLTimestampIntervals.SQL_FN_TSI_SECOND
            | SQLTimestampIntervals.SQL_FN_TSI_MINUTE
            | SQLTimestampIntervals.SQL_FN_TSI_HOUR
            | SQLTimestampIntervals.SQL_FN_TSI_DAY
            | SQLTimestampIntervals.SQL_FN_TSI_WEEK
            | SQLTimestampIntervals.SQL_FN_TSI_MONTH
            | SQLTimestampIntervals.SQL_FN_TSI_YEAR,
            InfoType.SQL_TIMEDATE_DIFF_INTERVALS: SQLTimestampIntervals.SQL_FN_TSI_SECOND
            | SQLTimestampIntervals.SQL_FN_TSI_MINUTE
            | SQLTimestampIntervals.SQL_FN_TSI_HOUR
            | SQLTimestampIntervals.SQL_FN_TSI_DAY,
            InfoType.SQL_TIMEDATE_FUNCTIONS: SQLTimeDateFunctions.SQL_FN_TD_NOW
            | SQLTimeDateFunctions.SQL_FN_TD_CURDATE
            | SQLTimeDateFunctions.SQL_FN_TD_DAYOFMONTH
            | SQLTimeDateFunctions.SQL_FN_TD_DAYOFWEEK
            | SQLTimeDateFunctions.SQL_FN_TD_DAYOFYEAR
            | SQLTimeDateFunctions.SQL_FN_TD_MONTH
            | SQLTimeDateFunctions.SQL_FN_TD_QUARTER
            | SQLTimeDateFunctions.SQL_FN_TD_WEEK
            | SQLTimeDateFunctions.SQL_FN_TD_YEAR
            | SQLTimeDateFunctions.SQL_FN_TD_CURTIME
            | SQLTimeDateFunctions.SQL_FN_TD_HOUR
            | SQLTimeDateFunctions.SQL_FN_TD_MINUTE
            | SQLTimeDateFunctions.SQL_FN_TD_SECOND
            | SQLTimeDateFunctions.SQL_FN_TD_TIMESTAMPADD
            | SQLTimeDateFunctions.SQL_FN_TD_TIMESTAMPDIFF
            | SQLTimeDateFunctions.SQL_FN_TD_DAYNAME,
            InfoType.SQL_TXN_CAPABLE: SQLTxnCapable.SQL_TC_ALL,
            InfoType.SQL_TXN_ISOLATION_OPTION: SQLTxnIsolationOption.SQL_TXN_READ_UNCOMMITTED
            | SQLTxnIsolationOption.SQL_TXN_READ_COMMITTED
            | SQLTxnIsolationOption.SQL_TXN_REPEATABLE_READ
            | SQLTxnIsolationOption.SQL_TXN_SERIALIZABLE,
            InfoType.SQL_UNION: SQLUnion.SQL_U_UNION | SQLUnion.SQL_U_UNION_ALL,
            InfoType.SQL_USER_NAME: "sa",
            InfoType.SQL_XOPEN_CLI_YEAR: "1994",
        }

    @property
    def expected_sql_get_type_info_w_return_values(self) -> Mapping[SQLDataType, list[dict[str, Any]]]:
        return {
            SQLDataType.SQL_BIGINT: [
                {
                    "TYPE_NAME": "int8",
                    "DATA_TYPE": SQLDataType.SQL_BIGINT,
                    "COLUMN_SIZE": 19,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": -5,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_BINARY: [],
            SQLDataType.SQL_BIT: [
                {
                    "TYPE_NAME": "bool",
                    "DATA_TYPE": SQLDataType.SQL_BIT,
                    "COLUMN_SIZE": 5,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 12,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_CHAR: [
                {
                    "TYPE_NAME": "char",
                    "DATA_TYPE": SQLDataType.SQL_CHAR,
                    "COLUMN_SIZE": 255,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": "max. length",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -8,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_DATETIME: [
                {
                    "TYPE_NAME": "date",
                    "DATA_TYPE": SQLDataType.SQL_DATETIME,
                    "COLUMN_SIZE": 10,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_CHAR,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_DECIMAL: [
                {
                    "TYPE_NAME": "numeric",
                    "DATA_TYPE": SQLDataType.SQL_DECIMAL,
                    "COLUMN_SIZE": 28,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": "precision, scale",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 6,
                    "SQL_DATA_TYPE": 2,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_DOUBLE: [
                {
                    "TYPE_NAME": "float8",
                    "DATA_TYPE": SQLDataType.SQL_DOUBLE,
                    "COLUMN_SIZE": 17,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 6,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_FLOAT: [
                {
                    "TYPE_NAME": "float8",
                    "DATA_TYPE": SQLDataType.SQL_FLOAT,
                    "COLUMN_SIZE": 17,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 6,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_GUID: [
                {
                    "TYPE_NAME": "uuid",
                    "DATA_TYPE": SQLDataType.SQL_GUID,
                    "COLUMN_SIZE": 37,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -11,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_INTEGER: [
                {
                    "TYPE_NAME": "int4",
                    "DATA_TYPE": SQLDataType.SQL_INTEGER,
                    "COLUMN_SIZE": 10,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 4,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_INTERVAL: [
                {
                    "TYPE_NAME": "time",
                    "DATA_TYPE": SQLDataType.SQL_INTERVAL,
                    "COLUMN_SIZE": 8,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_NUMERIC,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_LONGVARBINARY: [
                {
                    "TYPE_NAME": "bytea",
                    "DATA_TYPE": SQLDataType.SQL_LONGVARBINARY,
                    "COLUMN_SIZE": -4,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -4,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_LONGVARCHAR: [
                {
                    "TYPE_NAME": "text",
                    "DATA_TYPE": SQLDataType.SQL_LONGVARCHAR,
                    "COLUMN_SIZE": 8190,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -10,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_NUMERIC: [
                {
                    "TYPE_NAME": "numeric",
                    "DATA_TYPE": SQLDataType.SQL_NUMERIC,
                    "COLUMN_SIZE": 28,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": "precision, scale",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 6,
                    "SQL_DATA_TYPE": 2,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_REAL: [
                {
                    "TYPE_NAME": "float4",
                    "DATA_TYPE": SQLDataType.SQL_REAL,
                    "COLUMN_SIZE": 9,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 7,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_SMALLINT: [
                {
                    "TYPE_NAME": "int2",
                    "DATA_TYPE": SQLDataType.SQL_SMALLINT,
                    "COLUMN_SIZE": 5,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 5,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_SS_TABLE: [],
            SQLDataType.SQL_SS_TIME2: [],
            SQLDataType.SQL_SS_TIMESTAMPOFFSET: [],
            SQLDataType.SQL_SS_UDT: [],
            SQLDataType.SQL_SS_VARIANT: [],
            SQLDataType.SQL_SS_XML: [],
            SQLDataType.SQL_TIMESTAMP: [
                {
                    "TYPE_NAME": "timestamptz",
                    "DATA_TYPE": SQLDataType.SQL_TIMESTAMP,
                    "COLUMN_SIZE": 26,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 38,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_DECIMAL,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_TINYINT: [
                {
                    "TYPE_NAME": "int2",
                    "DATA_TYPE": SQLDataType.SQL_TINYINT,
                    "COLUMN_SIZE": 5,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 5,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_TYPE_DATE: [
                {
                    "TYPE_NAME": "date",
                    "DATA_TYPE": SQLDataType.SQL_TYPE_DATE,
                    "COLUMN_SIZE": 10,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_CHAR,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_TYPE_TIME: [
                {
                    "TYPE_NAME": "time",
                    "DATA_TYPE": SQLDataType.SQL_TYPE_TIME,
                    "COLUMN_SIZE": 8,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_NUMERIC,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_TYPE_TIME_WITH_TIMEZONE: [],
            SQLDataType.SQL_TYPE_TIMESTAMP: [
                {
                    "TYPE_NAME": "timestamptz",
                    "DATA_TYPE": SQLDataType.SQL_TYPE_TIMESTAMP,
                    "COLUMN_SIZE": 26,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 38,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_DECIMAL,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_TYPE_TIMESTAMP_WITH_TIMEZONE: [],
            SQLDataType.SQL_UNKNOWN_TYPE: [
                {
                    "TYPE_NAME": "int8",
                    "DATA_TYPE": SQLDataType.SQL_BIGINT,
                    "COLUMN_SIZE": 19,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": -5,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "bool",
                    "DATA_TYPE": SQLDataType.SQL_BIT,
                    "COLUMN_SIZE": 5,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 12,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "char",
                    "DATA_TYPE": SQLDataType.SQL_CHAR,
                    "COLUMN_SIZE": 255,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": "max. length",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -8,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "date",
                    "DATA_TYPE": SQLDataType.SQL_TYPE_DATE,
                    "COLUMN_SIZE": 10,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_CHAR,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "date",
                    "DATA_TYPE": SQLDataType.SQL_DATETIME,
                    "COLUMN_SIZE": 10,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_CHAR,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "numeric",
                    "DATA_TYPE": SQLDataType.SQL_DECIMAL,
                    "COLUMN_SIZE": 28,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": "precision, scale",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 6,
                    "SQL_DATA_TYPE": 2,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "float8",
                    "DATA_TYPE": SQLDataType.SQL_DOUBLE,
                    "COLUMN_SIZE": 17,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 6,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "float8",
                    "DATA_TYPE": SQLDataType.SQL_FLOAT,
                    "COLUMN_SIZE": 17,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 6,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "int4",
                    "DATA_TYPE": SQLDataType.SQL_INTEGER,
                    "COLUMN_SIZE": 10,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 4,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "bytea",
                    "DATA_TYPE": SQLDataType.SQL_LONGVARBINARY,
                    "COLUMN_SIZE": -4,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -4,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "text",
                    "DATA_TYPE": SQLDataType.SQL_LONGVARCHAR,
                    "COLUMN_SIZE": 8190,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -10,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "numeric",
                    "DATA_TYPE": SQLDataType.SQL_NUMERIC,
                    "COLUMN_SIZE": 28,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": "precision, scale",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 6,
                    "SQL_DATA_TYPE": 2,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "float4",
                    "DATA_TYPE": SQLDataType.SQL_REAL,
                    "COLUMN_SIZE": 9,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 7,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "int2",
                    "DATA_TYPE": SQLDataType.SQL_SMALLINT,
                    "COLUMN_SIZE": 5,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 5,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "time",
                    "DATA_TYPE": SQLDataType.SQL_TYPE_TIME,
                    "COLUMN_SIZE": 8,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_NUMERIC,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "timestamptz",
                    "DATA_TYPE": SQLDataType.SQL_TYPE_TIMESTAMP,
                    "COLUMN_SIZE": 26,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 38,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_DECIMAL,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "time",
                    "DATA_TYPE": SQLDataType.SQL_INTERVAL,
                    "COLUMN_SIZE": 8,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_NUMERIC,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "timestamptz",
                    "DATA_TYPE": SQLDataType.SQL_TIMESTAMP,
                    "COLUMN_SIZE": 26,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 38,
                    "SQL_DATA_TYPE": 9,
                    "SQL_DATETIME_SUB": SQLDataType.SQL_DECIMAL,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "int2",
                    "DATA_TYPE": SQLDataType.SQL_TINYINT,
                    "COLUMN_SIZE": 5,
                    "LITERAL_PREFIX": None,
                    "LITERAL_SUFFIX": None,
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": 0,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": 0,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": 0,
                    "MAXIMUM_SCALE": 0,
                    "SQL_DATA_TYPE": 5,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": 10,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "bytea",
                    "DATA_TYPE": SQLDataType.SQL_VARBINARY,
                    "COLUMN_SIZE": -4,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -4,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "varchar",
                    "DATA_TYPE": SQLDataType.SQL_VARCHAR,
                    "COLUMN_SIZE": 255,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": "max. length",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -9,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "char",
                    "DATA_TYPE": SQLDataType.SQL_WCHAR,
                    "COLUMN_SIZE": 255,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": "max. length",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -8,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "varchar",
                    "DATA_TYPE": SQLDataType.SQL_WVARCHAR,
                    "COLUMN_SIZE": 255,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": "max. length",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -9,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "text",
                    "DATA_TYPE": SQLDataType.SQL_WLONGVARCHAR,
                    "COLUMN_SIZE": 8190,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -10,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
                {
                    "TYPE_NAME": "uuid",
                    "DATA_TYPE": SQLDataType.SQL_GUID,
                    "COLUMN_SIZE": 37,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -11,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                },
            ],
            SQLDataType.SQL_VARBINARY: [
                {
                    "TYPE_NAME": "bytea",
                    "DATA_TYPE": SQLDataType.SQL_VARBINARY,
                    "COLUMN_SIZE": -4,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 0,
                    "SEARCHABLE": 2,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -4,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_VARCHAR: [
                {
                    "TYPE_NAME": "varchar",
                    "DATA_TYPE": SQLDataType.SQL_VARCHAR,
                    "COLUMN_SIZE": 255,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": "max. length",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -9,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_WCHAR: [
                {
                    "TYPE_NAME": "char",
                    "DATA_TYPE": SQLDataType.SQL_WCHAR,
                    "COLUMN_SIZE": 255,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": "max. length",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -8,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_WLONGVARCHAR: [
                {
                    "TYPE_NAME": "text",
                    "DATA_TYPE": SQLDataType.SQL_WLONGVARCHAR,
                    "COLUMN_SIZE": 8190,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": None,
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -10,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
            SQLDataType.SQL_WVARCHAR: [
                {
                    "TYPE_NAME": "varchar",
                    "DATA_TYPE": SQLDataType.SQL_WVARCHAR,
                    "COLUMN_SIZE": 255,
                    "LITERAL_PREFIX": "'",
                    "LITERAL_SUFFIX": "'",
                    "CREATE_PARAMS": "max. length",
                    "NULLABLE": 1,
                    "CASE_SENSITIVE": 1,
                    "SEARCHABLE": 3,
                    "UNSIGNED_ATTRIBUTE": None,
                    "FIXED_PREC_SCALE": 0,
                    "AUTO_UNIQUE_VALUE": None,
                    "LOCAL_TYPE_NAME": None,
                    "MINIMUM_SCALE": None,
                    "MAXIMUM_SCALE": None,
                    "SQL_DATA_TYPE": -9,
                    "SQL_DATETIME_SUB": None,
                    "NUM_PREC_RADIX": None,
                    "INTERVAL_PRECISION": 0,
                }
            ],
        }
