from django.conf.urls import url

from .views import views
from .views.api import ApiGetView

urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^api/', ApiGetView.as_view(),name='api') # Vue API
]
