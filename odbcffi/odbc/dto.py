"""Data structures used to represent result sets from Driver Manager calls."""

from dataclasses import dataclass

__all__ = ["ColumnDescription", "DriverInfo"]

from typing import Any

from odbcffi.odbc.enums import SQLDataType


@dataclass(frozen=True, slots=True)
class ColumnDescription:
    """The description of a column in a result set.

    Objects of this type are returned from ``DriverManager.sql_describe_col_w``.
    """

    column_number: int
    column_name: str
    data_type: SQLDataType
    column_size: int
    decimal_digits: int
    nullable: Any  # TODO: enum this


@dataclass(frozen=True, slots=True)
class DriverInfo:
    """The description and attributes of a driver, as determined by the driver manager.

    Objects of this type are returned from ``DriverManager.sql_drivers_w``.
    """

    description: str
    attributes: dict[str, str]
