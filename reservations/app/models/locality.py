from django.db import models

class Locality(models.Model):
    """ Locality model """
    postal_code = models.CharField(max_length=6, unique = True)
    locality = models.CharField(max_length=60, unique = True)

    class Meta:
        """ Artist model meta data """
        verbose_name = "Locality"
        verbose_name_plural = "Localities"
        ordering = ['postal_code', 'locality', 'pk']

    def __str__(self):
        """ Overloading __str__ method"""
        return " {} {} {}".format(self.pk, self.postal_code, self.locality)
