from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import views
from .views.show_detail_view import ShowDetailView
from .views.show_list_view import ShowListView
from .views.booking import BookingView
from .views.register import Register, Profile
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepageg
    #url(r'^shows/(?P<pk>[0-9]+)/$', ShowDetailView, name = 'showPkDetailView')
    url(r'^shows/$', ShowDetailView, name = 'showPkDetailView'),
    url(r'^showlist/$', ShowListView, name = 'showListView'),
    url(r'^booking/$', BookingView, name = 'BookingView'),
    url(r'^register/$', Register, name = 'RegisterView'),
    url(r'^profile/$', Profile, name = 'profile'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='app/login.html'), name = 'login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='app/logout.html'), name = 'logout')


]

if settings.DEBUG:
    # if we are in debug mode we modify the url
    #all this to allow our media to work with the browser
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
