from django.db import models
from django.urls import reverse

class Representation(models.Model):
    """ Representation model """

    show_id = models.ForeignKey('Show', on_delete=models.CASCADE, null=True, blank=True)
    when = models.DateTimeField()
    location_id = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True )

    class Meta:
        """ Representation meta definition """
        verbose_name = "Representation"
        verbose_name_plural = "Representations"

    """ String representation of Representation """
    def __str__(self):
        return f'({self.pk})'
