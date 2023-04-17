#!/usr/bin/env bash

set -e
set -x

# Move up two levels to create the building virtual environment outside of the source folder
cd ../../

# Create and activate the building virtual environment
python -m venv build_env
source build_env/bin/activate

# Install the required Python dependencies
python -m pip install --progress-bar=off numpy twine

# Build the source distribution
cd pdfo/pdfo
python setup.py sdist

# Check the distribution file
python -m twine check dist/*.tar.gz
