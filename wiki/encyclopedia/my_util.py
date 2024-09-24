from django.shortcuts import render
from django.utils.safestring import mark_safe

from markdown2 import markdown

from . import util



def get_substring(query):
    """
    Gets subtring input. Returns the appox seached query.
    """
    entries = util.list_entries()
    for entry in entries:
        if query.lower() in entry.lower() and len(query.lower()) > 2:
            return util.get_entry(entry)
                
    return None



def render_entry(request, title):
    """
    Returns a rendered content.
    """
    content = util.get_entry(title)
    if title not in util.list_entries():
        return render(request, "encyclopedia/error.html")
    
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "body": mark_safe(markdown(content)),
    })


