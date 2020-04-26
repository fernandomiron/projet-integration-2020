from django.conf.urls import url

from .views import views
from .views.show_detail_view import ShowDetailView

urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepageg
    #url(r'^shows/(?P<pk>[0-9]+)/$', ShowDetailView, name = 'showPkDetailView')
    url(r'^shows/$', ShowDetailView, name = 'showPkDetailView')
]
