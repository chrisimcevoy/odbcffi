from __future__ import annotations

import os
import platform
from dataclasses import dataclass
from typing import TYPE_CHECKING

import pytest

from odbcffi.odbc import ConnectionHandle, DriverManager, EnvironmentHandle

if TYPE_CHECKING:
    from collections.abc import Generator

PLATFORM = platform.system()

# These are set in docker-compose.yml.
# Default to localhost otherwise (e.g. in github actions).
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
POSTGRESQL_HOST = os.environ.get("POSTGRESQL_HOST", "localhost")
SQL_SERVER_HOST = os.environ.get("SQL_SERVER_HOST", "localhost")


@dataclass(frozen=True)
class ConnectionInfo:
    """Details about a connection used in the test suite."""

    dbms_name: str
    """The name of the DBMS.

    This should match the output of SQLGetInfoW called with SQL_DBMS_NAME.
    """

    driver: str
    """The ODBC driver to use."""

    host: str
    """The host to connect to."""

    port: int
    """The port to connect to."""

    username: str
    """The username to connect with."""

    password: str
    """The password to connect with."""

    suffix: str | None = None
    """An optional suffix to add to the connection string."""

    @property
    def connection_string(self) -> str:
        connection_str = (
            f"DRIVER={{{self.driver}}};PORT={self.port};SERVER={self.host};UID={self.username};PWD={self.password};"
        )
        if self.suffix is not None:
            connection_str += self.suffix
        return connection_str


@pytest.fixture(
    scope="session",
    params=[
        pytest.param(
            ConnectionInfo(
                dbms_name="Microsoft SQL Server",
                driver="ODBC Driver 17 for SQL Server",
                host=SQL_SERVER_HOST,
                port=1433,
                username="sa",
                password="Password123",  # noqa: S106
            ),
            id="msodbcsql17",
            marks=[
                pytest.mark.skipif(
                    os.getenv("SKIP_MSODBCSQL17", default=False),
                    reason="Skipped via environment variable",
                )
            ],
        ),
        pytest.param(
            ConnectionInfo(
                dbms_name="Microsoft SQL Server",
                driver="ODBC Driver 18 for SQL Server",
                host=SQL_SERVER_HOST,
                port=1433,
                username="sa",
                password="Password123",  # noqa: S106
                suffix="TrustServerCertificate=yes;",
            ),
            id="msodbcsql18",
            marks=[
                pytest.mark.skipif(
                    os.getenv("SKIP_MSODBCSQL18", default=False),
                    reason="Skipped via environment variable",
                )
            ],
        ),
        pytest.param(
            ConnectionInfo(
                dbms_name="Microsoft SQL Server",
                driver="SQL Server",
                host=SQL_SERVER_HOST,
                port=1433,
                username="sa",
                password="Password123",  # noqa: S106
            ),
            id="SQL Server (MDAC)",
            marks=[
                pytest.mark.skipif(
                    os.getenv("SKIP_MDAC", default=False),
                    reason="Skipped via environment variable",
                ),
                pytest.mark.skipif(
                    PLATFORM != "Windows",
                    reason=f"MDAC Driver not supported on {PLATFORM}.",
                ),
            ],
        ),
        pytest.param(
            ConnectionInfo(
                dbms_name="Microsoft SQL Server",
                driver="FreeTDS",
                host=SQL_SERVER_HOST,
                port=1433,
                username="sa",
                password="Password123",  # noqa: S106
            ),
            id="FreeTDS",
            marks=[
                pytest.mark.skipif(
                    os.getenv("SKIP_FREETDS", default=False),
                    reason="Skipped via environment variable",
                ),
                pytest.mark.skipif(
                    PLATFORM == "Windows",
                    reason="FreeTDS driver not supported on Windows.",
                ),
            ],
        ),
        pytest.param(
            ConnectionInfo(
                dbms_name="PostgreSQL",
                driver="PostgreSQL Unicode",
                host=POSTGRESQL_HOST,
                port=5432,
                username="sa",
                password="Password123",  # noqa: S106
            ),
            id="PgSQL Unicode",
            marks=[
                pytest.mark.skipif(
                    os.getenv("SKIP_PGSQL_W", default=False),
                    reason="Skipped via environment variable",
                ),
            ],
        ),
        pytest.param(
            ConnectionInfo(
                dbms_name="PostgreSQL",
                driver="PostgreSQL ANSI",
                host=POSTGRESQL_HOST,
                port=5432,
                username="sa",
                password="Password123",  # noqa: S106
            ),
            id="PgSQL ANSI",
            marks=[
                pytest.mark.skipif(
                    os.getenv("SKIP_PGSQL_A", default=False),
                    reason="Skipped via environment variable",
                ),
            ],
        ),
        pytest.param(
            ConnectionInfo(
                dbms_name="MySQL",
                driver="MySQL ODBC 9.3 Unicode Driver",
                host=MYSQL_HOST,
                port=3306,
                username="root",
                password="super-secret-password",  # noqa: S106
                # Enable multi statements.
                # https://dev.mysql.com/doc/connector-odbc/en/connector-odbc-configuration-connection-parameters.html#codbc-dsn-option-flags
                suffix="OPTION=67108864",
            ),
            id="MySQL Unicode",
            marks=[
                pytest.mark.skipif(
                    os.getenv("SKIP_MYSQL_W", default=False),
                    reason="Skipped via environment variable",
                ),
            ],
        ),
        pytest.param(
            ConnectionInfo(
                dbms_name="MySQL",
                driver="MySQL ODBC 9.3 ANSI Driver",
                host=MYSQL_HOST,
                port=3306,
                username="root",
                password="super-secret-password",  # noqa: S106
                suffix=(
                    # Enable multi statements.
                    # https://dev.mysql.com/doc/connector-odbc/en/connector-odbc-configuration-connection-parameters.html#codbc-dsn-option-flags
                    "OPTION=67108864"
                ),
            ),
            id="MySQL ANSI",
            marks=[
                pytest.mark.skipif(
                    os.getenv("SKIP_MYSQL_A", default=False),
                    reason="Skipped via environment variable",
                ),
            ],
        ),
    ],
)
def connection_info(
    request: pytest.FixtureRequest,
) -> ConnectionInfo:
    info = request.param
    assert isinstance(info, ConnectionInfo)
    return info


@pytest.fixture(scope="session")
def connection_string(connection_info: ConnectionInfo) -> str:
    return connection_info.connection_string


@pytest.fixture(scope="session")
def driver_manager() -> DriverManager:
    return DriverManager.autoload()


@pytest.fixture
def unixodbc_driver_manager() -> DriverManager:
    dm = DriverManager(driver_manager_lib_name="libodbc.so.2")
    assert dm.is_unixodbc, f"Expected unixODBC, got {dm.driver_manager_type} ({dm.driver_manager_lib_name})"
    return dm


@pytest.fixture(scope="session")
def environment_handle(driver_manager: DriverManager) -> Generator[EnvironmentHandle]:
    """An environment handle fixture, with the "session" pytest scope.

    Useful for making tests which do not mutate the environment state faster.
    """
    with EnvironmentHandle(driver_manager=driver_manager) as henv:
        yield henv


@pytest.fixture
def isolated_environment_handle(driver_manager: DriverManager) -> Generator[EnvironmentHandle]:
    """An environment handle fixture, with the default "function" pytest scope.

    Useful for tests which need to mutate the environment state.
    """
    with EnvironmentHandle(driver_manager=driver_manager) as henv:
        yield henv


@pytest.fixture(scope="session")
def connection_handle(
    environment_handle: EnvironmentHandle,
) -> Generator[ConnectionHandle]:
    """A connection handle fixture, with the "session" pytest scope.

    Useful for making tests which do not need to mutate the connection faster.
    """
    with ConnectionHandle(environment_handle=environment_handle) as hdbc:
        yield hdbc


@pytest.fixture
def isolated_connection_handle(
    environment_handle: EnvironmentHandle,
) -> Generator[ConnectionHandle]:
    """A connection handle fixture with the default "function" pytest scope.

    Useful for tests which need to mutate the connection state.
    """
    with ConnectionHandle(environment_handle=environment_handle) as hdbc:
        yield hdbc


@pytest.fixture(scope="session")
def open_connection_handle(
    environment_handle: EnvironmentHandle, connection_string: str
) -> Generator[ConnectionHandle]:
    """A connection handle that has already opened a connection, with the "session" pytest scope.

    Useful for making tests which do not mutate the connection state faster.
    """
    with ConnectionHandle(environment_handle=environment_handle) as hdbc:
        hdbc.open(connection_string=connection_string)
        yield hdbc


@pytest.fixture
def isolated_open_connection_handle(
    environment_handle: EnvironmentHandle, connection_string: str
) -> Generator[ConnectionHandle]:
    """A connection handle that has already opened a connection, with the default "function" pytest scope.

    Useful for tests which need to mutate the connection state.
    """
    with ConnectionHandle(environment_handle=environment_handle) as hdbc:
        hdbc.open(connection_string=connection_string)
        yield hdbc
