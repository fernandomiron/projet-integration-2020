from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from app.models.show import *

def show_detail (request) :
    detail_show = Show.objects.all()
    context = {"detail_show" : detail_show}
    return render (request, 'app/show_details.html', context)
    

