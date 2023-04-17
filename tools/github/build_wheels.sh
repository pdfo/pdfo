#!/usr/bin/env bash

set -e
set -x

cd python
python -m pip install --progress-bar=off cibuildwheel
python -m cibuildwheel --output-dir wheelhouse
