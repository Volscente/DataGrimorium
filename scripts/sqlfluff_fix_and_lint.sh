#!/bin/bash
#
# First fix and then lint BigQuery SQL Queries

# Check for the presence of argument file
if [ $# -ne 1 ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

# Assign path to fix & lint
file="$1"

echo
echo "-------- SQLFluff Fix & Lint --------"
echo

# Fix & lint
sqlfluff fix --dialect bigquery --exclude-rules "LT05, AM04" "$file" \
&& sqlfluff lint --dialect bigquery --exclude-rules "LT05, AM04" "$file"

echo
echo "----------------------------------------"
echo