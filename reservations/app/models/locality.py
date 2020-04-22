from django.db import models


class Locality(models.Model):
    """ Definition of model Locality"""

    zip_code = models.CharField(max_length=6, help_text="Postal Code")
    locality = models.TextField(max_length=60, help_text="Official designation locality")

    class Meta:
        """ Behavior of the model Locality """

        verbose_name = "Locality"
        verbose_name_plural = "Localities"

    def __str__(self):
        """ Conversion of Locality object to String  """

        return '{} - {}'.format(self.zip_code, self.locality)
