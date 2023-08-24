"""
Utilities to send specific notifications
"""

from dotenv import load_dotenv
from git import Repo
import requests
import os

# load environment variables
load_dotenv()

# get ntfy topic from environment variables
TOPIC = os.getenv("TOPIC")

def new_website_changes_detected():
    # send a notification indicating how many new shifts are available
    requests.post(
        "https://ntfy.sh/" + TOPIC,
        data = "There are new changes detected on the Guild website!",
        headers = {
            "Title": "New Changes Detected!",
            "Click": "https://github.com/MattyTheHacker/UoB-GoS-Website-Scrape"
        }
    )

def check_for_changes():
    # check if there are any changes to the repo
    repo = Repo(os.pardir)
    if repo.is_dirty():
        # changes detected
        return True
    else:
        # no changes detected
        return False