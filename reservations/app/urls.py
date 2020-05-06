from django.conf.urls import url
from django.contrib.auth import views as auth_views # import of the built-in Django authentication and give it a "auth_views" alias
from django.urls import path


from .views import views


urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^login/$', auth_views.LoginView.as_view(template_name = "app/login.html"), name='login'), #login url using LoginView built-in authentication
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name = "app/logout.html"), name='logout'),#logout url using LogoutView built-in authentication
]
