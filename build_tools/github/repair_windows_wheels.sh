#!/usr/bin/env bash

set -e
set -x

WHEEL=$1
DEST_DIR=$2

# Package the DLL dependencies in the wheel for windows
# delvewheel cannot mangle the libraries, stripping does not work
python -m delvewheel show "$WHEEL" && delvewheel repair -w "$DEST_DIR" "$WHEEL" --no-mangle-all
