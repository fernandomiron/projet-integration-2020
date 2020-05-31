import random

from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from app.models.show import Show
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.serializers import serializers 


@cache_page(30 * 60)
def home(request):
    """Default test homepage with base-template"""
    # shows = Show.objects.all()[:3]
    # # shows_random = random.sample(shows,3)
    # for obj in shows[0]:
    #     print (obj.slug)

    show1 = get_object_or_404(Show, slug="antoine-henaut")
    show2 = get_object_or_404(Show, slug="cyrano-de-bergerac")
    show3 = get_object_or_404(Show, slug="sweet-and-swing")
    context = {
        'show1': show1,
        'show2': show2,
        'show3': show3,
    }
    return render(request, 'app/home.html', context)
