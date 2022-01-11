#!/usr/bin/env bash

set -e
set -x

# Move up two levels to create the testing virtual environment outside of the source folder
cd ../../

# Create and activate the testing virtual environment
python -m venv test_env
source test_env/bin/activate

# Install PDFO via the source distribution
python -m pip install pdfo/pdfo/dist/*.tar.gz

# Initiate the tests of PDFO
python -m unittest pdfo.testpdfo
