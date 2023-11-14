from file_type_utils import *
from list_operations_utils import *
import requests

# we need a method to check if the url is valid and doesn't contain any errors
def valid_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return True
        else:
            print("[ERROR] Url " + url +
                  " returned error code: " + str(r.status_code))
            return False
    except:
        print("[ERROR] Something went wrong with url: " + url)
        if r is not None:
            if r.status_code is not None:
                print("[ERROR] Url " + url +
                      " returned error code: " + str(r.status_code))
        return False


# method to check if we should scrape the url or not
def should_scrape(url):
    if is_email(url):
        emails.append(url)
        return False
    if is_pdf(url):
        pdfs.append(url)
        return False
    if is_doc(url):
        docs.append(url)
        return False
    if is_rss(url):
        rss.append(url)
        return False
    if is_image(url):
        images.append(url)
        return False
    if not valid_url(url):
        invalids.append(url)
        return False
    if is_event(url):
        events.append(url)
        return False
    else:
        return False