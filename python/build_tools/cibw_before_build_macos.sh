#!/usr/bin/env bash

set -e
set -x

ls -l /opt/homebrew/bin
sudo ln -fs /usr/local/bin/gfortran-12 /usr/local/bin/gfortran
