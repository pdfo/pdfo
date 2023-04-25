#!/usr/bin/env bash

set -e
set -x

python -m venv venv
source venv/bin/activate
python -m pip install --progress-bar=off build
python -m build --sdist
deactivate
rm -r venv
