from django.shortcuts import render
from app.models.representation import Representation
from app.models.show import Show

def BookingView(request):
    """ Booking view """

    rep = Representation.objects.all()
    return render(request, 'app/booking.html', {'dico':rep})
