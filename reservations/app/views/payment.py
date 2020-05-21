from app.models import *
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt # permet de selectionner si on prend un post ou un get en fonction de la vue? 
from paypal.standard.forms import PayPalEncryptedPaymentsForm, PayPalPaymentsForm
from app.models import *
from django.conf import settings
from django.contrib import messages
from decimal import Decimal

def ppalhome(request):

    idreservation = request.GET.get('idreservation')
    reservation = Reservation.objects.get(pk=idreservation)
    host = request.get_host()

    args = {}

    paypal_dict = {
        'business' : settings.PAYPAL_RECEIVER_EMAIL,
        #reservation = Reservation.objects.get(pk=pk)
        #"amount" : reservation.price
        "amount" : reservation.price,
        "currency_code": "EUR",
        #"item_name" : reservation.representation 
        "item_name" : reservation.representation.show.title,
        "invoice": reservation.pk,
        "notify_url": 'http://{}{}'.format(host, reverse('paypal')),
        "return_url" : 'http://{}{}/{}'.format(host, reverse('paypalreturn'),reservation.pk),
        "cancel_return" : 'http://{}{}/{}'.format(host, reverse('paypalcancel'),reservation.pk),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    args['form'] = form
    return render(request,'app/ppalhome.html',args)


@csrf_exempt
def ppalreturn(request,pk):
    reservation = Reservation.objects.get(pk=pk)
    
    return render (request,'app/paypal_return.html',)


def ppalcancel(request,pk):
    reservation = Reservation.objects.get(pk=pk)

    return render (request,'app/paypal_cancel.html', )
