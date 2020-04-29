from django.urls import re_path, include, path
from django.contrib.auth import views as auth_views

from .views import views
from app.views import views, show, representation, user

app_name = 'app'
urlpatterns = [
    re_path(r'home$', views.HomeView.as_view(), name='home'),  # Homepage

    re_path(r'login/$', user.CustomLoginView.as_view(), name='login' ), #User login page
    re_path(r'^logout/', auth_views.LogoutView.as_view(template_name='app/user/logout.html'), name='logout'), #User logout page
    re_path(r'^register/', user.register, name='register'), #User registration page
    re_path(r'^password-reset/',
            auth_views.PasswordResetView.as_view(template_name='app/user/password_reset.html'),
            name='password_reset'), #User password reset page
    re_path(r'^password-reset/done/',
            auth_views.PasswordResetDoneView.as_view(template_name='app/user/password_reset_done.html'),
            name='password_reset_done'), #User password reset done page
    path('password-reset-confirm/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(template_name='app/user/password_reset_confirm.html'),
            name='password_reset_confirm'), #User password reset confirm page
    re_path(r'^password-reset/complete/',
            auth_views.PasswordResetCompleteView.as_view(template_name='app/user/password_reset_complete.html'),
            name='password_reset_complete'), #User password reset complete

    re_path(r'shows-index/$', show.ListView.as_view(), name='shows-list'), # ShowList page
    re_path(r'show/(?P<pk>[0-9]+)/$', show.DetailView.as_view(), name='show-detail'), # ShowDetail page

    re_path(r'representations-index/$', representation.ListView.as_view(), name='representations-list'), # RepresentationList page
    re_path(r'representation/(?P<pk>[0-9]+)/$', representation.DetailView.as_view(), name='representation-detail'), # RepresentationDetail page
]
