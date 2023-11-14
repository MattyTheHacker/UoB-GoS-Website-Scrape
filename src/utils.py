global urls; urls = []
global invalids; invalids = []
global pdfs; pdfs = []
global docs; docs = []
global emails; emails = []
global rss; rss = []
global images; images = []
global not_found; not_found = []
global events; events = []

# method to get a variable from a string
def get_variable_from_name(name):
    return globals()[name]