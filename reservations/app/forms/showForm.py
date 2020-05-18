from django import forms
from app.models.show import Show

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['title', 'description','poster','bookable','price']
