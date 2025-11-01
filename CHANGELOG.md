# v.1.0.4

------

- [x] Hotfix Function `_set_client` in `data_grimorium/bigquery_connector/bigquery_connector.BigQueryConnector`

# v.1.0.3

------

- [x] Add Pydantic `PostgreSQLClientConfig` in `data_grimorium/postgresql_connector/postgresql_types.py`
- [x] Add Pydantic `PostgreSQLQueryConfig` in `data_grimorium/postgresql_connector/postgresql_types.py`
- [x] Add Function `execute_query_from_config` in `data_grimorium/postgresql_connector/postgresql_connector.PostgreSQLConnector`
- [x] Add PyTest Fixture `fixture_postgresql_create_query` in `fixtures/postgresql_fixtures.py`
- [x] Add PyTest Fixture `fixture_postgresql_insert_query` in `fixtures/postgresql_fixtures.py`
- [x] Add PyTest Fixture `fixture_postgresql_update_query` in `fixtures/postgresql_fixtures.py`
- [x] Add PyTest Fixture `fixture_postgresql_select_query` in `fixtures/postgresql_fixtures.py`
- [x] Add PyTest `test_execute_query_from_config` in `postgresql_connector/test_postgresql_connector.py`
- [x] Add PyTest `test_execute_select_query_from_config` in `postgresql_connector/test_postgresql_connector.py`
- [x] Add Function `tables_exists` in `data_grimorium/postgresql_connector/postgresql_connector.PostgreSQLConnector`
- [x] Add PyTest `test_tables_exists` in `postgresql_connector/test_postgresql_connector.py`

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
- [x] Add Function `generate_embeddings` in `data_grimorium/data_preparation/data_preparation_utils.py`
- [x] Add Function `compress_embeddings` in `data_grimorium/data_preparation/data_preparation_utils.py`
- [x] Add Function `encode_text` in `data_grimorium/data_preparation/data_preparation_utils.py`
- [x] Add Function `extract_date_information` in `data_grimorium/data_preparation/data_preparation_utils.py`
- [x] Add Function `standardise_features` in `data_grimorium/data_preparation/data_preparation_utils.py`
- [x] Add Function `drop_outliers` in `data_grimorium/data_preparation/data_preparation_utils.py`
- [x] Add Function `manage_nan_values` in `data_grimorium/data_preparation/data_preparation_utils.py`
- [x] Add Function `prepare_numerical_features` in `data_grimorium/data_preparation/data_preparation_utils.py`
- [x] Add Function `create_flag_feature` in `data_grimorium/data_preparation/data_preparation_utils.py`
- [x] Add PyTest `test_set_client` in `tests/bigquery_connector/test_bigquery_connector.py`
- [x] Add PyTest `test_build_query_parameters` in `tests/bigquery_connector/test_bigquery_connector.py`
- [x] Add PyTest `test_table_exists` in `tests/bigquery_connector/test_bigquery_connector.py`
- [x] Add PyTest `test_execute_query_from_config` in `tests/bigquery_connector/test_bigquery_connector.py`
- [x] Add PyTest `test_wrap_dictionary_to_query_config` in `tests/bigquery_connector/test_bigquery_connector.py`
- [x] Add PyTest `test_generate_embeddings` in `tests/data_preparation/test_data_preparation.py`
- [x] Add PyTest `test_compress_embeddings` in `tests/data_preparation/test_data_preparation.py`
- [x] Add PyTest `test_encode_text` in `tests/data_preparation/test_data_preparation.py`
- [x] Add PyTest `test_extract_date_information` in `tests/data_preparation/test_data_preparation.py`
- [x] Add PyTest `test_standardise_features` in `tests/data_preparation/test_data_preparation.py`
- [x] Add PyTest `test_drop_outliers` in `tests/data_preparation/test_data_preparation.py`
- [x] Add PyTest `test_manage_nan_values` in `tests/data_preparation/test_data_preparation.py`
- [x] Add PyTest `test_prepare_numerical_features` in `tests/data_preparation/test_data_preparation.py`
- [x] Add PyTest `test_create_flag_feature` in `tests/data_preparation/test_data_preparation.py`
- [x] Add PyTest Fixture `fixture_bigquery_client_config` in `tests/fixtures/bigquery_fixtures.py`
- [x] Add PyTest Fixture `fixture_bigquery_connector` in `tests/fixtures/bigquery_fixtures.py`
- [x] Add PyTest Fixture `fixture_bigquery_read_query_config` in `tests/fixtures/bigquery_fixtures.py`
- [x] Add PyTest Fixture `fixture_bigquery_create_table_query_config` in `tests/fixtures/bigquery_fixtures.py`
- [x] Add PyTest Fixture `fixture_sentence_transformers_config` in `tests/fixtures/data_preparation_utils_fixtures.py`
- [x] Add PyTest Fixture `fixture_embeddings_config` in `tests/fixtures/data_preparation_utils_fixtures.py`
- [x] Add PyTest Fixture `fixture_pca_config` in `tests/fixtures/data_preparation_utils_fixtures.py`
- [x] Add PyTest Fixture `fixture_compress_embeddings_config` in `tests/fixtures/data_preparation_utils_fixtures.py`
- [x] Add PyTest Fixture `fixture_encode_text_config` in `tests/fixtures/data_preparation_utils_fixtures.py`
- [x] Add PyTest Fixture `fixture_sentences` in `tests/fixtures/data_preparation_utils_fixtures.py`
- [x] Add PyTest Fixture `fixture_date_extraction_config` in `tests/fixtures/data_preparation_utils_fixtures.py`
- [x] Add PyTest Fixture `fixture_numerical_features_config` in `tests/fixtures/data_preparation_utils_fixtures.py`

# v.0.1.0a

------

- [x] Refactor the structure of the packages and modules under `src`

# v.0.1.0

-------

- [x] Add Function `read_file_from_path` in `data_grimorium/general_utils/general_utils.py`
- [x] Add PyTest `test_read_file_from_path` in `test/general_utils/test_general_utils.py`
- [x] Add PyTest `test_read_file_from_path_exceptions` in `test/general_utils/test_general_utils.py`