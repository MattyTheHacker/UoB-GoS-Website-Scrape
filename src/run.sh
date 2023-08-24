#!/bin/bash

# cd to correct directory
cd /home/pi/Documents/UoB-GoS-Website-Scrape/src/

# pull any changes from github
git pull

# Run the python script
python scrape_without_prompts.py

# Add all files to git
git add --all

# Commit the files
git commit -m "update"

# Push files to github
git push
