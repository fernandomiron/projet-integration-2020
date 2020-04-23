from django.conf.urls import url
from django.urls import path
from django.shortcuts import render
from .views.booking import booking
from .views.show_detail import show_detail
from .views.shows_list import shows_list
from .views import booking
from .views.views import home

"""from app.views import shows_list"""


urlpatterns = [
    url(r'^$', home, name='home'),  # Test homepage
    url(r'^shows_list', shows_list, name='listeshows'),
    url(r'^shows/(?P<id_article>.+)', show_detail, name='show'),
    url(r'^booking', booking.booking, name='booking') 
]
