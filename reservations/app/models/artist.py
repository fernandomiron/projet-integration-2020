from django.db import models

class Artist(models.Model):

    """ Artist model definition """
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    types = models.ManyToManyField("Type")

    """ Artist meta definition """
    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    """ String representation of Artist """
    def __str__(self):
        return f'({self.pk}) {self.lastname} {self.firstname}'
