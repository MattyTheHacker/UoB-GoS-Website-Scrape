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


def is_event(url):
    if '/ents/event/' in url:
        end_of_url = url.split('/')[-2]
        if end_of_url.isdigit():
            return True
        else:
            print("[ERROR] Invalid event url: " + url)
            return False
    if '/events/' in url:
        # check if followed by some int at the end
        end_of_url = url.split('/')[-2]
        if end_of_url.isdigit():
            return True
        else:
            print("[ERROR] Invalid event url: " + url)
            return False