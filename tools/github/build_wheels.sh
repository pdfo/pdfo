#!/usr/bin/env bash

set -e
set -x

python -m pip install --progress-bar=off cibuildwheel
python -m cibuildwheel --output-dir wheelhouse
