
#!/usr/bin/env bash

set -e
set -x

WHEEL=$1
DEST_DIR=$2

python -m delvewheel show "$WHEEL" && delvewheel repair -w "$DEST_DIR" "$WHEEL" --no-mangle-all
