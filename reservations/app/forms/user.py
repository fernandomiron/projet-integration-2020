from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

from app.models import UserProfile # import of UserProfile

'''
UserSignupForm custom made class
'''

class UserSignupForm(UserCreationForm):

    class Meta: #meta for model user
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

'''
UserProfileSignupForm custom made class
'''
class UserProfileSignupForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['language']
