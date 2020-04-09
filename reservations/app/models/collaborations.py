from django.db import models

class Collaborations (models.Model):
    """model definition collaborations"""

    artist_type_id= models.ForeignKey('Artist_type',on_delete=models.CASCADE)
    show_id = models.ForeignKey('Shows',on_delete=models.CASCADE)

    class Meta:
        """meta for Collaborations."""

        verbose_name = "Collaboration"
        verbose_name_plural = "Collaborations"

        ordering = ['pk']
