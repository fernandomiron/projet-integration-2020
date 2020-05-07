from app.models.show import Show
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render


def show_list(request):
    """ This methode allow to list all shows """
    # use get GET.get to prevent error
    query = request.GET.get("query", None)
    shows = Show.objects.all()

    # if my query is not empty i change the way how the queryset is set
    if query is not None:
        shows = Show.objects.filter(title__icontains=query)

    # function about pagination i chose to put a default value directly with GEt.get method
    paginator = Paginator(shows, 16)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context = {
        'shows': page
    }
    return render(request, 'app/show_list.html', context)
