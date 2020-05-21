from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.urls import reverse
import requests

from app.models.show import Show, Representation


def show_list(request):
    """Render list of shows"""

    query = request.GET.get("query", None)  # use get GET.get to prevent error
    shows = Show.objects.all()

    if query is not None:  # if my query is not empty i change the way how the queryset is set
        shows = Show.objects.filter(title__icontains=query)

    # function about pagination i chose to put a default value directly with GEt.get method
    paginator = Paginator(shows, 16)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    context = {
        'shows': page
    }

    return render(request, 'app/show_list.html', context)


def show_detail(request, pk):
    """Display details of one selected show based on its pk"""

    show = Show.objects.get(pk=pk)
    representations = Representation.objects.filter(show=pk)

    # print(show)

    context = {
        'show': show,
        'representations': representations
    }

    return render(request, 'app/show_detail.html', context)


def show_detail_slug(request, slug):
    """Display details of one selected show based on its slug"""
    # TODO: Function has been duplicated for slug support, must be merged

    show = Show.objects.get(slug=slug)
    representations = Representation.objects.filter(show=show.pk)

    # print(show)

    context = {
        'show': show,
        'representations': representations
    }

    return render(request, 'app/show_detail.html', context)

def external_api_show_list(request):
    """Render list of shows from our api"""
    api_url = 'http://127.0.0.1:8000' + reverse('ext-api-show')
    r = requests.get(api_url, timeout=10)
    context = {
        'shows' : r
    }
    """ i = 0
    for item in r.json():
        context[str(i)] = context.update(item)
        i += 1 """
    if r.status_code == 200:
       return render(request, 'app/external_api_show_list.html', context) 

""" class ExternalAPIShowList(ListView):
    #Render list of shows from our api
    model = Show
    api_url = 'http://127.0.0.1:8000' + reverse('ext-api-show')
    r = requests.get(api_url, timeout=10)
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shows'] = r
        return context
     """
