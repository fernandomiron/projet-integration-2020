from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from app.models import Show

# Show ListView Class definitio
class Listshows(ListView):
    """explication"""
    model = Show
    template_name = 'app/shows/shows_list.html'
    context_object_name = 'shows'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """def context"""
        context = super(Listshows, self).get_context_data(**kwargs)
        context['title'] = "Liste des spectacles"
        return context