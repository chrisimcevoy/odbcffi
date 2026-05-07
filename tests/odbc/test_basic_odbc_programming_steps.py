from odbcffi.odbc import (
    ConnectionHandle,
    DriverManager,
    EnvironmentHandle,
    SQLAttrAutocommit,
    SQLAttrODBCVersion,
    StatementHandle,
)


def test_basic_odbc_programming_steps(connection_string: str) -> None:
    """Loosely based on https://learn.microsoft.com/en-us/sql/odbc/reference/develop-app/basic-odbc-application-steps"""
    # Step 1: Connect to the Data Source
    #
    # The first step in any application is to connect to the data source.
    #
    # The first step in connecting to the data source is to load the Driver
    # Manager and allocate the environment handle with SQLAllocHandle.

    driver_manager = DriverManager.autoload()

    with EnvironmentHandle(driver_manager) as henv:
        # The application then registers the version of ODBC to which it
        # conforms by calling SQLSetEnvAttr with the SQL_ATTR_APP_ODBC_VER
        # environment attribute.
        henv.odbc_version = SQLAttrODBCVersion.SQL_OV_ODBC3

        # Next, the application allocates a connection handle with
        # SQLAllocHandle and connects to the data source with SQLConnect,
        # SQLDriverConnect, or SQLBrowseConnect.
        with ConnectionHandle(henv) as hdbc:
            hdbc.open(connection_string)

            # The application then sets any connection attributes, such as
            # whether to manually commit transactions.
            hdbc.autocommit = SQLAttrAutocommit.SQL_AUTOCOMMIT_ON

            # Step 2: Initialize the Application
            #
            # The second step is to initialize the application. Exactly what
            # is done here varies with the application.

            # At this point, it is common to use SQLGetInfo to discover the
            # capabilities of the driver.
            print(hdbc.max_concurrent_activities)

            # All applications need to allocate a statement handle with
            # SQLAllocHandle, and many applications set statement attributes,
            # such as the cursor type, with SQLSetStmtAttr.

            with StatementHandle(hdbc):
                # TODO: Finish writing this test
                pass
