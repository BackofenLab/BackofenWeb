#!/bin/bash
set -x

sudo apt-get update
sudo apt-get install -y git rsync ruby-full build-essential zlib1g-dev

pwd ls -lah
export SOURCE_DATE_EPOCH=$(git log -1 --pretty=%ct)

##################
# Install Jekyll #
##################

export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"

gem install jekyll bundler


#####################
# Build the website #
#####################

bundle install
bundle exec jekyll build
mv _site/docs/index.html _site/index.html

######################
# Deploy the website #
######################

git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${GITHUB_ACTOR}@users.noreply.github.com"

docroot=$(mktemp -d)
rsync -av "_site/" "${docroot}/"

pushd "${docroot}"

git init
git remote add deploy "https://token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
git checkout -b gh-pages

cat > README.md <<EOF

# README
This branch is a cache for the website served from https://BackofenLab.github.io/BackofenWeb/ .

EOF


git add .

msg="Updating Website for commit ${GITHUB_SHA} made on `date --date="@${SOURCE_DATE_EPOCH}" --iso-8601=seconds` from {GITHUB_REF} by {GITHUB_ACTOR}"
git commit -am "${msg}"

# deploy to gh-pages
git push https://token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git gh-pages --force

popd

exit 0


