from list_operations_utils import *
import requests

fail_count = 0
fail_limit = 10

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



def increment_fail_count():
    global fail_count
    fail_count += 1


def get_fail_count():
    return fail_count

