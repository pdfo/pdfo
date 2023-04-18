#!/usr/bin/env bash

set -e
set -x

# Install gfortran
PLATFORM=$(PYTHONPATH=tools python -c 'import build_support; print(build_support.get_platform())')
if [[ $PLATFORM == 'macosx-x86_64' ]]; then
    # Get the same version as scipy-wheel builds
    curl -L https://github.com/isuruf/gcc/releases/download/gcc-11.3.0-2/gfortran-darwin-x86_64-native.tar.gz -o gfortran.tar.gz
    GFORTRAN_SHA256=$(shasum -a 256 gfortran.tar.gz)
    KNOWN_SHA256='981367dd0ad4335613e91bbee453d60b6669f5d7e976d18c7bdb7f1966f26ae4  gfortran.tar.gz'
    if [ "$GFORTRAN_SHA256" != "$KNOWN_SHA256" ]; then
        exit 1
    fi
    sudo mkdir -p /opt/
    sudo tar -xv -C /opt -f gfortran.tar.gz

    # Link these into /usr/local/
    for f in libgfortran.dylib libgfortran.5.dylib libgcc_s.1.dylib libgcc_s.1.1.dylib libquadmath.dylib libquadmath.0.dylib; do
        ln -sf /opt/gfortran-darwin-x86_64-native/lib/$f /usr/local/lib/$f
    done
    ln -sf /opt/gfortran-darwin-x86_64-native/bin/gfortran /usr/local/bin/gfortran
elif [[ $PLATFORM == 'macosx-arm64' ]]; then
    curl -L https://github.com/fxcoudert/gfortran-for-macOS/releases/download/12.1-monterey/gfortran-ARM-12.1-Monterey.dmg -o gfortran.dmg
    GFORTRAN_SHA256=$(shasum -a 256 gfortran.dmg)
    KNOWN_SHA256='e2e32f491303a00092921baebac7ffb7ae98de4ca82ebbe9e6a866dd8501acdf  gfortran.dmg'
    if [ "$GFORTRAN_SHA256" != "$KNOWN_SHA256" ]; then
        exit 1
    fi
    hdiutil attach -mountpoint /Volumes/gfortran gfortran.dmg
    sudo installer -pkg /Volumes/gfortran/gfortran.pkg -target /
    type -p gfortran
fi
