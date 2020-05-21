from app.models import *
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt # permet de selectionner si on prend un post ou un get en fonction de la vue? 
from paypal.standard.forms import PayPalEncryptedPaymentsForm, PayPalPaymentsForm
from app.models import *

def ppalhome(request):
    args = {}

    paypal_dict = {
        "Business" : "lionel.soupart@gmail.com",
        #reservation = Reservation.objects.get(pk=pk)
        #"amount" : reservation.price
        "amount" : "10.00",
        "currency_code": "EUR",
        #"item_name" : reservation.representation 
        "item_name" : "testlio",
        "invoice": "testinvoice",
        "notify_url": "http://localhost:8000/paypalveryhardtofind/",
        "return_url" : "http://localhost:8000/paypalreturn/",
        "cancel_return" : "http://localhost:8000/paypalreturn/",

    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    args['form'] = form

    return render('ppalhome.html',args)

@csrf_exempt
def ppalreturn(request):
    args= {'post' : request.POST,'get' : request.GET}
    return render ('paypal_return.html', args)


def ppalcancel(request):
    args= {'post' : request.POST,'get' : request.GET}
    return render ('paypal_cancel.html', args)

