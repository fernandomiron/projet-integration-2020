from django.db import models

class Artist(models.Model):

    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return f'{self.pk} {self.lastname} {self.firstname}'
