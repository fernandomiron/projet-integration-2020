from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

def shows_list(request):
        """Shows all the shows"""
    list_show = Show.object.all()
    context = {list_show : list_show}
    return render (request, 'app/shows_list.html',context)
