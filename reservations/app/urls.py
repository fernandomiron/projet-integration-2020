from django.conf.urls import url

from .views import views
from .feedrss import LastShowFeed, RepresentationFeed, LocationFeed


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^rss/show/?', LastShowFeed(), name='rss_show'),
    url(r'^rss/representation/?', RepresentationFeed(),
        name='rss_representation'),
    url(r'^rss/location/?', LocationFeed(), name='rss_location'),
]
