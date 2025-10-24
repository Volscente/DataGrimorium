/*
 * Test query to select values in a table
 */
SELECT *
FROM test_table_creation
WHERE row_id = %(row_id)s;