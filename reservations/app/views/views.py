from django.shortcuts import render


def home(request):
    """Default test homepage with base-template"""

    return render(request, 'app/home.html', {})
