from django.db import models


"""
Collaboration class
"""

class Collaboration(models.Model):

    artist_type_id = models.ForeignKey('Artist_type', on_delete=models.CASCADE)
    show_id = models.ForeignKey('Show', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Collaboration'
        verbose_name_plural = 'Collaborations'

    def __str__(self):
        return f'({self.pk}) Artist_type ID : {self.artist_type_id}, Show ID : {self.show_id}'