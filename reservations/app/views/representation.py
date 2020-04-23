from django.views.generic import DetailView

from app.models import Representation

# Show DetailView Class definition
class DetailView(DetailView):
    model = Representation
    template_name = 'app/representation/detail.html'
    context_object_name = 'representation'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context