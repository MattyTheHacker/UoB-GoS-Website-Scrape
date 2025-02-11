#!/bin/bash

# cd to correct directory
cd /home/cogs/Documents/UoB-GoS-Website-Scrape/src/

# pull any changes from github
git pull -X theirs

# Run the python script
python scrape_without_prompts.py

# Run the events script
python event_utilts.py

# Add all files to git
git add --all

# Commit the files
git commit -m "update"

# Push files to github
git push
