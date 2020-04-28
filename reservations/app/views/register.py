from django.shortcuts import render, redirect

from django.contrib import messages
#Using this for flash message alert

from django.contrib.auth.forms import UserCreationForm
#class that handle all the user's entry

def Register(request):
    if request.method == 'POST':
    #testing the kind of the request
        form = UserCreationForm(request.POST)
        #Catching all user's entries

        if form.is_valid():
        #testing the validity of the user's entries (django is_valid does that itself)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render (request, 'app/register.html', {'form':form})
