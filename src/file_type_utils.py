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
