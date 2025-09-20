#!/bin/bash
#
# Run Ruff

echo
echo "-------- Ruff Lint --------"
echo

# Check
ruff check --fix

# Format .data_grimorium and .tests folders
ruff format

echo
echo "--------------------------------"
echo