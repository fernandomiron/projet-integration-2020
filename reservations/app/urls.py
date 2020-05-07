from django.conf.urls import url
from django.urls import path

from .views import views, show


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    path('show/', show.show_list, name='show'),
    path('show/<int:pk>/', show.show_detail, name='show_detail'),
]
