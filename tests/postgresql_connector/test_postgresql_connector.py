"""
This test module includes all the tests for the
module src.postgresql_connector.
"""

# Import Standard Libraries
import pytest

# Import Package Modules
from postgresql_connector.postgresql_connector import PostgreSQLConnector


@pytest.mark.parametrize("database_name", ["test_postgres_db"])
def test_set_client(
    fixture_postgresql_connector: PostgreSQLConnector,
    database_name: str,
) -> bool:
    """
    Test the function src/postgresql_connector/postgresql_connector._set_client
    by checking the ``self._client`` and ``self._cursor`` attributes.

    Args:
        fixture_postgresql_connector (PostgreSQLConnector): PostgreSQL Connector
        database_name (String): Expected database name
    """
    assert fixture_postgresql_connector._client is not None
    assert fixture_postgresql_connector._client.info.dbname == database_name
    assert fixture_postgresql_connector._cursor.connection.info.dbname == database_name
