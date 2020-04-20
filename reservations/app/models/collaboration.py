""" artist_type_show """

from django.db import models

class Collaboration(models.Model):
    """ Collaboration model definition """
    artist_type = models.ForeignKey("Artist_type", on_delete=models.CASCADE)
    show = models.ForeignKey("Show", on_delete=models.CASCADE)    

    """ Collaboration meta definition """
    class Meta:
        verbose_name = "Collaboration"
        verbose_name_plural = "Collaborations"

    """ String representation of Collaboration """
    def __str__(self):
        return f'({self.pk}) Artist_type ID : {self.artist_type_id}, Show ID : {self.show_id}'
