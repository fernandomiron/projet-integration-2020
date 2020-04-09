from django.db import models
from django.urls import reverse
from app.models.artystType import ArtystType

class Collaboration(models.Model):
    """Collaboration model"""
    artistTypeId = models.ForeignKey(ArtystType, on_delete = models.CASCADE)
    showId = models.ForeignKey(Show,on_delete=models.CASCADE)
    class Meta:
        """ Collaboration meta data"""
        verbose_name = "Collaboration"
        verbose_name_plural = "Collaborations"
        ordering = ['pk']

    def __str__ (self):
        """ Overloading __str__ method"""
        return " {} {} {}".format(self.pk, self.artistTypeId,self.showId)
