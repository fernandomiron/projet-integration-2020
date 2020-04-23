from django.db import models
from .show import Show
from .location import Location

class Representation (models.Model) : 
    """model definition of Representations"""

    show= models.ForeignKey('Show',on_delete=models.CASCADE)
    time = models.DateTimeField ()
    location = models.ForeignKey('Location',on_delete=models.CASCADE, null =True, blank = True)
    total_seats = models.CharField(max_length = 11)
    available_seats = models.CharField(max_length=11)



 


    class Meta:
        """meta for Representations."""

        verbose_name = "Représentation"
        verbose_name_plural = "Représentations"

        ordering = ['pk']

    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {}".format(self.pk, self.show)