from django.db import models
from django.urls import reverse

class Locality(models.Model):

    """ Locality model definition """
    postal_code = models.CharField(max_length=6, unique=True)
    locality = models.CharField(max_length=60)

    """ Locality meta definition """
    class Meta:
        verbose_name = "Locality"
        verbose_name_plural = "Localities"

    """ String representation of Locality """
    def __str__(self):
        return f'({self.pk}) {self.postal_code} {self.locality}'

