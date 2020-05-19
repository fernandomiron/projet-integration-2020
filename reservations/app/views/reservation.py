<<<<<<< HEAD
from app.models import *
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse



def ReservationView(request):

    reservation = Reservation.objects.all() [0]
    context = {"reservation": reservation}
    template = "app/reservation.html"
    return render (request, template, context)

def add_to reservation(request, slug):
    reservation = Reservation.object.all() [0]

    try:
         representation = Representation.objects.get (slug = slug)
    except representation.DoesNotExist:
        pass
    except:
        pass
    reservation.representation.add(product)
=======
from django.shortcuts import render


def reservation_view(request):
    return render(request, "app/reservation_view.html")
>>>>>>> d4886f816841f381fea9b8d94b5821236f70721b
