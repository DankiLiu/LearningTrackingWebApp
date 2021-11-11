
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Project, Entry
from .forms import ProjectForm, EntryForm


def index(request):
    """The home page for learning log"""
    print("http response from index function.")
    return render(request, 'learning_logs/index.html')


@login_required
def projects(request):
    """The page for displaying learning projects"""
    print("http response from projects function.")

    projects = Project.objects.filter(owner=request.user).order_by('start_date')
    context = {'projects': projects}
    print(context)
    
    return render(request, 'learning_logs/projects.html', context)


@login_required
def project(request, project_id):
    """The page for displaying single project"""
    print("http reponse from project function")

    project = Project.objects.get(id=project_id)
    # Make sure the topic belongs to the current user.
    if project.owner != request.user:
        raise Http404
    entries = project.entry_set.order_by('date_added')
    context = {'project': project,
               'entries': entries}
    return render(request, 'learning_logs/project.html', context)


@login_required
def new_project(request):
    """The page for adding a new project"""
    print("http response from new project function")
    if request.method != 'POST':
        # No data submitted; create a blank form
        print("Get")
        form = ProjectForm()
    else:
        # POST data submitted; process data
        print("Post")
        form = ProjectForm(request.POST)
        if form.is_valid():
            print("is valid")
            # Commit=False -> modify before commit
            new_project = form.save(commit=False)
            new_project.owner = request.user
            new_project.save()
            return HttpResponseRedirect(reverse('learning_logs:projects'))
    context = {'form:': form}
    return render(request, 'learning_logs/new_project.html', context)


@login_required
def new_entry(request, project_id):
    """The page for adding a new entry"""
    print("http response from new entry function")
    project = Project.objects.get(id=project_id)
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
            new_entry.project = project
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:project', args=[project_id]))
    context = {'project': project, 'form:': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """The page for editing a entry"""
    entry = Entry.objects.get(id=entry_id)
    project = entry.project
    if project.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; prefill form with the current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:project', args=[project.id]))
    context = {'entry': entry,
               'project': project,
               'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


