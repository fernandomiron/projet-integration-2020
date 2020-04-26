from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
)

from app.models.user_profile import UserProfile

#User login form
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(label='Pseudo')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

