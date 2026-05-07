from tests.conftest import driver_manager

# odbcffi

A Python ODBC library implementing the DB-API 2.0 specification, built on cffi.

## Installation

```commandline
pip install odbcffi
```

## Usage

odbcffi offers two public APIs.

The higher-level API implements the [DB-API 2.0 specification](https://peps.python.org/pep-0249/) and will feel familiar to Python programmers who have developed database applications:

```python
import os

import odbcffi

CONNECTION_STRING = os.environ.get("CONNECTION_STRING")

connection: odbcffi.Connection = odbcffi.connect(CONNECTION_STRING)
cursor: odbcffi.Cursor = connection.cursor()
with cursor:
    cursor.execute("SELECT 1;")
    print(cursor.fetchone())
```

The lower-level API will feel more familiar to programmers who have [developed ODBC applications](https://learn.microsoft.com/en-us/sql/odbc/reference/develop-app/basic-odbc-application-steps):

```python
import os

from odbcffi import (
    ConnectionHandle,
    DriverManager,
    EnvironmentHandle,
    SQLAttrODBCVersion,
    StatementHandle,
)

CONNECTION_STRING = os.environ.get("CONNECTION_STRING")

driver_manager = DriverManager.autoload()

with EnvironmentHandle(driver_manager) as henv:  # SQLAllocHandle(ENV)
    henv.odbc_version = SQLAttrODBCVersion.SQL_OV_ODBC3  # SQLSetEnvAttr
    with ConnectionHandle(henv) as hdbc:  # SQLAllocHandle(DBC)
        hdbc.open(CONNECTION_STRING)  # SQLDriverConnect
        with StatementHandle(hdbc) as hstmt:  # SQLAllocHandle(STMT)
            ...
```
