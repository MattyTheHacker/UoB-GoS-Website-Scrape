import list_operations_utils

dirty_email_urls = list_operations_utils.load_list_from_file('../lists/emails.txt')

cleaned_emails = []


def strip_emails_from_urls():
    for url in dirty_email_urls:
        # find mailto: in the url, remove everything before this
        if url.find('mailto:') != -1:
            url = url[url.find('mailto:') + 7:]
        # find ? in the url, remove everything after this
        if url.find('?') != -1:
            url = url[:url.find('?')]
        
        cleaned_emails.append(url)

def remove_duplicates():
    cleaned_emails = list(dict.fromkeys(cleaned_emails))

def strip_and_save_to_file():
    strip_emails_from_urls()
    remove_duplicates()
    list_operations_utils.save_list_to_file(cleaned_emails, '../lists/cleaned_emails.txt')

if __name__ == '__main__':
    strip_and_save_to_file()