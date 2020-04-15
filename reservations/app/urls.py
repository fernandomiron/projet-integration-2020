from django.conf.urls import url
from django.urls import path


from .views import views
from .views import shows
from .views import show

urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^shows_list',shows.shows_list),
    url(r'^shows/(?P<id_article>.+)', show.show),
]
