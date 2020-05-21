from django.shortcuts import redirect, render

from app.forms.showForm import ShowForm
from app.models.show import Show


def CreateShow(request):
    """ Creating a show.

    This view will allow creating a show within our app if we got permissions
    """

    form = ShowForm(request.POST or None)
    # when the user will click at save he will POST contents
    # if there is something in POST create a form with contents if not create an empty form (NONE)

    if form.is_valid():
        form.save()
        return redirect('show')  #nom de l'url qui correspond à la vue

    return render(request, 'app/showCRUD.html', {'createform': form})

def UpdateShow(request, pk):
    """ Updating a show

    This view will allow updating a show with if we got permissions
    """
    a_show = Show.objects.get(pk=pk) #the slug we got on the url
    form = ShowForm(request.POST or None, instance=a_show)
    #it will allow us to modify filled with the instance of the "slug show"

    if form.is_valid():
        form.save()
        return redirect('show')  #nom de l'url qui correspond à la vue

    return render(request, 'app/showCRUD.html', {'updateform': form})

def DeleteShow(request, pk):
    """ Deleting a show

    This view will delete a show if we got permission"""

    a_show = Show.objects.get(pk=pk)
    if request.method == 'POST':
    #if the user click on the submit button (displayed by the template)
    #he will post and confirm a delete.

        a_show.delete()
        return redirect ('show')
    return render (request, 'app/deleteShow.html',{'a_show': a_show})
