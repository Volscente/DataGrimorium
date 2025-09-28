/*
 * Test query used in tests/test_bigquery_connector.py
 */
CREATE OR REPLACE TABLE `deep-learning-438509.dim_stackoverflow_data_model.test_table_creation` AS
SELECT
    @id AS id,
    @display_name AS display_name