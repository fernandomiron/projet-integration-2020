from django.urls import re_path, include

from .views import views

from app.views import views, show

app_name = 'app'
urlpatterns = [
    re_path(r'home$', views.HomeView.as_view(), name='home'),  # Homepage

    re_path(r'shows-index/$', show.ListView.as_view(), name='shows-list'), # ShowList page
    re_path(r'show/(?P<pk>[0-9]+)/$', show.DetailView.as_view(), name='show-detail'), # ShowDetail page
]
