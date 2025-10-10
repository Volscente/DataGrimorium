"""
The module includes the PostgreSQL connector to interact
with the PostgreSQL database.
"""

# Import Standard Libraries
import logging
import psycopg2

# Import Package Modules
from data_grimorium.postgresql_connector.postgresql_types import PostgreSQLClientConfig

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


class PostgreSQLConnector:
    """
    The class implements a PostgreSQL Connector
    in order to query PostgreSQL datasets and tables.

    Attributes:
        _client_config (PostgreSQLClientConfig): Client configurations
    """

    def __init__(self, client_config: PostgreSQLClientConfig):
        """
        Constructor of the class PostgreSQLConnector

        Args:
            client_config (PostgreSQLClientConfig): Config for instance a PostgreSQL Client
        """
        # Initialise attributes
        self._client_config = client_config

        # Set client
        self._set_client()

    def _set_client(self):
        """
        Set the attribute ``_client`` with an instance of the PostgreSQL Client.
        """
        self._logger.debug("_set_client - Start")

        self._logger.info("_set_client - Set the PostgreSQL client")

        # Initialise the client
        self._client = psycopg2.connect(**self._client_config.model_dump())

        # Create a cursor
        self._cursor = self._client.cursor()

        self._logger.info(
            f"_set_client - 🛢 Connected to Database {self._cursor.connection.info.dbname}"
        )

        self._logger.debug("_set_client - End")
