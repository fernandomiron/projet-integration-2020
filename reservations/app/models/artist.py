from django.db import models

class Artist(models.Model):
    """ Artist model """
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

    class Meta:
        """ Artist model meta data """
        verbose_name = "Artist"
        verbose_name_plural = "Artists"
        ordering = ['firstname', 'lastname', 'pk']

    def __str__(self):
        """ Overloading __str__ method"""
        return " {} {} {}".format(self.pk, self.firstname, self.lastname)
