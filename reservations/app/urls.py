from django.conf.urls import url
from django.urls import path
from .views.locationList import LocationListView
from .views.locationdetailed import LocationDetailedView

from .views import views, show


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    path('show/', show.show_list, name='show'),
    path('show/<int:pk>/', show.show_detail, name='show_detail'),
    url(r'^locationlist/$', LocationListView, name = 'LocationListView'),
    url(r'^locationdet/$', LocationDetailedView, name = 'LocationDetailedView'),
    url(r'^location/(?P<slug>.*)/$',LocationDetailedView, name = 'LocationPkView')
]
