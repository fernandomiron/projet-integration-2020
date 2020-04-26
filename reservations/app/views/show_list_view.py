from django.shortcuts import render
from app.models.show import Show

def ShowListView(request):
    """ Detailed view """

    shows = Show.objects.all()
    #dicoReturn = {'listShows' : shows, 'lisRep' : rep, 'listLoc':loc}
    return render(request, 'app/showlist.html', {'dico':shows})
