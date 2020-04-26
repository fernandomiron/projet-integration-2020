from django.contrib import messages
from django.contrib.auth.views import LoginView

from app.forms.user import CustomAuthenticationForm

class CustomLoginView(LoginView):
    template_name = 'app/user/login.html'
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        if form.is_valid():
            messages.success(self.request, "Vous êtes bien connecté")
        return super().form_valid(form)
