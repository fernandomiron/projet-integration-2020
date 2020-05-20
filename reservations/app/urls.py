from django.conf.urls import url

from app.feedrss import LastShowFeed, LocationFeed, RepresentationFeed
from app.views import views, show
from app.views.locationList import LocationListView
from app.views.locationdetailed import LocationDetailedView

from app.views.api import (
    ArtistApiView, 
    LocationApiView, 
    RepresentationApiView, 
    ShowApiView, 
    ExternalAPI,
    ExternalAPIShowView
    )


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'api-hello-view/$', views.APINameView.as_view()),

    # Shows
    url(r'^show/?$', show.show_list, name='show'),
    url(r'^show/(?P<pk>[0-9]+)/?$', show.show_detail, name='show_detail_pk'),
    url(r'^show/(?P<slug>[a-zA-Z0-9-]+)/?$', show.show_detail_slug,
        name='show_detail_slug'),

    # Locations
    url(r'^location/$', LocationListView, name='LocationListView'),
    url(r'^location/(?P<pk>[0-9]+)/?$', LocationDetailedView,
        name='LocationPkView_pk'),
    url(r'^location/(?P<slug>[a-zA-Z0-9-]+)/?$', LocationDetailedView,
        name='LocationPkView_slug'),

    # API
    url(r'^api/artist/', ArtistApiView.as_view(), name='api_artist'),
    url(r'^api/show/', ShowApiView.as_view(), name='api_show'),
    url(r'^api/representation/', RepresentationApiView.as_view(),
        name='api_representation'),
    url(r'^api/location/', LocationApiView.as_view(), name='api_location'),

    #External API
    url(r'^external-api/show2', ExternalAPI.as_view() , name='ext-api-show-2'),
    url(r'^external-api/show', ExternalAPIShowView.as_view(), name='ext-api-show'),
   
    

    # RSS Feeds
    url(r'^rss/show/?', LastShowFeed(), name='rss_show'),
    url(r'^rss/representation/?', RepresentationFeed(),
        name='rss_representation'),
    url(r'^rss/location/?', LocationFeed(), name='rss_location'),
]
