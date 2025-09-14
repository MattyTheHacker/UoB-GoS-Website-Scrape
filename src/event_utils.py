from utils import *
from list_operations_utils import *
from file_type_utils import *
import requests
from requests.adapters import HTTPAdapter, Retry
from bs4 import BeautifulSoup

events_urls = load_events_from_file()

session = requests.Session()

retries = Retry(total=10, backoff_factor=30, status_forcelist=[500, 502, 503, 504])

session.mount('http://', HTTPAdapter(max_retries=retries))

event_list = []

def get_organisation_from_event(url):
    # URL format: https://www.guildofstudents.com/org_ID/event_id
    # extract the org ID
    org_id = url.split("/")[4]

    # create the URL to get the org name
    org_url = "https://www.guildofstudents.com/organisation/" + org_id

    r = session.get(org_url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # get the first h1
    try:
        org_name = soup.find("h1").text.strip()
    except AttributeError:
        print("[ERROR] Could not find organisation name for org ID: " + org_id)
        org_name = "UNKNOWN_ORG_" + org_id
    return org_name

def get_event_details(url):
    print("[INFO] Getting details for event: " + url)
    # we want to get event title, description, date/time, organisation 
    # go to the url and strip the useful info from the page
    # title = first h1
    # append id,url

    # create an object to hold the event details
    event = {}

    if '/ents/event/' in url:
        # get the event id from the url
        # format: https://www.guildofstudents.com/ents/event/ID/
        event_id = url.split("/")[5]
        
        # append the event id to the event object
        event['id'] = event_id

        # if this format of URL, it's an official GUILD event
        organisation = "GUILD"

        # append the organisation to the event object
        event['organisation'] = organisation

    elif '/events/' in url:
        # format: https://www.guildofstudents.com/events/ORG_ID/EVENT_ID/
        split_url = url.split("/")
        event_id = split_url[-2]
        organisation_id = split_url[-3]

        # append the event id to the event object
        event['event_id'] = event_id

        # append the organisation id to the event object
        event['organisation_id'] = organisation_id

        # if this format of URL, it's a society event, so get the name
        organisation = get_organisation_from_event(url)

        # append the organisation to the event object
        event['organisation'] = organisation
    else:
        print("[ERROR] Invalid event url: " + url)
        return

    # append the url to the event object
    event['url'] = url

    # get the page
    r = session.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # get the first header
    title = soup.find("h1").text.strip()

    # append the title to the event object
    event['title'] = title

    # append the event object to the event_list
    event_list.append(event)


def scrape_all_events():
    # loop through the events_urls list
    for url in events_urls:
        # get the event details
        get_event_details(url)

    # save the event_list to a file
    save_list_to_file(event_list, '../lists/events_list.txt')

if __name__ == '__main__': 
    scrape_all_events()