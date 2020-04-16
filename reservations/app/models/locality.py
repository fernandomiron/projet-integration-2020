from django.db import models

class locality (models.Model):
    """model definition Localities"""

    zipcode= models.CharField(max_length = 6, unique = True)
    locality = models.CharField(max_length = 60, unique = True)

    class Meta:
        """meta for Localities."""

        verbose_name = "Locality"
        verbose_name_plural = "Localities"

        ordering = ['pk']

    
    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {} {}".format(self.pk, self.zipcode, self.locality)