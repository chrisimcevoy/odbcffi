import os

import pytest


@pytest.fixture(scope="module")
def suffix() -> str | None:
    # Enable multi statements.
    # https://dev.mysql.com/doc/connector-odbc/en/connector-odbc-configuration-connection-parameters.html#codbc-dsn-option-flags
    return "OPTION=67108864"


@pytest.fixture(scope="module")
def connection_string(driver: str, suffix: str | None) -> str:
    host = os.environ.get("MYSQL_HOST", "localhost")

    conn_str = f"DRIVER={{{driver}}};PORT=3306;SERVER={host};UID=root;PWD=super-secret-password;"

    if suffix:
        conn_str += suffix

    return conn_str
