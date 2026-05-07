import pytest

from odbcffi.odbc import ConnectionHandle, SQLAttrAccessMode, SQLAttrAutocommit


class TestConnectionHandle:
    @pytest.mark.parametrize(
        "access_mode",
        list(SQLAttrAccessMode),
    )
    def test_access_mode(
        self,
        connection_handle: ConnectionHandle,
        access_mode: SQLAttrAccessMode,
    ) -> None:
        connection_handle.access_mode = access_mode
        assert connection_handle.access_mode == access_mode

    @pytest.mark.parametrize(
        "autocommit",
        list(SQLAttrAutocommit),
    )
    def test_autocommit(
        self,
        connection_handle: ConnectionHandle,
        autocommit: SQLAttrAutocommit,
    ) -> None:
        connection_handle.autocommit = autocommit
        assert connection_handle.autocommit == autocommit

    def test_max_concurrent_activities(self, open_connection_handle: ConnectionHandle) -> None:
        actual: int = open_connection_handle.max_concurrent_activities

        assert actual in (0, 1)
