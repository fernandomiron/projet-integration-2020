from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import views
from .views.show_detail_view import ShowDetailView
from .views.show_list_view import ShowListView
from .views.booking import BookingView
from .views.register import Register

urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepageg
    #url(r'^shows/(?P<pk>[0-9]+)/$', ShowDetailView, name = 'showPkDetailView')
    url(r'^shows/$', ShowDetailView, name = 'showPkDetailView'),
    url(r'^showlist/$', ShowListView, name = 'showListView'),
    url(r'^booking/$', BookingView, name = 'BookingView'),
    url(r'^register/$', Register, name = 'RegisterView'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='app/login.html'), name = 'login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='app/logout.html'), name = 'logout')


]
