from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
    UserCreationForm,
)

from app.models.user_profile import UserProfile

#User login form
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(label='Pseudo')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

#Registration form
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Prénom")
    last_name = forms.CharField(label="Nom")
    username = forms.CharField(label="Pseudo")
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmation du mot de passe", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

