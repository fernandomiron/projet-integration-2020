from django.conf.urls import url
from django.contrib.auth import views as auth_views # import of the built-in Django authentication and give it a "auth_views" alias
from django.urls import path

# import of custom made views
from .views import views, authentication



urlpatterns = [
    url(r'^$', views.home, name='home'),  # Test homepage
    url(r'^signup/$', authentication.signup, name='signup'), # signup/register url for user registration
    url(r'^login/$', auth_views.LoginView.as_view(template_name = "app/login.html"), name='login'), #login url using LoginView built-in authentication
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name = "app/logout.html"), name='logout'),#logout url using LogoutView built-in authentication
    url(r'profile/$', authentication.ProfileView.as_view(), name='profile'), # user ProfileView url
    url(r'profile/update$', authentication.profileUpdate, name='profile-update'), # user ProfileView url    
    url(r'password-reset/$', auth_views.PasswordResetView.as_view(template_name = "app/password_reset_form.html"), name='password_reset'), # password reset url
    url(r'password-reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name = "app/password_reset_done.html"), name='password_reset_done'),#password reset done url
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name = "app/password_reset_confirm.html"), name='password_reset_confirm'), # password reset confirm url
    url(r'reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name = "app/password_reset_complete.html"), name='password_reset_complete'),# password reset complete url
    url(r'password/$', auth_views.PasswordChangeView.as_view(template_name = "app/password_change_form.html"), name='password_change_form'),# url for password change
    url(r'password-change/done/$', auth_views.PasswordChangeDoneView.as_view(template_name = "app/password_change_done.html"), name='password_change_done'),#confirmation url for password change
]
