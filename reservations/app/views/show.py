from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView

from app.models import Show

# Show ListView Class definition
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

# Show DetailView Class definition
class DetailView(DetailView):
    model = Show
    template_name = 'app/show/detail.html'
    context_object_name = 'show'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['title'] = f"show n°{ self.Show.pk }"
        return context