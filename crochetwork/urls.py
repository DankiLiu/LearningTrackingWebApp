"""Django URL patterns for work_page."""

from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    # Home page
    # url('', views.index, name='index') is wrong
    # https://stackoverflow.com/questions/31056789/difference-between-and-in-urls-django

    url(r'^$', views.index, name='index'),

    # Show all learning projects
    # url(r'^projects/$', views.projects, name='projects'),
    url(r'categories/$', views.categories, name='categories'),

    # Detail page for a singe project
    url(r'^categories/(?P<category_id>\d+)/$', views.category, name='category'),

    # Page for adding a new project
    url(r'^new_category/$', views.new_category, name='new_category'),

    # Page for adding a new entry
    url(r'^new_entry/(?P<category_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]