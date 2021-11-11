"""Django URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    # url('', views.index, name='index') is wrong
    # https://stackoverflow.com/questions/31056789/difference-between-and-in-urls-django
    url(r'^$', views.index, name='index'),

    # Show all learning projects
    # url(r'^projects/$', views.projects, name='projects'),
    url(r'projects/$', views.projects, name='projects'),

    # Detail page for a singe project
    url(r'^projects/(?P<project_id>\d+)/$', views.project, name='project'),

    # Page for adding a new project
    url(r'^new_project/$', views.new_project, name='new_project'),

    # Page for adding a new entry
    url(r'^new_entry/(?P<project_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]