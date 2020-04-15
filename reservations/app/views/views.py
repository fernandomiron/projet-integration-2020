from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Default test homepage with base-template"""

    return render(request, 'app/base.html', {})


