#!/usr/bin/env bash

set -e
set -x

python -m venv venv
source venv/bin/activate
python -m pip install --progress-bar=off dist/*.tar.gz
python -m unittest pdfo.testpdfo
deactivate
rm -r venv