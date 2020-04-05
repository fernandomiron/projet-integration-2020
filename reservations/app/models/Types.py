from django.db import models

class Types (models.Model) : 
    """model definition of types"""

    type = models.CharField(max_length = 60)

    class Meta:
        """meta for type."""

        verbose_name = "Type"
        verbose_name_plural = "Types"

        ordering = ['pk']

    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {}".format(self.pk, self.type)