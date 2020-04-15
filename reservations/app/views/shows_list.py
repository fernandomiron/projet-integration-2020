from django.shortcuts import render
from django.http import HttpResponse

def shows_list(request):

    return HttpResponse (
    "vue comprenant l'ensemble des shows" )


