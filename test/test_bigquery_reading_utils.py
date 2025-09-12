"""
This test module includes all the tests for the
module src.bigquery_utils.bigquery_reading_utils
"""
# Import Standard Modules
import pathlib
import pytest
from google.cloud import bigquery


# Import Package Modules
from bigquery_utils.bigquery_reading_utils import read_bq_from_query
from test.test_fixtures import (fixture_query_path, fixture_bigquery_client)


@pytest.mark.parametrize('input_id, expected_status', [
    (1, 'OK')
])
def test_read_bq_from_query(fixture_query_path: pathlib.Path,
                            fixture_bigquery_client: bigquery.Client,
                            input_id: int,
                            expected_status: str) -> bool:
    """
    Test the function src.bigquery_utils.bigquery_reading_utils.read_bq_from_query
    by comparing the retrieved data column value with the expected output

    Args:
        fixture_query_path: pathlib.Path local query path
        fixture_bigquery_client: bigquery.Client instance
        input_id: int row id value
        expected_status: str row 'status' expected value

    Returns:
    """

    # Retrieve data from BigQuery
    data = read_bq_from_query(fixture_query_path,
                              fixture_bigquery_client)

    assert data.loc[data['id'] == input_id, 'status'].iloc[0] == expected_status


@pytest.mark.parametrize('test_query_path, expected_error', [
    (pathlib.Path(__file__).parents[1] /
         'queries' /
         'test_queries' /
         'test_access_bigquery_query_exception.sql',
     Exception)
])
def test_read_bq_from_query_exceptions(fixture_bigquery_client: bigquery.Client,
                                       test_query_path: pathlib.Path,
                                       expected_error: Exception) -> bool:
    """
    Test the exceptions to the function
    src.bigquery_utils.bigquery_reading_utils.read_bq_from_query

    Args:
        fixture_bigquery_client: bigquery.Client instance
        test_query_path: pathlib.Path local wrong query path
        expected_error: Exception instance

    Returns:
    """

    with pytest.raises(expected_error):
        read_bq_from_query(test_query_path,
                           fixture_bigquery_client)
