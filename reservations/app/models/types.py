from django.db import models


class Types(models.Model):
    """ Definition of the model Types"""

    types = models.CharField(max_length=60, help_text="Artist Function (job)")

    class Meta:
        """ Behavior of the model Type(s) """

        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        """ conversion of Types object to String """

        return self.types
