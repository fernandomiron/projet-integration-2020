from django.urls import re_path, include
from django.conf.urls import url

from .views import views

from app.views import show

app_name = 'app'
urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    re_path(r'^shows-index/$', show.ListView.as_view(), name='shows-list'), # ShowList page
]
