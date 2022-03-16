#!/usr/bin/env bash

set -e
set -x

PROJECT_DIR="$1"
PLATFORM=$(PYTHONPATH=build_tools python -c "import build_support; print(build_support.get_platform())")

# Install GFortran
if [[ $RUNNER_OS == "macOS" ]]; then
    # Remove the existing gfortran
    sudo rm -rf /usr/local/gfortran/* /usr/local/bin/gfortran

    if [[ $PLATFORM == "macosx-arm64" ]]; then
        # Install gfortran using gfortran_utils
        export PLAT="arm64"
        source $PROJECT_DIR/build_tools/gfortran-install/gfortran_utils.sh
        install_arm64_cross_gfortran

        sudo ln -s "$FC" /usr/local/bin/gfortran
        sudo ln -s $(echo $FC_ARM64_LDFLAGS | awk -F\, '{ print $NF }') /usr/local/gfortran/lib
    else
        # Install gfortran (same version as the numpy-wheel builds)
        curl -L https://github.com/MacPython/gfortran-install/raw/master/archives/gfortran-4.9.0-Mavericks.dmg -o gfortran.dmg
        GFORTRAN_SHA256=$(shasum -a 256 gfortran.dmg)
        KNOWN_SHA256="d2d5ca5ba8332d63bbe23a07201c4a0a5d7e09ee56f0298a96775f928c3c4b30  gfortran.dmg"
        if [ "$GFORTRAN_SHA256" != "$KNOWN_SHA256" ]; then
            echo sha256 mismatch
            exit 1
        fi

        hdiutil attach -mountpoint /Volumes/gfortran gfortran.dmg
        sudo installer -pkg /Volumes/gfortran/gfortran.pkg -target /
        otool -L /usr/local/gfortran/lib/libgfortran.3.dylib
    fi
fi
