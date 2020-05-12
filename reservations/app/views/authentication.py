from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm #import of UserCreationForm generic view
from django.shortcuts import render, redirect

from app.forms.user import UserSignupForm, UserProfileSignupForm



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