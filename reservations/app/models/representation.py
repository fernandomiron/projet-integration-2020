from django.db import models
from datetime import datetime

from .show import Show


class Representation(models.Model):
    """ Definition of model Representation """

    show_id = models.ForeignKey(Show, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(help_text="Representation schedule", null=True)
    location_id = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)

    class Meta:
        """ Behavior of the model Representation """

        verbose_name = "Eepresentation"
        verbose_name_plural = "Representations"

    def __str__(self):
        """ Conversion of Representation object to String """

        return self.time
