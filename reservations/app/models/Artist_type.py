from django.db import models

class Artist_type (models.Model):
    """model definition Artist_type"""

    artist_id= models.ForeignKey('artist',on_delete=models.CASCADE)
    type_id = models.ForeignKey('Types',on_delete=models.CASCADE)

    class Meta:
        """meta for Artist_type."""

        verbose_name = "Type d'artiste"
        verbose_name_plural = "Types d'artiste"

        ordering = ['pk']