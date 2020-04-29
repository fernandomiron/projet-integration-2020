from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from app.forms.user import CustomAuthenticationForm, UserRegisterForm

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
            return redirect('app:login')
    else :
        form = UserRegisterForm()

    context = {
        'form' : form,
        'title' : 'Inscription',
    }

    return render(request, 'app/user/register.html', context)