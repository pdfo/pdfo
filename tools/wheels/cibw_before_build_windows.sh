#!/usr/bin/env bash

set -e
set -x

echo "[build]`ncompiler=mingw32" | Out-File -Encoding ASCII ~/pydistutils.cfg
