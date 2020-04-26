from django.conf.urls import url

from .views import views
from .views.show_detail_view import ShowDetailView
from .views.show_list_view import ShowListView
from .views.booking import BookingView

urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepageg
    #url(r'^shows/(?P<pk>[0-9]+)/$', ShowDetailView, name = 'showPkDetailView')
    url(r'^shows/$', ShowDetailView, name = 'showPkDetailView'),

    url(r'^showlist/$', ShowListView, name = 'showListView'),
    url(r'^booking/$', BookingView, name = 'BookingView')

]
