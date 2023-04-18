#!/usr/bin/env bash

set -e
set -x

# Install gfortran
PLATFORM=$(PYTHONPATH=tools python -c 'import build_support; print(build_support.get_platform())')
if [[ $PLATFORM == macosx-x86_64 ]]; then
    sudo ln -fs /usr/local/bin/gfortran-12 /usr/local/bin/gfortran
elif [[ $PLATFORM == macosx-arm64 ]]; then
    curl -L -O https://github.com/isuruf/gcc/releases/download/gcc-10-arm-20210228/gfortran-darwin-arm64.tar.gz
    export GFORTRAN_SHA=f26990f6f08e19b2ec150b9da9d59bd0558261dd
    if [[ "$(shasum gfortran-darwin-arm64.tar.gz)" != "${GFORTRAN_SHA}  gfortran-darwin-arm64.tar.gz" ]]; then
        exit 1
    fi
    sudo mkdir -p /opt/
    sudo cp "gfortran-darwin-arm64.tar.gz" /opt/gfortran-darwin-arm64.tar.gz
    pushd /opt
        sudo tar -xvf gfortran-darwin-arm64.tar.gz
        sudo rm gfortran-darwin-arm64.tar.gz
    popd
    sudo ln -fs "$(find /opt/gfortran-darwin-arm64/bin -name "*-gfortran")" /usr/local/bin/gfortran
    sudo ln -fs "$(dirname "$(find /opt/gfortran-darwin-arm64/lib -name libgfortran.dylib)")" /usr/local/gfortran/lib
fi
