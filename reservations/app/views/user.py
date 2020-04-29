from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from app.forms.user import CustomAuthenticationForm, UserRegisterForm, UserUpdateForm, UserProfileUpdateForm, CustomPasswordChangeForm

# Custom login generic view 
class CustomLoginView(LoginView):
    template_name = 'app/user/login.html'
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        if form.is_valid():
            messages.success(self.request, "Vous êtes bien connecté")
        return super().form_valid(form)

# Register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Votre compte a été créé { username }! Vous pouvez maintenant vous connectez.')
            return redirect('login')
    else :
        form = UserRegisterForm()

    context = {
        'form' : form,
        'title' : 'Inscription',
    }

    return render(request, 'app/user/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) #with the instance arg we can get the origin value on the form's fields 
        user_profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile) # request.FILES = file data comming with the request
        if (user_form.is_valid() and user_profile_form.is_valid()):
            user_form.save()
            user_profile_form.save()
            messages.success(request, f'Votre compte a bien été mis à jour!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        user_profile_form = UserProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'user_form' : user_form,
        'user_profile_form' : user_profile_form,
    }

    return render(request, 'app/user/profile.html', context)

