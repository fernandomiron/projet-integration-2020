from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from ..models.show import Show


def show(request):
    """Default test homepage with base-template"""
    template = loader.get_template('app/show_list.html')
    shows = Show.objects.all()
    context = {
        'title': 'un title  ',
        'shows': shows,
    }
    return HttpResponse(template.render(context, request))


def show_details(request, id):
    template = loader.get_template('app/show_details.html')
    try:
        showdetails = Show.objects.get(id=id)
    except Show.DoesNotExist:
        raise Http404
    context = {
        'showdetails': showdetails,
    }
    return HttpResponse(template.render(context, request))
