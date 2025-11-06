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
import pandas as pd
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
def test_get_connection(
    fixture_postgresql_connector: PostgreSQLConnector,
    database_name: str,
) -> bool:
    """
    Test the function postgresql_connector/postgresql_connector._get_connection
    by checking the connection attributes.

    Args:
        fixture_postgresql_connector (PostgreSQLConnector): PostgreSQL Connector
        database_name (String): Expected database name
    """
    # Retrieve connection
    connection = fixture_postgresql_connector._get_connection()

    assert connection.info.dbname == database_name


@pytest.mark.parametrize(
    "fixture_name, expected_output",
    [
        ("fixture_postgresql_create_query", True),
        ("fixture_postgresql_insert_query", True),
        ("fixture_postgresql_update_query", True),
    ],
)
def test_execute_query_from_config(
    fixture_name: str,
    expected_output: bool,
    fixture_postgresql_connector: PostgreSQLConnector,
    request: pytest.FixtureRequest,
) -> bool:
    """
    Test the function postgresql_connector/postgresql_connector.execute_query_from_config.

    Args:
        fixture_name (str): Name of the fixture query to use.
        expected_output (bool): Expected output.
        fixture_postgresql_connector (PostgreSQLConnector): PostgreSQL Connector.
        request (FixtureRequest): Object to load the required fixture.
    """
    # Load fixture
    query_config = request.getfixturevalue(fixture_name)

    # Execute query
    result = fixture_postgresql_connector.execute_query_from_config(query_config)

    assert bool(result) == expected_output


@pytest.mark.parametrize(
    "fixture_name, expected_output",
    [
        ("fixture_postgresql_select_query", "test_name_updated"),
    ],
)
def test_execute_select_query_from_config(
    fixture_name: str,
    expected_output: str,
    fixture_postgresql_connector: PostgreSQLConnector,
    request: pytest.FixtureRequest,
) -> bool:
    """
    Test the function postgresql_connector/postgresql_connector.execute_query_from_config.

    Args:
        fixture_name (str): Name of the fixture query to use.
        expected_output (str): Expected output.
        fixture_postgresql_connector (PostgreSQLConnector): PostgreSQL Connector.
        request (FixtureRequest): Object to load the required fixture.
    """
    # Load fixture
    query_config = request.getfixturevalue(fixture_name)

    # Execute query
    result = fixture_postgresql_connector.execute_query_from_config(query_config)

    assert result.loc[0, "display_name"] == expected_output


@pytest.mark.parametrize(
    "table_name, expected_output",
    [
        ("test_table_creation", True),
    ],
)
def test_tables_exists(
    fixture_postgresql_connector: PostgreSQLConnector,
    table_name: str,
    expected_output: bool,
) -> bool:
    """
    Test the function postgresql_connector/postgresql_connector.tables_exists.

    Args:
        fixture_postgresql_connector (PostgreSQLConnector): PostgreSQL Connector.
        table_name (str): Name of the table to check.
        expected_output (bool): Expected output.
    """
    # Check if the table exists
    result = fixture_postgresql_connector.tables_exists(table_name)

    assert result == expected_output


@pytest.mark.parametrize(
    "input_data, input_table_name, expected_output",
    [
        (
            pd.DataFrame({"row_id": [1, 2, 3], "display_name": ["A", "B", "C"]}),
            "test_table_creation",
            3,
        )
    ],
)
def test_upload_dataframe(
    fixture_postgresql_connector: PostgreSQLConnector,
    input_data: pd.DataFrame,
    input_table_name: str,
    expected_output: int,
) -> bool:
    """
    Test the function postgresql_connector/postgresql_connector.upload_dataframe
    by checking the number of uploaded rows.

    Args:
        fixture_postgresql_connector (PostgreSQLConnector): PostgreSQL Connector.
        input_data (pd.DataFrame): Data to upload.
        input_table_name (str): Name of the table.
        expected_output (int): Expected output number of affected rows.
    """
    # Upload data
    result = fixture_postgresql_connector.upload_dataframe(
        data=input_data, table_name=input_table_name, replace=True
    )

    assert result == expected_output


@pytest.mark.parametrize(
    "input_data, input_table_name, expected_exception",
    [
        (
            pd.DataFrame(),
            "test_table_creation",
            ValueError,
        )
    ],
)
def test_upload_dataframe_exceptions(
    fixture_postgresql_connector: PostgreSQLConnector,
    input_data: pd.DataFrame,
    input_table_name: str,
    expected_exception: Exception,
) -> bool:
    """
    Test exceptions for the function postgresql_connector/postgresql_connector.upload_dataframe
    by passing faulty parameters.

    Args:
        fixture_postgresql_connector (PostgreSQLConnector): PostgreSQL Connector.
        input_data (pd.DataFrame): Data to upload.
        input_table_name (str): Name of the table.
        expected_exception (Exception): Expected exception.
    """
    with pytest.raises(expected_exception):
        fixture_postgresql_connector.upload_dataframe(
            data=input_data, table_name=input_table_name, replace=True
        )
