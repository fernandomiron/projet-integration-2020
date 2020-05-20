from app.models import *
from django.shortcuts import redirect, render, render_to_response
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt # permet de selectionner si on prend un post ou un get en fonction de la vue? 
from paypal.standard.forms import PayPalEncryptedPaymentsForm
from app.models import *

def ppalhome(request):
    args{}

    paypal_dict = {
        "Business" : "lionel.soupart@gmail.com",
        #reservation = Reservation.objects.get(pk=pk)
        #"amount" : reservation.price
        "amount" : "10.00",
        "currency_code": "USD"
        #"item_name" : reservation.representation 
        "item_name" : "testlio",
        "invoice": "testinvoice",
        "notify_url": "http://localhost:8000/paypalveryhardtofind/",
        "return_url" : "http://localhost:8000/paypalreturn/",
        "cancel_return" : "http://localhost:8000/paypalreturn/",

    }
