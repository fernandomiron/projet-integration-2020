from django.conf.urls import url

from .views import views
from .views.api import ArtistApiView

urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^api/Artist/', ArtistApiView.as_view(),name='api')
    #url(r'^api/Artist/(?P<lastname>)/$', ArtistApiView.as_view(),name='api')
    #url(r'^api/', ApiGetView.as_view(),name='api') # Vue API
]
