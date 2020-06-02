from django import forms
from app.models.show import Show

class ShowForm(forms.ModelForm):
    """ Show Form """

    class Meta:
        model = Show
        fields = ['title','poster','price','description','bookable' ]
