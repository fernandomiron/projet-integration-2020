from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Default test homepage with base-template"""
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Accueil'
        return context