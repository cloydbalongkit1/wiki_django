import random
from markdown2 import markdown

from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from . import my_util, util
from .forms import EntryForm



def index(request):
    query = request.GET.get('q')
    if query:
        content = my_util.get_substring(query)
        if content is None:
            return render(request, "encyclopedia/error.html")

        return render(request, "encyclopedia/title.html", {
            "title": query,
            "body": mark_safe(markdown(content)),
        })

    entries = util.list_entries()
    title = "Home"
    return render(request, "encyclopedia/index.html", {
        "title": title,
        "entries": entries
    })



def title(request, title):
    return my_util.render_entry(request, title)



def random_entry(request):
    entries = util.list_entries()
    return my_util.render_entry(request, random.choice(entries))



def create(request):
    if request.method == "POST":
        input_title = request.POST.get('title')
        input_text = request.POST.get('body')

        if len(input_title) < 3 and  len(input_text) < 30:
            return render(request, "encyclopedia/error.html")
        
        util.save_entry(input_title, input_text)
        return redirect('index')

    form = EntryForm()
    page_title = 'Create Wiki'
    return render(request, "encyclopedia/entry_form.html", {'form': form, 'title': page_title})



def edit(request, title):
    if request.method == "POST":
        input_title = request.POST.get('title')
        input_text = request.POST.get('body')

        if not input_title and not input_text:
            return render(request, "encyclopedia/error.html")
        
        util.save_entry(input_title, input_text)
        return redirect('index')

    content = util.get_entry(title)
    existing_data = {
        'title': title,
        'body': content, 
        }
    form = EntryForm(existing_data)
    page_title = 'Edit Wiki'
    return render(request, "encyclopedia/entry_form.html", {'form': form, 'title': page_title})


