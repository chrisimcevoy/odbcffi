import os

import pytest


@pytest.fixture(scope="module")
def suffix() -> str | None:
    return None


@pytest.fixture(scope="module")
def connection_string(driver: str, suffix: str | None) -> str:
    host = os.environ.get("POSTGRESQL_HOST", "localhost")

    conn_str = f"DRIVER={{{driver}}};PORT=5432;SERVER={host};UID=sa;PWD=Password123;"

    if suffix:
        conn_str += suffix

    return conn_str
