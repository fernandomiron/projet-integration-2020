from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

def booking(request):

    return render(request,'app/booking.html')