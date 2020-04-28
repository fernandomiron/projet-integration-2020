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

    #url(r'^shows_list', shows_list, name='listeshows'),
    #url(r'^shows/(?P<id_article>.+)', show_detail, name='show'),
    re_path(r'shows-index/$', shows_list.ListView.as_view(), name='shows-list'), # ShowList page
    re_path(r'show/(?P<pk>[0-9]+)/$', show_detail.DetailView.as_view(), name='show-detail'), # ShowDetail page

    url(r'^booking', booking.booking, name='booking') 
]
