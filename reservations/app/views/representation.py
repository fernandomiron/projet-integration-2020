from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from ..models.representation import Representation


def representation(request, representation_id):
    """This a views for representig a representation"""
    template = loader.get_template('app/representation.html')
    try:
        representation = Representation.objects.get(id=representation_id)
    except Representation.DoesNotExist:
        raise Http404

    context = {
        'representation': representation
    }
    return HttpResponse(template.render(context, request))
