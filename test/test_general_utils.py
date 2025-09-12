"""
This test module includes all the tests for the
module src.general_utils.general_utils
"""
# Import Standard Modules
import pathlib
import pytest

# Import Package Modules
from general_utils.general_utils import read_configuration, read_file_from_path


@pytest.mark.parametrize('test_config_file, test_config, expected_value', [
    ('vg_ds_utils_config.yaml', 'test_value', 1),
])
def test_read_configuration(test_config_file: str,
                            test_config: str,
                            expected_value: int) -> bool:
    """
    Test the function src.general_utils.general_utils.read_configuration
    by reading test configuration entries

    Args:
        test_config_file: String configuration file name
        test_config: String configuration entry key
        expected_value: String configuration expected value

    Returns:
    """

    # Read configuration file
    config = read_configuration(test_config_file)

    assert config[test_config] == expected_value


@pytest.mark.parametrize('test_config_file, expected_error', [
    ('wrong_config.yaml', FileNotFoundError)
])
def test_read_configuration_exceptions(test_config_file: str,
                                       expected_error: FileNotFoundError) -> bool:
    """
    Test the exceptions to the function
    src.general_utils.general_utils.read_configuration

    Args:
        test_config_file: String wrong configuration file name
        expected_error: Exception instance

    Returns:
    """

    with pytest.raises(expected_error):

        read_configuration(test_config_file)


@pytest.mark.parametrize('input_path, expected_first_line', [
    (pathlib.Path(__file__).parents[1] /
        'queries' /
         'test_queries' /
         'test_access_bigquery_query.sql',
     '-- Query for testing purposes')
])
def test_read_file_from_path(input_path: pathlib.Path,
                             expected_first_line: str) -> bool:
    """
    Test the function src.general_utils.general_utils.read_file_from_path
    by reading a local file and compare the first line

    Args:
        input_path: pathlib.Path local file path
        expected_first_line: str of file first line

    Returns:
    """

    # Read the file
    file_read = read_file_from_path(input_path)

    assert file_read.partition('\n')[0] == expected_first_line


@pytest.mark.parametrize('input_path, expected_exception', [
    (pathlib.Path(__file__).parents[2] /
        'queries' /
         'test_queries' /
         'wrong_file.sql',
     FileNotFoundError)
])
def test_read_file_from_path_exceptions(input_path: pathlib.Path,
                                        expected_exception: Exception) -> bool:
    """
    Test the exceptions to the function
    src.general_utils.general_utils.read_file_from_path

    Args:
        input_path: pathlib.Path wrong local file path
        expected_exception: Exception instance

    Returns:
    """

    with pytest.raises(expected_exception):
        read_file_from_path(input_path)
