from django import forms
from app.models.show import Representation
from django.forms import DateTimeField

class RepresentationForm(forms.ModelForm):
    """ Representation Form """

    class Meta:
        model = Representation
        fields = ['show', 'location', 'time', 'total_seats']
