from django.shortcuts import render
from app.models.show import Show

def ShowDetailView(request):
    """ comment"""

    shows = Show.objects.all()
    #dicoReturn = {'listShows' : shows, 'lisRep' : rep, 'listLoc':loc}
    return render(request, 'app/show_detail.html', {'dico':shows})
