""" artist_type_show """

from django.db import models
from django.urls import reverse

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
        return f'({self.pk}) Artist_type ID : {self.artist_type}, Show ID : {self.show}'

    def get_absolute_url(self):
        return reverse("app:collaboration-detail", kwargs={"pk": self.pk})