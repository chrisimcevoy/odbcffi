from typing import Any

from odbcffi.odbc.driver_manager import DriverManager
from odbcffi.odbc.statement_handle import StatementHandle


def get_result_set(driver_manager: DriverManager, statement_handle: StatementHandle) -> list[dict[str, Any]]:
    """Return the result set for a given statement handle.

    This method assumes there is only one result set.

    :param driver_manager: The DriverManager instance.
    :param statement_handle: The StatementHandle to retrieve the result set for.
    :return: The result set as a list of python dictionaries. Each dictionary represents a row in the result set, with
        keyed by column name.
    """

    results: list[dict[str, Any]] = []

    num_cols = driver_manager.sql_num_result_cols(statement_handle=statement_handle)

    if num_cols == 0:
        return results

    column_descriptions = [
        driver_manager.sql_describe_col_w(statement_handle=statement_handle, column_number=i)
        for i in range(1, num_cols + 1)
    ]

    while driver_manager.sql_fetch(statement_handle=statement_handle):
        row: dict[str, Any | None] = {}

        for column_description in column_descriptions:
            value = driver_manager.sql_get_data(
                statement_handle=statement_handle,
                col_or_param_num=column_description.column_number,
                target_type=column_description.data_type.to_c_data_type(),
            )

            row[column_description.column_name] = value

        results.append(row)

    return results
