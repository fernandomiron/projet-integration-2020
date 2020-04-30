from django.conf.urls import url
from django.urls import path
from .views import views
from .views import show,show_details, representation


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    path('show/', show, name='show'),
    path('show/<int:id>', show_details, name='show_details'),
    path('representation/<int:representation_id>', representation, name='representation')
]
