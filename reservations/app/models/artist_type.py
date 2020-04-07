from django.db import models

class Artist_type(models.Model):

    """ Artist_type model definition """
    artist_id = models.ForeignKey("Artist", on_delete=models.CASCADE)
    type_id = models.ForeignKey("Type", on_delete=models.CASCADE)

    """ Artist_type meta definition """
    class Meta:
        verbose_name = "Artist_type"
        verbose_name_plural = "Artist_types"

    """ String representation of Artist_type """
    def __str__(self):
        return f'({self.pk}) Artist : {self.artist_id}, Type :  {self.type_id}'