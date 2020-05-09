from django.conf.urls import url

from .views import views
from .views.api import ArtistApiView

urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^api/Artist/', ArtistApiView.as_view(),name='apiArtist'),
    url(r'^api/Artist/(?P<lastname>[a-z])/$', ArtistApiView.as_view(),name='apiArtistname')
]
