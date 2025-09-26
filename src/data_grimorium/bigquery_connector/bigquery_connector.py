"""
Defines a Connector class in order to
interact with BigQuery datasets and tables.
"""

# Import Standard Modules
import logging
from pathlib import Path
from typing import Union, List
import pandas as pd
from google.cloud import bigquery

# Import Package Modules
from data_grimorium.bigquery_connector.bigquery_types import (
    ClientConfig,
    QueryParameter,
    QueryConfig,
)
from data_grimorium.general_utils.general_utils import read_file_from_path


class BigQueryConnector:
    """
    The class implements a BigQuery Connector
    in order to query datasets and tables

    Attributes:
        _root_path (pathlib.Path): Root path of the project
        _client_config (ClientConfig): Configurations for instance a BigQuery Client instance
        _client (bigquery.Client): BigQuery client object

    Methods:
        execute_query_from_config: Execute a query from local path and with a certain set of parameter configurations.
        table_exists: Check if a table exists in a dataset
        wrap_dictionary_to_query_config: Converts a dictionary of Query Configurations into a ``QueryConfig`` object.
    """

    def __init__(self, client_config: ClientConfig, root_path: Path):
        """
        Constructor of the class BigqueryConnector

        Args:
            client_config (ClientConfig): Config for instance a BigQuery Client
            root_path (Path): Root path to the project
        """
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

        # Initialise attributes
        self._client_config = client_config
        self._root_path = root_path

        # Set the client
        self._set_client()

    def _set_client(self):
        """
        Set the attribute ``_client`` with an instance of the BigQuery Client.
        """
        self._logger.info(
            f"💼 Set the BigQuery client with project id {self._client_config.project_id.value}"
        )

        # Set the client
        self._client = bigquery.Client(project=self._client_config.project_id.value)

    @staticmethod
    def _build_query_parameters(
        query_parameters: List[QueryParameter],
    ) -> List[Union[bigquery.ArrayQueryParameter, bigquery.ScalarQueryParameter]]:
        """
        Build BigQuery query parameters from a list of QueryParameter

        Args:
            query_parameters (List[QueryParameter]): Query parameters

        Returns:
            (List[Union[ArrayQueryParameter, ScalarQueryParameter]]):
            BigQuery list of parameters
        """

        # Initialise empty list BigQuery query parameters
        bigquery_query_parameters = []

        # Fetch all query parameters
        for query_parameter in query_parameters:
            # Check if the ScalarQueryParameter or ArrayQueryParameter is required
            # The difference is in the type of values passed (No list: scalar, list: array)
            if isinstance(query_parameter.value, list):
                # Build the parameter
                bigquery_parameter = bigquery.ArrayQueryParameter(
                    *query_parameter.__dict__.values()
                )
            else:
                # Build the parameter
                bigquery_parameter = bigquery.ScalarQueryParameter(
                    *query_parameter.__dict__.values()
                )

            # Append to the list of parameters
            bigquery_query_parameters.append(bigquery_parameter)

        return bigquery_query_parameters

    def execute_query_from_config(self, query_config: QueryConfig) -> Union[pd.DataFrame, bool]:
        """
        Execute a query from local path and with a certain set of parameter configurations.
        The query can either read data or create a table on BigQuery.

        Args:
            query_config (QueryConfig): Query configurations (path and parameters)

        Returns:
            result (Union[pd.DataFrame, bool]): The result of the query execution.

                  - pd.DataFrame: When the query is executed successfully and returns data.

                  - bool: `True` if the query executes successfully but does not return data
        """
        # Initialise result to return
        result = None

        # Retrieve query path
        query_path = Path(query_config.query_path)

        logging.info(f"execute_query_from_config - Reading query file: {query_path.as_posix()}")

        # Read query
        query = read_file_from_path(query_path, self._root_path)

        # Check if there are parameters
        if query_config.query_parameters is None:
            # Execute the job in BigQuery
            job = self._client.query(query)
        else:
            # Retrieve BigQuery query parameters
            parameters = self._build_query_parameters(query_config.query_parameters)

            # Execute the job BigQuery with parameters
            job = self._client.query(
                query=query,
                job_config=bigquery.QueryJobConfig(query_parameters=parameters),
            )

        # Extract the job result
        result = job.result()

        # Switch between a read query and a table creation query
        if job.statement_type == "CREATE_TABLE_AS_SELECT":
            self._logger.info("execute_query_from_config - Created table from query")

            # Return table creation status
            # NOTE: Using the 'job.done()' does not return True unless few time has passed
            result = job.done()

        else:
            self._logger.info("execute_query_from_config - Converting data to Pandas DataFrame")

            # Convert data to a Pandas DataFrame
            result = result.to_dataframe()

        self._logger.debug("execute_query_from_config - End")

        return result

    def table_exists(self, table_name: str, dataset_name: str) -> bool:
        """
        Check if a table exists in a dataset

        Args:
            table_name (String): Name of the table
            dataset_name (String): Name of the dataset

        Returns:
            exists (Boolean): Flag indicating if the table exists
        """
        self._logger.info("table_exists - Start")

        self._logger.info("table_exists - Retrieve list of tables for dataset: %s", dataset_name)

        # Retrieve the list of tables
        tables = self._client.list_tables(dataset_name)

        # Retrieve the list of table names
        table_names = [table.table_id for table in tables]

        # Check if the table exists
        exists = table_name in table_names

        self._logger.info("table_exists - Table %s exists: %s", table_name, exists)

        self._logger.info("table_exists - End")

        return exists

    def wrap_dictionary_to_query_config(self, query_config_dictionary: dict) -> QueryConfig:
        """
        Converts a dictionary of Query Configurations into a ``QueryConfig`` object.

        Args:
            query_config_dictionary (dict): The dictionary containing Query Configurations.

        Returns:
            (QueryConfig): Object with BigQuery query configurations.
        """
        self._logger.info("wrap_dictionary_to_query_parameters - Start")

        # Check if there are parameters
        if "query_parameters" not in query_config_dictionary.keys():
            self._logger.info("wrap_dictionary_to_query_parameters - No query parameters")
        else:
            self._logger.info("wrap_dictionary_to_query_parameters - Wrapping query parameters")

            # Retrieve parameters
            query_parameters = query_config_dictionary["query_parameters"]

            # Wrap query parameters
            wrapped_parameters = [
                QueryParameter(**query_parameters[parameter]) for parameter in query_parameters
            ]

            # Update the dictionary with the wrapped parameters
            query_config_dictionary["query_parameters"] = wrapped_parameters

        return QueryConfig(**query_config_dictionary)
