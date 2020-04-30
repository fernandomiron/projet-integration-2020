from django.conf.urls import url
from django.urls import re_path
from django.shortcuts import render
from .views.booking import booking
from .views import booking
from .views.views import home
from app.views import views, shows_list , show_detail

"""from app.views import shows_list"""

app_name = 'app'

urlpatterns = [
    url(r'^$', home, name='home'),  # Test homepage

    re_path(r'^shows_list', shows_list.Listshows.as_view(), name='listeshows'),
    re_path(r'^shows/(?P<pk>[0-9]+)/$', show_detail.DetailShow.as_view(), name='show'),

    url(r'^booking', booking.booking, name='booking') 
]
