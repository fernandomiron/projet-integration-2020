from django.db import models

class ArtistType(models.Model):
    """ artist type model """
    artistId = models.ForeignKey("Artist", on_delete=models.CASCADE)
    typeId = models.ForeignKey("Type", on_delete=models.CASCADE)
    class Meta:
        """ ArtistType model meta data """
        verbose_name = "Artist type"
        verbose_name_plural = "Artist types"
        ordering = ['pk']

    def __str__(self):
        """ Overloading __str__ method"""
        return " {} {} {}".format(self.pk, self.artistId, self.typeId)
