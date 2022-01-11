#!/usr/bin/env bash

set -e
set -x

# Create a Conda environment for uploading the artifacts
export PATH=$CONDA/bin:$PATH
conda create -n upload -y python=3.9
source activate upload
conda install -y anaconda-client

# Upload the artifacts and force replacement if the remote files already exist
anaconda -t "$ANACONDA_TOKEN" upload --force -u pdfo dist/artifact/*
