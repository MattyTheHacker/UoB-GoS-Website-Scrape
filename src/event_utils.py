from utils import *
from list_operations_utils import *
from file_type_utils import *


events_urls = load_events_from_file()


def get_event_details(url):
    print("[INFO] Getting details for event: " + url)
    # we want to get event title, description, date/time, organisation 
    


def get_all_event_details():
    for url in events_urls:
        