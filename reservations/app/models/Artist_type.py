from django.db import models
from .artist import Artist
from .type import Type

class ArtistTypes (models.Model):
    """model definition Artist_type"""

    artist= models.ForeignKey('Artist',on_delete=models.CASCADE)
    types = models.ForeignKey('Type',on_delete=models.CASCADE)

    class Meta:
        """meta for Artist_type."""

        verbose_name = "Type d'artiste"
        verbose_name_plural = "Types d'artiste"

        ordering = ['pk']

    def __str__(self) :
        """representation of Artist_type"""

        return "({}) {} {}".format(self.pk, self.artist, self.types)