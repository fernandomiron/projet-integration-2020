from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

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

'''
UserUpdateForm custom made class
'''

class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = [
            'last_name',
            'first_name',
            'username',
            'email',
        ]

'''
UserProfileUpdateForm custom made class
'''
class UserProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['language']