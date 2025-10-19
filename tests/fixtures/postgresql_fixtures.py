"""
The module includes Fixtures related to the module "postgresql_connector".
"""

# Import Standard Libraries
import os
import pathlib
import pytest
from dynaconf import Dynaconf

# Import Package Modules
from data_grimorium.postgresql_connector.postgresql_types import (
    PostgreSQLClientConfig,
    PostgreSQLQueryConfig,
)
from data_grimorium.postgresql_connector.postgresql_connector import PostgreSQLConnector


# Retrieve the root path
root_path = pathlib.Path(os.getenv("DATA_GRIMORIUM_ROOT_PATH"))

# Read the configuration file
config = Dynaconf(
    settings_files=[root_path / "configuration" / "datagrimorium_settings.toml"],
    environments=True,
    env="pytest",
)


@pytest.fixture
def fixture_postgresql_client_config(
    client_config: dict = config["postgresql"]["client"],
) -> PostgreSQLClientConfig:
    """
    Fixture for a PostgreSQLClientConfig object
    from src/postgresql_connector/postgresql_types.py.

    Args:
        client_config (Dictionary): Configurations for a PostgreSQLClientConfig object.

    Returns:
        (PostgreSQLClientConfig): Object of PostgreSQL client configurations
    """
    return PostgreSQLClientConfig(**client_config)


@pytest.fixture
def fixture_postgresql_connector(
    fixture_postgresql_client_config: PostgreSQLClientConfig,
) -> PostgreSQLConnector:
    """
    Fixture for a PostgreSQLConnector object in order to connect to a PostgreSQL Database.

    Args:
        fixture_postgresql_client_config (PostgreSQLClientConfig): Client configurations.

    Returns:
        (PostgreSQLConnector): Object of PostgreSQL Connector
    """
    return PostgreSQLConnector(client_config=fixture_postgresql_client_config, root_path=root_path)


@pytest.fixture
def fixture_postgresql_create_table_query(
    query_config=config["postgresql"]["create_table_query_config"],
) -> PostgreSQLQueryConfig:
    """
    Fixture for a PostgreSQLQueryConfig object in order to create a table.

    Args:
        query_config (PostgreSQLQueryConfig): Query configurations.

    Returns:
        (PostgreSQLQueryConfig): PostgreSQL query configuration object.
    """
    return PostgreSQLQueryConfig(**query_config.to_dict())
