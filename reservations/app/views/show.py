from django.shortcuts import render
from django.http import HttpResponse


def show(request):

    """Default test homepage with base-template"""

    return HttpResponse("""Je fais des test sur mes show """)
