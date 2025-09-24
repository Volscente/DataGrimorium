#!/bin/bash
#
# Run Ruff

echo
echo "-------- Ruff Lint --------"
echo

# Check
ruff check --fix

# Format .src and .tests folders
ruff format

echo
echo "--------------------------------"
echo