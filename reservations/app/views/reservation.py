from app.models import *
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt # permet de selectionner si on prend un post ou un get en fonction de la vue? 
from paypal.standard.forms import PayPalEncryptedPaymentsForm, PayPalPaymentsForm
from app.models import *
from django.conf import settings
from django.contrib import messages
from decimal import Decimal

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

def representation_detail(request, pk):

    representation = get_object_or_404(Representation, pk=pk)
    context = {"representation": representation}

    return render(request, "app/reservation_view.html", context)
