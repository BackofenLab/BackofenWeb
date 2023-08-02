#!/bin/bash
set -x

sudo apt-get update
sudo apt-get install -y git rsync python3 python3-pip

pip install -U bibtexparser Jinja2

pwd ls -lah
export SOURCE_DATE_EPOCH=$(git log -1 --pretty=%ct)

##############################
# Build the publication list #
##############################

cat bibtex/*.bib > bibtex/all.bib
python3 scripts/bibparser.py -i bibtex/all.bib -o _includes/pub-list.html

################
# Push changes #
################

git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${GITHUB_ACTOR}@users.noreply.github.com"

# Clone repository to a temporary directory
mainroot=$(mktemp -d)
git clone "https://token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" "${mainroot}"

pushd "${mainroot}"

# Add the generated file to the repository
cp ${GITHUB_WORKSPACE}/_includes/pub-list.html _includes/pub-list.html
git add _includes/pub-list.html

msg="Updating Publication-list for commit ${GITHUB_SHA} made on `date --date="@${SOURCE_DATE_EPOCH}" --iso-8601=seconds` from ${GITHUB_REF} by ${GITHUB_ACTOR}"
git commit -m "${msg}"

# Push the changes
git push https://token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git main

popd

exit 0