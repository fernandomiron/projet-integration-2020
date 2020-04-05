from django.db import models

"""
Creation of the Artist_type model
"""

"""
on_delete=models.CASCADE to delete referenced objects
"""
class Artist_type(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)

    class Meta:
        db_table = 'artist_type'
        verbose_name = "Artist_type"
        verbose_name_plural = "Artist_types"

    def __str__(self):
        return 'Artist : ' + self.artist_id + '\nType : ' + self.type_id