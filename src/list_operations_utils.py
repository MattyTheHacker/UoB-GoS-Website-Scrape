from utils import *

def remove_duplicates(list):
    return list(set(list))

url_lists = ['urls', 'invalids', 'pdfs', 'docs', 'emails', 'rss', 'images']
    
# check the url list for duplicates
def check_for_duplicate_urls(urls_list, name):
    for url in urls_list:
        if url.count(url) > 1:
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
        save_list_to_file(get_variable_from_name(url_list), '../lists/' + url_list + '.txt')


def load_all_lists_from_file():
    # the list of url lists is stored in a list, iterate over each list in the list and load the urls from the file
    for url_list in url_lists:
        with open('../lists/' + str(url_list) + '.txt', 'r') as f:
            for line in f:
                get_variable_from_name(url_list).append(line.strip())
