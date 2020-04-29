from django.shortcuts import render, redirect

from django.contrib import messages
#Using this for flash message alert

from .forms import UserRegisterForm
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
    return render (request, 'app/profile.html')
