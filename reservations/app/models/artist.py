
from django.db import models

"""
Artist model
"""
class Artist(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

    class Meta:
        db_table = 'artists'
        verbose_name_plural= 'Artists'
        verbose_name = 'Artist'

    def __str__(self):
        return self.lastname +' - '+self.firstname