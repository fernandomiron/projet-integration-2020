from django.conf.urls import url
from django.urls import path
from .views import views
from .views import booking
from .views import show


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    path('booking/', booking, name='booking'),
    path('show/', show, name='show')
]
