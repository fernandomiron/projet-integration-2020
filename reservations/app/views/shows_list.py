from django.shortcuts import render
from django.http import HttpResponse

def shows_list(request):

    return render (request,'app/shows_list.html',{})


