from django.db import models

from .artist_type import ArtistTypes
from .show import Show


class Collaboration(models.Model):
    """ Definition of model Collaboration"""

    artist_type_id = models.ForeignKey(ArtistTypes, on_delete=models.CASCADE, null=True)
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE, null=True)

    class Meta:
        """ Behavior of the model Collaboration """

        verbose_name = "Collaboration"
        verbose_name_plural = "Collaborations"

    def __str__(self):
        """ Conversion of Collaboration object to String """

        return self.pk + ' Artist Type id = ' + self.artist_type_id + 'Show id = ' + self.show_id
