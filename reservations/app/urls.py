from django.conf.urls import url
from django.urls import path
from django.shortcuts import render
from .views.booking import booking
from .views import booking
from .views.views import home
from app.views import views, shows_list , show_detail

"""from app.views import shows_list"""

app_name = 'app'

urlpatterns = [
    url(r'^$', home, name='home'),  # Test homepage
    url(r'^shows_list', shows_list, name='listeshows'),
    url(r'^shows/(?P<id_article>.+)', show_detail, name='show'),
    url(r'^booking', booking.booking, name='booking') 
]
