#!/bin/bash

# Run the python script
python scrape.py

# Add all files to git
git add --all

# Commit the files
git commit -m $(date)
