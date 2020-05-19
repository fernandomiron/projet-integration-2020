from app.models import *
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse

def reservation_view(request):

    reservation = Reservation.objects.all() [0]
    context = {"reservation": reservation}
    template = "app/reservation_view.html"
    return render(request, template, context, "app/reservation_view.html")
