import pytest

from odbcffi.odbc.enums import SQLAttrODBCVersion
from odbcffi.odbc.environment_handle import EnvironmentHandle


class TestEnvironmentHandle:
    def test_default_odbc_version(self, environment_handle: EnvironmentHandle) -> None:

        assert environment_handle.odbc_version == SQLAttrODBCVersion.SQL_OV_ODBC3

    @pytest.mark.parametrize("odbc_version", list(SQLAttrODBCVersion))
    def test_odbc_version_setter_getter(
        self,
        isolated_environment_handle: EnvironmentHandle,
        odbc_version: SQLAttrODBCVersion,
    ) -> None:
        isolated_environment_handle.odbc_version = odbc_version

        assert isolated_environment_handle.odbc_version == odbc_version
