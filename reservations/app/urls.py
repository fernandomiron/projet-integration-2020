from django.conf.urls import url

from .views import views
from .feedrss import LastShowFeed


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
 
]
