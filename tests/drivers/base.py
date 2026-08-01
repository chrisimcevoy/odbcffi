from abc import ABC, abstractmethod
from collections.abc import Mapping
from contextlib import nullcontext
from typing import Any

import pytest

from odbcffi.odbc.connection_handle import ConnectionHandle
from odbcffi.odbc.driver_manager import DriverManager
from odbcffi.odbc.enums import *
from odbcffi.odbc.statement_handle import StatementHandle


class DriverTest(ABC):
    """Base class for driver-specific tests.

    This base class contains the definition of each test method.

    Derived classes are only required to provide the expected return values for those tests, which are specific to a
    driver.
    """

    @property
    @abstractmethod
    def expected_sql_get_info_w_return_values(self) -> Mapping[InfoType, Any]:
        raise NotImplementedError

    @property
    @abstractmethod
    def expected_sql_get_type_info_w_return_values(self) -> Mapping[SQLDataType, list[dict[str, Any]] | Exception]:
        raise NotImplementedError

    @pytest.mark.parametrize("info_type", list(InfoType), ids=lambda x: x.name)
    def test_sql_get_info_w(
        self,
        module_scoped_open_connection_handle: ConnectionHandle,
        driver_manager: DriverManager,
        info_type: InfoType,
    ) -> None:

        expected = self.expected_sql_get_info_w_return_values[info_type]

        if callable(expected):
            # Allow pytest.skip() for unstable return values.
            expected()

        context = (
            pytest.raises(type(expected), check=lambda exc: str(exc) == str(expected))
            if isinstance(expected, Exception)
            else nullcontext()
        )

        with context:
            actual = driver_manager.sql_get_info_w(
                connection_handle=module_scoped_open_connection_handle,
                info_type=info_type,
            )

            assert actual == expected

    @pytest.mark.parametrize("data_type", list(SQLDataType), ids=lambda x: x.name)
    def test_sql_get_type_info_w(
        self, driver_manager: DriverManager, module_scoped_statement_handle: StatementHandle, data_type: SQLDataType
    ) -> None:

        expected = self.expected_sql_get_type_info_w_return_values[data_type]

        context = (
            pytest.raises(type(expected), check=lambda exc: str(exc) == str(expected))
            if isinstance(expected, Exception)
            else nullcontext()
        )

        with context:
            driver_manager.sql_get_type_info_w(statement_handle=module_scoped_statement_handle, data_type=data_type)

            num_cols = driver_manager.sql_num_result_cols(statement_handle=module_scoped_statement_handle)

            assert num_cols > 0

            column_descriptions = [
                driver_manager.sql_describe_col_w(statement_handle=module_scoped_statement_handle, column_number=i)
                for i in range(1, num_cols + 1)
            ]

            actual: list[dict[str, Any]] = []

            while driver_manager.sql_fetch(statement_handle=module_scoped_statement_handle):
                row: dict[str, Any | None] = {}

                for column_description in column_descriptions:
                    value = driver_manager.sql_get_data(
                        statement_handle=module_scoped_statement_handle,
                        col_or_param_num=column_description.column_number,
                        target_type=column_description.data_type.to_c_data_type(),
                    )

                    if (
                        column_description.column_name == "DATA_TYPE"
                        or column_description.column_name == "SQL_DATATYPE"
                    ):
                        value = SQLDataType(value)
                    elif column_description.column_name == "SQL_DATETIME_SUB":
                        if row["DATA_TYPE"] in (
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

                actual.append(row)

            assert actual == expected
