from django.views.generic import ListView, DetailView

from app.models import Representation


# representation ListView Class definition
class ListView(ListView):
    model = Representation
    template_name = 'app/representation/index.html'
    context_object_name = 'representations'
    ordering = ['when']
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['title'] = "Liste des prochains spectacles"
        return context

# Representation DetailView Class definition
class DetailView(DetailView):
    model = Representation
    template_name = 'app/representation/detail.html'
    context_object_name = 'representation'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context

# 