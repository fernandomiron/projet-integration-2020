from django.shortcuts import render, redirect

from django.contrib import messages
#Using this for flash message alert

from .forms import UserRegisterForm
#Class I created in forms.py that'll handle all the user's entries


def Register(request):
    if request.method == 'POST':
    #testing the kind of the request

        form = UserRegisterForm(request.POST)
        #Catching all user's entries

        if form.is_valid():
        #testing the validity of the user's entries (django is_valid does that itself)
            form.save() #saving the new user in the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render (request, 'app/register.html', {'form':form})
