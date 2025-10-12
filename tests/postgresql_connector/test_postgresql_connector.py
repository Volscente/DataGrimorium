"""
This test module includes all the tests for the
module src.postgresql_connector.
"""

# Import Standard Libraries
import os
import pathlib
import pytest
import psycopg2
import time
from dynaconf import Dynaconf
from types import ModuleType

# Import Package Modules
from data_grimorium.postgresql_connector.postgresql_connector import PostgreSQLConnector

# Retrieve the root path
root_path = os.getenv("DATA_GRIMORIUM_ROOT_PATH")

# Read the configuration file
config = Dynaconf(
    settings_files=[pathlib.Path(root_path) / "configuration" / "datagrimorium_settings.toml"],
    environments=True,
    env="pytest",
)


def setup_module(module: ModuleType) -> None:
    """
    Setup run once before any tests in this module to check if PostgreSQL database
    is running.

    Args:
        module (ModuleType): Current Python module
    """
    max_retries = 3

    # 3 Times retry mechanisms
    for attempt in range(max_retries):
        try:
            conn = psycopg2.connect(
                host=config["postgresql"]["client"]["host"],
                port=config["postgresql"]["client"]["port"],
                user=config["postgresql"]["client"]["user"],
                password=config["postgresql"]["client"]["password"],
                dbname=config["postgresql"]["client"]["dbname"],
                connect_timeout=3,
            )
            conn.close()
            print(f"✅ PostgreSQL is up (checked on attempt {attempt + 1})")
            return
        except psycopg2.OperationalError:
            print(f"⏳ PostgreSQL not ready, retrying ({attempt + 1}/{max_retries})...")
            time.sleep(3)

    pytest.exit("❌ PostgreSQL is not running or not reachable. Exiting tests.")


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
