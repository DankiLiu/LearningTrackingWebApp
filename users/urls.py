"""Django URL patterns for users."""

from django.urls import path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import include

from . import views


urlpatterns = [
    # Login page
    path(r'^login/$', LoginView.as_view(template_name='users/login.html',
                                        ), name='login'),
    # path(r'^login/$', views.my_login, name='login'),
    path(r'^logout/$', views.logout_view, name='logout'),
    path(r'^register/$', views.register, name='register'),
]