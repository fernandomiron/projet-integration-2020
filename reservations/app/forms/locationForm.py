from django import forms
from app.models.location import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['designation', 'address','locality','phone','website']
