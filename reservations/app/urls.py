from django.conf.urls import url

from .views import views
from .feedrss import LastShowFeed, RepresentationFeed, LocationFeed


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^showrss/',LastShowFeed(), name='showrss'),
    url(r'^representationrss/',RepresentationFeed(), name='representationrss'),
    url(r'^locationrss/',LocationFeed(), name='locationrss'),
]
