"""
This test module includes all the tests for the
module src.general_utils.general_utils
"""

# Import Standard Modules
import os
import pathlib
import pytest

# Import Package Modules
from src.general_utils.general_utils import read_file_from_path

# Retrieve root path
root_path = pathlib.Path(os.getenv("DATA_GRIMORIUM_ROOT_PATH"))


@pytest.mark.parametrize(
    "input_path, root_path_file, expected_first_line",
    [
        (
            pathlib.Path("data/test/test_read_query.sql"),
            root_path,
            "/*",
        )
    ],
)
def test_read_file_from_path(input_path: pathlib.Path, root_path_file: pathlib.Path, expected_first_line: str) -> bool:
    """
    Test the function src/general_utils/general_utils.read_file_from_path
    by reading a local file and compare the first line

    Args:
        input_path (pathlib.Path): Local file path
        root_path_file (pathlib.Path): Local root path
        expected_first_line (String): File first line
    """

    # Read the file
    file_read = read_file_from_path(
        file_path=input_path,
        root_path=root_path_file
    )

    assert file_read.partition("\n")[0] == expected_first_line


@pytest.mark.parametrize(
    "input_path, expected_exception",
    [
        (
            pathlib.Path(__file__).parents[2] / "queries" / "test_queries" / "wrong_file.sql",
            FileNotFoundError,
        )
    ],
)
def test_read_file_from_path_exceptions(
    input_path: pathlib.Path, expected_exception: Exception
) -> bool:
    """
    Test the exceptions to the function
    src/general_utils/general_utils.read_file_from_path

    Args:
        input_path (pathlib.Path): Wrong local file path
        expected_exception (Exception): Instance of triggered exception
    """

    with pytest.raises(expected_exception):
        read_file_from_path(input_path)