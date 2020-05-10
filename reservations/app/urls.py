from django.conf.urls import url

from app.views import views, show
from app.views.locationList import LocationListView
from app.views.locationdetailed import LocationDetailedView


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage

    # Shows
    url(r'^show/?$', show.show_list, name='show'),
    url(r'^show/(?P<pk>[0-9]+)/?$', show.show_detail, name='show_detail_pk'),
    url(r'^show/(?P<slug>[a-zA-Z0-9-]+)/?$', show.show_detail_slug,
        name='show_detail_slug'),

    # Locations
    url(r'^location/$', LocationListView, name='LocationListView'),
    # url(r'^locationdet/$', LocationDetailedView,
    #     name='LocationDetailedView'),  # DetailView
    url(r'^location/(?P<pk>[0-9]+)/?$', LocationDetailedView,
        name='LocationPkView_pk'),
    url(r'^location/(?P<slug>[a-zA-Z0-9-]+)/?$', LocationDetailedView,
        name='LocationPkView_slug'),
]
