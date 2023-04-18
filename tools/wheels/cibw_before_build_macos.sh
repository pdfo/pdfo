#!/usr/bin/env bash

set -e
set -x

# Install gfortran and pkg-config
PLATFORM=$(PYTHONPATH=tools python -c 'import build_support; print(build_support.get_platform())')
if [[ $PLATFORM == macosx-x86_64 ]]; then
    sudo ln -fs /usr/local/bin/gfortran-12 /usr/local/bin/gfortran
elif [[ $PLATFORM == macosx-arm64 ]]; then
    curl -L -O https://github.com/isuruf/gcc/releases/download/gcc-11.3.0-2/gfortran-darwin-arm64-cross.tar.gz
    export GFORTRAN_SHA=527232845abc5af21f21ceacc46fb19c190fe804
    if [[ "$(shasum gfortran-darwin-arm64-cross.tar.gz)" != "${GFORTRAN_SHA}  gfortran-darwin-arm64-cross.tar.gz" ]]; then
        exit 1
    fi
    sudo mkdir -p /opt/
    sudo cp gfortran-darwin-arm64-cross.tar.gz /opt/gfortran-darwin-arm64-cross.tar.gz
    pushd /opt
        sudo tar -xvf gfortran-darwin-arm64-cross.tar.gz
        sudo rm gfortran-darwin-arm64-cross.tar.gz
    popd
    sudo ln -fs /opt/gfortran-darwin-arm64-cross/bin/gfortran /usr/local/bin/gfortran
    brew install pkg-config
fi
