from django.db import models
from django.urls import reverse

class Artist(models.Model):

    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

    class Meta:
        db_table = "artists"
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    def get_absolute_url(self):
        return reverse("Artist_detail", kwargs={"pk": self.pk})
