"""Data structures used to represent result sets from Driver Manager calls."""

from dataclasses import dataclass


@dataclass(frozen=True)
class DriverInfo:
    """The description and attributes of a driver, as determined by the driver manager.

    Objects of this type are returned from ``DriverManager.sql_drivers_w``.
    """

    description: str
    attributes: dict[str, str]
