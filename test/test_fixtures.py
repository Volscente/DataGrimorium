"""
This test module includes all the fixtures necessary
for running PyTest tests
"""
# Import Standard Libraries
import pathlib
import pytest
from google.cloud import bigquery

# Import Package Modules
from general_utils.general_utils import read_configuration

# Read configuration file
configuration = read_configuration('vg_ds_utils_config.yaml')


@pytest.fixture
def fixture_query_path() -> pathlib.Path:
    """
    Fixture for a pathlib.Path Query local path

    Returns:
        query_path: pathlib.Path local query path
    """
    # Create the Path object
    query_path = pathlib.Path(__file__).parents[1] / \
        'queries' / \
        'test_queries' / \
        'test_access_bigquery_query.sql'
    return query_path


@pytest.fixture
def fixture_bigquery_client(project_id: str = configuration['bigquery_project_id']) \
        -> bigquery.Client:
    """
    Fixture for a Google BigQuery client

    Args:
        project_id: str Google project ID

    Returns:
        bigquery_client: bigquery.Client object
    """
    # Initialise the BigQuery client
    bigquery_client = bigquery.Client(project=project_id)

    return bigquery_client
