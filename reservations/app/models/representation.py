from django.db import models
from django.urls import reverse


class Representation(models.Model):

    """ Representation model definition """
    show_id = models.ForeignKey("Locality", on_delete=models.SET_NULL, null=True)
    when = models.DateField(auto_now=False, auto_now_add=False)
    location_id = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
    """ Representation meta definition """
    class Meta:
        verbose_name = "Representation"
        verbose_name_plural = "Representations"

    """ String representation of Representation """
    def __str__(self):
        return f'({self.pk})'
