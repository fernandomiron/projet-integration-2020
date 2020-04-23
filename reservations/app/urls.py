from django.conf.urls import url
from django.urls import path


from .views import views
from .views import shows_list
from .views import show_detail
from .views import booking

urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^shows_list',shows_list.shows_list, name='listeshows'),
    url(r'^shows/(?P<id_article>.+)', show_detail.show, name='show'),
    url(r'^booking',booking.booking,name='booking')
]
