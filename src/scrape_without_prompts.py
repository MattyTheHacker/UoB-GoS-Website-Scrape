# python script to scrape an entire website recursively
from file_type_utils import *
from requests.adapters import HTTPAdapter, Retry
from list_operations_utils import *
from url_utils import *
from downloader import *
from bs4 import BeautifulSoup
from notif_utils import *
import requests
import strip_emails

domain = 'https://www.guildofstudents.com'

session = requests.Session()

retries = Retry(total=10, backoff_factor=30, status_forcelist=[500, 502, 503, 504])

session.mount('http://', HTTPAdapter(max_retries=retries))

# method to scrape the site recursively
def scrape(site):
    try:
        r = session.get(site)
        soup = BeautifulSoup(r.content, 'html.parser')
        for link in soup.find_all('a'):
            url = link.get('href')
            if url is None:
                print("[ERROR] Url provided is none. This shouldn't happen...")
                continue
            if 'http' in url:
                # make it so that only urls on the domain are scraped
                if 'www.guildofstudents.com' in url:
                    if url not in urls:
                        urls.append(url)
                        print("[INFO] Found: " + url)
                        if not should_scrape(url):
                            print("[WARN] Skipping bad url: " + url)
                        else:
                            scrape(url)
            else:
                # if the url is relative, add the domain to it
                url = domain + url
                if url not in urls:
                    urls.append(url)
                    print("[INFO] Found: " + url)
                    if not should_scrape(url):
                        print("[WARN] Skipping bad url: " + url)
                    else:
                        scrape(url)
    except:
        print("[ERROR] Something went wrong with url: " + url)
        if r is not None:
            if r.status_code is not None:
                print("[ERROR] Url " + url + " returned error code: " + str(r.status_code))
        return False


if __name__ == '__main__':
    # Re-run the scrape
    scrape(domain)

    # check for duplicates
    print("[INFO] Checking for duplicates...")
    check_all_lists_for_duplicates()
    print("[INFO] Done checking for duplicates.")

    # save the urls to a file
    print("[INFO] Saving urls to file...")
    save_all_lists_to_file()
    print("[INFO] Done saving urls to file.")

    # print count of urls from each file not from the lists
    load_all_lists_from_file()
    for url_list in url_lists:
        print("[INFO] " + str(len(get_variable_from_name(url_list))) +
              " urls found in " + str(url_list) + ".txt")

    # download all the files
    download_all_files()

    # strip emails from all the files
    strip_emails.strip_and_save_to_file()

    # check for changes, if so, send a notification
    if check_for_changes():
        print("[INFO] Changes detected, sending notification...")
        new_website_changes_detected()
    else:
        print("[INFO] No changes detected.")