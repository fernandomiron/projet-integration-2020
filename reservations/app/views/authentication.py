from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm #import of UserCreationForm generic view
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView

from app.forms.user import UserSignupForm, UserProfileSignupForm, UserUpdateForm, UserProfileUpdateForm 


def signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        user_profile_form = UserProfileSignupForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid() :
            user_form.save()
            user_profile_form.save()
            username = user_form.cleaned_data.get('username')
            first_name = user_form.cleaned_data.get('first_name')
            last_name = user_form.cleaned_data.get('last_name')
            email = user_form.cleaned_data.get('email')
            raw_password = user_form.cleaned_data.get('password1')
            raw_password2 = user_form.cleaned_data.get('password2')
            language = user_profile_form.cleaned_data.get('language')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('home')
    else:
        user_form = UserSignupForm()
        user_profile_form = UserProfileSignupForm()

    context = {
        'user_form': user_form,
        'user_profile_form': user_profile_form
    }    
    return render(request, 'app/signup.html', context)


class ProfileView(TemplateView):
    # User profile View
    template_name = 'app/profile.html'

def profileUpdate(request):
    # User update profile view
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user) #with the instance arg we can get the origin value on the form's fields 
        user_profile_update_form = UserProfileUpdateForm(request.POST, instance=request.user.userprofile) # request.FILES = file data comming with the request
        if (user_update_form.is_valid() and user_profile_update_form.is_valid()):
            user_update_form.save()
            user_profile_update_form.save()
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        user_profile_update_form = UserProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'user_update_form' : user_update_form,
        'user_profile_update_form' : user_profile_update_form,
    }

    return render(request, 'app/profile_update.html', context)
