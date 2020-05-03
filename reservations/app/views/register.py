from django.shortcuts import render, redirect
from app.models.user_profile import User

from django.contrib import messages
#Using this for flash message alert

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
#Class I created in forms.py that'll handle all the user's entries

from django.contrib.auth.decorators import login_required
#to make sure we're logged in before displaying user content.

def Register(request):
    if request.method == 'POST':
    #testing the kind of the request

        form = UserRegisterForm(request.POST)
        #Catching all user's entries

        if form.is_valid():
        #testing the validity of the user's entries (django is_valid does that itself)
            form.save() #saving the new user in the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ton compte a été créée, {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render (request, 'app/register.html', {'form':form})

@login_required
def Profile(request):
#To update and save the new data of the user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ton compte a été modifié ')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'u_form': u_form,
    'p_form': p_form
    }
    return render (request, 'app/profile.html', context)
