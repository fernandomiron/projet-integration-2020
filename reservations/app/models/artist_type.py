from django.db import models

"""
Creation of the Artist_type model
"""

"""
on_delete=models.CASCADE to delete referenced objects
"""
class Artist_type(models.Model):
    artist_id = models.ForeignKey('Artist', on_delete=models.CASCADE)
    type_id = models.ForeignKey('Type', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Artist Type"
        verbose_name_plural = "Artist Types"

    def __str__(self):
        return 'Artist : ' + self.artist_id + '\nType : ' + self.type_id