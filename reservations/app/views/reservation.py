from app.models.reservation import Reservation, RESERVATION_STATUS
from app.models import *
from django.shortcuts import redirect, render
from django.urls import reverse



def ReservationView(request):

    reservation = Reservation.objects.all() [0]
    context = {"reservation": reservation}
    template = "app/reservation.html"
    return render (request, template, context)