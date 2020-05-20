from app.models import *
from django.shortcuts import redirect, render
from django.urls import reverse

#def reservationview(request):
   # try:
   #     the_id = request.session['reservation_pk']
    #except:
   #     the_id = None
    #if the_id:
    #    reservation = Reservation.objects.get(pk=the_id)
    #    context = {"reservation": reservation}
    #else:
    #    reservation = Reservation.objects.all()[0]
    #    context = {"reservation": reservation}
   # template = "app/reservationview.html"
   # return render(request, template, context)

#def updatereservationview2(request,id, qty):
    #try:
    #    qty = request.GET.get('qty')
    #    updateseats = True
    #except:
    #    qty = ''
    #    updateseats = False
    #try: 
    #    the_id = request.session['reservation_pk']
    #except:
    #    new_reservation = Reservation()
    #    new_reservation.save()
    #    request.session['reservation_pk'] = new_reservation.pk
    #    the_id = new_reservation.pk

    #reservation = Reservation.objects.get(pk=id)
    

    #if qty == '':
    #    reservation.seats = 55
    #elif qty:
    #    reservation.seats = qty
    #    reservation.save()

    #template = "app/reservationview.html"
    #return render(request, template, context)

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