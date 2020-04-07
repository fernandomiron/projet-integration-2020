from django.db import models

class Artist_type(models.Model):

    artist_id = models.ForeignKey("Artist", on_delete=models.CASCADE)
    type_id = models.ForeignKey("Type", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Artist_type"
        verbose_name_plural = "Artist_types"

    def __str__(self):
        return f'Artist : {self.artist_id}, Type :  {self.type_id}'