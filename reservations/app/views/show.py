from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView

from app.models import Show

class ListView(ListView):
    model = Show
    template_name = 'app/show/index.html'
    context_object_name = 'shows'
    ordering = ['pk']
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['title'] = "Liste des spectacles"
        return context