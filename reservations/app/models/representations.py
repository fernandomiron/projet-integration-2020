from django.db import models

class Representations (models.Model) : 
    """model definition of Representations"""

    show_id = models.ForeignKey('Shows',on_delete=models.CASCADE)
    when = models.DateField ()
    location_id = models.ForeignKey('locations',on_delete=models.CASCADE)

 


    class Meta:
        """meta for Representations."""

        verbose_name = "Représentation"
        verbose_name_plural = "Représentations"

        ordering = ['pk']

    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {}".format(self.pk, self.show_id )