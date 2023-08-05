#!/bin/bash

# cd to correct directory
cd /home/pi/Documents/UoB-GoS-Website-Scrape/src/

# Run the python script
python scrape_without_prompt.py

# Add all files to git
git add --all

# Commit the files
git commit -m '$(date)'
