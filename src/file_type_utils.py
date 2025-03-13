def is_pdf(url) -> bool:
    return '.pdf' in url


def is_email(url) -> bool:
    return 'mailto:' in url


def is_doc(url) -> bool:
    return any(extension in url for extension in ['.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx'])


def is_rss(url) -> bool:
    return 'rss' in url


def is_image(url) -> bool:
    return any(extension in url for extension in ['.jpg', '.png', '.jpeg', '.gif'])


def is_event(url) -> bool:
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
        
    return False