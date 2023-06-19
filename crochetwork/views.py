
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Category, Entry
from .forms import CategoryForm, EntryForm


def index(request):
    """The home page for learning log"""
    print("http response from index function.")
    return render(request, 'work_page/index.html')


@login_required
def categories(request):
    """The page for displaying categories, a button for adding a new one"""
    print("http response from projects function.")

    categories = Category.objects.filter(owner=request.user).order_by('start_date')
    context = {'categories': categories}
    print(context)
    
    return render(request, 'work_page/categories.html', context)


@login_required
def category(request, category_id):
    """The page for displaying single project"""
    print("http reponse from project function")

    category = Category.objects.get(id=category_id)
    # Make sure the topic belongs to the current user.
    if category.owner != request.user:
        raise Http404
    entries = category.entry_set.order_by('date_added')
    context = {'category': category,
               'entries': entries}
    return render(request, 'work_page/category.html', context)


@login_required
def new_category(request):
    """The page for adding a new project"""
    print("http response from new project function")
    # todo: if a new category is created, create a new file to save img
    if request.method != 'POST':
        # No data submitted; create a blank form
        print("Get - create form")
        form = CategoryForm()
    else:
        # POST data submitted; process data
        print("Post - process")
        form = CategoryForm(request.POST)
        print(form.clean().values())
        if form.is_valid():
            print("is valid")
            # Commit=False -> modify before commit
            new_cat = form.save(commit=False)
            new_cat.owner = request.user
            new_cat.save()
            return HttpResponseRedirect(reverse('crochetwork:categories'))
        else:
            messages.error(request, "Error by creating the category")
    context = {'form:': form}
    return render(request, 'work_page/add_category.html', context)


@login_required
def new_entry(request, category_id):
    """The page for adding a new entry"""
    print("http response from new entry function")
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        # POST data submitted; process data
        entryform = EntryForm(request.POST, request.FILES)
        print(entryform)
        if entryform.is_valid():
            print("entry form is valid")
            new_entry = entryform.save(commit=False)
            new_entry.category = category
            new_entry.save()
            return HttpResponseRedirect(reverse('crochetwork:category', args=[category_id]))
        else:
            print("entry form is not valid")
    else:
        # No data submitted; create a blank form
        entryform = EntryForm()
    context = {'category': category, 'entryform:': entryform}
    return render(request, 'work_page/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """The page for editing a entry"""
    entry = Entry.objects.get(id=entry_id)
    category = entry.category
    if category.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; prefill form with the current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('crochetwork:category', args=[category.id]))
    context = {'entry': entry,
               'category': category,
               'form': form}
    return render(request, 'work_page/edit_entry.html', context)


