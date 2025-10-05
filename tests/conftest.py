"""
This module references the project's fixtures.
"""

# Define the project fixtures
pytest_plugins = [
    "tests.fixtures.bigquery_fixtures",
    "tests.fixtures.data_preparation_utils_fixtures",
]
