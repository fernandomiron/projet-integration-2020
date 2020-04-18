from django.db import models

from .representation import Representation
from django.contrib.auth.models import User


class RepresentationUser(models.Model):
    """ Definition of model Representation """

    representation_id = models.ForeignKey(Representation, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.IntegerField(help_text="Number of seats ")

    class Meta:
        """ Behavior of the model Representation """

        verbose_name = "RepresentationUser"
        verbose_name_plural = "RepresentationsUsers "

    def __str__(self):
        """ Conversion of RepresentationUser object to String """

        return self.seat
