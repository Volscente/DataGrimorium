# v.0.1.1

------

- [x] Add Class `BigQueryConnector` in `data_grimorium/bigquery_connector/bigquery_connector.py`
- [x] Add Function `_set_client` in `data_grimorium/bigquery_connector/bigquery_connector.BigQueryConnector`
- [x] Add Function `_build_query_parameters` in `data_grimorium/bigquery_connector/bigquery_connector.BigQueryConnector`
- [x] Add Function `execute_query_from_config` in `data_grimorium/bigquery_connector/bigquery_connector.BigQueryConnector`
- [x] Add Function `table_exists` in `data_grimorium/bigquery_connector/bigquery_connector.BigQueryConnector`
- [x] Add Function `wrap_dictionary_to_query_config` in `data_grimorium/bigquery_connector/bigquery_connector.BigQueryConnector`
- [x] Add Pydantic `BQClientConfig` in `data_grimorium/bigquery_connector/bigquery_types.py`
- [x] Add Pydantic `BQQueryParameter` in `data_grimorium/bigquery_connector/bigquery_types.py`
- [x] Add Pydantic `BQQueryConfig` in `data_grimorium/bigquery_connector/bigquery_types.py`
- [x] Add Pydantic `SentenceTransformersConfig` in `data_grimorium/data_preparation/data_preparation_types.py`
- [x] Add Pydantic `EmbeddingsConfig` in `data_grimorium/data_preparation/data_preparation_types.py`
- [x] Add Pydantic `PCAConfig` in `data_grimorium/data_preparation/data_preparation_types.py`
- [x] Add Pydantic `CompressEmbeddingsConfig` in `data_grimorium/data_preparation/data_preparation_types.py`
- [x] Add Pydantic `EncodingTextConfig` in `data_grimorium/data_preparation/data_preparation_types.py`
- [x] Add Pydantic `DateExtractionConfig` in `data_grimorium/data_preparation/data_preparation_types.py`
- [x] Add Pydantic `StandardisationMethod` in `data_grimorium/data_preparation/data_preparation_types.py`
- [x] Add Pydantic `OutlierMethod` in `data_grimorium/data_preparation/data_preparation_types.py`
- [x] Add Pydantic `NanStrategy` in `data_grimorium/data_preparation/data_preparation_types.py`
- [x] Add Pydantic `OutlierConfig` in `data_grimorium/data_preparation/data_preparation_types.py`
- [x] Add Pydantic `NumericalFeaturesConfig` in `data_grimorium/data_preparation/data_preparation_types.py`
- [x] Add Pydantic `FlagFeatureConfig` in `data_grimorium/data_preparation/data_preparation_types.py`


# v.0.1.0a

------

- [x] Refactor the structure of the packages and modules under `src`

# v.0.1.0

-------

- [x] Add Function `read_file_from_path` in `data_grimorium/general_utils/general_utils.py`
- [x] Add PyTest `test_read_file_from_path` in `test/general_utils/test_general_utils.py`
- [x] Add PyTest `test_read_file_from_path_exceptions` in `test/general_utils/test_general_utils.py`