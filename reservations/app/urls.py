from django.conf.urls import url
from .views import views
from .views.locationList import LocationListView
from .views.locationdetailed import LocationDetailedView


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^locationlist/$', LocationListView, name = 'LocationListView'),
    url(r'^locationdet/$', LocationDetailedView, name = 'LocationDetailedView'),
    url(r'^location/(?P<slug>.*)/$',LocationDetailedView, name = 'LocationPkView')
    #url(r'^search/$', Search, name='Search' )
    #url(r'^login/$', auth_views.LoginView.as_view(template_name='app/login.html'), name = 'login'),
]
