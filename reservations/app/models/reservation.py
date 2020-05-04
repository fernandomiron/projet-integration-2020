from django.contrib.auth.models import User
from django.db import models

from app.models.show import Representation


class Reservation(models.Model):
    """Model definition for Reservation."""

    representation = models.ForeignKey(Representation,
                                       on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()

    class Meta:
        """Meta definition for Reservation."""

        verbose_name = 'Réservation'
        verbose_name_plural = 'Réservations'

    def __str__(self):
        """Unicode representation of Reservation."""

        return "[{}] Réservation de {}, le {}, pour {}".format(
                self.pk,
                self.representation.show.title,
                self.representation.time,
                self.seats
            )

    def get_absolute_url(self):
        """Return absolute url for Reservation."""

        return ('')  # TODO: Define absolute url + url name

    # TODO: Define custom methods here
