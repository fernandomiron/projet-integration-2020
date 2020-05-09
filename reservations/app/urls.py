from django.conf.urls import url

from .views import views
from .views.api import ArtistApiView, representationApiView

urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^api/artist/', ArtistApiView.as_view(),name='apiArtist'),
    url(r'^api/representation/',representationApiView.as_view(), name='apirepresentation'),
    
]
