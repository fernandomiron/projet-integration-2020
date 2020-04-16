from django.db import models

class Location (models.Model) : 
    """model definition of Locations"""

    locality_id = models.ForeignKey('Locality',on_delete=models.CASCADE)
    slug = models.CharField(max_length = 60, unique=True)
    designation = models.CharField(max_length = 60)
    adress = models.CharField(max_length = 255)
    website = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 30)


    class Meta:
        """meta for Locations."""

        verbose_name = "Location"
        verbose_name_plural = "Locations"

        ordering = ['pk']

    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {}".format(self.pk, self.designation )