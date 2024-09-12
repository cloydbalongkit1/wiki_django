from django.shortcuts import render

from . import util



def get_entry_content(title):
    entry = util.get_entry(title)
    if entry is None:
        return None, None
    
    contents = entry.split()
    if len(contents) < 3:
        return None, None
    
    body = ' '.join(contents[2:])
    return contents[1], body



def index(request):
    query = request.GET.get('q')
    if query:
        title, body = get_entry_content(query)
        if title is None:
            return render(request, "encyclopedia/error.html", {"title": query})
        
        return render(request, "encyclopedia/title.html", {
            "title": title,
            "body": body,
        })

    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })



def title(request, title):
    title, body = get_entry_content(title)
    if title is None:
        return render(request, "encyclopedia/error.html", {"title": title})
    
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "body": body,
    })


