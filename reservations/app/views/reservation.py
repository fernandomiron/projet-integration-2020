from app.models import *
from django.shortcuts import redirect, render
from django.urls import reverse


def reservationglobalview(request):


    reservation = Reservation.objects.all()[3]

    print(reservation)

    context = {"reservation": reservation}
    template = "app/reservationview.html"

    return render(request, template, context)


def reservationview(request,pk):

    
    reservation = Reservation.objects.get(pk=pk)
    qty = request.GET.get('qty')
    if qty == '':
        reservation.seats = 1
    else:
        reservation.seats=float(qty)
    
    reservation.save()
    # print(reservation)

    context = {"reservation": reservation}
    template = "app/reservationview.html"

    return render(request, template, context)