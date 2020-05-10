from django.conf.urls import url

from .views import views


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'api-hello-view/$', views.APINameView.as_view()),
]
