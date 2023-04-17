#!/usr/bin/env bash

set -e
set -x

# Fetch the distributions uploaded to Anaconda
PDFO_URL="https://pypi.anaconda.org/pdfo/simple/pdfo/"
python -m pip install --progress-bar=off wheelhouse_uploader
python -m wheelhouse_uploader fetch --version "$PDFO_VERSION" --local-folder dist/ pdfo "$PDFO_URL"
