from django.urls import re_path, include

from .views import views

from app.views import views, show, representation

app_name = 'app'
urlpatterns = [
    re_path(r'home$', views.HomeView.as_view(), name='home'),  # Homepage

    re_path(r'shows-index/$', show.ListView.as_view(), name='shows-list'), # ShowList page
    re_path(r'show/(?P<pk>[0-9]+)/$', show.DetailView.as_view(), name='show-detail'), # ShowDetail page

    re_path(r'representations-index/$', representation.ListView.as_view(), name='representations-list'), # RepresentationList page
    re_path(r'representation/(?P<pk>[0-9]+)/$', representation.DetailView.as_view(), name='representation-detail'), # RepresentationDetail page
]
