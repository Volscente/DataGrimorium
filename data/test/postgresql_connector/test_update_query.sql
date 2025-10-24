/*
 * Test query to updates values in a table
 */
UPDATE test_table_creation
SET display_name = %(display_name)s
WHERE row_id = %(row_id)s;