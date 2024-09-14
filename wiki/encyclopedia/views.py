from django.shortcuts import render

from . import own_util, util



def index(request):
    query = request.GET.get('q')
    if query:
        title, body = own_util.get_substring(query)
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
    title, body = own_util.get_entry_content(title)
    if title is None:
        return render(request, "encyclopedia/error.html", {"title": title})
    
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "body": body,
    })


