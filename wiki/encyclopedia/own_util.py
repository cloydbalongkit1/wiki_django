from . import util



def get_entry_content(title):
    """
    Getting the input of the user from the search form.
    Returns None if entry is not exist otherwise returns
    content. 
    """
    entry = util.get_entry(title)
    if entry is None:
        return None, None
    
    contents = entry.split()
    if len(contents) < 3:
        return None, None
    
    body = ' '.join(contents[2:])
    return contents[1], body



def get_substring(query):
    """ 
    Get substring input from user and return searched word
    otherwise None.
    """
    entries = util.list_entries()
    for entry in entries:
        if query.lower() in entry.lower() and len(query.lower()) > 2:
            full_entry = util.get_entry(entry)
            if full_entry:
                contents = full_entry.split()
                if len(contents) > 2:
                    body = ' '.join(contents[2:])
                    return contents[1], body
    return None, None


