from django.shortcuts import render, redirect
from app.models.show import Representation
from app.models.show import Location
from app.forms.representationForm import RepresentationForm, RepresentationFormMod

def CreateRepresentation(request,pk):
    """ Creating a Representation

    This view will allow creating a representation within our app if we got permissions
    """
    location = Location.objects.get(pk=pk)
    #getting the id in order to stay in the current location detailed view, matching the pk

    form = RepresentationForm(request.POST or None)
    #when the user will click at save he will POST contents
    # if there is something in POST create a form with contents if not create an empty form (NONE)


    if form.is_valid():
        location = Location.objects.get(pk=pk)
        #getting the id in order to stay in the current location detailed view, matching the pk
        form.save()
        return redirect (location) #we'll be redirect again at the current location detailed view.

    return render(request, 'app/representationCRUD.html', {'CreateRep':form})

def UpdateRepresentation(request, pk):
    """ Updating a representation

    This will allow updating a representation """

    representation = Representation.objects.get(pk=pk)
    form = RepresentationFormMod(request.POST or None, instance=representation)
    if form.is_valid():
        location = representation.location #getting the location matching the current representation.
        form.save()
        return redirect(location)

    return render(request, 'app/representationCRUD.html', {'UpdateRep':form})

def DeleteRepresentation(request, pk):
    """ Deleting a representation

    This will allow deleting a representation"""

    representation = Representation.objects.get(pk=pk)
    location = representation.location #getting the location matching the current representation.
    if request.method == 'POST':
    #if the user click on the submit button (displayed by the template)
    #he will post and confirm a delete.

        representation.delete()
        return redirect (location)
    return render (request, 'app/deleteRepresentation.html',{'representation': representation, 'location' : location})
