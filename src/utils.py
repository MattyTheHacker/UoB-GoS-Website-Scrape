global urls; urls = []
global invalids; invalids = []
global pdfs; pdfs = []
global docs; docs = []
global emails; emails = []
global rss; rss = []
global images; images = []

# method to get a variable from a string
def get_variable_from_name(name):
    return globals()[name]