# python script to scrape an entire website recursively

from bs4 import BeautifulSoup
import requests

domain = 'https://www.guildofstudents.com'

fail_count = 0
fail_limit = 10

urls = []
invalids = []
pdfs = []
docs = []
emails = []
rss = []
images = []

url_lists = ['urls', 'invalids', 'pdfs', 'docs', 'emails', 'rss', 'images']

# method to scrape the site recursively
def scrape(site):
    try:
        r = requests.get(site)
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


def download_file(url, destination_folder):
    # if we fail 5 times, stop the script
    if get_fail_count() > fail_limit:
        print("[ERROR] Failed 5 times, aborting...")
        exit()

    # get the filename from the url
    filename = url.split('/')[-1]

    # remove the new line
    filename = filename.replace('\n', '')
    filename = filename.strip()

    # create the file path
    file_path = destination_folder + '/' + filename

    # download the file
    try:
        r = requests.get(url, allow_redirects=True)

        if r is None:
            print("[ERROR] Something went wrong with url: " + url)
            increment_fail_count()
            return

        if r.status_code != 200:
            print("[ERROR] Url " + url +
                  " returned error code: " + str(r.status_code))
            increment_fail_count()
            return

        # write the file to the destination folder
        with open(file_path, 'wb') as f:
            f.write(r.content)
            print("[INFO] Downloaded file: " + file_path)
    except:
        print("[ERROR] Something went wrong with url: " + url)
        increment_fail_count()
        if r is not None:
            if r.status_code is not None:
                print("[ERROR] Url " + url +
                      " returned error code: " + str(r.status_code))
        return


# function to download all the files identified by the scraper
def download_all_files():
    # first, load the data from the files, optimise this later cba now
    load_all_lists_from_file()

    # pdfs first
    for pdf in pdfs:
        download_file(pdf, "pdfs")

    # docs
    for doc in docs:
        download_file(doc, "docs")

    # images
    for image in images:
        download_file(image, "images")


# method to get a variable from a string
def get_variable_from_name(name):
    return globals()[name]

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


def is_pdf(url):
    if '.pdf' in url:
        return True
    else:
        return False


def is_email(url):
    if 'mailto:' in url:
        return True
    else:
        return False


def is_doc(url):
    if '.docx' in url:
        return True
    if '.doc' in url:
        return True
    if '.ppt' in url:
        return True
    if '.pptx' in url:
        return True
    else:
        return False


def is_rss(url):
    if 'rss' in url:
        return True
    else:
        return False


def is_image(url):
    if '.jpg' in url:
        return True
    if '.png' in url:
        return True
    else:
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
    else:
        return True


def increment_fail_count():
    global fail_count
    fail_count += 1


def get_fail_count():
    return fail_count


def remove_duplicates(list):
    return list(set(list))


# check the url list for duplicates
def check_for_duplicate_urls(urls_list, name):
    for url in urls_list:
        if urls.count(url) > 1:
            print("[WARNING] Duplicate url found: " + url)
            return True
    print("[INFO] No duplicates found in " + name)
    return False


def check_all_lists_for_duplicates():
    for url_list in url_lists:
        if check_for_duplicate_urls(get_variable_from_name(url_list), str(url_list)):
            url_list = remove_duplicates(url_list)


# save the urls to a file
def save_list_to_file(list, filename):
    with open(filename, 'w') as f:
        for item in list:
            f.write("%s" % str(item))
            f.write("\n")


def save_all_lists_to_file():
    for url_list in url_lists:
        save_list_to_file(get_variable_from_name(url_list), url_list + '.txt')


def load_all_lists_from_file():
    # the list of url lists is stored in a list, iterate over each list in the list and load the urls from the file
    for url_list in url_lists:
        with open(str(url_list) + '.txt', 'r') as f:
            for line in f:
                get_variable_from_name(url_list).append(line.strip())


if __name__ == '__main__':
    # ask the user if they'd like to re-run the scrape
    answer = input("[INFO] Would you like to re-run the scrape? (y/n) ")
    if answer == 'y':
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

    # ask if the user would like to download the files
    answer = input("[INFO] Would you like to download all files? (y/n) ")
    if answer == 'y':
        # download all the files
        download_all_files()
