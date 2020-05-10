from django.conf.urls import url

from .views import views
from .views.api import ArtistApiView, RepresentationApiView, ShowApiView

urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^api/artist/', ArtistApiView.as_view(),name='apiArtist'), #view api artist
    url(r'^api/representation/',RepresentationApiView.as_view(), name='apirepresentation'),# view api representation
    url(r'^api/show/',ShowApiView.as_view(), name='apishow'),# view api show
]
