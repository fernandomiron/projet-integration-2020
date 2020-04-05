from django.db import models

class Artist (models.Model):
    """model definition Artist"""

    firstname= models.CharField(max_length = 60)
    lastname = models.CharField(max_length = 60)

    class Meta:
        """meta for Artist."""

        verbose_name = "Artist"
        verbose_name_plural = "Artists"

        ordering = ['pk']

    
    def __str__(self) :
        """representation of MODELNAME"""

        return "({}) {} {}".format(self.pk, self.firstname, self.lastname)

