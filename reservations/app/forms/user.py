from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
    UserCreationForm,
    PasswordChangeForm,
    ReadOnlyPasswordHashField,
    UserChangeForm,
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

class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(label="Prénom")
    last_name = forms.CharField(label="Nom")
    username = forms.CharField(label="Pseudo")
    email = forms.EmailField(label="E-mail")
    password = ReadOnlyPasswordHashField(
        label="Mot de passe",
        disabled=True,
        widget=forms.PasswordInput(attrs={'placeholder':'**********'}),
        help_text=  "Les mots de passe bruts ne sont pas stockés,\
                    il n'y a donc aucun moyen de voir le mot de passe de cet utilisateur,\
                    mais vous pouvez le changer en utilisant ce \
                    <a href='/password-change/'>formulaire.</a>",
    )

    class Meta:
        model = User
        fields = [
            'last_name',
            'first_name',
            'username',
            'email',
            
        ]

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = []

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Ancien mot de passe", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Nouveau mot de passe", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=" Confirmation du nouveau mot de passe", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password1',
            'new_password2',            
        ]