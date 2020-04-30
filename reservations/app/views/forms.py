from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models.user_profile import UserProfile

class UserRegisterForm(UserCreationForm):
    """ class that will allow other field in our form
    than the ones already established """
    email = forms.EmailField()

    class Meta:
        model = User #the model that will be affected.
        fields = ['username', 'email', 'password1','password2']
        #This are the fields who want to be shown"

class UserUpdateForm(forms.ModelForm):
#this class to update the username and the email of the user
        email = forms.EmailField()

        class Meta:
            model = User #the model that will be affected.
            fields = ['username', 'email']
            #This are the fields who want to be shown"

class ProfileUpdateForm(forms.ModelForm):
#this class to update the profil pics of the users
    class Meta:
        model = UserProfile
        fields = ['image']
