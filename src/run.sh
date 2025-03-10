#!/bin/bash

# cd to correct directory
cd "$(dirname "$0")"

# pull any changes from github
git fetch --all

git reset --hard origin/main

# Use the venv
source .venv/bin/activate

# Run the python script
python scrape_without_prompts.py

# Run the events script
python event_utilts.py

# Run the emails script
python strip_emails.py

# Add all files to git
git add --all

# Commit the files
git commit -m "update"

# Push files to github
git push
