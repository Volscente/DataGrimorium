/*
 * Test query used in tests/test_bigquery_connector.py
 */
SELECT
    id,
    display_name
FROM
    `bigquery-public-data.stackoverflow.users`
WHERE
    id = @id
    AND display_name = @display_name
LIMIT 1