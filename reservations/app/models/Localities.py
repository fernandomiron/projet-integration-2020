from django.db import models

class Localities (models.Model):
    """model definition Localities"""

    postal_code= models.CharField(max_length = 6, unique = True)
    locality = models.CharField(max_length = 60, unique = True)

    class Meta:
        """meta for Localities."""

        verbose_name = "Locality"
        verbose_name_plural = "Localities"

        ordering = ['pk']

    
    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {} {}".format(self.pk, self.postal_code, self.locality)