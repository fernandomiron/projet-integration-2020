from django.urls import re_path, include
from django.contrib.auth import views as auth_views

from .views import views
from app.views import views, show, representation, user

app_name = 'app'
urlpatterns = [
    re_path(r'home$', views.HomeView.as_view(), name='home'),  # Homepage

    re_path(r'login/$', user.CustomLoginView.as_view(), name='login' ), #User login page
    re_path(r'^logout/', auth_views.LogoutView.as_view(template_name='app/user/logout.html'), name='logout'), #User logout page

    re_path(r'shows-index/$', show.ListView.as_view(), name='shows-list'), # ShowList page
    re_path(r'show/(?P<pk>[0-9]+)/$', show.DetailView.as_view(), name='show-detail'), # ShowDetail page

    re_path(r'representations-index/$', representation.ListView.as_view(), name='representations-list'), # RepresentationList page
    re_path(r'representation/(?P<pk>[0-9]+)/$', representation.DetailView.as_view(), name='representation-detail'), # RepresentationDetail page
]
