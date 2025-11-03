"""
The module includes the PostgreSQL connector to interact
with the PostgreSQL database.
"""

# Import Standard Libraries
import logging
import psycopg2
import pandas as pd
from pathlib import Path
from typing import Union


# Import Package Modules
from data_grimorium.general_utils.general_utils import read_file_from_path
from data_grimorium.postgresql_connector.postgresql_types import (
    PostgreSQLClientConfig,
    PostgreSQLQueryConfig,
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M",
)


class PostgreSQLConnector:
    """
    The class implements a PostgreSQL Connector
    in order to query PostgreSQL datasets and tables.

    Attributes:
        _root_path (pathlib.Path): Root path of the project
        _client_config (PostgreSQLClientConfig): Client configurations
    """

    def __init__(self, client_config: PostgreSQLClientConfig, root_path: Path):
        """
        Constructor of the class PostgreSQLConnector

        Args:
            client_config (PostgreSQLClientConfig): Config for instance a PostgreSQL Client
        """
        # Initialise attributes
        self._client_config = client_config
        self._root_path = root_path

    def _get_connection(self):
        """
        Creates and returns a new PostgreSQL connection.
        """
        # Open connection
        connection = psycopg2.connect(**self._client_config.model_dump())

        logging.info(f"🛢 Connected to database {connection.info.dbname}")

        return connection

    def execute_query_from_config(
        self, query_config: PostgreSQLQueryConfig
    ) -> Union[pd.DataFrame, bool]:
        """
        Execute a query from local path and with a certain set of parameter configurations.

        Args:
            query_config (PostgreSQLQueryConfig): Query configuration

        Returns:
            (Union[pd.DataFrame, bool]): The result of the query execution.
            Either the data or a bool in case of table creation.
        """
        # Retrieve query path
        query_path = Path(query_config.query_path)

        # Read query
        query = read_file_from_path(query_path, self._root_path)

        # Execute within a context manager to auto-close connection
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    # Execute the query with the parameters (if present)
                    cur.execute(query, query_config.query_parameters or None)

                    # If query returns data (e.g., SELECT), fetch into DataFrame
                    if cur.description:
                        columns = [desc[0] for desc in cur.description]
                        data = cur.fetchall()
                        result = pd.DataFrame(data, columns=columns)
                    else:
                        result = True  # For CREATE, INSERT, UPDATE, etc.

                    conn.commit()
                    logging.info(f"✅ Query executed successfully from {query_path}")
                    return result

        except psycopg2.Error as e:
            logging.error(f"❌ Database error: {e}")
            raise

    def tables_exists(self, table_name: str) -> bool:
        """
        Check if a table exists in the database.

        Args:
            table_name (str): Name of the table to check.

        Returns:
            (bool): True if the table exists, False otherwise.
        """
        # Execute within a context manager to auto-close connection
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    # Execute the query with the parameters (if present)
                    cur.execute(
                        "select * from information_schema.tables where table_name=%s", (table_name,)
                    )
                    conn.commit()

                    logging.info(f"🕵🏻 Table {table_name} exists? → {bool(cur.rowcount)}")

                    return bool(cur.rowcount)

        except psycopg2.Error as e:
            logging.error(f"❌ Database error: {e}")
            raise

    def upload_dataframe(self, data: pd.DataFrame, table_name: str, replace: bool = False) -> None:
        """
        Upload a DataFrame to a PostgreSQL table.

        Args:
            data (pd.DataFrame): Data to upload.
            table_name (str): Name of the table.
            replace (bool): If True, replace the rows if it already exists.
        """
        pass
