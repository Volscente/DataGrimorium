"""
The module includes Fixtures related to the module "bigquery_connector".
"""

# Import Standard Libraries
import os
import pathlib
import pytest
from dynaconf import Dynaconf

# Import Package Modules
from src.data_grimorium.bigquery_connector.bigquery_types import (
    ClientConfig,
    QueryParameter,
    QueryConfig,
)
from src.data_grimorium.bigquery_connector.bigquery_connector import BigQueryConnector

# Retrieve the root path
root_path = os.getenv("DATA_GRIMORIUM_ROOT_PATH")

# Read the configuration file
config = Dynaconf(
    settings_files=[pathlib.Path(root_path) / "configuration" / "datagrimorium_settings.toml"],
    environments=True,
    env="pytest",
)


@pytest.fixture
def fixture_bigquery_client_config(
    project_id: str = config["bigquery"]["client"]["project_id"],
) -> ClientConfig:
    """
    This fixture returns a BigQueryClientConfig object

    Args:
        project_id (str): GCP project id

    Returns:
        client_config (ClientConfig): BigQuery object
    """
    # Instance a BigQueryClientConfig object
    client_config = ClientConfig(project_id=project_id)

    return client_config


@pytest.fixture
def fixture_bigquery_connector(
    fixture_bigquery_client_config: ClientConfig,
) -> BigQueryConnector:
    """
    This fixture returns a BigQueryConnector object

    Args:
        fixture_bigquery_client_config (BigQueryClientConfig): Configurations of BigQuery client

    Returns:
        bigquery_connector (BigQueryConnector): BigQuery Connector object
    """
    # Instance a BigQueryConnector object
    bigquery_connector = BigQueryConnector(
        client_config=fixture_bigquery_client_config, root_path=root_path
    )

    return bigquery_connector


@pytest.fixture
def fixture_read_query_config(
    query_config: dict = config["bigquery"]["read_query_config"],
) -> QueryConfig:
    """
    Fixture for a BigQueryQueryConfig read query configobject

    Args:
        query_config (Dictionary): Query configurations

    Returns:
        (BigQueryQueryConfig): Query configurations as an object
    """
    # Unpack configs
    query_path, query_parameters = (
        query_config["query_path"],
        query_config["query_parameters"],
    )

    return QueryConfig(
        query_path=query_path,
        query_parameters=[
            QueryParameter(**query_parameters[parameter_key]) for parameter_key in query_parameters
        ],
        local_path=None,
        table_name=None,
    )


@pytest.fixture
def fixture_create_table_query_config(
    query_config: dict = config["bigquery"]["create_table_query_config"],
) -> QueryConfig:
    """
    Fixture for a BigQueryQueryConfig that creates a table query config object

    Args:
        query_config (Dictionary): Query configurations

    Returns:
        (BigQueryQueryConfig): Query configurations as an object
    """
    # Unpack configs
    query_path, query_parameters = (
        query_config["query_path"],
        query_config["query_parameters"],
    )

    return QueryConfig(
        query_path=query_path,
        query_parameters=[
            QueryParameter(**query_parameters[query_parameter])
            for query_parameter in query_parameters
        ],
        local_path=None,
        table_name=None,
    )
