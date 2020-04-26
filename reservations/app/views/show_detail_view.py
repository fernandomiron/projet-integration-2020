from django.shortcuts import render
from app.models.representation import Representation

def ShowDetailView(request):
    """ Detailed view """

    rep = Representation.objects.all()
    #dicoReturn = {'listShows' : shows, 'lisRep' : rep, 'listLoc':loc}
    return render(request, 'app/show_detail.html', {'dico':rep})
