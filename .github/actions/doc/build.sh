#!/usr/bin/env bash

set -e
set -x

# Install dependencies
python -m pip install --progress-bar=off .[doc]

# Build the documentation
export BUILDDIR=/tmp/pdfo-doc
(
cd doc || exit
make html
)

# Configure git
git config user.name github-actions[bot]
git config user.email github-actions[bot]@users.noreply.github.com

# Publish the documentation
git switch gh-pages || git switch -c gh-pages
git rm -r '*' 2> /dev/null || true
git clean -fxd
mv $BUILDDIR/html/* .
: > .nojekyll
echo "${{ env.CNAME }}" > CNAME
git add -A
git commit -m "${{ env.COMMIT_MESSAGE }}"
git push -f origin gh-pages
