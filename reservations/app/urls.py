from django.conf.urls import url

from .views import views
from .views.api import ArtistApiView, RepresentationApiView, ShowApiView, LocationApiView

urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^api/artist/', ArtistApiView.as_view(),name='api_artist'), #view api artist
    url(r'^api/representation/',RepresentationApiView.as_view(), name='api_representation'),# view api representation
    url(r'^api/show/',ShowApiView.as_view(), name='api_show'),# view api show
    url(r'^api/location/',LocationApiView.as_view(), name='api_location'),# view api location

]
