from django.db import models
from .artist_type import ArtistTypes

class Collaboration (models.Model):
    """model definition collaborations"""

    artist_types= models.ForeignKey('ArtistTypes',on_delete=models.CASCADE)
    show = models.ForeignKey('Show',on_delete=models.CASCADE)

    class Meta:
        """meta for Collaborations."""

        verbose_name = "Collaboration"
        verbose_name_plural = "Collaborations"

        ordering = ['pk']
