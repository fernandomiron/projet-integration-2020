from django.db import models

from .artist import Artist
from .types import Types


class ArtistTypes(models.Model):
    """ Definition of model ArtistTypes"""

    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    types_id = models.ForeignKey(Types, on_delete=models.CASCADE, null=True)

    class Meta:
        """ Behavior of the model Artist Types"""

        verbose_name = "Artist Type"
        verbose_name_plural = "Artist Types"

    def __str__(self):
        """ conversion of Artist Types object to String """

        return self.pk + ' Artist id = ' + self.artist_id + 'type id = ' + self.types_id
