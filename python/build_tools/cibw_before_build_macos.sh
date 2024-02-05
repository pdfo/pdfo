#!/usr/bin/env bash

set -e
set -x

ARCH=$(uname -m)
if [ "$ARCH" == "arm64" ]; then
    sudo ln -fs /opt/homebrew/bin/gfortran-12 /opt/homebrew/bin/gfortran
else
    sudo ln -fs /usr/local/bin/gfortran-12 /usr/local/bin/gfortran
fi
