#!/usr/bin/env bash

set -e
set -x

brew install gcc@12
brew link --overwrite gcc@12
ls -l /usr/local/bin
# sudo ln -fs /usr/local/bin/gfortran-12 /usr/local/bin/gfortran
