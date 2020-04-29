from django.db import models
from django.urls import reverse

class Artist_type(models.Model):

    """ Artist_type model definition """
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    type = models.ForeignKey("Type", on_delete=models.CASCADE)

    """ Artist_type meta definition """
    class Meta:
        verbose_name = "Artist_type"
        verbose_name_plural = "Artist_types"

    """ String representation of Artist_type """
    def __str__(self):
        return f'({self.pk}) Artist : {self.artist}, Type :  {self.type}'


    def get_absolute_url(self):
        return reverse("app:artist-type-detail", kwargs={"pk": self.pk})