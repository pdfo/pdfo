#!/usr/bin/env bash

set -e
set -x

# Install gfortran
PLATFORM=$(PYTHONPATH=tools python -c 'import build_support; print(build_support.get_platform())')
if [[ $PLATFORM == 'macosx-x86_64' ]]; then
    sudo ln -fs /usr/local/bin/gfortran-12 /usr/local/bin/gfortran
elif [[ $PLATFORM == 'macosx-arm64' ]]; then
    echo 'To do'
fi
