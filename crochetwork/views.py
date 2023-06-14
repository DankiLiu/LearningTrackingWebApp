
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Category, Entry
from .forms import CategoryForm, EntryForm


def index(request):
    """The home page for learning log"""
    print("http response from index function.")
    return render(request, 'work_page/index.html')


@login_required
def categories(request):
    """The page for displaying learning projects"""
    print("http response from projects function.")

    categories = Category.objects.filter(owner=request.user).order_by('start_date')
    context = {'categories': categories}
    print(context)
    
    return render(request, 'work_page/add_category.html', context)


@login_required
def category(request, project_id):
    """The page for displaying single project"""
    print("http reponse from project function")

    category = Category.objects.get(id=project_id)
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
    if request.method != 'POST':
        # No data submitted; create a blank form
        print("Get")
        form = CategoryForm()
    else:
        # POST data submitted; process data
        print("Post")
        form = CategoryForm(request.POST)
        if form.is_valid():
            print("is valid")
            # Commit=False -> modify before commit
            new_cat = form.save(commit=False)
            new_cat.owner = request.user
            new_cat.save()
            return HttpResponseRedirect(reverse('crochetwork:categories'))
    context = {'form:': form}
    return render(request, 'work_page/add_category.html', context)


@login_required
def new_entry(request, category_id):
    """The page for adding a new entry"""
    print("http response from new entry function")
    category = Category.objects.get(id=category_id)
    if request.method != 'POST':
        # No data submitted; create a blank form
        print("Get")
        form = EntryForm()
    else:
        # POST data submitted; process data
        print("Post")
        form = EntryForm(request.POST)
        if form.is_valid():
            print("is valid")
            new_entry = form.save(commit=False)
            new_entry.category = category
            new_entry.save()
            return HttpResponseRedirect(reverse('crochetwork:category', args=[category_id]))
    context = {'category': category, 'form:': form}
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


