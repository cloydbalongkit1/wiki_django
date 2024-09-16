import random

from django.shortcuts import render, redirect

from . import own_util, util
from .forms import EntryForm



def index(request):
    query = request.GET.get('q')
    if query:
        title, body = own_util.get_substring(query)
        if title is None:
            return render(request, "encyclopedia/error.html")

        return render(request, "encyclopedia/title.html", {
            "title": title,
            "body": body,
        })

    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })



def render_entry(request, entry_title):
    title, body = own_util.get_entry_content(entry_title)
    if title is None:
        return render(request, "encyclopedia/error.html")
    
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "body": body,
    })



def title(request, title):
    return render_entry(request, title)



def random_entry(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return render_entry(request, entry)



def create(request):
    if request.method == "POST":
        input_title = request.POST.get('title')
        input_text = request.POST.get('body')

        if not input_title and not input_text:
            return render(request, "encyclopedia/error.html")
        
        util.save_entry(input_title, input_text)
        return redirect('index')

    form = EntryForm()
    title = 'Create New Page'
    return render(request, "encyclopedia/entry_form.html", {'form': form, 'title': title})



def edit(request, title):
    if request.method == "POST":
        input_title = request.POST.get('title')
        input_text = request.POST.get('body')

        if not input_title and not input_text:
            return render(request, "encyclopedia/error.html")
        
        util.save_entry(input_title, input_text)
        return redirect('index')


    title, body = own_util.get_entry_content(title)
    existing_data = {
        'title': title,
        'body': f"# {title}\n{body}", 
        }
    form = EntryForm(existing_data)
    title = 'Edit New Page'
    return render(request, "encyclopedia/entry_form.html", {'form': form, 'title': title})




