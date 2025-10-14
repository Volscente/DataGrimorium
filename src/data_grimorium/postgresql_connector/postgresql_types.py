"""
The module includes Pydantic types for PostgreSQL Connector.
"""

# Import Standard Modules
import pandas as pd
from typing import Dict, Any
from pydantic import BaseModel, Field


class PostgreSQLClientConfig(BaseModel):
    """
    PostgreSQL client configuration.

    Attributes:
        dbname (str): Database name.
        user (str): Username.
        password (str): Password.
        host (str): Host URL.
        port (str): Port number.
    """

    dbname: str = Field(..., description="Database name", alias="dbname")
    user: str = Field(..., description="Username", alias="user")
    password: str = Field(..., description="Password", alias="password")
    host: str = Field(..., description="Host URL", alias="host")
    port: int = Field(..., description="Port number", alias="port")

    def as_dict(self) -> Dict[str, Any]:
        """
        Return the model as a Python dictionary (using field aliases).
        """
        return self.model_dump(by_alias=True)

    def as_json(self) -> str:
        """
        Return the model as a JSON string (with indentation for readability).
        """
        return self.model_dump_json(by_alias=True, indent=2)

    def as_df(self) -> pd.DataFrame:
        """
        Return the model as a single-row pandas DataFrame.
        """
        return pd.DataFrame([self.as_dict()])


class PostgreSQLQueryConfig(BaseModel):
    # TODO
    pass
