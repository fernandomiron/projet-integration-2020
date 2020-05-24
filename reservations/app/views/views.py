from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.serializers import serializers 


def home(request):
    """Default test homepage with base-template"""

    return render(request, 'app/home.html', {})
