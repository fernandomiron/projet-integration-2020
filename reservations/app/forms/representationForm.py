from django import forms
from app.models.show import Representation
from django.forms import DateTimeField

class RepresentationForm(forms.ModelForm):
    """ Representation Form """
    time = forms.DateTimeField(label='Time', widget=forms.TextInput(attrs={"placeholder": "JJ/MM/AAAA HH:mm:ss"}))

    class Meta:
        model = Representation
        fields = ['show', 'location', 'time','total_seats','available_seats']

class RepresentationFormMod(forms.ModelForm):
    """ Representation Form """

    class Meta:
        model = Representation
        fields = ['show', 'location']
