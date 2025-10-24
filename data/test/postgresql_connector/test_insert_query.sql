/*
 * Test query to insert values into a table
 */
INSERT INTO test_table_creation (row_id, display_name)
VALUES (%(row_id)s, %(display_name)s);