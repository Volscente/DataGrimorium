"""
The module includes Pydantic types for PostgreSQL Connector.
"""

# Import Standard Modules
from pydantic import BaseModel, Field


class PostgreSQLClientConfig(BaseModel):
    """
    PostgreSQL client configuration.

    Attributes:
        dbname (String): Database name.
        user (String): Username.
        password (String): Password.
        host (String): Host URL.
        port (Integer): Port number.
    """

    dbname: str = Field(..., description="Database name")
    user: str = Field(..., description="Username")
    password: str = Field(..., description="Password")
    host: str = Field(..., description="Host URL")
    port: int = Field(..., description="Port number")
