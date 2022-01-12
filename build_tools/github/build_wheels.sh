#!/usr/bin/env bash

set -e
set -x

if [[ "$RUNNER_OS" == macOS ]]; then
    if [[ "$CIBW_BUILD" == *-macosx_arm64 ]]; then
        # ARM64 builds must cross compile because CI runs on x64
        export PYTHON_CROSSENV=1

        # SciPy requires 12.0 on ARM architectures to prevent kernel panics
        # https://github.com/scipy/scipy/issues/14688
        export MACOSX_DEPLOYMENT_TARGET=12.0
    else
        export MACOSX_DEPLOYMENT_TARGET=10.13
    fi

    # Provide gfortran on macOS
    # https://github.com/actions/virtual-environments/issues/2524
    # https://github.com/cbg-ethz/dce/blob/master/.github/workflows/pkgdown.yaml
    sudo ln -s /usr/local/bin/gfortran-11 /usr/local/bin/gfortran
    sudo mkdir /usr/local/gfortran
    sudo ln -s /usr/local/Cellar/gcc@11/*/lib/gcc/11 /usr/local/gfortran/lib
    gfortran --version
fi

# The version of the built dependencies are specified in the pyproject.toml file,
# while the tests are run against the most recent version of the dependencies
python -m pip install --progress-bar=off cibuildwheel
python -m cibuildwheel --output-dir wheelhouse
